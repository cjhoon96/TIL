const express = require('express');

const router = express.Router();

// Get / user 라우터
router.get('/', (req, res) => {
  res.send('Hello, User');
});

module.exports = router;