// In module file, like custom_hello.js (1 public method)
var hello = function() {
  console.log("Hello World");
}

module.exports = hello;

// Module file called custom_goodbye.js (can have multiple public methods)
exports.goodbye = (function() {
  console.log("bye!");
})

// In app.js file
var hello = require('./custom_hello.js');
hello();

var gb = require('./custom_goodbye.js');
gb.goodbye();

   //an also be written as
require('./custom_goodbye.js').goodbye();


// You can specify which functions to make public in your modules by doing
exports.foo = foo // Where foo is a function in the module
