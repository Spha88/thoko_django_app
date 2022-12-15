// Add or Remove the "open" class on nav list container on mobile devices
let nav_button = document.getElementById("mobile-nav-button")
let nav_items_container = document.getElementById("nav-items")

nav_button.addEventListener("click", e => {
    let open = nav_items_container.classList.contains("open")
    if (open) {
        nav_items_container.classList.remove("open")
    } else {    
        nav_items_container.classList.add("open")
    }
})