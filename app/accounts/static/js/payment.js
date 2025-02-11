const ErrorStar = document.querySelectorAll(".error-star");
const BtnPayment = document.querySelector(".btn-payment");
const PaymentFrom = document.querySelector(".payment-from");
const SummaPayment = document.getElementById("summa_payment");
const Email = document.getElementById("email");
const PeriodPayment = document.getElementById("period_payment");
const MinusBlock = document.querySelector(".minus-block");
const Hide = document.querySelector(".hide");
const BtnDetail = document.querySelector(".btn-detail");
const PlusNone = document.querySelector(".plus-none");

BtnDetail.addEventListener("click", () => {
    if (Hide.style.display === "none") {
        Hide.style.display = "contents";
    } else {
        Hide.style.display = "none";
    };
});

BtnPayment.addEventListener("click", (event) => {
    for (let i = 0; i < ErrorStar.length; i++) {
        ErrorStar[i].style.display = "none";
    }

    // Отключаем отправку формы
    event.preventDefault();

    // Переключатель
    let hasError = false;

    // Проверяем поле SummaPayment
    if (SummaPayment.value === "") {
        ErrorStar[0].style.display = "inline";
        hasError = true;
    };

    // Проверяем поле Email
    if (Email.value === "") {
        ErrorStar[1].style.display = "inline";
        hasError = true;
    };

    // Проверяем поле PeriodPayment
    if (PeriodPayment.value === "") {
        ErrorStar[2].style.display = "inline";
        hasError = true;
    };

    //Включаем отправку формы
    if (!hasError) {
        PlusNone.style.display = "block";
        MinusBlock.style.display = "none";

        setTimeout(function() {

            PaymentFrom.submit();

            setTimeout(function() {
                location.reload();
            }, 1000);
        }, 2000);
    }
});
