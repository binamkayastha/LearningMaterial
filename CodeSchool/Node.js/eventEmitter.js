//Event emitter
var EventEmiiter = require('events').EventEmitter;

var logger = new EventEmitter();
// We want there to be error, warn, and info events.
// We also want to create a listener to listen for these events.

logger.on('error', function(message) {
  console.log('ERR: ' + message);
});

// Example
logger.emit('error', 'Spilled Milk');
