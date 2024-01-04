#!/usr/bin/node
const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (!error) {
    const todos = JSON.parse(body);
    const completedCountByUser = {};

    todos.forEach((todo) => {
      if (todo.completed) {
        const userId = todo.userId;

        if (!completedCountByUser[userId]) {
          completedCountByUser[userId] = 1;
        } else {
          completedCountByUser[userId]++;
        }
      }
    });

    console.log(completedCountByUser);
  }
});
