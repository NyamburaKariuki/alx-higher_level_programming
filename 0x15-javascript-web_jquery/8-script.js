//  script that fetches and lists the title for all movies by using this URL:
//  https://swapi-api.hbtn.io/api/films/?format=json

$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  console.log(data);
  data.results.forEach(film => {
    $('UL#list_movies').append(film.title);
  });
});
