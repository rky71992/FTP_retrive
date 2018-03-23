import ftplib
filename1 = "Name of file you want to get"
try:
    ftp = ftplib.FTP("IP Address if FTP server")
    ftp.login("Username", "Password")
    ftp.cwd("/mediaworker")
    ftp.retrbinary("RETR " + filename1 ,open(filename1, 'wb').write)
except ftplib.all_errors as ex:
    print str(ex)