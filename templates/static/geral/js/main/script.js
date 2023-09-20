function ToggleTheme() {
    const sections = document.querySelectorAll('section');

    sections.forEach(section => {
        section.classList.toggle("dark");
    })
    
}