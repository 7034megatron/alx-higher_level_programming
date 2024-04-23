#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch task data. Status code: ${response.statusCode}`);
    return;
  }

  const tasks = JSON.parse(body);

  const completedTasksByUser = tasks.reduce((completed, task) => {
    if (task.completed) {
      if (completed[task.userId]) {
        completed[task.userId]++;
      } else {
        completed[task.userId] = 1;
      }
    }
    return completed;
  }, {});

  console.log(completedTasksByUser);
});
