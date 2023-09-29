const express = require('express');
const { exec } = require('child_process');
const path = require('path');

const app = express();
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));

app.set('view engine', 'ejs');

app.get('/', (req, res) => res.render('index'));

app.post('/ask', (req, res) => {
    exec(`python3 app.py "${req.body.question}"`, (error, stdout) => {
        if (error) {
            console.error(`Error executing Python script: ${error}`);
            return res.status(500).send('Error occurred');
        }

        let pythonResult;
        try {
            pythonResult = JSON.parse(stdout);
            res.render('result', {
                question: pythonResult.question,
                answer: pythonResult.answer
            });
        } catch (e) {
            console.error('Error parsing Python result:', e);
            return res.status(500).send('Error occurred');
        }
    });
});

app.listen(3000, () => console.log('Server started on port 3000'));
