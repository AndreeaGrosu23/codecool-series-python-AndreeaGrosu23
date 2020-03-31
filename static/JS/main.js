// Modals register and login
let registerBtn = document.querySelector('#bt_register');
let closeBtn = document.querySelector('#close');
let modal = document.querySelector('#my-modal');

registerBtn.addEventListener('click', openModal);
closeBtn.addEventListener('click', closeModal);

function closeModal() {
    modal.style.display = 'none';
};

function openModal() {
    modal.style.display = 'block';
};


let closeBtnLogin = document.querySelector('#closeLogin');
let modalLogin = document.querySelector('#my-modal-login');
let loginBtn = document.querySelector('#bt_login');

loginBtn.addEventListener('click', openModalLogin);
closeBtnLogin.addEventListener('click', closeModalLogin);

function openModalLogin() {
    modalLogin.style.display = 'block';
}

function closeModalLogin() {
    modalLogin.style.display = 'none';
};


// Toggle actors to show movies where they played
document.querySelectorAll('.actor').forEach(p => p.addEventListener('click', e => {
    e.preventDefault();
    e.target.nextElementSibling.classList.toggle('hide');
}));


// Show episodes for seasons
let seasons = document.querySelectorAll('h4');
for (let season of seasons)  {
    season.addEventListener('click', showOverview);
}

function showOverview(e) {
    e.preventDefault();
    e.target.nextElementSibling.classList.toggle('hide');
}


// Show favorites list when logged in
let faves = document.querySelector('#faves');
faves.addEventListener('click', openFaves);
function openFaves(faves) {
    faves.preventDefault();
    faves.target.nextElementSibling.classList.toggle('hide');
}