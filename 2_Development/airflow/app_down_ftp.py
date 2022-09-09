import os
import ftplib
from dotenv import load_dotenv

load_dotenv()

nemetec_url = os.getenv("NEMETEC_HOST")
nemetec_user = os.getenv("NEMETEC_USER")
nemetec_pass = os.getenv("NEMETEC_PASS")
nemetec_orig = os.getenv("NEMETEC_ORIG")
nemetec_list = os.getenv("NEMETEC_LIST")

# print(nemetec_url, nemetec_user, nemetec_pass, nemetec_orig, nemetec_list)


# path = '/public_html/'
# filename = 'file_download.xpt'
ftp = ftplib.FTP(nemetec_url) 
ftp.login(nemetec_user, nemetec_pass) 
data_x = ftp.retrlines("LIST")
print(data_x)
# remotefile = "test.txt"
# download = "file_down.txt"

# with open(download,'wb') as file:
#     ftp.retrbinary('RETR %s' % remotefile, file.write)
# # ftp.cwd(path)
# # ftp.retrbinary("RETR " + filename, open(filename, 'wb').write)
# ftp.quit()