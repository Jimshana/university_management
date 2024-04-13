import face_recognition
import numpy as np
s = r"D:\Corezone\Unique Id\Web\uniqueid\static\image\ams16mca01.jpg"
regno='ams12mca01'

picture_of_me = face_recognition.load_image_file(s)
my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]
import qrcode


import hashlib

# Example string
data = my_face_encoding



qry="insert into `key` values(null,'"+regno+"','"+str(my_face_encoding)+"')"
from DBConnection_new import Dbnew
db=Dbnew()
db.insert(qry)
# print(type(my_face_encoding))
#
# face_str = np.array2string(my_face_encoding)
# print(face_str)
# g=regno+"#"+face_str
# data = f"Registration Number: {regno}\nFace Features: {face_str}"
# # Generate QR code
# qr = qrcode.QRCode(version=1, box_size=10, border=5)
# qr.add_data(data)
# qr.make(fit=True)
# qr_img = qr.make_image(fill_color="black", back_color="white")
# qr_img.save("qr_code.png")
# print(my_face_encoding)
# print(regno)
# #
# # picture_of_post = face_recognition.load_image_file(r"D:\Corezone\Stas cyber kottayam\lockchat  secure\lockchat  secure\static\login_check\\"+ filename)
# #
# # others_face_encoding = face_recognition.face_encodings(picture_of_post)
# #
# # totface = len(others_face_encoding)
# # print(totface)
# # m=0
# # for i in  others_face_encoding:
# #     res = face_recognition.compare_faces([my_face_encoding], i, tolerance=0.5)
# #     print(res)
# #
# #     l = 0
# #
# #     if res[0]:
# #         print("yes")
