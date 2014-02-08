dropbox-api-python
==================

Example of using the Dropbox Python SDK to connect and store a file.

Prerequisites
===========
+ Python 3
+ Dropbox Python API SDK

Documentation
=============

Instantiate the class
---------------------

    engine = BoxTaper(app_key, app_secret)

Authenticate & Instantiate
--------------------------
You can run the negotiate function which will auhenticate and then create the flow object, like so...

    engine.negotiate()

...or you can run the two seperately if you want to modularise the process, like so...

    engine.authenticate()
    engine.instantiate()

Upload a File
-------------
You will once authenticated want to upload a file...

    engine.put_file(file_contents, file_name)

Download a File
---------------
You might also want to download a file...

    engine.get_file(file_name)


