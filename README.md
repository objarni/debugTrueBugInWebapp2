debugTrueBugInWebapp2
=====================

Minimal webapp2 app showing a possible bug

The bug has been reported to googleappengine issue list, link: https://code.google.com/p/googleappengine/issues/detail?id=11557

Run
---
    dev_appserver.py debugTrueBugInWebapp2

.. then point your browser to http://localhost:8080.

The expected behaviour is for the browser to print a stack trace.

What is really happening is that the stack trace is shown in terminal window, and the browser shows a blank page.


Environment
-----------

I'm on an Ubuntu14.04-64 bit system with default Python2.7 installation, using latest version of Google App Server.

Details:

    $ cat /etc/*-release
    DISTRIB_ID=Ubuntu
    DISTRIB_RELEASE=14.04
    DISTRIB_CODENAME=trusty
    DISTRIB_DESCRIPTION="Ubuntu 14.04.1 LTS"
    NAME="Ubuntu"
    VERSION="14.04.1 LTS, Trusty Tahr"
    ID=ubuntu
    ID_LIKE=debian
    PRETTY_NAME="Ubuntu 14.04.1 LTS"
    VERSION_ID="14.04"
    HOME_URL="http://www.ubuntu.com/"
    SUPPORT_URL="http://help.ubuntu.com/"
    BUG_REPORT_URL="http://bugs.launchpad.net/ubuntu/"

    $ python -V
    Python 2.7.6

    $ which dev_appserver.py 
    /home/olof/google_appengine/dev_appserver.py
    
    $ cat /home/olof/google_appengine/VERSION
    release: "1.9.17"
    timestamp: 1415734244
    api_versions: ['1']
    supported_api_versions:
      python:
        api_versions: ['1']
      python27:
        api_versions: ['1']
      go:
        api_versions: ['go1']
      java7:
        api_versions: ['1.0']


