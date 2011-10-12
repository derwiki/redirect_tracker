import logging
import sys
import json
import time

from vendor.bottle import bottle
from vendor.bottle.bottle import request
from vendor.bottle.bottle import route

bottle.debug(True)
log = logging.getLogger('servlet')
log.setLevel(logging.DEBUG)

@route('/track/:step')
def track(step):
  time.sleep(1)
  bottle.redirect('/track/%i' % (int(step)+1))


port = sys.argv[1] if len(sys.argv) > 1 else 8080
bottle.run(host='0.0.0.0', port=port)
