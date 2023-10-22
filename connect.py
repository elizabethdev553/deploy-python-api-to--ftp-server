import ftplib

ftp = ftplib.FTP("backend.realestatewisdom.ca", "dh_y3y2yq", "bdGgMvjbDx")

with open("scriptFile.py", "rb") as file:
   ftp.storlines("STOR scriptFile.py", file)
   ftp.sendcmd("SITE EXEC scriptFile.py")

   ftp.quit()