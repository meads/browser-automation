import time
from enum import Enum

import pyperclip
import pyautogui as rpa; rpa.PAUSE = 2.5
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class DevToolsDock(Enum):
    Right = 1
    Bottom = 2
    Left = 3
    Undock = 4
dock_pos = {}
dock_pos[DevToolsDock.Right] = "dock right"
dock_pos[DevToolsDock.Bottom] = "dock bottom"
dock_pos[DevToolsDock.Left] = "dock left"
dock_pos[DevToolsDock.Undock] = "undock"

class DevToolsRendering(Enum):
    EmulateCssPrintMediaType = 1
    EmulateCssPrefersColorSchemeLight = 2
    EmulateCssPrefersColorSchemeDark = 3
    EmulateCssPrefersReducedMotionReduce = 4
    EmulateNoVisionDeficiency = 5
    EmulateDeuteranopia = 6
    EmulateTritanopia = 7
    EmulateAchromatopsia = 8
    EmulateProtanopia = 9
    EmulateAFocusedPage = 10
    HighlightAdFrames = 11
    DisableLocalFonts = 12
    ShowFramesPerSecondMeter = 13
    ShowHitTestBorders = 14
    ShowLayoutShiftRegions = 15
    ShowPaintFlashingRectanges = 16
    ShowScrollPerformanceBottlenecks = 17
render_opts = {}
render_opts[DevToolsRendering.EmulateCssPrintMediaType] = "emulate css print"
render_opts[DevToolsRendering.EmulateCssPrefersColorSchemeLight] = "emulate css prefers-color-scheme light"
render_opts[DevToolsRendering.EmulateCssPrefersColorSchemeDark] = "emulate css prefers-color-scheme dark"
render_opts[DevToolsRendering.EmulateCssPrefersReducedMotionReduce] = "emulate css prefers-reduced-motion"
render_opts[DevToolsRendering.EmulateNoVisionDeficiency] = "do not emulate any vision deficiency"
render_opts[DevToolsRendering.EmulateDeuteranopia] = "emulate deuteranopia"
render_opts[DevToolsRendering.EmulateTritanopia] = "emulate tritanopia"
render_opts[DevToolsRendering.EmulateAchromatopsia] = "emulate achromatopsia"
render_opts[DevToolsRendering.EmulateProtanopia] = "emulate protanopia"
render_opts[DevToolsRendering.EmulateAFocusedPage] = "emulate a focused page"
render_opts[DevToolsRendering.HighlightAdFrames] = "highlight ad frames"
render_opts[DevToolsRendering.DisableLocalFonts] = "disable local fonts"
render_opts[DevToolsRendering.ShowFramesPerSecondMeter] = "show frames per sec"
render_opts[DevToolsRendering.ShowHitTestBorders] = "show hit-test borders"
render_opts[DevToolsRendering.ShowLayoutShiftRegions] = "show layout shift regions"
render_opts[DevToolsRendering.ShowPaintFlashingRectanges] = "show paint flashing rectangles"
render_opts[DevToolsRendering.ShowScrollPerformanceBottlenecks] = "show scroll performance bottlenecks"

class DevToolsAppearance(Enum):
    SwitchToDarkTheme = 1
    SwitchToLightTheme = 2
appearance_opts = {}
appearance_opts[DevToolsAppearance.SwitchToDarkTheme] = "switch to dark theme"
appearance_opts[DevToolsAppearance.SwitchToLightTheme] = "switch to light theme"    


def devtools_customize():
    devtools_appearance(DevToolsAppearance.SwitchToDarkTheme)
    devtools_command_palette("reload devtools")
    # devtools_rendering(DevToolsRendering.ShowPaintFlashingRectanges)
    # devtools_rendering(DevToolsRendering.ShowHitTestBorders)

def devtools_dock(pos: DevToolsDock):
    devtools_command_palette(dock_pos[pos])

def devtools_rendering(opt: DevToolsRendering):
    devtools_command_palette(render_opts[opt])

def devtools_appearance(opt: DevToolsAppearance):
    devtools_command_palette(appearance_opts[opt])



def devtools_inspect():
    # devtools_customize()
    rpa.hotkey("ctrl", "shift", "c")

def devtools_command_palette(cmd):
    devtools_command_palette_open()
    rpa.typewrite(cmd,interval=0)
    rpa.press("enter")

def devtools_command_palette_open():
    rpa.hotkey("ctrl", "shift", "p", interval=0.25)



def copy(text):
    pyperclip.copy("")
    pyperclip.copy(text)

def paste() -> str:
    v = pyperclip.paste()
    pyperclip.copy("")
    return v

def console(expression):
    devtools_command_palette_open()
    rpa.typewrite("show console")
    rpa.press("enter")
    rpa.typewrite(expression)
    rpa.press("enter")

def console_paste(x):
    rpa.typewrite(x)
    rpa.press("enter")


# https://developers.google.com/web/tools/chrome-devtools/console/utilities 
def inspect_element(x, y):
    devtools_inspect()
    console('function xpathFromElement(e){var n=e;if(n.id)return\'//*[@id="\'+n.id+\'"]\';for(var r=[];n&&n.nodeType===Node.ELEMENT_NODE;){for(var i=0,o=!1,a=n.previousSibling;a;)a.nodeType!==Node.DOCUMENT_TYPE_NODE&&a.nodeName===n.nodeName&&i++,a=a.previousSibling;for(a=n.nextSibling;a;){if(a.nodeName===n.nodeName){o=!0;break}a=a.nextSibling}var d=n.prefix?n.prefix+":":"",N=i||o?"["+(i+1)+"]":"";r.push(d+n.localName+N),n=n.parentNode}return r.length?"/"+r.reverse().join("/"):""}')
    console_paste("$0")
    # _ = rpa.screenshot("command_result1.png")
    # time.sleep(2)
    rpa.press("enter")
    # _ = rpa.screenshot("command_result2.png")
    # time.sleep(2)

    console("copy(xpathFromElement($0))")
    xpath_selector = paste()
    # time.sleep(2)

    devtools_command_palette("show elements")
    rpa.hotkey("ctrl", "f")
    rpa.typewrite(xpath_selector)
    # _ = rpa.screenshot("xpath_inspect_result1.png") 
    # time.sleep(4)
    rpa.press("enter")
    # _ = rpa.screenshot("xpath_inspect_result2.png") 
    # time.sleep(4)
    
    return xpath_selector



try:
    chrome = webdriver.Chrome()
    chrome.get('https://www.google.com')
    chrome.maximize_window()

    # launch the devtools with current mouse position being inspected
    devtools_inspect()

    # hover and click on some element at x,y
    rpa.moveTo(280, 290, 2, rpa.easeInOutQuad, logScreenshot=True)
    
    # get the current position of the mouse
    x, y = rpa.position()
    # location = rpa.locateOnScreen('/home/ubuntu/dev/rpa_browser/images/console.png')

    # point = rpa.center(location)
    # x, y = point
    rpa.click(x, y)

    # inspect the element at current mouse position
    xpath_selector = inspect_element(x, y)
    print(f"This is xpath... {xpath_selector}")
    rpa.moveTo(380, 390, 2, rpa.easeInOutQuad)
    rpa.moveTo(280, 290, 2, rpa.easeInOutQuad)
    # rpa.screenshot('inspect_element1.png')
    
    # time.sleep(4)

except rpa.ImageNotFoundException as e:
    raise e
except Exception as e:
    raise e
finally:
    chrome.quit()
