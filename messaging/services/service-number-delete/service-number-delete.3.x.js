// Download the Node helper library from twilio.com/docs/libraries/node
// These consts are your accountSid and authToken from https://www.twilio.com/console
const accountSid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX';
const authToken = 'your_auth_token';

const client = require('twilio')(accountSid, authToken);
const service = client.messaging.services('MG2172dd2db502e20dd981ef0d67850e1a');

service.phoneNumbers('PN557ce644e5ab84fa21cc21112e22c485')
       .remove()
       .then(function(response) {
         console.log(response);
       }).catch(function(error) {
         console.log(error);
       });
