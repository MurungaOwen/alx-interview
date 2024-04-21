#!/usr/bin/node
const request = require('request');

async function fetchData () {
  const argument = process.argv[2];
  try {
    const filmResponse = await new Promise((resolve, reject) => {
      request.get(`https://swapi-api.alx-tools.com/api/films/${argument}/`, (error, response, body) => {
        if (error) {
          reject(error);
          return;
        }

        if (response.statusCode !== 200) {
          reject(new Error(`Status code: ${response.statusCode}`));
          return;
        }

        resolve(JSON.parse(body));
      });
    });
    await Promise.all(filmResponse.characters.map(async (characterUrl) => {
      try {
        const characterResponse = await new Promise((resolve, reject) => {
          request.get(characterUrl, (error, response, body) => {
            if (error) {
              reject(error);
              return;
            }

            if (response.statusCode !== 200) {
              reject(new Error(`Status code: ${response.statusCode}`));
              return;
            }

            resolve(JSON.parse(body));
          });
        });
        console.log(characterResponse.name);
      } catch (error) {
        console.error('Error fetching character data:', error);
      }
    }));
  } catch (error) {
    console.error('Error fetching film data:', error);
  }
}

fetchData();
