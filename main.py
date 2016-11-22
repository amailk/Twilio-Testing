#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from twilio.rest import TwilioRestClient

account_sid = "ACa533284a0258f6118f7866a793bca1f4"
auth_token  = "fad88e45964698bb6209ba401d780b42"
twilio_number = "+16473609059"
client = TwilioRestClient(account_sid, auth_token)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.render("index.html")


class SMSHandler(webapp2.RequestHandler):
    def get(self):
        message = self.request.get("message")
        number = "+1" + self.request.get("number")

        print "Message:", message
        print "Number:", number
        self.response.write("Sent sms!")

        message = client.messages.create(body=message,
            to=number,
            from_=twilio_number)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/sms', SMSHandler)
], debug=True)
