//codigo conectar con una base de datos de mongoDB


const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const MongoClient = require('mongodb').MongoClient;
const ObjectId = require('mongodb').ObjectId;
const cors = require('cors');
const port = 3000;

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(cors());

var db;

MongoClient.connect('mongodb://localhost:27017', (err, client) => {
    if (err) return console.log(err);
    db = client.db('mokepon');
    app.listen(port, () => {
        console.log('listening on 3000');
    });
    });

app.get('/', (req, res) => {
    res.send('Hello World!');
});

app.get('/mokepon', (req, res) => {
    db.collection('mokepon').find().toArray((err, result) => {
        if (err) return console.log(err);
        res.send(result);
    });
});