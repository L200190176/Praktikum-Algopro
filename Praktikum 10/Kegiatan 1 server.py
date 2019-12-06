import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",50008))
s.listen(5)
print "Program komunikasi tentang data diri"
data = ""
kamus = {"nama" : "Tiara Danirmala",
         "NIM" :"L200190176",
         "angkatan":"2019",
         "keluar":"siap!"}
while data.lower() != "keluar":
    komm, addr = s.accept()
    while data.lower() != "keluar":
        data = komm.recv(1024)
        print "Perintah: ", data
        if kamus.has_key(data):
            komm.send(kamus[data])
        else:
            komm.send("Maaf perintah anda tidak di mengerti")
                  
