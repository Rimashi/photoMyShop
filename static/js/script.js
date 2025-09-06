$(document).ready(() => {
    const $burgerIcon = $('.burger-base');
    const $burgerMenu = $('.base-function');
    let k = 0;
    $burgerIcon.click(() => {
        if ($burgerMenu.hasClass("active") && k == 1) {
            k = 3
            $burgerMenu.toggleClass('active');
            setTimeout(() => $burgerMenu.toggleClass('nonactive'), 0.005);
            $burgerIcon.text("открыть");
            setTimeout(() => {
                $burgerMenu.toggleClass('nonactive');
                k = 0;
                $burgerMenu.toggleClass('flex');
            }, 600);

        } else {
            if (k == 0) {
                k = 1
                $burgerMenu.toggleClass('flex');
                $burgerMenu.toggleClass('active');
                $burgerIcon.text("закрыть");
            }
        }
    });

    $(window).on('resize', function () {
        if ($(window).width() <= 700) {
            if ($burgerMenu.hasClass("flex")) {
                $burgerMenu.toggleClass('flex');
                k = 0
                $burgerIcon.text("открыть");
            }
            if ($burgerMenu.hasClass("active")) {
                $burgerMenu.toggleClass('active');
            }
            if ($burgerMenu.hasClass("nonactive")) {
                $burgerMenu.toggleClass('nonactive');
            }
        }
    })


    $('#image').on('change', function () {
        const file = this.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function (event) {
                let img = document.createElement('img');
                img.src = event.target.result;
                $('.insert-pic__image').css("background-image", `url(${img.src})`);
            }
            reader.readAsDataURL(file);
        }
    });

    $('#get_text').click(() => {
        event.preventDefault();
        let file = $('#image')[0].files;
        let formData = new FormData();

        if (file.length > 0) {
            formData.append('file', file[0]);
        }

        $.ajax({
            url: '/get/text',
            type: 'POST',
            processData: false,
            contentType: false,
            data: formData,
            success: function (res) {
                console.log(res['text']);
                alert(res['text']);
            },
            error: function (jqXHR, textStatus, errorThrown) {
                console.error("Ошибка AJAX:", textStatus, errorThrown);
            }
        })
    })


    $('#delete_noise').click(() => {
        event.preventDefault();
        let file = $('#image')[0].files;
        let formData = new FormData();

        if (file.length > 0) {
            formData.append('file', file[0]);
        }

        $.ajax({
            url: '/blur',
            type: 'POST',
            processData: false,
            contentType: false,
            data: formData,
            success: function (res) {
                console.log(res['image']);
                $('.insert-pic__image').css("background-image", `url(/show ${res['image']['path']})`);
                $('#save').val(res['image']['path']);
            },
            error: function (jqXHR, textStatus, errorThrown) {
                console.error("Ошибка AJAX:", textStatus, errorThrown);
            }
        })
    })


    $('#delete_fon').click(() => {
        event.preventDefault();
        let file = $('#image')[0].files;
        let formData = new FormData();

        if (file.length > 0) {
            formData.append('file', file[0]);
        }

        $.ajax({
            url: '/remove/background',
            type: 'POST',
            processData: false,
            contentType: false,
            data: formData,
            success: function (res) {
                console.log(res['image']['path']);
                $('.insert-pic__image').css("background-image", `url(/show ${res['image']['path']})`);
                $('#save').val(res['image']['path']);
            },
            error: function (jqXHR, textStatus, errorThrown) {
                console.error("Ошибка AJAX:", textStatus, errorThrown);
            }
        })
    })


    $('#better').click(() => {
        event.preventDefault();
        let file = $('#image')[0].files;
        let formData = new FormData();

        if (file.length > 0) {
            formData.append('file', file[0]);
        }

        $.ajax({
            url: '/make/better',
            type: 'POST',
            processData: false,
            contentType: false,
            data: formData,
            success: function (res) {
                console.log(res['image']);
                $('.insert-pic__image').css("background-image", `url(/show ${res['image']['path']})`);
                $('#save').val(res['image']['path']);
            },
            error: function (jqXHR, textStatus, errorThrown) {
                console.error("Ошибка AJAX:", textStatus, errorThrown);
            }
        })
    })


    $('#make_big_2').click(() => {
        event.preventDefault();
        let file = $('#image')[0].files;
        let formData = new FormData();

        if (file.length > 0) {
            formData.append('file', file[0]);
        }

        formData.append('num', 2);
        console.log(formData);
        $.ajax({
            url: '/make/bigger/',
            type: 'POST',
            processData: false,
            contentType: false,
            data: formData,
            success: function (res) {
                console.log(res['image']);
                $('.insert-pic__image').css("background-image", `url(/show ${res['image']['path']})`);
                $('#save').val(res['image']['path']);
            },
            error: function (jqXHR, textStatus, errorThrown) {
                console.error("Ошибка AJAX:", textStatus, errorThrown);
            }
        })
    })

    $('#make_big_3').click(() => {
        event.preventDefault();
        let file = $('#image')[0].files;
        let formData = new FormData();

        if (file.length > 0) {
            formData.append('file', file[0]);
        }

        formData.append('num', 3);
        $.ajax({
            url: '/make/bigger/',
            type: 'POST',
            processData: false,
            contentType: false,
            data: formData,
            success: function (res) {
                console.log(res['image']);
                $('.insert-pic__image').css("background-image", `url(/show ${res['image']['path']})`);
                $('#save').val(res['image']['path']);
            },
            error: function (jqXHR, textStatus, errorThrown) {
                console.error("Ошибка AJAX:", textStatus, errorThrown);
            }
        })
    })

    $('#make_big_4').click(() => {
        event.preventDefault();
        let file = $('#image')[0].files;
        let formData = new FormData();

        if (file.length > 0) {
            formData.append('file', file[0]);
        }
        formData.append('num', 4);

        $.ajax({
            url: '/make/bigger/',
            type: 'POST',
            processData: false,
            contentType: false,
            data: formData,
            success: function (res) {
                console.log(res['image']);
                $('.insert-pic__image').css("background-image", `url(/show ${res['image']['path']})`);
                $('#save').val(res['image']['path']);
            },
            error: function (jqXHR, textStatus, errorThrown) {
                console.error("Ошибка AJAX:", textStatus, errorThrown);
            }
        })
    })


    $('#save').click(() => {
        event.preventDefault();
        let filename = $('#save').val();
        filename = filename.substring(1, filename.length);
        console.log(filename, $('#save').val(), $('#save').valueOf());
        $.ajax({
            url: '/download/',
            type: 'GET',
            data: {filename: filename},
            success: function (res) {
            },
            error: function (jqXHR, textStatus, errorThrown) {
                console.error("Ошибка AJAX:", textStatus, errorThrown);
            }
        })
    })
})