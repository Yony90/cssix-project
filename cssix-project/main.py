#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import os
import logging
from BlogPost import BlogPost

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/main-html.html')

        postSubjects = ['cplusplus', 'python', 'javascript']
        postInfo = ['C++ is an object-oriented programming (OOP) language that is viewed by many as the best language for creating large-scale applications. C++ is a superset of the C language.',
        "An interpreted language, Python has a design philosophy that emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than curly brackets or keywords), and a syntax that allows programmers to express concepts in fewer lines of code than might be used in languages such as C++",
        "an object-oriented computer programming language commonly used to create interactive effects within web browsers."]
        postDictionary = {}
        for x in range(len(postSubjects)):
            postDictionary[postSubjects[x]] = postInfo[x]
        # lang = BlogPost(subject=self.request.get('lang'))



        self.response.out.write(template.render())
        
    def post(self):
        temp_dict = self.request.get('lang')
        print "PRINT ??????" + temp_dict

class SecondHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/SubjectSearch.html')
        lang = self.request.get('lang')
        print "PRINT ???? "+ lang

        self.response.out.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/resources', SecondHandler)
], debug=True)
