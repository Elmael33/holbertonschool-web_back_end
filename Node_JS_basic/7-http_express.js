const express = require('express');
const fs = require('fs');

const app = express();
const port = 1245;

function countStudents(database) {
  return new Promise((resolve, reject) => {
    fs.readFile(database, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      lines.shift();
      const students = {};

      lines.forEach((line) => {
        const [firstname, , , field] = line.split(',');
        if (field) {
          if (!students[field]) students[field] = [];
          students[field].push(firstname);
        }
      });

      const summary = [`Number of students: ${lines.length}`];

      for (const [field, names] of Object.entries(students)) {
        summary.push(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
      }

      resolve(summary.join('\n'));
    });
  });
}

app.get('/', (req, res) => {
  res.setHeader('Content-Type', 'text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  res.setHeader('Content-Type', 'text/plain');
  const database = process.argv[2];

  if (!database) {
    res.send('This is the list of our students\nCannot load the database');
    return;
  }

  countStudents(database)
    .then((data) => {
      res.send(`This is the list of our students\n${data}`);
    })
    .catch((err) => {
      res.send(`This is the list of our students\n${err.message}`);
    });
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});

module.exports = app;
