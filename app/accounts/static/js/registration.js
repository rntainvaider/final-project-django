const formErrorStar = document.querySelectorAll(".form__error-star");
const formButtonNext = document.querySelector(".form-button__next");
const regForm = document.querySelector(".reg-form");

const LastName = document.getElementById("last_name");
const FirstName = document.getElementById("first_name");
const RegFormInput = document.querySelectorAll(".reg-form__input");

formButtonNext.addEventListener("click", (event) => {
    event.preventDefault();

    let hasError = false;

    for (let i = 0; i < RegFormInput.length; i++) {
        if (RegFormInput[i].value === "") {
            formErrorStar[i].style.display = "inline";
            RegFormInput[i].style.border = "1px solid var(--red-red-7)";
            RegFormInput[i].style.color = "var(--red-red-7)";
            hasError = true;
        } else {
            formErrorStar[i].style.display = "none";
            RegFormInput[i].style.border = "";
            RegFormInput[i].style.color = "";
        };
    };

    if (!hasError) {
        regForm.submit();
    };
});
