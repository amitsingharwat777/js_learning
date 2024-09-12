const express = require('express');
const connection = require('./db'); // Import the connection
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());  // Parse JSON data from requests

// Route to add a new user
app.post('/add-user', (req, res) => {
  const { name, email, password } = req.body;

  const query = `INSERT INTO users (name, email, password) VALUES (?, ?, ?)`;

  connection.query(query, [name, email, password], (err, results) => {
    if (err) {
      console.error('Error inserting data:', err);
      res.status(500).send('Error inserting data');
      return;
    }
    res.send('User added successfully');
  });
});

// Start the server
const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
