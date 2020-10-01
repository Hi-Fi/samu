*** Settings ***
Library         Collections
Library         Process
Library         RequestsLibrary
Suite Setup     Start local server
Suite Teardown  Stop local server

*** Variables ***

*** Test cases ***
Valid request
    ${resp}                             Post Request    test_api    /v1/samu    json=aa ii aa oo
    Request Should Be Successful        ${resp}
    Should Be Equal As Strings          ${resp.json()}          ii aa oo aa

Invalid request
    ${resp}                             Post Request           test_api    /v1/samu
    Should Be Equal As Integers         ${resp.status_code}    400
    
*** Keywords ***
Start local server
    Start Process   pipenv         run                     prod
    Create Session  test_api       http://localhost:8000
    Process Should Be Running
    Wait Until Keyword Succeeds    10s                     1s    Check server healthy    test_api

Stop local server
    Terminate All Processes     kill=${True}

Check server healthy
    [Arguments]    ${connection alias}
    [Teardown]     Set Log Level    ${log_level}
    Comment        Not logging other than errors, as library prints out failed connections as warn
    ${log_level}   Set Log Level        ERROR
    ${resp}        Get Request          ${connection alias}    /healthz
    Request Should Be Successful        ${resp}