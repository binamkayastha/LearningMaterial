// Install: npm install -g coffee-script
// coffee -c test.coffee // Creates test.js
// coffee -cw test.coffee // Recompiles test.js every time test.coffee updated
// coffee -c src -o js // Compile all .coffee files in teh src dir into the js dir

// Functions
coffee = ->
  // Runs the confirm function with parameter "Ready for some Coffee?"
  confirm "Ready for some Coffee?" // parenthesis optional
  // Last statement for any coffeeScript function is always going to be returned
  "Your answer is  #{answer}"

// Default parameters:
cofee = (message = "Ready for some coffee?") ->
  answer = confirm message
  "Your answer is #{answer}"

// @ = this

// object? // Checks if it's null

// and or not unless operators.

// Ranger
range = [1..4] // [1,2,3,4]
range = [1...4] // [1, 2, 3]
range = [1..-1] // goes to end of array
numbers can also be variables

// Foreach loops can look like this (where storeLocations in an array)
for location in storeLocations:
  #{location}

// With filter
newLocations = (location for location in storeLocation when location isnt 'Sanford')

// Object oriented
class Coffee
  constructor: (name, strength=1)
    @name = name
    @strength = strength

  constructor: (@name, @strength=1) -> //Shortcut same thing as above
  brew: -> alert "brewing #{@name}"

//inheritence
class MaxgoodHouse extends Coffee
  constructor: (@name, @strength=0) ->
    @brand = "Maxgood House"

  brew: -> alert "Brewing #{@brand} #{@name}" //Overwrites parent if included

  => (changes this keyword to refer to class instead of object)

  Create objects like so:
  coffee = new Cofee(parm, param)
