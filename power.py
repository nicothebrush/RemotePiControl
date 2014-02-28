import time
import cgi
form = cgi.FieldStorage()
 
print "Content-Type: text/html"
print
print '<!doctype html>'
print '<title>Power</title>'
 
if not ("device" in form and "power" in form and "pass" in form):
    print "<p class=error> Incorrect params have been provided."
    print "<script>" 
    print "function goBack()"
    print "{"
    print "window.history.back()"
    print "}"
    print "</script>"
    print "<body>"
    print """<button onclick="goBack()">Go Back</button>"""
    print "</body>"
    exit() #end here if errors
 
device_id, power, powerOnTime = int(form['device'].value), form['power'].value, int(form['time'].value)
 
if not ('pass' in form and form['pass'].value == "p@ssw0rd"): 
	print "<p class=errr> Password is incorrect."
        exit() 

from tellcore.telldus import TelldusCore
core = TelldusCore()
devices = core.devices()
 
if not (power in ['off','on','time'] and
        device_id <= len(devices)):
        print "<p class=err> Incorrect values for the params have been provided."
        print "<script>"
        print "function goBack()"
        print "{"
        print "window.history.back()"
        print "}"
        print "</script>"
        print "<body>"
        print """<button onclick="goBack()">Go Back</button>"""
        print "</body>"
        exit() #end here if errors

device = devices[device_id]
if power == 'on':
    device.turn_on()
if power == 'off':
    device.turn_off()

if powerOnTime > 0:
    device.turn_on()
    time.sleep(powerOnTime)
    device.turn_off()
print '<p class=success> Device ID %s has been turned %s for %s seconds' % (device_id,power,powerOnTime)
print "<script>"
print "function goBack()"
print "{"
print "window.history.back()"
print "}"
print "</script>"
print "<body>"
print """<button onclick="goBack()">Go Back</button>"""
print "</body>"
