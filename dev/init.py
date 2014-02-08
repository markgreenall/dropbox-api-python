from btConnector import connector

app_key    = '04qs1wgvgn99a7d'
app_secret = 'assbqqncsu0ts6i'

""" Instantiate Flow """
instance = connector(app_key, app_secret)
instance.negotiate() # Negotaite the authentication and client creation

""" Perform some file operations """
datastore = instance.datastore

# Define an test filename
file_name = "BoxTaper_TEST1.txt"

# Upload a file...
datastore.put_file("Hello this is a test", file_name)

# Download a file...
datastore.get_file(file_name)

