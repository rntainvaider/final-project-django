let FormButtonBtn = document.querySelector(".form-button__btn")
let GroupRight = document.querySelector(".group__right")
let GroupLeft = document.querySelector(".group__left")

FormButtonBtn.addEventListener("click", () => {
    GroupRight.style.display = "block";
    GroupLeft.style.display = "none";
})
