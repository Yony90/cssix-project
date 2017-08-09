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


        postInfoList = ['C++ is an object-oriented programming (OOP) language that is viewed by many as the best language for creating large-scale applications. C++ is a superset of the C language.',
        "An interpreted language, Python has a design philosophy that emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than curly brackets or keywords), and a syntax that allows programmers to express concepts in fewer lines of code than might be used in languages such as C++",
        "an object-oriented computer programming language commonly used to create interactive effects within web browsers."]

        self.response.out.write(template.render())
    def post(self):
        blogPostInfo = BlogPost(subject=self.request.get('blogPostSubject'),text=self.request.get('blogPostText'))
        blogPostInfo.put()

        self.redirect('/')

class SecondHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/SubjectSearch.html')

        lang = self.request.get('lang')

        lang_info = {
          'python': {
             'lang': 'Python',
             'pngLink': 'https://techspawn.com/wp-content/uploads/2016/10/Python_logo.png'
          },
          'cplusplus': {
             'lang': 'C++',
             'pngLink': "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/C_plus_plus.svg/1200px-C_plus_plus.svg.png"
          },
          'javascript': {
             'lang': 'JavaScript',
             'pngLink': "https://cdn-images-1.medium.com/max/1600/1*ot7tWiPCYC01pV0kGmK3qQ.png"
          }
        }

        subjectInfo = lang_info[lang] #{ lang : pngLink }

        items_query = BlogPost.query()
        test = items_query.filter(subjectInfo['lang'] == BlogPost.subject)
        print test
        items = test.fetch()
        print items
        for item in items:
            print item.text
        # query_filtered = items.filter("subject IN", lang)
        # for item in items:
        #     if lang in item.
        #     for txt in item:
        #         print txt
        # query_filtered = items_query.filter("subject IN", lang)

        # items = query_filtered.fetch()

        # logging.info(items)

        self.response.out.write(template.render(subjectInfo))
#existing_item_query = ShoppingItem.query(ShoppingItem.name==item_name)
#existing_item = existing_item_query.get()  --- for first item, use .fetch() for all
#   if

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/resources', SecondHandler)
], debug=True)
