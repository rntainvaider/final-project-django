const BtnNext = document.getElementById("btn__next");
const RegFormInputLeft = document.querySelectorAll(".reg-form__input-left");
const FormErrorStarLeft = document.querySelectorAll(".form-error__star-left");
const RegFormLeft = document.querySelector(".reg-form__left");
const RegFormRight = document.querySelector(".reg-form__right");

const FormPasswordInputBtn = document.querySelectorAll(".form-password-input__btn");
const FormPasswordInputField = document.querySelectorAll(".form-password-input__field");

const BtnRegistration = document.getElementById("btn__registration");
const RegFormInpuRight = document.querySelectorAll(".reg-form__input-right");
const FormErrorStarRight = document.querySelectorAll(".form-error__star-right");
const InputPassword = document.querySelector(".input__password");
const InputPasswordRepeat = document.querySelector(".input__password-repeat");

const Email = document.getElementById("email");
const Password = document.getElementById("password");
const PasswordRepeat = document.getElementById("password_repeat");

const isLatinLetters = document.getElementById("is-latin__letters");
const isLenghtEight = document.getElementById("is-lenght__eight");
const isDigit = document.getElementById("is-digit");
const isLower = document.getElementById("is-lower");
const isUpper = document.getElementById("is-upper");
const regFormPasswordErrorWrapper = document.querySelectorAll(".reg-form-password__error-wrapper");
const regLatin = /^[A-Za-z0-9]+$/;
const regLength = /^.{8,}$/;
const regDigit = /\d/;
const regLower = /[a-z]/;
const regUpper = /[A-Z]/;

const RegForm = document.querySelector(".reg-form");

const regTypeText = /^[А-Яа-я]+$/;
const regTypePhone = /^\+7\s\(\d{3}\)\s\d{3}-\d{2}-\d{2}$/;
const regTypeEmaill = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;


BtnNext.addEventListener("click", (event) => {

    event.preventDefault();

    let hasError = false;

    for (let i = 0; i < RegFormInputLeft.length; i++) {
        const input = RegFormInputLeft[i];
        const errorStar = FormErrorStarLeft[i];

        if (i === RegFormInputLeft.length - 1) {
            if (input.value.trim() === "") {
                errorStar.style.display = "inline";
                input.style.border = "1px solid var(--red-red-7)";
                hasError = true;
            } else if (!regTypePhone.test(input.value.trim())) {
                errorStar.style.display = "none";
                input.style.border = "1px solid var(--red-red-7)";
                hasError = true;
            } else {
                errorStar.style.display = "none";
                input.style.border = "1px solid var(--gray-gray-4)";
            }
        } else {
            if (input.value.trim() === "") {
                errorStar.style.display = "inline";
                input.style.border = "1px solid var(--red-red-7)";
                hasError = true;
            } else if (!regTypeText.test(input.value.trim())) {
                errorStar.style.display = "none";
                input.style.border = "1px solid var(--red-red-7)";
                hasError = true;
            } else {
                errorStar.style.display = "none";
                input.style.border = "1px solid var(--gray-gray-4)";
            }
        };

    };

    if (!hasError && window.getComputedStyle(RegFormRight).display === "none") {
        RegFormLeft.style.display = "none";
        RegFormRight.style.display = "flex"
    };

});

function maskPhone(input) {
    let phone = input.value.replace(/\D/g, ''); // Убираем все нецифровые символы

    // Если введено больше 10 цифр, обрезаем до 10
    if (phone.length > 11) {
        phone = phone.substring(0, 11);
    }

    // Применяем маску
    let maskedPhone = '';

    if (phone.length > 0) {
        maskedPhone = '+7 ';
    }
    if (phone.length > 1) {
        maskedPhone += '(' + phone.substring(1, 4);
    }
    if (phone.length > 4) {
        maskedPhone += ') ' + phone.substring(4, 7);
    }
    if (phone.length > 7) {
        maskedPhone += '-' + phone.substring(7, 9);
    }
    if (phone.length > 9) {
        maskedPhone += '-' + phone.substring(9, 11);  // Последняя цифра
    }

    input.value = maskedPhone; // Обновляем значение в поле
}

// Функция, которая применяет маску сразу при фокусе, если поле пустое
function applyMask(input) {
    // Если поле пустое, сразу ставим маску
    if (input.value === '') {
        input.value = '+7 ';
    }
}


for (let i = 0; i < FormPasswordInputBtn.length; i++) {
    FormPasswordInputBtn[i].addEventListener("click", (event) => {

        event.preventDefault();

        if (FormPasswordInputField[i].type === "password") {
            FormPasswordInputField[i].type = "text";
        } else {
            FormPasswordInputField[i].type = "password";
        };
    });
};

//////////////////////////////

// Регулярные выражения для проверки полей
const regTypeEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Проверка email
const regTypePassword = /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$/; // Минимум 8 символов, 1 заглавная, 1 строчная, 1 цифра

// Список правил для проверки пароля
const passwordValidators = [
    {
        id: "is-latin__letters",
        regex: /^[a-zA-Z0-9]+$/, // Только латинские буквы и цифры
    },
    {
        id: "is-lenght__eight",
        regex: /^.{8,}$/, // Минимум 8 символов
    },
    {
        id: "is-digit",
        regex: /\d/, // Наличие цифры
    },
    {
        id: "is-lower",
        regex: /[a-z]/, // Наличие строчной буквы
    },
    {
        id: "is-upper",
        regex: /[A-Z]/, // Наличие заглавной буквы
    },
];

// Сброс стилей для полей
function resetStyles(input, errorStar) {
    input.style.border = "1px solid var(--gray-gray-4)";
    if (errorStar) {
        errorStar.style.display = "none";
    }
}

// Проверка одного поля по регулярному выражению
function validateField(input, regex, errorStar) {
    if (!regex.test(input.value)) {
        input.style.border = "1px solid var(--red-red-7)";
        if (errorStar) {
            errorStar.style.display = "inline";
        }
        return false;
    }
    resetStyles(input, errorStar);
    return true;
}

// Проверка пароля на основе правил
function validatePassword(password) {
    let isValid = true;
    passwordValidators.forEach(({ id, regex }) => {
        const errorElement = document.getElementById(id);
        if (!regex.test(password)) {
            if (errorElement) {
                errorElement.style.display = "flex";
            }
            isValid = false;
        } else {
            if (errorElement) {
                errorElement.style.display = "none";
            }
        }
    });
    return isValid;
}

// Главный обработчик для отправки формы
BtnRegistration.addEventListener("click", (event) => {
    event.preventDefault();

    let hasError = false;

    for (let i = 0; i < RegFormInpuRight.length; i++) {
        const input = RegFormInpuRight[i];
        const errorStar = FormErrorStarRight[i];

        // Проверка на пустоту
        if (input.value === "") {
            input.style.border = "1px solid var(--red-red-7)";
            errorStar.style.display = "inline";
            hasError = true;
            continue;
        } else {
            resetStyles(input, errorStar);
        }

        // Проверка email (i === 0)
        if (i === 0) {
            if (!validateField(input, regTypeEmail, errorStar)) {
                hasError = true;
            }
        }

        // Проверка пароля (i === 1)
        if (i === 1) {
            const passwordValid = validatePassword(input.value);
            if (!passwordValid) {
                hasError = true;
            }
        }

        // Проверка подтверждения пароля (i === 2)
        if (i === 2) {
            const password = RegFormInpuRight[1].value;
            const confirmPassword = input.value;

            if (password !== confirmPassword) {
                input.style.border = "1px solid var(--red-red-7)";
                errorStar.style.display = "inline";
                hasError = true;
            } else {
                resetStyles(input, errorStar);
            }
        }
    }

    // Если ошибок нет, отправляем форму
    if (!hasError) {
        RegForm.submit();
    }
});

// Сброс стилей при вводе в поля
RegFormInpuRight.forEach((input, index) => {
    const errorStar = FormErrorStarRight[index];

    input.addEventListener("input", () => {
        if (input.value !== "") {
            resetStyles(input, errorStar);
        }
    });
});

// Реальная проверка пароля на каждом вводе
Password.addEventListener("input", (event) => {
    const passwordValue = event.target.value;
    validatePassword(passwordValue);
});
