'''unit tests for mf2tojf2.py '''

import mf2tojf2
import unittest

class BasicCheck(unittest.TestCase):
    def test_checkEmpty(self):
        self.assertEqual(mf2tojf2.mf2tojf2({}), {})
    def test_checkEmptyItems(self):
        self.assertEqual(mf2tojf2.mf2tojf2({"items":[]}), {})
    def test_checkEmptyHentry(self):
         self.assertEqual(mf2tojf2.mf2tojf2({"items":[{"type":["h-entry"]}]}), {'type':'entry'})
    def test_checkFlatHentry(self):
         self.assertEqual(mf2tojf2.mf2tojf2({"items":[{"type": ["h-entry"], "properties": {"url": ["http://kevinmarks.com/hwc2015-06-17.html"], "name": ["Homebrew Website Club notes 2015-06-17"], "published": ["2015-06-17"]}}]}), 
            {
            "type": "entry",
            "published": "2015-06-17",
            "name": "Homebrew Website Club notes 2015-06-17",
            "url": "http://kevinmarks.com/hwc2015-06-17.html"
            })
    def test_checkHentryeContent(self):
         self.assertEqual(mf2tojf2.mf2tojf2({"items":[{"type": ["h-entry"], "properties": 
                {"content":[{"html":"<p>this is <b>content</b>","value":"this is content"}],
                 "name": ["Homebrew Website Club"]}}]}), 
            {
            "type": "entry",
            "name": "Homebrew Website Club",
            "content": "this is content"
            })
    def test_checkHentryTextAuthor(self):
         self.assertEqual(mf2tojf2.mf2tojf2({"items":[{"type": ["h-entry"], "properties": 
                {"author":["fred bloggs"],
                 "name": ["Homebrew Website Club"]}}]}), 
            {
            "type": "entry",
            "name": "Homebrew Website Club",
            "author":"fred bloggs",
            })
    def test_checkHentryNestedAuthor(self):
         self.assertEqual(mf2tojf2.mf2tojf2({"items":[{"type": ["h-entry"], "properties": 
                {"author":[{"type":["h-card"],"properties": {"name":["fred bloggs"]}}],
                 "name": ["Homebrew Website Club"]}}]}), 
            {
            "type": "entry",
            "name": "Homebrew Website Club",
            "author": {"type":"card",
                        "name":"fred bloggs",}
            })

    def test_checkHfeedChildEntry(self):
         self.assertEqual(mf2tojf2.mf2tojf2({"items":[{"type": ["h-feed"], 
         "children":[{"type":["h-entry"],"properties":{"name":["short post"]}}], "properties": 
                {"author":[{"type":["h-card"],"properties": {"name":["fred blog"]}}],
                 "name": ["Homebrew Website Club"]}}]}), 
            {
            "type": "feed",
            "name": "Homebrew Website Club",
            "author": {"type":"card", "name":"fred blog",},
            "children":[
                {"type":"entry","name":"short post"}
                ],
            })

    def test_bareEntries(self):
         self.assertEqual(mf2tojf2.mf2tojf2({"items":[
                {"type":["h-entry"],"properties":{"name":["bare post"]}},
                {"type":["h-entry"],"properties":{"name":["longer bare post"]}},
                ]}), 
            {
            "children":[
                {"type":"entry","name":"bare post"},
                {"type":"entry","name":"longer bare post"},
                ],
            })

    def test_checkHfeed2ChildEntry(self):
         self.assertEqual(mf2tojf2.mf2tojf2({"items":[{"type": ["h-feed"], 
            "children":[{"type":["h-entry"],"properties":{"name":["short post"]}},
                        {"type":["h-entry"],"properties":{"name":["longer post"]}},
                        ], 
            "properties": 
                {"author":[{"type":["h-card"],"properties": {"name":["fred bloggs"]}}],
                 "name": ["Homebrew Website Club"]}}]}), 
            {
            "type": "feed",
            "name": "Homebrew Website Club",
            "author": {"type":"card", "name":"fred bloggs",},
            "children":[
                {"type":"entry","name":"short post"},
                {"type":"entry","name":"longer post"},
                ],
            })

class SpeckCheck(unittest.TestCase):
    def test_checkExample(self):
        self.assertEqual(mf2tojf2.mf2tojf2(
            {
              "items": [
                {
                  "type": [
                    "h-entry"
                  ],
                  "properties": {
                    "author": [
                      {
                        "type": [
                          "h-card"
                        ],
                        "properties": {
                          "name": [
                            "A. Developer"
                          ],
                          "url": [
                            "http://example.com"
                          ]
                        },
                        "value": "A. Developer"
                      }
                    ],
                    "name": [
                      "Hello World"
                    ],
                    "summary": [
                      "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus imperdiet ultrices pulvinar."
                    ],
                    "url": [
                      "http://example.com/2015/10/21"
                    ],
                    "published": [
                      "2015-10-21T12:00:00-0700"
                    ],
                    "content": [
                      {
                        "html": "<p>Donec dapibus enim lacus, <i>a vehicula magna bibendum non</i>. Phasellus id lacinia felis, vitae pellentesque enim. Sed at quam dui. Suspendisse accumsan, est id pulvinar consequat, urna ex tincidunt enim, nec sodales lectus nulla et augue. Cras venenatis vehicula molestie. Donec sagittis elit orci, sit amet egestas ex pharetra in.</p>",
                        "value": "Donec dapibus enim lacus, a vehicula magna bibendum non. Phasellus id lacinia felis, vitae pellentesque enim. Sed at quam dui. Suspendisse accumsan, est id pulvinar consequat, urna ex tincidunt enim, nec sodales lectus nulla et augue. Cras venenatis vehicula molestie. Donec sagittis elit orci, sit amet egestas ex pharetra in."
                      }
                    ]
                  }
                }
              ]
            }), 
            {
              "type": "entry",
              "author": {
                "type": "card",
                "url": "http://example.com",
                "name": "A. Developer"
              },
              "url": "http://example.com/2015/10/21",
              "published": "2015-10-21T12:00:00-0700",
              "name": "Hello World",
              "summary": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus imperdiet ultrices pulvinar.",
              "content": "Donec dapibus enim lacus, a vehicula magna bibendum non. Phasellus id lacinia felis, vitae pellentesque enim. Sed at quam dui. Suspendisse accumsan, est id pulvinar consequat, urna ex tincidunt enim, nec sodales lectus nulla et augue. Cras venenatis vehicula molestie. Donec sagittis elit orci, sit amet egestas ex pharetra in."
            })

if __name__ == '__main__':
    unittest.main()
