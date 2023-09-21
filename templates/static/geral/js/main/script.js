const elemToggleFunc = function(elem) { elem.classList.toggle("active"); }



function changeTheme() {

    const themeToggleBtn = document.querySelector("[data-theme-btn]");

    elemToggleFunc(themeToggleBtn);

    if (themeToggleBtn.classList.contains("active")) {
        document.body.classList.remove("dark_theme");
        document.body.classList.add("light_theme");

        localStorage.setItem("theme", "light_theme");
    } else {
        document.body.classList.add("dark_theme");
        document.body.classList.remove("light_theme");

        localStorage.setItem("theme", "dark_theme");
    }

}