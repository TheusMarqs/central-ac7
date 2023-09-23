const elemToggleFunc = function(elem) {
    elem.classList.toggle("active");
};

function changeTheme() {
    const themeToggleBtns = document.querySelectorAll("[data-theme-btn]");

    themeToggleBtns.forEach(function(btn) {
        elemToggleFunc(btn);

        if (btn.classList.contains("active")) {
            document.body.classList.remove("dark_theme");
            document.body.classList.add("light_theme");

            localStorage.setItem("theme", "light_theme");
        } else {
            document.body.classList.add("dark_theme");
            document.body.classList.remove("light_theme");

            localStorage.setItem("theme", "dark_theme");
        }
    });
}