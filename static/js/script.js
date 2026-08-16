/* ==================================================
   1. CONTACT FORM
   ================================================== */

// Contact Form খুঁজে বের করা
const form = document.getElementById("contactForm");


// Form Submit হলে এই function কাজ করবে
form.addEventListener("submit", function(event) {

    // Page Reload বন্ধ করা
    event.preventDefault();


    // Form-এর data সংগ্রহ করা
    const formData = new FormData(form);


    // Flask-এর /contact route-এ data পাঠানো
    fetch("/contact", {
        method: "POST",
        body: formData
    })

    // Flask থেকে response আসার পর
    .then(response => response.text())

    .then(data => {

        console.log(data);


        /* ------------------------------------------
           SUCCESS MESSAGE
           ------------------------------------------ */

        // আগের Success Message থাকলে মুছে দেওয়া
        const oldMessage = form.querySelector(".success-message");

        if (oldMessage) {
            oldMessage.remove();
        }


        // নতুন Success Message তৈরি করা
        const message = document.createElement("p");

        message.className = "success-message";

        message.textContent = "Form submitted successfully!";


        // Success Message-এর Design
        message.style.color = "green";
        message.style.textAlign = "center";
        message.style.marginTop = "15px";


        // Form-এর নিচে Message দেখানো
        form.appendChild(message);


        // Form খালি করা
        form.reset();

    })

    // কোনো error হলে
    .catch(error => {

        console.error("Error:", error);

    });

});



/* ==================================================
   2. MOBILE HAMBURGER MENU
   ================================================== */

// Hamburger Button খুঁজে বের করা
const menuToggle = document.getElementById("menuToggle");


// Navigation Menu খুঁজে বের করা
const navLinks = document.querySelector(".nav-links");


// Hamburger Button-এ Click করলে Menu Open/Close হবে
menuToggle.addEventListener("click", function() {

    navLinks.classList.toggle("active");

});