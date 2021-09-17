from os import access
import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token= access_token

    def upload_file(self,file_from, file_to):
        dbx= dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
        access_token = 'sl.A4q1cDxWYUejpQPAXa9k-_Fj4l0xHpALdqJhB4ctlBdqQFCPY1YRDwN28GupL9I3bb74CqkHkOy9V8b-HDNp8xIMwjSbzMEX7ThruacEwJ8Lwn-7YibPxxKlgITSIoBmXU7jGYY'
        transferData= TransferData(access_token)

        file_from = input("Enter the file path to transfer")
        file_to = input("Enter the full path to for uploading to dropbox")

        transferData.upload_file(file_from, file_to)
        print("The files have been moved successfully!")

main()
    