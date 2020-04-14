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
import jinja2 as jinja2
import webapp2
from webapp2_extras import jinja2


class MainHandler(webapp2.RequestHandler):
    def post(self):
        cif = self.request.get("cif")
        nom = self.request.get("nom")
        dir = self.request.get("dir")
        poblation = self.request.get("poblation")
        province = self.request.get("province")
        cpostal = self.request.get("cpostal")
        pays = self.request.get("pays")
        contact = self.request.get("contact")
        email = self.request.get("email")
        telephone = self.request.get("telephone")
        cifc = self.request.get("cifc")
        nomc = self.request.get("nomc")
        dirc = self.request.get("dirc")
        poblationc = self.request.get("poblationc")
        provincec = self.request.get("provincec")
        cpostalc = self.request.get("cpostalc")
        paysc = self.request.get("paysc")
        contactc = self.request.get("contactc")
        emailc = self.request.get("emailc")
        telephonec = self.request.get("telephonec")
        info = self.request.get("info")

        jinja = jinja2.get_jinja2(app=self.app)

        valeurs ={
            "cif": cif,
            "nom": nom,
            "dir": dir,
            "poblation": poblation,
            "province": province,
            "cpostal": cpostal,
            "pays": pays,
            "contact": contact,
            "email": email,
            "telephone": telephone,
            "cifc": cifc,
            "nomc": nomc,
            "dirc": dirc,
            "poblationc": poblationc,
            "provincec": provincec,
            "cpostalc": cpostalc,
            "paysc": paysc,
            "contactc": contactc,
            "emailc": emailc,
            "telephonec": telephonec,
            "info": info
        }
        self.response.write(jinja.render_template("reponse.html", **valeurs))


app = webapp2.WSGIApplication([
    ('/calculatteur', MainHandler)
], debug=True)
