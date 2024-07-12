import { getData } from "./forward.js";
import express from 'express';
import path from 'path';
import { fileURLToPath } from 'url';
import cors from "cors"
import opn from "opn"
const PORT = 3000;


const app = express();
app.use(cors())
app.use(express.json());
app.use(express.static('./public'));

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);


app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, './index.html'));
});

app.get('/play', (req, res) => {
    res.sendFile(path.join(__dirname, './play.html'));
});

app.get('/getrandom', async (req, res) => {
    let response = getData();
    res.json(response);
})

app.listen(PORT, () => {
    console.log('server running at localhost:' + PORT);
    // opn('http://localhost:' + PORT); 
});
