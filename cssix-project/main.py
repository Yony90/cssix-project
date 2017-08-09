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

#Set up Jinja Environment
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/main-html.html')
        self.response.out.write(template.render())


    def post(self):
        #Post info to DataStore
        blogPostInfo = BlogPost(subject=self.request.get('blogPostSubject'),text=self.request.get('blogPostText'))
        blogPostInfo.put()
        #Redirect back to main page to avoid blank page
        self.redirect('/')

class SecondHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/SubjectSearch.html')
        #grab language from GET
        lang = self.request.get('lang')
        #set up dictionary to mae dynamic template
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
        #create sub-dictionary from lang_info dicitonary
        subjectInfo = lang_info[lang] #{ lang : pngLink }

        #create query and filter
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
