*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    Env.py
#Library    Zoomba.GUILibrary     plugins=Zoomba.Helpers.EdgePlugin
*** Variables ***
${Browser}    chrome
${URL}    https://pypi.org/
${BrowserFF}    firefox
${BrowserEdge}    Edge

*** Test Cases ***
Test Case Different Browsers
    environmentSetup
    open browser    ${URL}    ${Browser}
    open browser    ${URL}    ${BrowserFF}
    #open browser    ${URL}    ${BrowserEdge}    options=use_chromium=True

