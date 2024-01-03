#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const content = JSON.parse(body).results;

    let count = 0;

    content.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.endsWith('/18/')) {
          count += 1;
        }
      });
    });

    console.log(count);
  } else {
    console.error('Error:', error);
  }
});
