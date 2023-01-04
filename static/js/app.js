let alertWrapper = document.querySelector(".alert");
let alertClose = document.querySelector(".alert__close");
if (alertWrapper) {
  alertClose.addEventListener(
    "click",
    () => (alertWrapper.style.display = "none")
  );
}
// Get Search form and page links
