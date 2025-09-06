from rembg import remove
import cv2
import pytesseract
import numpy as np
import re


def transliterate_filename(filename):
    # Словарь для замены символов
    translit_dict = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh',
        'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
        'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'ts',
        'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu',
        'я': 'ya', ' ': '_', ',': '', '.': '', '/': '', '\\': '', ':': '', ';': '', '?': '',
        '!': '', '@': '', '#': '', '$': '', '%': '', '^': '', '&': '', '*': '', '(': '',
        ')': '', '[': '', ']': '', '{': '', '}': ''
    }

    # Преобразование имени файла символ за символом
    translit_filename = ''
    extname = filename.split('.')[-1]
    filename = "".join(filename.split('.')[0:-1])
    for char in filename.lower():
        if char in translit_dict:
            translit_filename += translit_dict[char]
        else:
            translit_filename += char

    # Удаление повторяющихся подчёркиваний
    translit_filename = re.sub('_+', '_', translit_filename)
    translit_filename += "." + extname
    return translit_filename

class Edit:
    def __init__(self, filename):
        self.img = cv2.imread(filename)  # добавить загрузку и считывание в static
        self.filename = filename

    def remove_background(self):
        self.img = remove(self.img)
        return self

    def universal_filter(self):
        sharped = cv2.filter2D(self.img, -10, np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]))
        self.img = cv2.medianBlur(sharped, 5)
        # sharped = cv2.filter2D(self.img, -10, np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]))
        # denoised = cv2.GaussianBlur(sharped, (5, 5), 0)
        # self.img = denoised
        return self

    def make_bigger(self, num):
        if int(num) in [2, 3, 4]:
            sr = cv2.dnn_superres.DnnSuperResImpl_create()
            path = f'EDSR_x{num}.pb'
            sr.readModel(path)
            sr.setModel('edsr', num)
            self.img = sr.upsample(self.img)
        return self

    def blur(self):  # типа удаление шума, по факту размытие
        self.img = cv2.GaussianBlur(self.img, (7, 7), 0)
        return self

    def pick_to_text(self):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        text = pytesseract.image_to_string(self.img, lang='rus+eng')
        return text.replace('\n', ' ').strip()

    def remove_lines(self):
        kernel = np.ones((5, 5), np.float32) / 25
        restored_image = cv2.filter2D(self.img, -1, kernel)
        self.img = restored_image
        return self

    def save(self, filename):
        cv2.imwrite(filename, self.img)


