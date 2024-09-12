const mysql = require('mysql2');

// Create a connection to the database
const connection = mysql.createConnection({
  host: 'localhost',  // Change this if using a remote DB
  user: 'root',       // Your MySQL username
  password: 'root', // Your MySQL password
  database: 'user_data' // The database you created earlier
});

// Connect to MySQL
connection.connect((err) => {
  if (err) {
    console.error('Error connecting to MySQL:', err);
    return;
  }
  console.log('Connected to MySQL');
});

module.exports = connection;
