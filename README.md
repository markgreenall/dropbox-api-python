# dropbox-api-python

Example of using the Dropbox Python SDK to connect and store a file.

## Documentation

### Prerequisites
+ Python 2 / 3
+ Dropbox Python API SDK

### Initialise!
To get started we want to instantiate the class and negotiate a connection.

    from btConnector import connector

    app_key    = '04qs1wgvgn99a7d'
    app_secret = 'assbqqncsu0ts6i'

    """ Instantiate Flow """
    instance = connector(app_key, app_secret)

### Authenticate & Instantiate
You can run the negotiate function which will auhenticate and then create the flow object, like so...

    engine.negotiate()

...or you can run the two seperately if you want to modularise the process, like so...

    engine.authenticate()
    engine.instantiate()

### Instantiate the Datastore Object
    datastore = instance.datastore

### Perform actions on the datastore

    # Define an test filename
    file_name = "BoxTaper_TEST1.txt"

    # Upload a file...
    datastore.put_file("Hello this is a test", file_name)

    # Download a file...
    datastore.get_file(file_name)

## Information

### Token Storage
Currently the app will store the token in a plain text file within the same launch directory. As this is only an example this is fine, but you should consider sotring this securely for a production environment.

### Dropbox API Status
The app is currently in development mode (with the included key and secret).  Please use your own app details if possible.
