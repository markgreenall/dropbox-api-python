class datastore(object):

    def __init__(self, client):
        self.client = client

    """ Put a file in the datastore """
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
            print "PASS: File has been uploaded."
            return response

        except ValueError:
            print "FAIL: You must specify some content, and the file name in which to save it."
            exit()

    """ Delete a file from the datastore """
    def delete_file(self, remote_file):

        try:
            client = self.client() # Get the client object
        except Exception:
            print 'FAIL: Could not get the client object.'
            exit()

        try:
            if remote_file is "":
                raise ValueError

            try:
                response = client.file_delete(remote_file)
                print "PASS: File has been deleted."
                return response

            except Exception:
                print "FAIL: There was a problem deleting the file from the datastore."
                exit()

        except ValueError:
            print "FAIL: You must specify the remote file name in which to delete."
            exit()

    """ Download and save a file from the datastore """
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

    """ Get contents of a file in the datastore """
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
                print "PASS: File has been downloaded."
                return content

            except IOError:
                print "FAIL: There was a problem writing the downloaded file to disk."
                exit()

        except ValueError:
            print "FAIL: You must specify a file_name in which to get."
            exit()

    """ Create a folder in the datastore """
    def create_folder(self, remote_folder):

        try:
            client = self.client() # Get the client object
        except Exception:
            print 'FAIL: Could not get the client object.'
            exit()

        try:
            if remote_folder is "":
                raise ValueError

            try:
                response = client.file_create_folder(remote_folder)
                print "PASS: Folder has been created."
                return response

            except Exception:
                print "FAIL: There was a problem creating the folder in the datastore, It might already exist!"
                exit()

        except ValueError:
            print "FAIL: You must specify the remote folder name in which to create."
            exit()

    """ Delete a file from the datastore """
    def delete_folder(self, remote_folder):

        try:
            client = self.client() # Get the client object
        except Exception:
            print 'FAIL: Could not get the client object.'
            exit()

        try:
            if remote_folder is "":
                raise ValueError

            try:
                response = client.file_delete(remote_folder)
                print "PASS: File has been deleted."
                return response

            except Exception:
                print "FAIL: There was a problem deleting the file from the datastore."
                exit()

        except ValueError:
            print "FAIL: You must specify the remote file name in which to delete."
            exit()
