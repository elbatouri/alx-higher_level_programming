// fetches and lists the title for all movies by using link

let link = 'https://swapi-api.alx-tools.com/api/films/?format=json';

$.get(link, function (data) {
  let films = data.results;
  for (let film of films) {
    $('ul#list_movies').append(`<li>${film.title}</li>`);
  }
});
