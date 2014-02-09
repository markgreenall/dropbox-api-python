# dropbox-api-python

Example of using the Dropbox Python SDK to connect and store a file.

## Documentation

### Prerequisites
+ Python 2 / 3
+ Dropbox Python API SDK

### Initialise!
To get started we want to instantiate the class and negotiate a connection.

    from boxtaper.core import connector

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

### Get the account details for the authenticated user
Note the it's the instance object that is used to get this information.

    print instance.getAccountDetails()

### Perform actions on the datastore

#### Upload a file
Provides a response from the Dropbox API but you don't need to capture this.

    # Define test filenames...
    file_name  = "BoxTaper_TEST1.txt"

    # Upload a file...
    datastore.put_file("Hello this is a test", file_name)

Important: This will NOT fail if the remote resource already exists, it will simply overwrite the destination file.

#### Download a file
Does not provide a response, instead saves the file to the local_file destination.

    # Define test filenames...
    local_file = "myTest.txt"
    file_name  = "BoxTaper_TEST1.txt"

    # Download a file...
    datastore.get_file(local_file, file_name)

Important: This may fail if the remote resource does not exist.

#### Download a file's content
Provides response with the contents of the file.

    # Define test filenames...
    file_name  = "BoxTaper_TEST1.txt"

    # Download a file's contents...
    content = datastore.get_file_contents(file_name)
    print "FILE CONTENTS: %s" % (content)

Important: This may error if the remote resource does not exist.

#### Delete a file
This function provides a Dropbox API response, you don't need to capture this, it will work asychronously.

    # Delete a file...
    remote_file = "myTest.txt"
    datastore.delete_file(remote_file)

Important: This may error if the remote resource does not exist, it cannot delete something which doesn't exist, so fails.

#### Create a folder
This function provides a Dropbox API response, you don't need to capture this, it will work asychronously.

    # Create a folder...
    remote_folder = "myTestFolder"
    datastore.create_folder(remote_folder)

Important: This may error if the remote resource already exists, it cannot create something which already exists, so fails.

#### Delete a folder
This function provides a Dropbox API response, you don't need to capture this, it will work asychronously.

    # Delete a folder...
    remote_folder = "myTestFolder"
    datastore.delete_folder(remote_folder)

Important: This may error if the remote resource does not exist, it cannot delete something which doesn't exist, so fails.

## Information

### Token Storage
Currently the app will store the token in a plain text file within the same launch directory. As this is only an example this is fine, but you should consider sotring this securely for a production environment.

### Dropbox API Status
The app is currently in development mode (with the included key and secret).  Please use your own app details if possible.
