<?php

// This line loads the library
require('Services/Twilio.php');

// Find your Account Sid and Token at twilio.com/user/account
$sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX";
$token = "AUTH_TOKEN";

// Initialize the client
$client = new IPMessaging_Services_Twilio($sid, $token);

// Retrieve the service
$service = $client->services->get("ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX");

// List the channels
$channels = $service->channels;
$all_channels = print_r($channels,true);
print $all_channels;