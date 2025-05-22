import { readDatabase } from '../utils';

export default class StudentsController {
  static async getAllStudents(req, res) {
    try {
      const studentsByField = await readDatabase('database.csv');
      let message = 'This is the list of our students\n';

      for (const [field, students] of Object.entries(studentsByField)) {
        message += `Number of students in ${field}: ${students.length}. List: ${students.join(', ')}\n`;
      }

      res.status(200).send(message);
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const { major } = req.params;

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    try {
      const studentsByField = await readDatabase('database.csv');
      const students = studentsByField[major] || [];

      res.status(200).send(`List: ${students.join(', ')}`);
      return;
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }
}
