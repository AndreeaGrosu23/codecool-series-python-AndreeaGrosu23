// document.querySelectorAll('p').forEach(p => p.addEventListener('click', e =>{
//     e.prevent.Default();
//     e.target.nextElementSibling.classList.toggle('hide')
//     }
// ));

// let seasons = document.querySelectorAll('h4');
//         for (season of seasons)  {
//             season.addEventListener('click', showOverview);
//         }
//
//         function showOverview(e) {
//             e.preventDefault();
//             e.target.nextElementSibling.classList.toggle('hide');
//         }

// let actors = document.querySelectorAll('p');
// for (actor of actors) {
//     actor.addEventListener('click', showMovies);
// };
//
// function showMovies(e) {
//     e.prevent.Default();
//     e.target.nextElementSibling.classList.toggle('hide');
// };

// let dataHandler = {
//     _data: {},
//     _api_get: function (url, callback) {
//         fetch(url, {
//             method: 'GET',
//             credentials: 'same-origin'
//         })
//             .then(response => response.json())
//             .then(json_response => callback(json_response))
//     },
//     _api_post: function (url, data, callback) {
//     },
//     init: function () {
//     },
//     getShows: function (callback) {
//         this._api_get('/get-shows', (response) => {
//             this._data = response;
//             callback(response);
//         })
//     }
// }
//
// let dom = {
//     init: function() {
//     },
//     loadShows: function () {
//         dataHandler.getShows(function(shows) {
//             dom.showShows(shows);
//         });
//     },
//     showShows: function (list_items) {
//         DisplayList(list_items, list_element, rows, current_page);
//         SetupPagination(list_items, pagination_element, rows);
//     }
// }
//
//
// function init() {
//     // init data
//     dom.init();
//     // loads the boards to the screen
//     dom.loadShows();
//
// }
//
// init();


// const getShows = async () => {
//
//     let showGet = await fetch(`${window.origin}/get-shows`);
//     showGet = await showGet.json();
//
//     console.log(showGet);
//     return showGet;
// };


// const list_items = [
//     "Item 1",
//     "Item 2",
//     "Item 3",
//     "Item 4",
//     "Item 5",
//     "Item 6",
//     "Item 7",
//     "Item 8",
//     "Item 9",
//     "Item 10",
//     "Item 11",
//     "Item 12",
//     "Item 13",
//     "Item 14",
//     "Item 15",
//     "Item 16"
// ];
//
//
// const list_element = document.getElementById('list');
//
// const pagination_element = document.getElementById('pagination');
//
// let current_page = 1;
// let rows = 5;
//
// function DisplayList(items, wrapper, rows_per_page, page) {
//     wrapper.innerHTML="";
//     page --;
//     let start = rows_per_page * page;
//     let end = start + rows_per_page;
//     let paginatedItems = items.slice(start, end);
//
//     for (let i = 0; i < paginatedItems.length; i ++) {
//         let item = paginatedItems[i];
//
//         let item_element = document.createElement('div');
//         item_element.classList.add('item');
//         item_element.innerText = item;
//
//         wrapper.appendChild(item_element);
//
//     }
// }
//
//
// function SetupPagination(items, wrapper, rows_per_page) {
//     wrapper.innerHTML = "";
//     let page_count = Math.ceil(items.length/rows_per_page);
//     for (let i = 1; i <= page_count; i ++) {
//         let btn = PaginationButton(i, items);
//         wrapper.appendChild(btn);
//     }
//     console.log(page_count)
// }
//
//
// function PaginationButton(page, items) {
//     let button = document.createElement('button');
//     button.innerText = page;
//
//     if (current_page == page) button.classList.add('active');
//
//     button.addEventListener('click', function() {
//         current_page = page;
//         DisplayList(items, list_element, rows, current_page);
//         let current_btn = document.querySelector('.pagenumbers button.active');
//         current_btn.classList.remove('active');
//         button.classList.add('active');
//     })
//     return button;
// }
//
// DisplayList(list_items, list_element, rows, current_page);
// SetupPagination(list_items, pagination_element, rows);