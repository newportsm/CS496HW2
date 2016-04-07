#!/usr/bin/env python

import webapp2

app = webapp2.WSGIApplication([
    ('/view', 'view.View'),
    ('/edit', 'edit.Edit'),
    ('/', 'admin.Admin'),
], debug=True)
