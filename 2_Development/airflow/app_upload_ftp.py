import ftplib
from pathlib import Path

# localfile = "{0}".format(Path().absolute()) + '\\' + 'datahistorica.csv'
localfile = "test.txt"
# routeDestination = "/public_html/"
routeDestination = "/"
remotefile = 'test.txt'
try:
    ftp = ftplib.FTP("ftp.nuevatel.com")
    ftp.login("bisauser", "bisanteldos12")
    with open(localfile, "rb") as file:
        ftp.cwd(routeDestination)
        ftp.storbinary('STOR %s' % remotefile, file)
    ftp.quit()
except Exception as e:
    print(e)