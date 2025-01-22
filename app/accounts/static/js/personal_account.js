let ErrorStar = document.querySelectorAll(".error_star");
let FormButtonBtn = document.querySelector(".form-button__btn");

let RegistrationForm = document.querySelector(".registration__form");
let FormGroupInputBorderRed = document.querySelector(".from-group__input-border__red");

let FormGroupInput = document.querySelector(".from-group__input")
let Email = document.getElementById("email");
let Password = document.getElementById("password");

// Регулярные выражения
const EmailRegex = /^[A-z0-9.]+@[a-z]+\.[a-z]+$/; // Поле Email

FormButtonBtn.addEventListener("click", (event) => {

    // Скрываем все звездочки поля ErrorStar
    for (let i = 0; i < ErrorStar.length; i++) {
        ErrorStar[i].style.display = "none";
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

    // Если ошибок нет продолжаем отправку формы
    if (!hasError) {
        RegistrationForm.submit();
    }

})
