// Modal register
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


// Modal login
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


// Show episodes details for seasons and seasons for shows
let seasons = document.querySelectorAll('h4');
for (let season of seasons)  {
    season.addEventListener('click', showOverview);
};

function showOverview(e) {
    e.preventDefault();
    e.target.nextElementSibling.classList.toggle('hide');
    let table = document.querySelector('.show-title');
    table.nextElementSibling.classList.toggle('hide');

    let seasonId = e.toElement.id;
    fetch(`http://127.0.0.1:5000/api/tv-show/${seasonId}`)
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            createEpisodesTable(data);
    });
};

function createEpisodesTable(data) {
    let episodes = document.querySelector('.episodes_details');
    episodes.innerHTML = '';
    for (let i in data) {
        episodes.innerHTML += `
                    <tr>
                        <td>${data[i].seasons_title}</td>
                        <td>${data[i].episode_number}</td>
                        <td>${data[i].title}</td>
                        <td>${data[i].overview}</td>
                        <td class="action-column">
                            <button type="button" class="icon-button"><i class="fa fa-edit fa-fw"></i></button>
                            <button type="button" class="icon-button"><i class="fa fa-trash fa-fw"></i></button>
                        </td>
                    </tr>`;
    }
};


// Show favorites list when logged in
let faves = document.querySelector('#faves');
faves.addEventListener('click', openFaves);
function openFaves(faves) {
    faves.preventDefault();
    faves.target.nextElementSibling.classList.toggle('hide');
}