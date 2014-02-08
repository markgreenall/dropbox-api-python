# Include the Dropbox SDK
import dropbox

class BoxTaper(object):

    def __init__(self, key, secret):

        try:
            if key is '' or secret is "":
                raise ValueError

            self.app_key      = key
            self.app_secret   = secret
            self.access_token = ''
            self.access_token_file = 'OAuth.token'
            self.client       = ''

        except ValueError:
                print "FAIL: You must set both the app_key and the app_secret"
                exit()

    """ Authenticate the API """
    def authenticate(self):

        try:
            token = open(self.access_token_file).read()

            if token.startswith('key->'):
                self.access_token = token[len('key->'):]
                print "PASS: Loaded OAuth2 Key from File"

            else:
                print "FAIL: File is not formatted correctly."
                exit()

        except IOError:

            """ Get the auth key from the user """
            try:
                flow = dropbox.client.DropboxOAuth2FlowNoRedirect(self.app_key, self.app_secret)
                authorize_url = flow.start()

                print '1. Go to: ', authorize_url
                print '2. Click "Allow" (you might have to log in first)'
                print '3. Copy the authorization code.'

                code = raw_input("Enter the authorization code here: ").strip()

                if code is "":
                    raise ValueError

                """ Finish flow """
                access_token, user_id = flow.finish(code)

                """ Define into globals """
                self.access_token = access_token
                self.user_id      = user_id

                """ Write the token into the token file """
                try:
                    with open(self.access_token_file, 'w') as f:
                        f.write('key->' + access_token)
                        print "PASS: Written Key to Token File"

                except IOError:
                    print "FAIL: Could not save the OAuth token into the configured file."
                    exit()

            except ValueError:
                print "FAIL: You did not provide an authorisation code."
                exit()

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
        try:
            if contents is "" or file_name is "":
                raise ValueError

            response = self.client.put_file(file_name, contents)
            print "RESPONSE: ", response
            print "PASS: File has been uploaded."

        except ValueError:
            print "FAIL: You must specify some content, and the file name in which to save it."
            exit()

    """ Let's put a test file in the Dropbox """
    def get_file(self, file_name):
        try:
            if file_name is "":
                raise ValueError

            try:
                out = open(file_name, 'wb')
                with self.client.get_file(file_name) as f:
                    out.write(f.read())
                print "PASS: File has been downloaded and saved."

            except IOError:
                print "FAIL: There was a problem writing the downloaded file to disk."
                exit()

        except ValueError:
            print "FAIL: You must specify a file_name in which to get."
            exit()


app_key    = '04qs1wgvgn99a7d'
app_secret = 'assbqqncsu0ts6i'

""" Instantiate Flow """
engine = BoxTaper(app_key, app_secret)

""" Negotaite the authentication and client creation """
engine.negotiate()

""" Define an test filename """
file_name = "BoxTaper_TEST1.txt"

""" Upload some test text """
engine.put_file("Hello this is a test", file_name)

""" Download the file  and save it """
engine.get_file(file_name)

