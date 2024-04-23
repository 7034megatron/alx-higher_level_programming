#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch movie details. Status code: ${response.statusCode}`);
    return;
  }

  const movie = JSON.parse(body);
  const charactersUrls = movie.characters;

  // Function to fetch character name from character URL
  const fetchCharacterName = (url) => {
    return new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
          return;
        }
        if (response.statusCode !== 200) {
          reject(`Failed to fetch character details. Status code: ${response.statusCode}`);
          return;
        }
        const character = JSON.parse(body);
        resolve(character.name);
      });
    });
  };

  // Fetch names of all characters in parallel
  Promise.all(charactersUrls.map(fetchCharacterName))
    .then((characterNames) => {
      characterNames.forEach((name) => console.log(name));
    })
    .catch((error) => {
      console.error(error);
    });
});
