const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.split('\n').filter((line) => line.trim() !== ''); // Remove empty lines

    if (lines.length <= 1) {
      throw new Error('Cannot load the database');
    }

    console.log(`Number of students: ${lines.length - 1}`);

    const fields = {};
    for (let i = 1; i < lines.length; i += 1) {
      const student = lines[i].split(',');
      if (student.length === 4) {
        const field = student[3];
        const firstName = student[0];
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstName);
      }
    }

    for (const [field, students] of Object.entries(fields)) {
      console.log(`Number of students in ${field}: ${students.length}. List: ${students.join(', ')}`);
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
