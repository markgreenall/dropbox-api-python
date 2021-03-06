from boxtaper.core import connector

app_key    = '04qs1wgvgn99a7d'
app_secret = 'assbqqncsu0ts6i'

""" Instantiate Flow """
instance = connector(app_key, app_secret)
instance.negotiate() # Negotaite the authentication and client creation

""" Perform some file operations """

# Instantiate the datastore object...
datastore = instance.datastore

# Define test filenames...
file_name  = "BoxTaper_TEST1.txt"
local_file = "./tmp/myTest.txt"

# Upload a file...
datastore.put_file("Hello this is a test", file_name)

# Download a file...
datastore.get_file(local_file, file_name)

# Download a file's contents...
content = datastore.get_file_contents(file_name)
print "FILE CONTENTS: %s" % (content)

# Create and delete a folder...
remote_folder = "WoopWoopTest"
datastore.create_folder(remote_folder)
datastore.delete_folder(remote_folder)
