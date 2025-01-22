let FormButtonBtn = document.querySelector(".form-button__btn");

let ErrorStar = document.querySelectorAll(".error-star");
let FormGroupInputError = document.querySelectorAll(".form-group__input-error");

let ErrorPasswordImages = document.querySelectorAll(".error-password__images");
let ErrorPasswordText = document.querySelectorAll(".error-password__text");

let RegistrationForm = document.querySelector(".registration__form");
let FullName = document.getElementById("full_name");
let Email = document.getElementById("email");
let Phone = document.getElementById("phone");
let Password = document.getElementById("password");
let RepeatPassword = document.getElementById("repeat_password");

let Checkbox = document.getElementById("checkbox");

let GroupRight = document.querySelector(".group__right");
let GroupLeft = document.querySelector(".group__left");

// Регулярные выражения
const PhoneRegex = /^\+\d\s\(\d{3}\)\s\d{3}-\d{2}-\d{2}$/; // Поле Phone
const EmailRegex = /^[A-z0-9.]+@[a-z]+\.[a-z]+$/; // Поле Email

// Регулярные выражения поля Password
const isLatinLetters = /^[A-z0-9]+$/; // Содержит только латинские буквы
const isMinLength = /^.{8,}$/; // Содержит минимум 8 символов
const isDigits = /[0-9]/; // Включает цифры
const isLowerCase = /[a-z]/; // Включает строчные буквы
const isUpperCase = /[A-Z]/; // Включает заглавные буквы

FormButtonBtn.addEventListener("click", (event) => {
    // Останавливаем отправку формы по умолчанию
    event.preventDefault();

    // Скрываем все ошибки поля ErrorStar
    for (let i = 0; i < ErrorStar.length; i++) {
        ErrorStar[i].style.display = "none";
    }

    // Скрываем все ошибки поля FormGroupInputError
    for (let i = 0; i < FormGroupInputError.length; i++) {
        FormGroupInputError[i].style.display = "none";
    }

    // Скрываем все ошибки поля ErrorPasswordImages
    for (let i = 0; i < ErrorPasswordImages.length; i++) {
        ErrorPasswordImages[i].style.display = "none";
    }

    // Скрываем все ошибки поля ErrorPasswordText
    for (let i = 0; i < ErrorPasswordText.length; i++) {
        ErrorPasswordText[i].style.display = "none";
    }

    // Переключатель
    let hasError = false;

    // Проверка каждого поля
    if (FullName.value === "") {
        ErrorStar[0].style.display = "inline";
        hasError = true;
    }

    if (Email.value === "") {
        ErrorStar[1].style.display = "inline";
        hasError = true;
    }

    if (Phone.value === "") {
        ErrorStar[2].style.display = "inline";
        hasError = true;
    }

    if (Password.value === "") {
        ErrorStar[3].style.display = "inline";
        hasError = true;
    }

    if (RepeatPassword.value === "") {
        ErrorStar[4].style.display = "inline";
        hasError = true;
    }

    if (!EmailRegex.test(Email.value)) {
        FormGroupInputError[0].style.display = "inline";
        hasError = true;
    }

    if (!PhoneRegex.test(Phone.value)) {
        FormGroupInputError[1].style.display = "inline";
        hasError = true;
    }

    if (RepeatPassword.value !== Password.value) {
        FormGroupInputError[2].style.display = "inline";
        hasError = true;
    }

    if (!isLatinLetters.test(Password.value)) {
        ErrorPasswordImages[0].style.display = "inline";
        ErrorPasswordText[0].style.display = "inline";
        hasError = true;
    }

    if (!isMinLength.test(Password.value)) {
        ErrorPasswordImages[1].style.display = "inline";
        ErrorPasswordText[1].style.display = "inline";
        hasError = true;
    }

    if (!isDigits.test(Password.value)) {
        ErrorPasswordImages[2].style.display = "inline";
        ErrorPasswordText[2].style.display = "inline";
        hasError = true;
    }

    if (!isLowerCase.test(Password.value)) {
        ErrorPasswordImages[3].style.display = "inline";
        ErrorPasswordText[3].style.display = "inline";
        hasError = true;
    }

    if (!isUpperCase.test(Password.value)) {
        ErrorPasswordImages[4].style.display = "inline";
        ErrorPasswordText[4].style.display = "inline";
        hasError = true;
    }

    if (!Checkbox.checked) {
        hasError = true;
    }

    // Если ошибок нет, продолжаем отправку формы
    if (!hasError) {
        RegistrationForm.submit();
    }
})
