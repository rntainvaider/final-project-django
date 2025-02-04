const MainForm = document.querySelector(".main__form");

const MainErrorStar = document.querySelectorAll(".main_error__star");

const MainFormButtonSave = document.querySelector(".main-form__button-save");

const MainFormBlockTwoImg = document.querySelectorAll(".main-form__block-two__img");
const MainFormBlockTwoText = document.querySelectorAll(".main-form__block-two__text");

const FullName = document.getElementById("full_name");
const Email = document.getElementById("email");
const PhoneNumber = document.getElementById("phone_number");
const Password = document.getElementById("password");
const RepeatPassword = document.getElementById("repeat_password");

const MainFormInput = document.querySelectorAll(".main-form__input");

// Регулярные выражения
const PhoneRegex = /^\+\d\s\(\d{3}\)\s\d{3}-\d{2}-\d{2}$/; // Поле Phone
const EmailRegex = /^[A-z0-9.]+@[a-z]+\.[a-z]+$/; // Поле Email

// Регулярные выражения поля Password
const isLatinLetters = /^[A-z0-9]+$/; // Содержит только латинские буквы
const isMinLength = /^.{8,}$/; // Содержит минимум 8 символов
const isDigits = /[0-9]/; // Включает цифры
const isLowerCase = /[a-z]/; // Включает строчные буквы
const isUpperCase = /[A-Z]/; // Включает заглавные буквы

// Обработчик нажатия на кнопку
MainFormButtonSave.addEventListener("click", (event) => {

    // Скрываем поля MainErrorStar
    for (let i = 0; i < MainErrorStar.length; i++) {
        MainErrorStar[i].style.display = "none";
    }

    // Останавливаем отправку поля
    event.preventDefault();

    // Переключатель
    let hasError = false;

    //Проверяем на пустоту поля
    if (FullName.value === "") {
        MainErrorStar[0].style.display = "inline";
        hasError = true;
    }

    if (Email.value === "") {
        MainErrorStar[1].style.display = "inline";
        hasError = true;
    }

    if (PhoneNumber.value === "") {
        MainErrorStar[2].style.display = "inline";
        hasError = true;
    }

    if (Password.value === "") {
        MainErrorStar[3].style.display = "inline";
        hasError = true;
    }

    if (RepeatPassword.value === "") {
        MainErrorStar[4].style.display = "inline";
        hasError = true;
    }

    // Если ошибок нет, то продолжаем отправку
    if (!hasError) {
        MainForm.submit();
    }
})
