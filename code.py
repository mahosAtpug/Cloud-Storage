import dropbox

class TransferData:
    def __init__ (self , access_token):
        self.access_token = access_token

    def upload_files(self , file_from , file_to):
        dbx = dropbox.Dropbox(self.access_token)
        # rb --> read binary
        f = open(file_from , "rb") 
        dbx.files_upload(f.read() , file_to )

def main():
    access_token = "2n_rtZTMbAoAAAAAAAAAAQKZ1-fwtDiGG-YDWKj-l_twukan9ooILZsoKXc5WXoP"
    transferData = TransferData(access_token)
    file_from = input("Enter the File Path to Transfer : " )
    file_to = input("Enter the Path to Upload To Dropbox : ")
    # file_from = "C:/Users/Soham Gupta/Desktop/whj files/Phyton/dropbox/dummie.txt"
    # file_to = "/python_codes/dummie.txt"
    transferData.upload_files(file_from , file_to)
    print("File Moved")

main()