// Nodes is very low level
// Express is a web framework for Nodes

var express = require ('express');
// npm insall --save express (installs the module and adds it to our deprendency file (package.json))
var app = express();

app.get('/', function(request, response) {
  response.sendFile(__dirname + "/index.html"); // dirname is the current directory
})

app.listen(8080);

// ejs, templating library
// npm install --save ejs
