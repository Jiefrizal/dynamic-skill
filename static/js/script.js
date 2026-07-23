// Navbar scroll effect
window.addEventListener("scroll", function () {
    const navbar = document.querySelector(".navbar");

    if (window.scrollY > 30) {
        navbar.classList.add("scrolled");
    } else {
        navbar.classList.remove("scrolled");
    }
});

// Scroll Animation (Intersection Observer)
document.addEventListener("DOMContentLoaded", function () {
    const observerOptions = {
        threshold: 0.15
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("animate-visible");
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    const animItems = document.querySelectorAll(".animate-on-scroll");
    animItems.forEach(item => {
        observer.observe(item);
    });
});



