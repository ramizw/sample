*** Settings ***

Library    Zoomba.GUILibrary     plugins=Zoomba.Helpers.EdgePlugin
Library    Zoomba.GUILibrary     plugins=Zoomba.Helpers.EdgePlugin
*** Variables ***
${Browser}    chrome
${URL}    https://pypi.org/
${BrowserFF}    firefox
${BrowserEdge}    edge
#python -m robot TC1.robot
*** Test Cases ***
Test Case Different Browsers
    Open Browser   ${URL}   browser=Edge     options=use_chromium=True

