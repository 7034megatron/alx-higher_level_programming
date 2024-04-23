#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch movie details. Status code: ${response.statusCode}`);
    return;
  }

  const films = JSON.parse(body).results;
  const characterId = '18'; // Wedge Antilles character ID

  const moviesWithWedge = films.filter(film =>
    film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
  );

  console.log(moviesWithWedge.length);
});
