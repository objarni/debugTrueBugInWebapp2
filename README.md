debugTrueBugInWebapp2
=====================

Minimal webapp2 app showing a possible bug

Run
---
    dev_appserver.py debugTrueBugInWebapp2

.. then point your browser to http://localhost:8080.

The expected behaviour is for the browser to print a stack trace.

What is really happening is that the stack trace is shown in terminal window, and the browser shows a blank page.

