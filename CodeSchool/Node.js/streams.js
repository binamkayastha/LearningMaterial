// With files
var fs = require('fs');
var file = fs.createReadStream('text.txt');

file.on('readable', function() {
  var chunks = null;
  if (null !== (chunks = file.read())) {
    console.log(chunks.toString()):
  }
})

// Piping from readable string to writable stream
file.pipe(process.stdout);

// Reading from and writing to server
var fs = require('fs');
var http = require('http');

http.createServer(function(request, response) {
  response.writeHead(200, {'Content-Type': 'text/html'});

  var file = fs.createReadStream('index.html');
  file.pipe(response);
}).listen(8080);
