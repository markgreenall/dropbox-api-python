# Include the Dropbox SDK
import dropbox

class BoxTaper(object):

    def __init__(self, key, secret):
        self.app_key      = key
        self.app_secret   = secret
        self.access_token = ''
        self.access_token_file = 'OAuth.token'
        self.client       = ''

    """ Authenticate the API """
    def authenticate(self):

        try:
            token = open(self.access_token_file).read()

            if token.startswith('key->'):
                self.access_token = token[len('key->'):]
                print "PASS: Loaded OAuth2 Key from File"

            else:
                print "FAIL: File is not formatted correctly."

        except IOError:

            flow = dropbox.client.DropboxOAuth2FlowNoRedirect(self.app_key, self.app_secret)
            authorize_url = flow.start()

            print '1. Go to: ' + authorize_url
            print '2. Click "Allow" (you might have to log in first)'
            print '3. Copy the authorization code.'

            """ Get the auth key from the user """
            code = raw_input("Enter the authorization code here: ").strip()

            """ Finish flow """
            access_token, user_id = flow.finish(code)

            """ Define into globals """
            self.access_token = access_token
            self.user_id      = user_id

            """ Write the token into the token file """
            with open(self.access_token_file, 'w') as f:
                f.write('key->' + access_token)
                print "PASS: Written Key to Token File"

    """ Instantiate the client """
    def instantiate(self):
        print "ACTION: Instantiating with access code '" + self.access_token + "'..."
        self.client = dropbox.client.DropboxClient(self.access_token)

    """ Get the account details """
    def getAccountInfo(self):
        print self.client.account_info()

    """ Authenticate and instantiate """
    def negotiate(self):
        engine.authenticate()
        engine.instantiate()

    """ Let's put a test file in the Dropbox """
    def put_file(self, contents, file_name):
        response = self.client.put_file(file_name, contents)
        print "RESPONSE:\n", response, "\n"


app_key    = '04qs1wgvgn99a7d'
app_secret = 'assbqqncsu0ts6i'

""" Instantiate Flow """
engine = BoxTaper(app_key, app_secret)

""" Negotaite the authentication and client creation """
engine.negotiate()

""" Upload some test text """
contents  = 'Hello this is a test'
file_name = "BoxTaper_TEST1.txt"
engine.put_file(contents, file_name)

