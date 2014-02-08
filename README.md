# dropbox-api-python

Example of using the Dropbox Python SDK to connect and store a file.

## Documentation

### Prerequisites
+ Python 2 / 3
+ Dropbox Python API SDK

### Instantiate the class

    engine = BoxTaper(app_key, app_secret)

### Authenticate & Instantiate
You can run the negotiate function which will auhenticate and then create the flow object, like so...

    engine.negotiate()

...or you can run the two seperately if you want to modularise the process, like so...

    engine.authenticate()
    engine.instantiate()

### Upload a File
You will once authenticated want to upload a file...

    engine.put_file(file_contents, file_name)

### Download a File
You might also want to download a file...

    engine.get_file(file_name)

## Information

### Token Storage
Currently the app will store the token in a plain text file within the same launch directory. As this is only an example this is fine, but you should consider sotring this securely for a production environment.

### Dropbox API Status
The app is currently in development mode (with the included key and secret).  Please use your own app details if possible.
