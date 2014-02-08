# Import the Dropbox API SDK
import dropbox
from btDatastore import datastore

class connector(object):

    def __init__(self, key, secret):

        try:
            if key is '' or secret is "":
                raise ValueError

            self.app_key      = key
            self.app_secret   = secret
            self.access_token = ''
            self.access_token_file = 'OAuth.token'
            self.client       = ''
            self.datastore    = datastore(self.handover)

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
        self.authenticate()
        self.instantiate()

    def handover(self):
        return self.client


