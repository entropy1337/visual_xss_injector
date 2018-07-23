from selenium import webdriver  
from selenium.webdriver.common.keys import Keys
import time
import gtk.gdk

##Setting the screenshotter###
w = gtk.gdk.get_default_root_window()
sz = w.get_size()

### setting up the web browser####
browser = webdriver.Firefox()
browser.get('http://localhost/xss.php')
time.sleep(2)

### Setting up the payload ####
count = 0
payloads = open('smalltest.txt','r').readlines()

### Open initial page ####
main_window = browser.current_window_handle
#Open new tab 

for payload in payloads:

	browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
	browser.get('http://localhost/xss.php?userinput='+str(payload))
	#Make a call to the webpage with payload and wait for a second.
	time.sleep(1)
	
	###take a screenshot ####
	pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
	pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
	if (pb != None):
		pb.save(str(count)+'-xss_payload.png',"png")
		#~ print "Screenshot saved to "+str(count)+'-xss_payload.png'
	else:
		print "Unable to get the screenshot."

	#Close New tab. The first tab remains open.
	browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w') 
	count = count +1
	
browser.quit()
