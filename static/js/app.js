let alertWrapper = document.querySelector(".alert");
let alertClose = document.querySelector(".alert__close");
if (alertWrapper) {
  alertClose.addEventListener(
    "click",
    () => (alertWrapper.style.display = "none")
  );
}
// Get Search form and page links
const mobile_icon = document.getElementById("mobile-icon");
const mobile_menu = document.getElementById("mobile-menu");
const hamburger_icon = document.querySelector("#mobile-icon i");

function openCloseMenu() {
  mobile_menu.classList.toggle("block");
  mobile_menu.classList.toggle("active");
}

function changeIcon(icon) {
  icon.classList.toggle("fa-xmark");
}

mobile_icon.addEventListener("click", openCloseMenu);

const tabs = document.querySelectorAll(".tabs");
const tab = document.querySelectorAll(".tab");
const panel = document.querySelectorAll(".tab-content");

function onTabClick(event) {
  // deactivate existing active tabs and panel

  for (let i = 0; i < tab.length; i++) {
    tab[i].classList.remove("active");
  }

  for (let i = 0; i < panel.length; i++) {
    panel[i].classList.remove("active");
  }

  // activate new tabs and panel
  event.target.classList.add("active");
  let classString = event.target.getAttribute("data-target");
  console.log(classString);
  document
    .getElementById("panels")
    .getElementsByClassName(classString)[0]
    .classList.add("active");
}

for (let i = 0; i < tab.length; i++) {
  tab[i].addEventListener("click", onTabClick, false);
}

const dropdownButton = document.querySelector(".profileShowAndHideDropdown");
const dropdownMenu = document.querySelector(".contentShowHide");

dropdownButton.addEventListener("click", () => {
  dropdownMenu.classList.toggle("hidden");
});
