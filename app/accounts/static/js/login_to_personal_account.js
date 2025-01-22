let ErrorStar = document.querySelectorAll(".error_star");
let FormFroupInputError = document.querySelectorAll(".form-group__input-error")
let FormButtonBtn = document.querySelector(".form-button__btn");

let AuthorizationForm = document.querySelector(".authorization__form");

let Email = document.getElementById("email");
let Password = document.getElementById("password");

// Регулярные выражения
const EmailRegex = /^[A-z0-9.]+@[a-z]+\.[a-z]+$/; // Поле Email
const PasswordRegex = /^[A-z0-9].{8,}$/; // Поле Password

FormButtonBtn.addEventListener("click", (event) => {

    // Скрываем поля ErrorStar
    for (let i = 0; i < ErrorStar.length; i++) {
        ErrorStar[i].style.display = "none";
    }

    // Скрываем поля FormFroupInputError
    for (let i = 0; i < FormFroupInputError.length; i++) {
        FormFroupInputError[i].style.display = "none";
    }

    // Отключаем отправку формы
    event.preventDefault();

    // Переключатель
    let hasError = false;

    if (Email.value === "") {
        ErrorStar[0].style.display = "inline";
        hasError = true;
    }

    if (Password.value === "") {
        ErrorStar[1].style.display = "inline";
        hasError = true;
    }

    if (!EmailRegex.test(Email.value)) {
        FormFroupInputError[0].style.display = "inline";
        hasError = true;
    }

    if (!PasswordRegex.test(Password.value)) {
        FormFroupInputError[1].style.display = "inline";
        hasError = true;
    }

    // Если ошибок нет продолжаем отправку формы
    if (!hasError) {
        AuthorizationForm.submit();
    }

})
