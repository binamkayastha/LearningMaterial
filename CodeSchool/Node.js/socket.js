// npm install --save socket.io
var express = require('express');
var app = express();
var server = require('http').createServer(app);
var io = require('socket.io')(server);

io.on('connection', function(client) {
  console.log('Client connected...');
  client.emit('messages', { hello: 'world' });
  client.broadcast.emit('message', { hello: "world"}) // broadcasts to multiple client
  client.on('messages', function(client) {
    console.log(data);
  })
})

app.get('/', function(req, res) {
  res.sendFile(__dirname _ '/index.html');
})

server.listen(8080);

// In html
<script src="/socket.io/socket.io.js"></script>
<script>
var socket = io.connect('http://localhost:8080');
socket.on('messages', function(data) {
  alert(data.hello);
})
</script>
