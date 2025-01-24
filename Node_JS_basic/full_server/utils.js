import fs from 'fs';
import path from 'path';
import readline from 'readline';

export const readDatabase = (filePath) => {
  return new Promise((resolve, reject) => {
    const studentsByField = {
      CS: [],
      SWE: [],
    };

    const fileStream = fs.createReadStream(filePath);
    const rl = readline.createInterface({
      input: fileStream,
      crlfDelay: Infinity,
    });

    rl.on('line', (line) => {
      const [firstname, field] = line.split(',');

      if (firstname && field && studentsByField[field]) {
        studentsByField[field].push(firstname);
      }
    });

    rl.on('close', () => {
      resolve(studentsByField);
    });

    rl.on('error', (error) => {
      reject(new Error('Cannot load the database'));
    });
  });
};
