# photoMyShop

Веб-приложение в стиле "мини-фотошопа", написанное на **FastAPI**.  
Позволяет обрабатывать изображения с использованием компьютерного зрения и готовых нейросетей.

---

## ✨ Функционал
- 📝 **OCR** — извлечение текста с изображений (Tesseract OCR)  
- 🖼 **Удаление фона** — нейросеть **U²-Net** (через библиотеку `rembg`)  
- 🔍 **Суперразрешение** — увеличение качества изображения с помощью моделей **EDSR (x2, x3, x4)**  
- 🎨 **Фильтрация** — улучшение и базовая обработка изображений (OpenCV)  
- 🌫 **Удаление шума / размытие**

---

## 🛠 Технологии
- **Backend:** [FastAPI](https://fastapi.tiangolo.com/), Python  
- **ML/AI:**  
  - [rembg (U²-Net)](https://github.com/danielgatis/rembg) — удаление фона  
  - [EDSR (Enhanced Deep Residual Networks)](https://arxiv.org/abs/1707.02921) — суперразрешение  
  - [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) — извлечение текста  
- **Computer Vision:** [OpenCV](https://opencv.org/)  
- **Frontend:** HTML, CSS, jQuery  

---

