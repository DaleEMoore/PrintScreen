__author__ = 'dalem'
# From http://stackoverflow.com/questions/4589206/python-windows-7-screenshot-without-pil

import win32gui, win32ui, win32con, win32api

iteration = 1

# TODO; Capture PrintScreen and AltPrintScreen button pushes.
# http://stackoverflow.com/questions/17832717/python-auto-save-printscreen
# http://schurpf.com/python/python-hotkey-module/
# https://github.com/schurpf/pyhk
# http://stackoverflow.com/questions/tagged/pyhook
# http://stackoverflow.com/questions/18972716/unable-to-install-pyhook-and-pywin32
# https://github.com/schurpf/pyhk
# http://timgolden.me.uk/python/win32_how_do_i/catch_system_wide_hotkeys.html
# https://github.com/idachev/python-utils/
# https://pypi.python.org/pypi/PyScreeze/0.1.0
# http://www.blog.pythonlibrary.org/2010/04/16/how-to-take-a-screenshot-of-your-wxpython-app-and-print-it/
# https://pypi.python.org/pypi/pyHook/1.5.1
# http://sourceforge.net/p/pyhook/wiki/Main_Page/
# http://sourceforge.net/p/pyhook/wiki/PyHook_Tutorial/
# http://sourceforge.net/projects/pyhook/
# http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyhook



def main():
    global iteration
    hwin = win32gui.GetDesktopWindow()
    width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
    height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
    left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
    top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
    hwindc = win32gui.GetWindowDC(hwin)
    srcdc = win32ui.CreateDCFromHandle(hwindc)
    memdc = srcdc.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(srcdc, width, height)
    memdc.SelectObject(bmp)
    memdc.BitBlt((0, 0), (width, height), srcdc, (left, top), win32con.SRCCOPY)
    # TODO; warn that I'm overwriting existing files.
    # the file name increments.
    print(str(iteration))
    # TODO; save as PNG or JPG?
    bmp.SaveBitmapFile(memdc, 'screenshot' + str(iteration) + '.bmp')
    iteration += 1
    #bmp.SaveBitmapFile(memdc, 'screenshot.bmp')

if __name__ == "__main__":
    main()