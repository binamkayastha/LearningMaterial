var http = require('http');

http.createServer(function(request, response) {
  response.writeHead(200); // Status code in header
  response.write("Hello, World.");
  response.end();
}).listen(8080);
console.log('listening on port 8080')

// Here, the known event is the request function inside of createServer
// Because it is a known event, it will let console.log run in parallel.
// Events are processed in an event queue (FIFO)
