*** Settings ***
Library    SeleniumLibrary
Library    FPScreenshot.py
Library    Env.py
Library    SSpy1.py
Library    SSstep1.py
*** Test Cases ***
Get FUll Page Screenshot
    environmentSetup
    OPEN BROWSER    https://pypi.org/project/robotframework-jsonvalidator/    headlesschrome
    maximize browser window
    capture

