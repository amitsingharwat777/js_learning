const readline = require('readline');

// Create an interface for reading input from the terminal
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Function to take input for a given number of students
let students = [];
let numberOfStudents;
let studentCount = 0;

// Helper function to take student data
function askForStudentData() {
  if (studentCount < numberOfStudents) {
    rl.question(`Enter name for student ${studentCount + 1}: `, (name) => {
      rl.question(`Enter age for student ${studentCount + 1}: `, (age) => {
        rl.question(`Enter gender for student ${studentCount + 1}: `, (gender) => {
          rl.question(`Enter roll number for student ${studentCount + 1}: `, (rollNo) => {
            let student = { name, age, gender, rollNo };
            students.push(student);
            studentCount++;
            askForStudentData(); // Ask for the next student data
          });
        });
      });
    });
  } else {
    // Output all student data
    console.log("\nStudent Information:");
    students.forEach((student, index) => {
      console.log(`Student ${index + 1}:`);
      console.log(`Name: ${student.name}`);
      console.log(`Age: ${student.age}`);
      console.log(`Gender: ${student.gender}`);
      console.log(`Roll No: ${student.rollNo}`);
      console.log('--------------------');
    });
    rl.close(); // Close the input interface when done
  }
}

// Start by asking how many students to enter
rl.question("Enter the number of students: ", (answer) => {
  numberOfStudents = parseInt(answer);
  askForStudentData(); // Start asking for student details
});
