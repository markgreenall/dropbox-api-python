class datastore(object):

    def __init__(self, client):
        self.client = client

    """ Let's put a test file in the Dropbox """
    def put_file(self, contents, file_name):

        try:
            client = self.client() # Get the client object
        except Exception:
            print 'FAIL: Could not get the client object.'
            exit()

        try:
            if contents is "" or file_name is "":
                raise ValueError

            response = client.put_file(file_name, contents)
            print "RESPONSE: ", response
            print "PASS: File has been uploaded."

        except ValueError:
            print "FAIL: You must specify some content, and the file name in which to save it."
            exit()

    """ Let's put a test file in the Dropbox """
    def get_file(self, local_file, remote_file):

        try:
            client = self.client() # Get the client object
        except Exception:
            print 'FAIL: Could not get the client object.'
            exit()

        try:
            if local_file is "" or remote_file is "":
                raise ValueError

            try:
                out = open(local_file, 'wb')
                with client.get_file(remote_file) as f:
                    out.write(f.read())
                print "PASS: File has been downloaded and saved."

            except IOError:
                print "FAIL: There was a problem writing the downloaded file to disk."
                exit()

        except ValueError:
            print "FAIL: You must specify a file_name in which to get."
            exit()

    """ Let's put a test file in the Dropbox """
    def get_file_contents(self, remote_file):

        try:
            client = self.client() # Get the client object
        except Exception:
            print 'FAIL: Could not get the client object.'
            exit()

        try:
            if remote_file is "":
                raise ValueError

            try:
                with client.get_file(remote_file) as f:
                    content = f.read()
                print "PASS: File has been downloaded and saved."
                return content

            except IOError:
                print "FAIL: There was a problem writing the downloaded file to disk."
                exit()

        except ValueError:
            print "FAIL: You must specify a file_name in which to get."
            exit()
