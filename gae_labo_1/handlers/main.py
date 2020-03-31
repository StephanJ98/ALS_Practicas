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


class MainHandler(webapp2.RequestHandler):
    def post(self):
        dist = float(self.request.get("dist"))
        temps = float(self.request.get("temps"))
        consom = float(self.request.get("consom"))
        if not isinstance(dist, float) or dist == 0.0:
            dist = 1
        if not isinstance(temps, float) or temps == 0.0:
            temps = 1
        if not isinstance(consom, float) or consom == 0.0:
            consom = 1
        self.response.write("Velocidad Media: " + str(float(dist) / float(temps)) + " Km/H \n")
        self.response.write("Consumo Total: " + str(float(consom) * float(float(dist) / 100)) + " L")


app = webapp2.WSGIApplication([
    ('/calculatteur', MainHandler)
], debug=True)
