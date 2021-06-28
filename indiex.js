
const express = require('express')
const app = express()
 
app.get('/', function (req, res) {
var accountSid = 'ACd9925bb0f680b4c25739b13d4b46da2f'; // Your Account SID from www.twilio.com/console
var authToken = '986b71d5fae73af3bbb22d9340c1beb6';   // Your Auth Token from www.twilio.com/console

var twilio = require('twilio');
var client = new twilio(accountSid, authToken);

client.messages.create({
    body: 'Hello from Node',
    to: '+917595090342',  // Text this number
    from: '+13056801026' // From a valid Twilio number
})
.then((message) =>  res.send(`This message with id: ${JSON.stringify(message)} was sent`));
})
 
app.listen(3000)