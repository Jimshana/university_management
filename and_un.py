from flask import Flask, render_template, request, session, jsonify
from  flask.globals import session
from DBConnection import Db
import random
from DBConnection_new import Dbnew
from flask import Flask,request
from flask.templating import render_template

from flask.globals import session
from flask.json import jsonify
import qrcode
import requests
import base64
import os
from mailbox import ExternalClashError
from tracemalloc import StatisticDiff
from builtins import str

app = Flask(__name__)

app.secret_key='hi'


@app.route("/and_algo", methods=['post'])
def algandroid():
    a = request.form["str"]
    print("a="+a)
    # b = base64.b64decode(a)
    # fh = open("static/image/10mca.jpg", "wb")
    # fh.write(b)
    # fh.close()
    imgdata = base64.b64decode(a)
    filename = 'static/image/10mca.jpg'  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(imgdata)

    subscription_key = "783e50517a5a4dc4b2703ecb7ac354cf"
    face_api_url = "https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect?returnFaceId=true&returnFaceLandmarks=true"
    #     headers = { 'Ocp-Apim-Subscription-Key': subscription_key }


    headers = {'Content-Type': 'application/octet-stream', 'Ocp-Apim-Subscription-Key': subscription_key}
    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise'}
    data = open("static/image/10mca.jpg", 'rb')
    print (data)

    response = requests.post(face_api_url, params=params, headers=headers, data=data)  # json={"url": image_url})
    faces = response.json()
    print(faces)

    print(faces[0]["faceId"])
    width = (faces[0]["faceRectangle"]["width"])
    height = (faces[0]["faceRectangle"]["height"])
    top = (faces[0]["faceRectangle"]["top"])
    left = (faces[0]["faceRectangle"]["left"])
    mouthleft_x = (faces[0]["faceLandmarks"]["mouthLeft"]["x"])
    mouthleft_y = (faces[0]["faceLandmarks"]["mouthLeft"]["y"])
    eyeRightTop_x = (faces[0]["faceLandmarks"]["eyeRightTop"]["x"])
    eyeRightTop_y = (faces[0]["faceLandmarks"]["eyeRightTop"]["y"])
    upperLipBottom_x = (faces[0]["faceLandmarks"]["upperLipBottom"]["x"])
    upperLipBottom_y = (faces[0]["faceLandmarks"]["upperLipBottom"]["y"])
    eyeLeftInner_x = (faces[0]["faceLandmarks"]["eyeLeftInner"]["x"])
    eyeLeftInner_y = (faces[0]["faceLandmarks"]["eyeLeftInner"]["y"])
    pupilRight_x = (faces[0]["faceLandmarks"]["pupilRight"]["x"])
    pupilRight_y = (faces[0]["faceLandmarks"]["pupilRight"]["y"])
    eyeRightBottom_x = (faces[0]["faceLandmarks"]["eyeRightBottom"]["x"])
    eyeRightBottom_y = (faces[0]["faceLandmarks"]["eyeRightBottom"]["y"])
    eyebrowRightInner_x = (faces[0]["faceLandmarks"]["eyebrowRightInner"]["x"])
    eyebrowRightInner_y = (faces[0]["faceLandmarks"]["eyebrowRightInner"]["y"])
    noseTip_x = (faces[0]["faceLandmarks"]["noseTip"]["x"])
    noseTip_y = (faces[0]["faceLandmarks"]["noseTip"]["y"])
    eyebrowLeftInner_x = (faces[0]["faceLandmarks"]["eyebrowLeftInner"]["x"])
    eyebrowLeftInner_y = (faces[0]["faceLandmarks"]["eyebrowLeftInner"]["y"])
    eyebrowRightOuter_x = (faces[0]["faceLandmarks"]["eyebrowRightOuter"]["x"])
    eyebrowRightOuter_y = (faces[0]["faceLandmarks"]["eyebrowRightOuter"]["y"])
    eyebrowLeftOuter_x = (faces[0]["faceLandmarks"]["eyebrowLeftOuter"]["x"])
    eyebrowLeftOuter_y = (faces[0]["faceLandmarks"]["eyebrowLeftOuter"]["y"])
    eyeLeftTop_x = (faces[0]["faceLandmarks"]["eyeLeftTop"]["x"])
    eyeLeftTop_y = (faces[0]["faceLandmarks"]["eyeLeftTop"]["y"])
    eyeRightInner_x = (faces[0]["faceLandmarks"]["eyeRightInner"]["x"])
    eyeRightInner_y = (faces[0]["faceLandmarks"]["eyeRightInner"]["y"])
    mouthRight_x = (faces[0]["faceLandmarks"]["mouthRight"]["x"])
    mouthRight_y = (faces[0]["faceLandmarks"]["mouthRight"]["y"])
    eyeLeftOuter_x = (faces[0]["faceLandmarks"]["eyeLeftOuter"]["x"])
    eyeLeftOuter_y = (faces[0]["faceLandmarks"]["eyeLeftOuter"]["y"])
    noseRightAlarOutTip_x = (faces[0]["faceLandmarks"]["noseRightAlarOutTip"]["x"])
    noseRightAlarOutTip_y = (faces[0]["faceLandmarks"]["noseRightAlarOutTip"]["y"])
    underLipTop_x = (faces[0]["faceLandmarks"]["underLipTop"]["x"])
    underLipTop_y = (faces[0]["faceLandmarks"]["underLipTop"]["y"])
    eyeRightOuter_x = (faces[0]["faceLandmarks"]["eyeRightOuter"]["x"])
    eyeRightOuter_y = (faces[0]["faceLandmarks"]["eyeRightOuter"]["y"])
    pupilleft_x = (faces[0]["faceLandmarks"]["pupilLeft"]["x"])
    pupilLeft_y = (faces[0]["faceLandmarks"]["pupilLeft"]["y"])
    noseRightAlarTop_x = (faces[0]["faceLandmarks"]["noseRightAlarTop"]["x"])
    noseRightAlarTop_y = (faces[0]["faceLandmarks"]["noseRightAlarTop"]["y"])
    underLipBottom_x = (faces[0]["faceLandmarks"]["underLipBottom"]["x"])
    underLipBottom_y = (faces[0]["faceLandmarks"]["underLipBottom"]["y"])
    noseLeftAlarTop_x = (faces[0]["faceLandmarks"]["noseLeftAlarTop"]["x"])
    noseLeftAlarTop_y = (faces[0]["faceLandmarks"]["noseLeftAlarTop"]["y"])
    eyeLeftBottom_x = (faces[0]["faceLandmarks"]["eyeLeftBottom"]["x"])
    eyeLeftBottom_y = (faces[0]["faceLandmarks"]["eyeLeftBottom"]["y"])
    upperLipTop_x = (faces[0]["faceLandmarks"]["upperLipTop"]["x"])
    upperLipTop_y = (faces[0]["faceLandmarks"]["upperLipTop"]["y"])
    noseRootLeft_x = (faces[0]["faceLandmarks"]["noseRootLeft"]["x"])
    noseRootLeft_y = (faces[0]["faceLandmarks"]["noseRootLeft"]["y"])
    noseLeftAlarOutTip_x = (faces[0]["faceLandmarks"]["noseLeftAlarOutTip"]["x"])
    noseLeftAlarOutTip_y = (faces[0]["faceLandmarks"]["noseLeftAlarOutTip"]["y"])
    noseRootRight_x = (faces[0]["faceLandmarks"]["noseRootRight"]["x"])
    noseRootRight_y = (faces[0]["faceLandmarks"]["noseRootRight"]["y"])
    gender = (faces[0]["faceAttributes"]["gender"])
    smile = (faces[0]["faceAttributes"]["smile"])
    exposure_value = (faces[0]["faceAttributes"]["exposure"]["value"])
    exposure_exposureLevel = (faces[0]["faceAttributes"]["exposure"]["exposureLevel"])
    noise_value = (faces[0]["faceAttributes"]["noise"]["value"])
    noise_noiseLevel = (faces[0]["faceAttributes"]["noise"]["noiseLevel"])
    # emotion_fear=(faces[0]["faceAttributes"]["emotion"]["fear"])
    # emotion_sadness=(faces[0]["faceAttributes"]["emotion"]["sadness"])
    # emotion_happiness=(faces[0]["faceAttributes"]["emotion"]["happiness"])
    # emotion_sadness=(face
    glasses = (faces[0]["faceAttributes"]["glasses"])
    age = (faces[0]["faceAttributes"]["age"])
    accessories = (faces[0]["faceAttributes"]["accessories"])
    headPose_yaw = (faces[0]["faceAttributes"]["headPose"]["yaw"])
    headPose_roll = (faces[0]["faceAttributes"]["headPose"]["roll"])
    headPose_pitch = (faces[0]["faceAttributes"]["headPose"]["pitch"])
    occlusion_eyeOccluded = (faces[0]["faceAttributes"]["occlusion"]["eyeOccluded"])
    occlusion_foreheadOccluded = (faces[0]["faceAttributes"]["occlusion"]["foreheadOccluded"])
    occlusion_mouthOccluded = (faces[0]["faceAttributes"]["occlusion"]["mouthOccluded"])
    blur_value = (faces[0]["faceAttributes"]["blur"]["value"])
    blur_blurLevel = (faces[0]["faceAttributes"]["blur"]["blurLevel"])
    makeup_eyeMakeup = (faces[0]["faceAttributes"]["makeup"]["eyeMakeup"])
    makeup_lipMakeup = (faces[0]["faceAttributes"]["makeup"]["lipMakeup"])
    facialHair_beard = (faces[0]["faceAttributes"]["facialHair"]["beard"])
    facialHair_moustache = (faces[0]["faceAttributes"]["facialHair"]["moustache"])
    age = (faces[0]["faceAttributes"]["age"])
    age1 = ((pupilleft_x - pupilRight_x) * (pupilleft_x - pupilRight_x))
    print(age1)
    age2 = age1 / width
    print(age2)
    x1 = eyeLeftOuter_x
    x2 = eyeLeftOuter_y
    x3 = eyeRightOuter_x
    x4 = eyeRightOuter_y
    x5 = eyeLeftInner_x
    x6 = eyeLeftInner_y
    x7 = eyeRightInner_x
    x8 = eyeRightInner_y
    print("hi")
    icd = (((x5 - x7) * (x5 - x7)) + ((x6 - x8) * (x6 - x8))) / width
    print(icd)
    ocd = (((x1 - x3) * (x1 - x3)) + ((x2 - x4) * (x2 - x4)) / width)
    print(ocd)
    strr = str(age2) + "#" + str(icd) + "#" + str(ocd)
    #print("str="+str)
    return jsonify(status=strr)


@app.route('/key', methods=['post'])
def key():
    con, cu = connection()

    bb = request.form['reg']
    query = "select sk from secr_key where reg='"+bb+"''"
    cu.execute(query)
    con.commit()
    res = cu.fetchone()

    if res is not None:
        return jsonify(status="ok", sk22=res[1])
    else:
        return jsonify(status="no")


@app.route('/view_profile', methods=['POST'])
def view_profile():
    a = request.form["sk"]

    qry = "select regno,name,college.clgname,coursealloc.crs,student.place,student.phno,gender,student.email,photo from student,course,college,coursealloc,secr_key where student.clgid=college.clgid and coursealloc.clgname=college.clgid and secr_key.reg=student.regno and secr_key.sk='"+a+"'"
    print(qry);
    con, cu = connection();
    cu.execute(qry);
    res = cu.fetchone();
    if res is not None:
        return jsonify(status='ok',rno=res[0],sname=res[1],clg=res[2],crs=res[3],plc=res[4],ph=res[5],gen=res[6],email=res[7],pho=res[8])
    else:
        return jsonify(status='no')




if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port=5050)

