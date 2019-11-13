#!/usr/bin/env python3

import datetime
import os

def do_magic():
  now = datetime.datetime.now()
  return "Hello! {0}".format(now)

def application(env, start_response):
  start_response('200 OK', [('Content-Type','text/html')])
  return [do_magic()]

if __name__ == "__main__":
  if 'REQUEST_URI' in os.environ:
    print("Content-type: text/html\n\n")
  print(do_magic())
