"""
PrintScreen program to capture the screen to a graphics file in a
folder when the PrintScreen button is pressed.
"""
__author__ = 'dalem'

import os
import pythoncom, pyHook
import withWIN32

def OnKeyboardEvent(event):
    caughtYet = False
    if event.KeyID == 44 and event.ScanCode == 55 and event.Alt == 0: # PrintScreen
        caughtYet = True
        print("PrintScreen key pressed")
        withWIN32.main()
    if event.KeyID == 44 and event.ScanCode == 84 and event.Alt == 32: # AltPrintScreen
        caughtYet = True
        print("AltPrintScreqen key pressed")
        withWIN32.main()
    if event.KeyID == 81 and event.ScanCode == 16 and event.Alt == 0: # q for Quit
        caughtYet = True
        print("q for Quit pressed")
        exit()
    if not caughtYet:
        print 'MessageName:',event.MessageName
        print 'Message:',event.Message
        print 'Time:',event.Time
        print 'Window:',event.Window
        print 'WindowName:',event.WindowName
        print 'Ascii:', event.Ascii, chr(event.Ascii)
        print 'Key:', event.Key
        print 'KeyID:', event.KeyID
        print 'ScanCode:', event.ScanCode
        print 'Extended:', event.Extended
        print 'Injected:', event.Injected
        print 'Alt', event.Alt
        print 'Transition', event.Transition
        print '---'

# return True to pass the event to other handlers
    return True

if __name__ == "__main__":
    if os.name == "nt":
        print("Yea Windows, I run here.")
    else:
        print("Bummer; I don't run here " + os.name + "!")
        exit()

    # create a hook manager
    hm = pyHook.HookManager()
    # watch for all mouse events
    hm.KeyDown = OnKeyboardEvent
    # set the hook
    hm.HookKeyboard()
    print("Waiting for key press...")
    # wait forever
    pythoncom.PumpMessages()

    #withWIN32.main()
    #withWIN32.main()
    #main()
"""
--- PrintScreen key:
MessageName: key down
Message: 256
Time: 103725111
Window: 721360
WindowName: PrintScreen - [C:\Users\dalem\PycharmProjects\PrintScreen] - ...\main.py - PyCharm Community Edition 3.4.1
Ascii: 0  
Key: Snapshot
KeyID: 44
ScanCode: 55
Extended: 1
Injected: 0
Alt 0
Transition 0

--- AltPrintScreen key:
MessageName: key sys down
Message: 260
Time: 103782738
Window: 721360
WindowName: PrintScreen - [C:\Users\dalem\PycharmProjects\PrintScreen] - ...\main.py - PyCharm Community Edition 3.4.1
Ascii: 0  
Key: Snapshot
KeyID: 44
ScanCode: 84
Extended: 0
Injected: 0
Alt 32
Transition 0

--- q for Quit key:
MessageName: key down
Message: 256
Time: 104151072
Window: 721360
WindowName: PrintScreen - [C:\Users\dalem\PycharmProjects\PrintScreen] - ...\main.py - PyCharm Community Edition 3.4.1
Ascii: 113 q
Key: Q
KeyID: 81
ScanCode: 16
Extended: 0
Injected: 0
Alt 0
Transition 0
"""

