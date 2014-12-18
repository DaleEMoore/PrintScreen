"""
PrintScreen program to capture the screen to a graphics file in a
folder when the PrintScreen button is pressed.
"""
__author__ = 'dalem'

# From http://stackoverflow.com/questions/2846947/get-screenshot-on-windows-with-python
# pip install wx
# pip install wxPython
# No package for wx or wxPython
import wx
app = wx.App()  # Need to create an App instance before doing anything
screen = app.ScreenDC()
size = screen.GetSize()
bmp = app.EmptyBitmap(size[0], size[1])
mem = app.MemoryDC(bmp)
mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
del mem  # Release bitmap
bmp.SaveFile('screenshot.png', app.BITMAP_TYPE_PNG)

#app = wx.App()  # Need to create an App instance before doing anything
#screen = wx.ScreenDC()
#size = screen.GetSize()
#bmp = wx.EmptyBitmap(size[0], size[1])
#mem = wx.MemoryDC(bmp)
#mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
#del mem  # Release bitmap
#bmp.SaveFile('screenshot.png', wx.BITMAP_TYPE_PNG)
