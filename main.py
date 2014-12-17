"""
PrintScreen program to capture the screen to a graphics file in a
folder when the PrintScreen button is pressed.
"""
__author__ = 'dalem'

# From http://www.blendedtechnologies.com/quick-screenshots-script-python-pil/38
"""
Simple script to capture your screen, save it named with today's date and then
open it to allow editing and markup (circle problems, etc)

Created by Greg Pinero (gregpinero@gmail.com) Spring 2005

To run this you'll need:
>Python Imaging Library (PIL) -http://www.pythonware.com/products/pil/
>Python 2.3 or later - http://www.python.org
>Windows?
"""
import os
import sys
import time
import Image
import ImageGrab
#---------------------------------------------------------
#User Settings:
SaveDirectory=r'C:\Documents and Settings\Gregory\Desktop'
ImageEditorPath=r'C:\WINDOWS\system32\mspaint.exe'
#Here is another example:
#ImageEditorPath=r'C:\Program Files\IrfanView\i_view32.exe'
#---------------------------------------------------------

img=ImageGrab.grab()
saveas=os.path.join(SaveDirectory,'ScreenShot_'+time.strftime('%Y_%m_%d%_%H_%M_%S')+'.jpg')
img.save(saveas)
editorstring='""%s" "%s"'% (ImageEditorPath,saveas) #Just for Windows right now?
#Notice the first leading " above? This is the bug in python that no one will admit...
os.system(editorstring)


# From http://stackoverflow.com/questions/2846947/get-screenshot-on-windows-with-python
# pip install wx
# pip install wxPython
# No package for wx or wxPython
#import wx
#app = wx.App()  # Need to create an App instance before doing anything
#screen = app.ScreenDC()
#size = screen.GetSize()
#bmp = app.EmptyBitmap(size[0], size[1])
#mem = app.MemoryDC(bmp)
#mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
#del mem  # Release bitmap
#bmp.SaveFile('screenshot.png', app.BITMAP_TYPE_PNG)

#app = wx.App()  # Need to create an App instance before doing anything
#screen = wx.ScreenDC()
#size = screen.GetSize()
#bmp = wx.EmptyBitmap(size[0], size[1])
#mem = wx.MemoryDC(bmp)
#mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
#del mem  # Release bitmap
#bmp.SaveFile('screenshot.png', wx.BITMAP_TYPE_PNG)
