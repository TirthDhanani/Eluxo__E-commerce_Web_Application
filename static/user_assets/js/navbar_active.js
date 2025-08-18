function nav_active(){
    // Get a reference to an HTML element (e.g., a div with id "myDiv")
    const home = document.querySelector('.home-js');
    const  contact = document.querySelector('.contact-js');
    const  about= document.querySelector('.about-js');
    const  account= document.querySelector('.account-js');
    const  login= document.querySelector('.login-js');

    // Toggle the 'active' class on click
    home.addEventListener('click', () => {
    home.classList.toggle('active');
    });
    contact.addEventListener('click', () => {
    contact.classList.toggle('active');
    });
    about.addEventListener('click', () => {
    about.classList.toggle('active');
    });
    account.addEventListener('click', () => {
    account.classList.toggle('active');
    });
    login.addEventListener('click', () => {
    login.classList.toggle('active');
    });

}
nav_active()