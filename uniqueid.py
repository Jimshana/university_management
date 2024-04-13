import ast
import uuid
import numpy as np
import face_recognition
import qrcode
from flask import Flask, render_template, request, session, jsonify, redirect, url_for
from  flask.globals import session
# from qrcode import QRCode
import datetime

from DBConnection import Db
from DBConnection_new import Dbnew
import random




from flask import Flask,request
from flask.templating import render_template

from flask.globals import session
from flask.json import jsonify



import base64
import os
# from mailbox import ExternalClashError
# from tracemalloc import StatisticDiff
# from builtins import str



UPLOAD_FOLDER = 'D:\\New folder\\Project\\uniqueid\\uniqueid\\static\\'
app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



app = Flask(__name__)

app.secret_key='hi'

@app.route('/')
def hello_world():
    return render_template("new_index.html")

@app.route('/aa')
def ha():

    return render_template("aa.html")

@app.route('/templnew')
def templnew():
    return render_template("templnew.html")
@app.route('/templ55new')
def templ55new():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    return render_template("College_index.html")

@app.route('/tst_res1')
def tst_res1():
    return render_template("tst_res.html")



@app.route('/login')
def login():
    session["lid"]=""
    return render_template("Login.html")
@app.route('/login_post',methods=['post'])
def login1():
    uname=request.form["uname"]
    pswd=request.form["pswd"]
    print("u="+uname)
    print("p=" + pswd)

    qry="select * from login WHERE Username='"+uname+"'and pswd='"+pswd+"'"
    print(qry)
    c=Db()
    re=c.selectOne(qry)
    print(re)
    if re is not None:
        session["lid"]=re[0]
        if (re[3]=='admin'):
            #  return render_template("templnew.html")
             return render_template("Adminindex.html")

        elif(re[3]=='college'):
            qry1="select * from college where email='"+uname+"'"
            print(qry1)

            res=c.selectOne(qry1)

            print(re)
            session["uid"]=res[0]
            return render_template("College_index.html")
        elif (re[3] == 'subadmin'):
            qry1 = "select * from subadmin where loginid='" + str(re[0]) + "'"
            print(qry1)

            res = c.selectOne(qry1)
            if res is not None:
                print(re)
                session["uid"] = res[0]
                return render_template("Subadminindex.html")
            else:
                return '''<script>alert('Invalid username or password');window.location='/login'</script>'''
        elif (re[3] == 'teacher'):
            qry1 = "select * from teacher where login_id='" + str(re[0]) + "'"
            print(qry1)

            res = c.selectOne(qry1)
            if res is not None:
                print(re)
                session["uid"] = res[0]
                session["clgid"]=res[14]
                session["mcid"]=res[14]
                return render_template("Staffindex.html")
            else:
                return
                '''<script>alert('Invalid username or password');window.location='/login'</script>'''
        elif (re[3] == 'student'):
            qry1 = "select * from student where login_id='" + str(re[0]) + "'"
            print(qry1)

            res = c.selectOne(qry1)
            if res is not None:
                print(re)
                session["uid"] = res[0]
                session["clgid"]=res[1]
                return render_template("Studentindex.html")
            else:
                return
                '''<script>alert('Invalid username or password');window.location='/login'</script>'''
        else:
            return render_template("Login.html")
    else:
        return '''<script>alert('Invalid username or password');window.location='/login'</script>'''
@app.route('/logout')
def logout():
    session["lid"]=""
    # session.clear()
    return render_template("Login.html")
@app.route('/send_reply_post',methods=['post'])
def send_reply_post():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    reply=request.form['textarea']
    id=request.form["cid"]
    qry="UPDATE `complaint` SET reply='"+reply+"',STATUS='replied' WHERE complaint_id='"+id+"'"
    db=Db()
    res=db.update(qry)
    return viewuser_complaint()
@app.route("/admin_view_reports")
def admin_view_reports():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    qry="SELECT * FROM `report` INNER JOIN `verifier` ON `verifier`.`login_id`=`report`.`verifier_lid` "
    db=Dbnew()
    data=db.select(qry)
    return render_template("admin_view_reports.html",data=data)
@app.route("/admin_home")
def admin_home():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    return render_template("admin_header.html")
    
@app.route('/viewuser_complaint')
def viewuser_complaint():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    db=Dbnew()
    qry="SELECT * FROM `complaint` INNER JOIN `subadmin` ON `subadmin`.`subadminid`=`complaint`.`uid` WHERE `from`='subadmin'"
    res=db.select(qry)
    qry2 = "SELECT * FROM `complaint` INNER JOIN `student` ON `student`.`stdntid`=`complaint`.`uid` WHERE `from`='student'"
    res2 = db.select(qry2)
    return render_template('viewuser complaint.html', data=res,data2=res2)


@app.route('/send_reply/<id>')
def send_reply(id):
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    return render_template('send reply.html', id=id)

@app.route('/Addbatch')
def Addbatch():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    a = "select crsid,crs from course"
    db=Db()
    data=db.select(a)
    return render_template("Admin_AddBatch.html",data1=data)


@app.route('/edit_batch/<id>')
def edit_batch(id):
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    a = "select crsid,crs from course"
    db=Db()
    session["ba_id"]=id

    re1 = db.select(a)


    a1 = "select * from batch where id='"+id+"'"

    re2 = db.select(a1)


    return render_template("edit_batch1.html",crs1=re1,crs2=re2[0])


@app.route('/edit_batch1',methods=['POST'])
def edit_batch1():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    aa=session["ba_id"]
    crs = request.form["course"]
    bat = request.form["batch"]
    qry = "update batch set crsid='"+crs+"',batch='"+bat+"' where id='"+aa+"'"
    db=Db()
    i=db.update(qry)
    
    return view_batch1()
    


@app.route('/Addbatch1',methods=['post'])
def Addbatch1():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    crs=request.form["course"]
    batch=request.form["batch"]
    db = Db()
    qryt="SELECT * FROM `batch` WHERE `batch`='"+batch+"' AND `crsid`='"+crs+"'"
    res=db.select(qryt)
    if len(res)==0:
        qry="insert into batch(crsid,batch)values('"+crs+"','"+batch+"')"

        o=db.insert(qry)
        if o >0:
            return  '''<script>alert('Success');window.location='/Addbatch'</script>'''
        else:
            return '''<script>alert('Failed');window.location='/Addbatch'</script>'''
    else:
        return '''<script>alert('Batch already exists');window.location='/Addbatch'</script>'''
@app.route('/Addcourse')
def Addcourse():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    data={}
    qdp = "select * from department"
    db=Db()
    data['dptview'] = db.select(qdp)
    return render_template("Admin_AddCourse.html",data=data)

@app.route('/Addcourse1',methods=['post'])
def Addcourse1():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    crs=request.form["course"]
    crscode=request.form["coursecd"]
    dptid=request.form["dptid"]
    qry="insert into course(crs,crscode,department_id)values('"+crs+"','"+crscode+"','"+dptid+"')"
    db=Db()
    i=db.insert(qry)
    if i >0:

        return Viewcourse()
    else:
        return render_template("AdminHome.html")
@app.route("/ahome")
def ahome():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    return  render_template("AdminHome.html")
@app.route('/Viewcourse')
def Viewcourse():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    qry = "select course.*,department.department from course inner join department using (department_id)"
    db=Db()
    re = db.select(qry)

    return render_template("Admin_ViewCourse.html", data=re)
@app.route('/deletecourse/<id>')
def deletecourse(id):
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    qry = "delete from course where crsid='" + id + "'"
    db=Db()
    db.delete(qry)
    return  Viewcourse()
@app.route('/updatecourse1/<id>')
def updatecourse(id):
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    qry = "select * from course where crsid='" + id + "'"
    db=Db()
    re = db.selectOne(qry)
    data = {}
    qdp = "select * from department"
    db = Db()
    data['dptview'] = db.select(qdp)
    return render_template("Admin_EditCourse.html",data=re,data1=data)
@app.route('/updatecourse',methods=['post'])
def updatecourse1():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    id=request.form["id"]
    newcrs= request.form["course"]
    newcrscd= request.form["coursecd"]
    dptid = request.form["dptid"]
    qry="update course set crs='"+newcrs+"', crscode='"+newcrscd+"',department_id='"+dptid+"' where crsid='"+id+"'"
    print(qry)
    db=Db()
    i=db.update(qry)
    if i >0 :
        return Viewcourse()
    else:
        return "sorry...... not updated"

@app.route('/Addcollege')
def Addcollege():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    return render_template("Admin_AddCollege.html")

@app.route('/Addcollege1',methods=['post'])
def Addcollege1():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    collegename=request.form["clgname"]
    phoneno=request.form["phno"]
    emailid= request.form["email"]
    plc= request.form["place"]
    strt= request.form["street"]
    pincd= request.form["pin"]
    r=random.randint(1000,10000)
    db=Db()
    qry1 = "insert into login(Username,pswd,type) values('" + str(emailid) + "','" + str(r) + "','college')"

    i=db.insert(qry1)
    qry = "insert into college(clgname,phno,email,place,street,pin,login_id)values('" + str(collegename) + "','" + str(
        phoneno) + "','" + str(emailid) + "','" + str(plc) + "','" + str(strt) + "','" + str(pincd) + "','"+str(i)+"')"

    db=Db()
    ii = db.insert(qry)
    if ii >0:

        return Viewcollege()
    else:
        return "Sorry..! Try again..."


@app.route('/Viewcollege')
def Viewcollege():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    qry = "select * from college"
    db=Db()
    re = db.select(qry)

    return render_template("Admin_ViewCollege.html", data=re)
@app.route('/deletecollege/<id>')
def deletecollege(id):
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    qry = "delete from college where clgid='" + id + "'"
    db=Db()
    db.delete(qry)
    return  Viewcollege()
@app.route('/updatecollege/<id>')
def updatecollege(id):
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    qry = "select * from college where clgid='" + id + "'"
    db=Db()
    re = db.selectOne(qry)

    return render_template("Admin_EditCollege.html",data=re)
@app.route('/updatecollege1',methods=['post'])
def updatecollege1():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    id=request.form["id"]
    clgname= request.form["clgname"]
    phno= request.form["phno"]
    email= request.form["email"]
    place = request.form["place"]
    street= request.form["street"]
    pin = request.form["pin"]
    qry="update college set clgname='"+clgname+"', phno='"+phno+"',email='"+email+"',place='"+place+"',street='"+street+"',pin='"+pin+"' where clgid='"+id+"'"
    db=Db()
    i=db.update(qry)

    return Viewcollege()

@app.route('/Addsubject')
def Addsubject():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    a = "select crsid,crs from course"
    db=Db()
    re = db.select(a)

    b = "select batch,id from batch"
    print("b="+b)

    re1 =db.select(b)

    return render_template("Admin_AddSubject.html", data=re,data1=re1)


# @app.route('/admin_add_department',methods=['get','post'])
# def admin_add_department():
#     if session['lid']=="":
#         return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
#     data={}
#     if "ADD" in request.form:
#         dpt=request.form['dptname']

#         db=Db()

#         qdpt="insert into department values(null,'%s')"%(dpt)
#         logid = db.insert(qdpt)
#         return '''<script>alert('Successfully Added');window.location='/admin_add_department'</script>'''

#     return render_template('Admin_add_department.html')


@app.route('/admin_add_department', methods=['GET', 'POST'])
def admin_add_department():
    if 'lid' not in session or session['lid'] == "":
        return redirect(url_for('login'))

    if request.method == 'POST':
        dpt = request.form.get('dptname')
        db = Db()  # Assuming you have a database connection object

        # Check if department already exists
        q2 = "SELECT department FROM department WHERE department='%s'" % dpt
        existing_department = db.select(q2)

        if existing_department:
            return '''<script>alert('Department already added');window.location='/admin_add_department'</script>'''
        else:
            qdpt = "INSERT INTO department VALUES (null, '%s')" % dpt
            logid = db.insert(qdpt)
            return '''<script>alert('Department added successfully');window.location='/admin_add_department'</script>'''

    return render_template('Admin_add_department.html')

@app.route('/admin_view_department',methods=['get','post'])
def admin_view_department():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    data={}
    db=Db()
    qvd="select * from department"
    data['dptmview']=db.select(qvd)
    return render_template('Admin_view_department.html',data=data)

@app.route('/admin_delete_department/<id>')
def admin_delete_department(id):
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    data={}
    db=Db()
    qdel = "delete from department where department_id='%s'" % (id)
    db.delete(qdel)
    return  '''<script>alert('Successfully Deleted');window.location='/admin_view_department'</script>'''


@app.route('/admin_edit_department/<id>',methods=['get','post'])
def admin_edit_department(id):
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    data={}

    db=Db()

    if "update" in request.form:
        dpt = request.form['dptname']
        did=request.form["did"]
        qcrs = "update  department set department='%s' where department_id='%s'" % (dpt,did)
        db.update(qcrs)
        print(qcrs)
        return '''<script>alert('Successfully Edited');window.location='/admin_view_department'</script>'''


    qsc = "select * from department  where department_id='%s'" % (id)
    print(qsc)

    data['cosview'] = db.select(qsc)



    return render_template('Admin_Edit_department.html',data=data)

@app.route("/view_verifier")
def view_verifier():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    qry="SELECT * FROM verifier"
    db=Db()
    data=db.select(qry)
    return render_template("admin_view_verifiers.html",data=data)

@app.route('/Addsubject1',methods=['post'])
def Addsubject1():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    course1=request.form["course"]
    semester1=request.form["semester"]
    batch1=request.form["batch"]
    sub1=request.form["ss"]

    session["crs"]=course1
    session["sem"]=semester1
    session["batch"]=batch1

    qry = "insert into subject(crs,sem,batch,subject)values('"+course1+"','"+semester1+"','"+batch1+"','"+sub1+"')"
    db=Db()
    i=db.insert(qry)

    return Addsubject()

@app.route('/Add_edit_subject1',methods=['post'])
def Add_ed_subject1():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    sid=session["ssid"]
    course1=request.form["course"]
    semester1=request.form["semester"]
    batch1=request.form["batch"]
    sub1=request.form["ss"]

    session["crs"]=course1
    session["sem"]=semester1
    session["batch"]=batch1

    qry = "update subject set crs='"+course1+"',sem='"+semester1+"',batch='"+batch1+"',subject='"+sub1+"' where subjectid='"+sid+"'"
    db=Db()
    db.insert(qry)
    return view_sub()




@app.route('/subject_view_ed/<sid>')
def Addsubjectview_ed(sid):
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    db=Db()
    uuid=sid
    session["ssid"]=sid
    ww="select subject from subject where subjectid='"+uuid+"'"
    print("w="+ww)

    res55 = db.selectOne(ww)
    print(res55,"-------------------")
    a = "select crsid,crs from course"
    print("w1=" + a)
    print("a=" + a)


    re = db.select(a)

    b = "select crsid,batch,id from batch"
    print("b="+b)

    re1 = db.select(b)

    return render_template("adm_sub_edit.html", data=re,data1=re1,sub1=res55[0])


@app.route('/Addsubsubject1_upda1', methods=['post'])
def Addsubsubject_upd1():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    sid=request.form["sid22"]
    subject = request.form["subject"]
    course=session["crs"]
    semester=session["sem"]
    batch=session["batch"]
    qry = "update subject set crs='"+course+"' ,sem='"+semester+"',batch='"+batch+"',subject='"+subject+"' where subjectid='"+sid+"'"
    db=Db()
    i=db.insert(qry)
    return Addsubject()

@app.route('/AddCallinternal')
def AddCallinternal():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    # a = "select course.crsid,course.crs from coursealloc inner join course on coursealloc.crs = course.crsid "
    # con, cu= connection(F)
    # cu.execute(a)
    # re = cu.fetchall()
    # # print("re="+re)
    # con.commit()
    # b = "select id,batch from batch"
    # con, cu = connection()
    # cu.execute(b)
    # re1 = cu.fetchall()
    # # con.commit()
    c= "select clgid,clgname from college"
    db=Db()
    re2 = db.select(c)

    return render_template("Admin_Call_Internal.html",data2=re2)
@app.route('/selectcourse')
def selectcourse():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    print("hellow")
    college=request.args.get("clgid")
    print(college,"ooooooooooo")
    qry = "select course.crsid,course.crs from coursealloc inner join course on coursealloc.crs = course.crsid where coursealloc.clgname='"+college+"'  "
    print("qq"+qry)
    db=Dbnew()
    res = db.select(qry)
    print(res)
    if res is not None:
        return jsonify(res)
    else:
        return jsonify(status="ok")

# @app.route('/Addcallinternal1',methods=['post'])
# def Addcallinternal1():
#     if session['lid']=="":
#         return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
#     college=request.form["college"]
#     batch = request.form["batch"]
#     course=request.form["course"]
#     semester = request.form["semester"]
#     message=request.form["message"]
#     qry = "insert into callinternal(clg,crsid,batch,sem,message,status)values('"+college+"','" +course + "','"+batch+"','"+ semester+"','"+message+"','pending')"
#     db=Db()
#     db.insert(qry)
#     se="select max(callid) from callinternal"

#     re=db.selectOne(se)
#     id=re
#     a="insert into notifctn(message,clg,date,type,callid)VALUES ('"+message+"','"+college+"',CURDATE(),'internal','"+str(id)+"')"
#     db.insert(a)
#     return AddCallinternal()

@app.route('/Addcallinternal1',methods=['post'])
def Addcallinternal1():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    college=request.form["college"]
    batch = request.form["batch"]
    course=request.form["course"]
    semester = request.form["semester"]
    message=request.form["message"]
    qry = "insert into callinternal(clg,crsid,batch,sem,message,status)values('"+college+"','" +course + "','"+batch+"','"+ semester+"','"+message+"','pending')"
    db=Db()
    kk=db.insert(qry)
    se="select max(callid) from callinternal"

    re=db.selectOne(se)
    id=re
    a="insert into notifctn(message,clg,date,type,callid)VALUES ('"+message+"','"+college+"',CURDATE(),'internal','"+str(kk)+"')"
    db.insert(a)
    return AddCallinternal()

@app.route('/Viewinternalcall')
def Viewinternalcall():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    qry = "select `callid`,`sem`,`message`,`status`,`clgname`,`batch`.`batch`,`course`.`crs`,course.crsid,callinternal.clg,batch.id from callinternal inner join `course` on `course`.`crsid`=`callinternal`.`crsid` inner join `batch` on `batch`.id=`callinternal`.`batch` inner join `college` on `college`.`clgid`=`callinternal`.`clg`"
    db=Db()
    re=db.select(qry)
    ss=[]
    for i in re:
        select="SELECT * FROM `internalmk` INNER JOIN `subject` ON `subject`.`subjectid`=`internalmk`.`subjectid` INNER JOIN `batch` ON `batch`.`id`=`subject`.`batch` INNER JOIN `course` ON `course`.`crsid`=`batch`.`crsid` INNER JOIN `student` ON `student`.`batch`=`batch`.`id`  WHERE `batch`.`id`=`student`.`batch` AND `student`.`crs`='"+str(i[7])+"' AND `student`.`batch`='"+str(i[9])+"' AND `subject`.sem='"+str(i[1])+"' AND `student`.`clgid`='"+str(i[8])+"'"
        print(select)
        sel=db.selectOne(select)
        if sel is  None:
            ss.append("pending")
        else:
            ss.append("Completed")

    return render_template("Admin_View_Internal.html", data=re,ss=ss,d=len(ss))


@app.route('/deleteinternalcall/<id>')
def deleteinternalcall(id):
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    qry = "delete from callinternal where callid='" + id + "'"
    db=Db()
    db.delete(qry)
    return  Viewinternalcall()
@app.route('/alloccourse')
def alloccourse():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    clgname = request.args.get("clgna")
    qry = "select crsid,crs from course  where crsid not in (select crs from coursealloc where clgname='"+clgname+"')"
    print("qq=" + qry)
    db=Dbnew()
    res = db.select(qry)
    print(res)
    if res is not None:
        return jsonify(res)
    else:
        return jsonify(status="ok")

@app.route('/Allocate')
def Allocate():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    a = "select clgid,clgname from college"
    db=Db()
    re=db.select(a)

    b="select crsid,crs from course"

    re1 = db.select(b)
    return render_template("Admin_Allocourse.html",data=re,data1=re1)

@app.route('/Allocate1',methods=['post'])
def Allocate1():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    college1=request.form["clgname"]
    course1=request.form.getlist("crs");
    print(college1,course1)
    
    
    print("val",course1)
    sz = len(course1)
    i=0

    for r in range (sz):
        print(college1,"000000000000000000000000000000000000000")
        print(course1[r])
        db=Db()
        se="SELECT * FROM `coursealloc` WHERE `clgname`='"+college1+"'   AND `crs`='"+course1[r]+"'"
        res = db.selectOne(se)
        print(res,"--------------------------------------------------------")
        if res is not None:
            pass
        else:
            # return '''<script>alert('Already Allocated'); window.location='/Allocate'</script>'''
            db=Db()
            qry = "insert into coursealloc(clgname,crs)values('" + college1 + "','" + course1[r] + "')"
            print(qry)
        
            res=db.insert(qry)
    
    return Viewalloccourse()
    



@app.route('/Viewalloccourse')
def Viewalloccourse():
    

    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    qry = "SELECT * FROM coursealloc INNER JOIN `course` ON `course`.`crsid`=`coursealloc`.`crs` INNER JOIN  `college` ON `college`.`clgid`=`coursealloc`.`clgname`"
    print(qry)
    db=Db()
    re = db.select(qry)
    print(re)
    return render_template("Admin_ViewAllocoursec.html", data=re)

@app.route('/Viewalloccourses/<idd>')
def Viewalloccourses(idd):
    print(idd)

    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    qry = "SELECT * FROM coursealloc INNER JOIN `course` ON `course`.`crsid`=`coursealloc`.`crs` WHERE `clgname`='"+idd+"' "
    print(qry)
    db=Db()
    re = db.select(qry)
    return render_template("Admin_ViewAllocourse.html", data=re)
@app.route('/deleteallocourse/<id>')
def deleteallocourse(id):
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    qry = "delete from coursealloc where crsallocid='" + id + "'"
    db=Db()
    db.delete(qry)
    return  Viewcollege()
@app.route('/Addnotif')
def Addnotif():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    a = "select clgid,clgname from college"
    db=Db()
    re=db.select(a)
    return render_template("Admin_AddNotification.html",data=re)
@app.route('/Addnotif1',methods=['post'])
def Addnotif1():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    msg=request.form["msg"]
    clg=request.form["clg"]
    if(clg==0):
        qry="insert into notifctn(message,clg,date,type) values('"+msg+"','0',CURDATE(),'normal')"
        db=Db()
        db.insert(qry)
    else:
        qry="insert into notifctn(message,clg,date,type) values('"+msg+"','"+clg+"',CURDATE(),'normal')"
        db=Db()
        db.insert(qry)
    return Addnotif()
@app.route('/Viewnotif')
def Viewnotif():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    qry = "SELECT * FROM notifctn,`college` WHERE `college`.`clgid`=`notifctn`.`clg` and `notifctn`.`type`='normal'"
    db=Db()
    re=db.select(qry)
    return render_template("Admin_ViewNotification.html", data=re)
@app.route('/deletenotif/<id>')
def deletenotif(id):
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    qry = "delete from notifctn where notfid='" + id + "'"
    db=Db()
    db.delete(qry)
    return  Viewnotif()


@app.route('/admin_view_marks')
def admin_view_marks():
    if session['lid'] == "":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''

    c = "select clgid,clgname from college"
    db = Db()
    re2 = db.select(c)

    return render_template("Admin_view_externals.html", data2=re2)


@app.route('/Addxternal')
def Addxternal():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''

    c="select clgid,clgname from college"
    db=Db()
    re2=db.select(c)


    return render_template("Admin_Add_externalmark.html",data2=re2)

@app.route('/selectbatch')
def selectbatch():

    courseid=request.args.get("crsid")
    qry="select id,batch from batch where crsid='"+courseid+"'"
    print("qq="+qry)
    db=Dbnew()
    res = db.select(qry)
    print(res)
    if res is not None:

        return jsonify(res)
    else:
        return jsonify(status="ok")

@app.route('/selectsubject')
def selectsubject():
    sem1=request.args.get("sem")
    print(sem1)
    courseid=request.args.get("crsid")
    print(courseid)

    batchid=request.args.get("bid")
    print(batchid)
    qry="select subjectid,subject from subject where crs='"+str(courseid)+"' and batch='"+str(batchid)+"' and sem='"+sem1+"'"
    print("qqq="+qry)
    db = Dbnew()
    res = db.select(qry)

    print(res)
    if res is not None:

        return jsonify(res)
    else:
        return jsonify(status="ok")


@app.route('/Addxternal1', methods=['post'])
def Addxternal1():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    batch = request.form["batch"]
    course = request.form["course"]
    college = request.form["college"]
    semester = request.form["semester"]
    subject=request.form["subject"]
    print(college, semester, batch, subject,course)

    session["batch"] = batch
    session["crs"] = course
    session["clg"]=college
    session["sem"] = semester
    session["subject"]=subject

    qry = "select student.regno,name,internmrk from student inner join subject on subject.crs=student.crs inner join internalmk on  `internalmk`.`subjectid`=subject.subjectid    where student.crs='"+course+"' and subject.subjectid='"+subject+"' and student.batch='"+batch+"' and subject.sem='"+semester+"' and clgid='"+college+"' and internalmk.regno=student.regno"
    print(qry)
    db=Db()
    re=db.select(qry)
    print(qry)
    return render_template("Admin_Add_externalmarkII.html", data=re)



@app.route('/ff', methods=['post'])
def ff():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    batch = request.form["batch"]
    course = request.form["course"]
    college = request.form["college"]
    semester = request.form["semester"]
    subject=request.form["subject"]
    print(college, semester, batch, subject,course)

    session["batch"] = batch
    session["crs"] = course
    session["clg"]=college
    session["sem"] = semester
    session["subject"]=subject

    qry = "select student.regno,name,internmrk,mark from student inner join subject on subject.crs=student.crs inner join internalmk on  `internalmk`.`subjectid`=subject.subjectid inner join externalmk on  `externalmk`.`inter_id`=internalmk.subjectid    where student.crs='"+course+"' and subject.subjectid='"+subject+"' and student.batch='"+batch+"' and subject.sem='"+semester+"' and clgid='"+college+"' and internalmk.regno=student.regno  and externalmk.regno=student.regno"
    print(qry)
    db=Db()
    re=db.select(qry)
    print(qry)
    return render_template("Admin_vv.html", data=re)

@app.route('/Addxternal2',methods=['post'])
def Addxternal2():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    batch=session["batch"]
    course = session["crs"]
    college=session["clg"]
    semester=session["sem"]
    subject = session["subject"]
    print(college,semester,batch,subject)


    qry = "select regno from student where crs='"+course+"' and batch='"+batch+"' and sem='"+semester+"' and clgid='"+college+"'  "
    db=Db()
    re = db.select(qry)
    stid=[]
    for i in re:
        stid.append(i[0])

    mark=request.form.getlist("mark")
    sz=len(mark)
    print(mark)
    a="select regno from student where crs='"+course+"' and batch='"+batch+"' and sem='"+semester+"' and clgid='"+college+"' "
    re=db.select(a)
    if re is not None:
        for r in range(sz):
            if int(mark[r])<=60:
                print("hai")
                b = "select regno,inter_id from externalmk where regno='" + str(stid[r]) + "'and inter_id='" + str(session["subject"]) + "'"
                print(b)
                re1=db.selectOne(b)
                # con.commit()

                if re1 is not None:
                    pass
                    # return "data is already entered"
                else:

                    qry = "insert into externalmk(mark,regno,inter_id)values('" + str(mark[r]) + "','" + str(
                        stid[r]) + "','" + str(session["subject"]) + "')"
                    print(qry)
                    db.insert(qry)
                    # return "data is already entered"

        return '''<script>alert('Saved');window.location='/Addxternal'</script>'''




    else:
        return '''<script>alert('Data is already entered');window.location='/Addxternal'</script>'''



@app.route("/tests")
def tests():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    # id="helllo"
    # print("hello")
    # qr = QRCode(version=1, error_correction=QRCode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    # qr.add_data(str(id))
    # qr.make(fit=True)
    # img = qr.make_image()
    # # sid = session['RegisterNo']
    #
    # img.save("D:\\a.jpg")
    import qrcode
    img = qrcode.make('Some kdkjhkdsh hjhhhjhkh jhjhjh khh jhj hkhk hk hkh jkhjkh khjkh jkhjkh jhjh jkhkh  here')
    img.save("D:\\a.jpg")


    return "hello"



@app.route('/view_sub')
def view_sub():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    else:
        qry = "select subjectid,course.crs,sem,batch.batch,subject from subject,course,batch where course.crsid=subject.crs and `batch`.`id`=`subject`.`batch`"
        db=Db()
        re = db.select(qry)
        return render_template("adm_sub_view.html", data=re)



@app.route('/view_batch1')
def view_batch1():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''

    qry = "select id,crs,batch from batch,course where batch.crsid=course.crsid"
    db=Db()
    re=db.select(qry)
    return render_template("view_batch1.html", data=re)

@app.route('/del_sub/<stid>')
def del_sub(stid):
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    query = "delete from subject where subjectid='"+stid+"'"
    db = Db()
    re = db.delete(query)
    return view_sub()


@app.route('/result_generation')
def result():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    qry1 = "select clgid,clgname from college"
    print("qq=" + qry1)

    db=Db()
    res22=db.select(qry1)
    return render_template("admin_rslt_gen.html",data2=res22)

@app.route('/rr22',methods=['post'])
def rr222():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    cid =request.form["course"]
    print("c=" + cid)

    clgid2=request.form["college"]
    print("c1=" + clgid2)
    bat = request.form["batch"]



    print("c2=" + bat)


    qry = "select regno,name,gender from student where clgid='%s' and crs='%s' and batch='%s'"%(clgid2,cid,bat)
    db=Db()
    re=db.select(qry)
    return render_template("resut33.html", data=re)


@app.route('/result_generation1/<uid>')
def ps55(uid):
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    session["nnn"]="nnn"
    session["ccc"]="ccc"
    session["rrr"]="rrr"
    #reg =request.form["uid"]

    print("res="+uid)

    db=Db()
    qry1 = "select sem,course.crsid,batch ,name,course.crs,regno,photo from  student inner join course on course.crsid=student.crs where regno='"+uid+"'"
    res22=db.selectOne(qry1)
    print(qry1)
    sem=res22[0]
    crs=res22[1]
    bat=res22[2]
    regno=res22[5]
    name = res22[3]
    photo = res22[6]
    crsname=res22[4]
    k=0
    aa=0
    sublen=0
    for i in range(1,7):
        qt1="SELECT * FROM `subject` WHERE `crs`='"+str(crs)+"' AND `batch`='"+str(bat)+"' AND `sem`='"+str(sem)+"'"
        dbn=Dbnew()
        rest1=dbn.select(qt1)
        print(rest1)
        for j in rest1:
            subject=str(j["subjectid"])
            sublen+=1
            query1="SELECT `externalmk`.`mark`,`internalmk`.`internmrk` FROM `internalmk` INNER JOIN `subject` ON `subject`.`subjectid`=`internalmk`.`subjectid` INNER JOIN `externalmk` ON `externalmk`.`inter_id`=`subject`.`subjectid` WHERE `subject`.`subjectid`='"+str(subject)+"' AND `externalmk`.`regno`='"+str(regno)+"' AND `internalmk`.`regno`='"+str(regno)+"'"
            res1 = dbn.selectOne(query1)
            print(res1)
            if res1 is not None:
                mark=int(res1['mark'])
                intmark=int(res1["internmrk"])
                aa+=mark+intmark
                if mark < 20 and intmark <15:
                    status="failed"
                    k+=1
                else:
                    status="pass"
    print(sublen)
    if k==0:
        h=sublen*100
        avg=(aa/h)*100
        if avg<=100 and aa>=70:
            gd="Grade A"
        elif aa<=69 and aa>=40:
            gd="Grade B"
        elif aa<=39 and aa>=20:
            gd="Grade C"
        else:
            gd="Grade U"
    else:
        gd="Grade U"


    if gd=="Grade U":
        return '''<script>alert('failed');window.location='/result_generation'</script>'''

    else:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(regno)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white")
        qr_img.save(r"C:\Users\HP\Desktop\uniqueid\static\qr\\"+str(regno)+".png")
        name=name.upper()
        return render_template('resultpub.html',gd=gd,crs=crsname,name=name,reg=regno,pho="/static/qr/"+regno+".png")



@app.route('/searchcourse',methods=['post'])
def searchcourse():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    searchtxt=request.form["txtsearch"]

    qry = "select course.*,department.department from course inner join department using (department_id) where crs like '%"+searchtxt+"%' "

    db = Db()
    re = db.select(qry)
    return render_template("Admin_ViewCourse.html", data=re)
@app.route('/searchcollege',methods=['post'])
def searchcollege():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    searchtxt=request.form["txtsearch1"]
    print(searchtxt)
    qry = "select * from college where clgname like '%"+searchtxt+"%'"
    print(qry)
    db=Db()
    re = db.select(qry)
    return render_template("Admin_ViewCollege.html", data=re)

        # else:
        #     return render_template("College_View_Notification.html", data=re, m="1")


# @app.route('/statusupdate')
# def statusupdate():



# --------------------------------subadmin-----------------------
    

@app.route('/Viewstudentdatar')
def Viewstudentdatar():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    qry = "select * from student inner join college on college.clgid=student.clgid "
    db = Db()
    re = db.select(qry)
    return render_template("Admin_View_Studentdata.html", data=re)


@app.route('/Viewmored/<id>')
def Viewmored(id):
    if session['lid'] == "":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    qry = "SELECT student.*,course.*,batch.batch AS bt FROM student INNER JOIN `course` ON `course`.`crsid`=`student`.`crs` INNER JOIN batch ON `batch`.`id`=`student`.`batch` WHERE `student`.`stdntid`='" + id + "'"
    db = Db()

    re = db.selectOne(qry)
    return render_template("Admin_Viewmore.html", data=re)

# @app.route('/admin_add_subadmin')
# def admin_add_subadmin():
#   return render_template('admin/admin add subadmin.html')

@app.route('/admin_add_subadmin',methods=['get','post'])
def admin_add_subadmin():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    db=Db()
    qry1="select * from subadmin"
    res3=db.select(qry1)
    print(res3)
   
    if 'submit' in request.form:
        name=request.form['name']
        gender=request.form['Gender']
        dob=request.form['dob']
        photo=request.files['photo']
        date=datetime.datetime.now().strftime('%y%m%d-%H%M%S')
        photo.save("C:\\Users\\HP\\Desktop\\uniqueid\\static\subadmin\\"+date+".jpg")
        path="/static/subadmin/"+date+".jpg"
        email=request.form['email']
        phone=request.form['phone']
        # Username=request.form['Username']
        pswd = request.form['pswd']
        db=Db()
        qry = "insert into login (Username,pswd,type)values('" + email + "','" + pswd + "','subadmin')"
        res =db.insert(qry)
        qry1="insert into subadmin(`loginid`,`name`,`gender`,`dob`,`photo`,`email`,`phone`)VALUES ('"+str(res)+"','"+name+"','"+gender+"','"+dob+"','"+str(path)+"','"+email+"','"+phone+"')"
        res1=db.insert(qry1)
    return render_template('admin_add_subadmin.html',data=res3)


@app.route("/delete_sub_admin/<id>")
def delete_sub_admin(id):
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    qry="DELETE FROM `subadmin` WHERE `subadminid`='"+id+"'"
    db=Db()
    res=db.delete(qry)
    return redirect('/admin_add_subadmin')



@app.route('/edit_subadmin/<sid>')
def edit_subadmin(sid):
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    db=Db()
    session["sid"]=sid
    qry="select * from subadmin where subadminid='"+str(sid)+"'"
    res=db.selectOne(qry)
    print(res)
    print(sid,"+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    return render_template('edit subadmin.html', data=res)

@app.route('/edit_subadmin_post',methods=['post'])
def edit_subadmin_post():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    name = request.form['textfield']
    gender = request.form['RadioGroup1']
    DOB = request.form['textfield2']
    email = request.form['textfield3']
    phone = request.form['textfield4']
    db=Db()
    print(session["sid"],"--------------------------------------------------------")
    if 'fileField' in request.files:
        photo = request.files['fileField']
        if photo.filename!="":
            date = datetime.datetime.now().strftime('%y%m%d-%H%M%S')
            photo.save("C:\\Users\\HP\\Desktop\\uniqueid\\static\\subadmin\\" + date + ".jpg")
            path = "/static/subadmin/" + date + ".jpg"
            qry="update subadmin set `name`='"+name+"',gender='"+gender+"',dob='"+DOB+"',Photo='"+str(path)+"',email='"+email+"',phone='"+phone+"' where subadminid='"+str(session["sid"])+"'"
            print(qry)
            res=db.update(qry)
        else:
            qry = "update subadmin set `name`='" + name + "',gender='" + gender + "',dob='" + DOB + "',email='" + email + "',phone='" + phone + "' where subadminid='"+str(session["sid"])+"'"
            print(qry)
            res = db.update(qry)
    else:
        qry = "update subadmin set `name`='" + name + "',gender='" + gender + "',dob='" + DOB + "',email='" + email + "',phone='" + phone + "' where subadminid='"+str(session["sid"])+"'"
        print(qry)
        res = db.update(qry)
    return redirect('/admin_add_subadmin')




@app.route('/admin_view_colleges_id')
def admin_view_colleges_id():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    qry = "select * from college"
    db=Db()
    re = db.select(qry)

    return render_template("Admin_view_clg.html", data=re)

# @app.route('/admin_view_studentss/<id>')
# def admin_view_studentss(id):
#     if session['lid']=="":
#         return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
#     session["crsid"]=id
#     qry = "select * from `student` inner join course on course.crsid=student.crs WHERE `clgid`='"+str(session["clgid"])+"' and crsid='"+id+"'"
#     print(qry)
#     db=Db()
#     re = db.select(qry)

#     return render_template("Admin_student_Data.html", data=re)

@app.route('/admin_view_studentss/<id>')
def admin_view_studentss(id):
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    session["crsid"]=id
    qry = "select * from `student` inner join course on course.crsid=student.crs WHERE `clgid`='"+str(session["clgid"])+"' and crsid='"+id+"'"
    print(qry)
    db=Db()
    re = db.select(qry)
    print(re)
    return render_template("Admin_student_Data.html", data=re)

@app.route('/admin_view_coursess/<id>')
def admin_view_coursess(id):
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    session["clgid"]=id
    qry = "SELECT * FROM `coursealloc` INNER JOIN `course` ON `coursealloc`.`crs`=`course`.`crsid` WHERE `coursealloc`.`clgname`='"+str(id)+"'"
    db=Db()
    re = db.select(qry)
    print(qry)
    return render_template("Admin_view_crs.html", data=re)

# ---------------------------- Subadmin --------------------------------


@app.route('/subadmin_view_profile')
def subadmin_view_profile():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    qry = "select * from subadmin where subadminid = '"+str(session["uid"])+"'"
    print(qry)
    db=Db()
    re = db.selectOne(qry)
    return render_template("Subadmin_view_profile.html", data=re)




@app.route('/subadmin_view_colleges_search',methods=['post'])
def subadmin_view_colleges_search():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    searchtxt=request.form["txtsearch1"]
    print(searchtxt)
    qry = "select * from college where clgname like '%"+searchtxt+"%'"
    print(qry)
    db=Db()
    re = db.select(qry)
    return render_template("SubAdmin_ViewCollege.html", data=re)


@app.route('/subadmin_view_colleges')
def subadmin_view_colleges():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    qry = "select * from college"
    db=Db()
    re = db.select(qry)

    return render_template("SubAdmin_ViewCollege.html", data=re)

@app.route('/subadmin_view_students/<id>')
def subadmin_view_students(id):
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    session["crsid"]=id
    qry = "select * from `student` inner join course on course.crsid=student.crs WHERE `clgid`='"+str(session["clgid"])+"' and crsid='"+id+"'"
    db=Db()
    re = db.select(qry)
    print(qry)
    return render_template("Subadmin_View_Studentdata.html", data=re)

@app.route('/subadmin_view_courses/<id>')
def subadmin_view_courses(id):
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    session["clgid"]=id
    qry = "SELECT * FROM `coursealloc` INNER JOIN `course` ON `coursealloc`.`crs`=`course`.`crsid` WHERE `coursealloc`.`clgname`='"+str(id)+"'"
    db=Db()
    re = db.select(qry)

    return render_template("SubAdmin_ViewCourse.html", data=re)

@app.route('/subadmin_send_complaints')
def subadmin_send_complaints():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    return render_template("Subadmin_send_complaint.html")



@app.route('/subadmin_send_complaint',methods=['POST'])
def subadmin_send_complaint():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    complaint=request.form["textarea"]
    qry="insert into `complaint`(`complaint`,`date`,`reply`,`status`,`uid`,`from`)values('"+complaint+"',curdate(),'pending','pending','"+str(session["uid"])+"','subadmin')"
    db=Db()
    db.insert(qry)
    return '''<script>alert('Complaint send successfully');window.location='/subadmin_send_complaints'</script>'''

@app.route('/Subadmin_view_reply')
def Subadmin_view_reply():
    lid=session["uid"]
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''

    db=Db()
    qry="SELECT * FROM `complaint` WHERE `uid`='"+str(lid)+"' AND `from`='subadmin'"
    res=db.select(qry)
    print(res)
    return render_template("Subadmin_view_reply.html",data=res)



@app.route('/subadmin_change_password')
def subadmin_change_password():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    return render_template('Subadmin_change_password.html')


@app.route('/subadmin_change_password_post',methods=['post'])
def subadmin_change_password_post():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    oldpassword=request.form['textfield']
    newpassword=request.form['textfield2']
    reenternewpassword=request.form['textfield3']
    db=Db()
    qry="select * from login where pswd='"+oldpassword+"' and login_id='"+str(session['lid'])+"' "
    res=db.selectOne(qry)
    if res is not None:
        if newpassword==reenternewpassword:
            qry1="update login set pswd='"+reenternewpassword+"' where pswd='"+oldpassword+"'"
            res1=db.update(qry1)
            return '''<script>alert("update succesfully");window.location="/"</script>'''
        else:
            return '''<script>alert("confirm password deosn't match");history.back();</script>'''
    else:
        return '''<script>alert("current password doesnot match");window.location="/subadmin_change_password"</script>'''


# ----------------------------------


@app.route('/college_view_profile')
def college_view_profile():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    qry = "select * from college where clgid = '"+str(session["uid"])+"'"
    print(qry)
    db=Db()
    re = db.selectOne(qry)
    return render_template("college_view_profile.html", data=re)

@app.route('/College_view_crs_alloc')
def College_view_crs_alloc():
    print()
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''


    qry = "SELECT * FROM coursealloc INNER JOIN `course` ON `course`.`crsid`=`coursealloc`.`crs` WHERE `clgname`='"+str(session["uid"])+"' "
    print(qry)
    db=Db()
    re = db.select(qry)
    return render_template("College_ViewAllocourse.html", data=re)



@app.route('/college_view_batches/<id>')
def college_view_batches(id):
    print()
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    session["crs"]=id
    print(id)
    qry = "SELECT `batch`.`crsid` AS bcourse_id,`batch`.*,`course`.* FROM `batch`,`course` WHERE `course`.`crsid`=`batch`.`crsid` AND `course`.`crsid`='"+id+"'"
    print(qry)
    db=Db()
    re = db.select(qry)
    return render_template("college_view_batches.html", data=re)



@app.route('/college_view_students/<id>')
def college_view_students(id):
    print()
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    session["batch"]=id
    pp=session["uid"]
    rr=session["crs"]
    print(id)
    print(pp)
    print(rr)
    qry = "SELECT * FROM `student`,`course` WHERE `course`.`crsid`=`student`.`crs` and `clgid`='"+str(session["uid"])+"' AND `student`.`crs`='"+str(session["crs"])+"' AND `batch`='"+id+"'"
    print(qry)
    db=Db()
    re = db.select(qry)
    return render_template("College_View_Studet.html", data=re)


@app.route('/clgvwnot',methods=['post'])
def clgvwnot():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    type=request.form["notification"]
    if type=="normal":
        qry = "select * from notifctn WHERE type='"+type+"' and clg='"+str(session["uid"])+"' union (select * from notifctn where type='normal')"
        db=Db()
        res=db.select(qry)
        return render_template("college_view_Nnotif.html", data=res,m="1")
    elif type=="internal":
        aa=session["uid"]
        print("aa="+str(aa))
        qry = "select * from notifctn,callinternal WHERE type='"+type+"' and status='pending' and notifctn.callid=callinternal.callid"

        db=Db()
        res=db.select(qry)

        return render_template("College_View_Notification.html", data=res,m="1")


@app.route('/studreg')
def studreg():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    a = "select course.crsid,course.crs from coursealloc inner join course on coursealloc.crs = course.crsid where clgname='" + str(
        session["uid"]) + "'"
    ds = Db()
    re1 = ds.select(a)
    return render_template("College_StudentEnrollment.html", data1=re1)


@app.route('/studreg1', methods=['post'])
def studreg1():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    Name = request.form["name"]
    Gender = request.form["gender"]
    dob = request.form["dob"]
    Hname = request.form["hname"]
    place = request.form["place"]
    street = request.form["street"]
    post = request.form["post"]
    pin = request.form["pin"]
    state = request.form["state"]
    guardian = request.form["guardian"]
    lguardian = request.form["lguardian"]
    course = request.form["crs"]
    batch = request.form["batch"]
    sem = request.form["semester"]
    phno = request.form["phno"]
    regno = request.form["regno"]
    email = request.form["email"]
    im = regno + ".jpg"
    photo = request.files["photo"]
    # photo.save("D:\\uniqueid\static\\image\\"+im)
    photo.save(r"C:\\Users\\HP\\Desktop\\uniqueid\\static\\image\\" + im)
    db = Db()
    qry = "insert into login (Username,pswd,type)values('" + email + "','" + phno + "','student')"
    res = db.insert(qry)
    qry = "insert into student(clgid,name,gender,dob,hname,place,street,post,pin,state,guardian,lguardian,crs,batch,sem,phno,regno,email,photo,login_id)values('" + str(
        session[
            "uid"]) + "','" + Name + "','" + Gender + "','" + dob + "','" + Hname + "','" + place + "','" + street + "','" + post + "','" + pin + "','" + state + "','" + guardian + "','" + lguardian + "','" + course + "','" + batch + "','" + sem + "','" + phno + "','" + regno + "','" + email + "','" + im + "','" + str(
        res) + "')"

    id = db.insert(qry)
    # return algorithm()

    ##########
    # picture_of_me = face_recognition.load_image_file(r"D:\New folder\Project\uniqueid\uniqueid\static\image\\" + im)
    # my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]
    # print(my_face_encoding)
    # qry="insert into `key` values(null,'"+regno+"','"+str(my_face_encoding)+"')"
    # db.insert(qry)
    return '''<script>alert('Success');window.location='/studreg'</script>'''




    #########


    # return "ok"
    # if i == 1:
    #     return "saved"
    # else:
    #     return "missing field"


@app.route('/Viewstudentdata')
def Viewstudentdata():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    p=session["uid"]
    print(p,'================')
    # qry = "select * from student inner join college on college.clgid=student.clgid where college.clgid='"+str(session["uid"])+"'"
    qry = "SELECT * FROM student inner join college on college.clgid=student.clgid inner join `course` on  `course`.`crsid`=`student`.`crs` WHERE  `course`.`crsid`=`student`.`crs` AND college.clgid='"+str(session["uid"])+"'"

    db = Db()
    re = db.select(qry)
    return render_template("College_View_Studentdata.html", data=re)


@app.route('/Viewmore/<id>')
def Viewmore(id):
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    qry = "SELECT student.*,course.*,batch.batch AS bt FROM student INNER JOIN `course` ON `course`.`crsid`=`student`.`crs` INNER JOIN batch ON `batch`.`id`=`student`.`batch` WHERE `student`.`stdntid`='" + id + "'"
    db=Db()
    
    re=db.selectOne(qry)
    return render_template("College_Viewmore.html", data=re)


@app.route('/Viewmore1/<id>')
def Viewmore1(id):
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    qry = "SELECT student.*,course.*,batch.batch AS bt FROM student INNER JOIN `course` ON `course`.`crsid`=`student`.`crs` INNER JOIN batch ON `batch`.`id`=`student`.`batch` WHERE `student`.`stdntid`='" + id + "'"
    db = Db()

    re = db.selectOne(qry)
    return render_template("Staff_Viewmore.html", data=re)

@app.route('/deletestudent/<id>')
def deletestudent(id):
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    qry = "delete from student where stdntid='" + id + "'"
    db=Db()
    db.delete(qry)
    return Viewstudentdata()


@app.route('/del_batch/<id>')
def del_batch(id):
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    qry = "delete from batch where id='" + id + "'"
    db = Db()
    db.delete(qry)
    return view_batch1()


@app.route('/updatestudent/<id>')
def updatestudent(id):
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    a = "select course.crsid,course.crs from coursealloc inner join course on coursealloc.crs = course.crsid where clgname='" + str(
        session["uid"]) + "'"
    db=Db()
    re1 = db.select(a)

    qry = "select student.*,course.crs from student,course where student.crs=course.crsid and student.stdntid='" + id + "'"

    re =db.selectOne(qry)

    print(re)

    return render_template("College_Edit_Studentdata.html", data=re, data1=re1)


@app.route('/updatestudent1', methods=['post'])
def updatestudent1():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    id = request.form["id"]
    Name = request.form["name"]
    Gender = request.form["gender"]
    dob = request.form["dob"]
    Hname = request.form["hname"]
    place = request.form["place"]
    street = request.form["street"]
    post = request.form["post"]
    pin = request.form["pin"]
    state = request.form["state"]
    guardian = request.form["guardian"]
    lguardian = request.form["lguardian"]
    # course = request.form["course"]
    # batch = request.form["batch"]
    # sem = request.form["semester"]
    phno = request.form["phno"]
    regno = request.form["regno"]
    email = request.form["email"]
    if 'photo' in request.files:
        im = regno + ".jpg"
        photo = request.files["photo"]
        photo.save("C:\\Users\\HP\\Desktop\\uniqueid\\static\image\\" + im)
        qry = "update student set name='" + Name + "', gender='" + Gender + "',dob='" + dob + "',hname='" + Hname + "',place='" + place + "',street='" + street + "',post='" + post + "',pin='" + pin + "',state='" + state + "',guardian='" + guardian + "',lguardian='" + lguardian + "',phno='" + phno + "',regno='" + regno + "',email='" + email + "',photo='" + im + "' where stdntid='" + id + "'"
    else:
        qry = "update student set name='" + Name + "', gender='" + Gender + "',dob='" + dob + "',hname='" + Hname + "',place='" + place + "',street='" + street + "',post='" + post + "',pin='" + pin + "',state='" + state + "',guardian='" + guardian + "',lguardian='" + lguardian + "',phno='" + phno + "',regno='" + regno + "',email='" + email + "' where stdntid='" + id + "'"

    db=Db()
    db.update(qry)
    return  '''<script>alert('Success');window.location='/Viewstudentdata'</script>'''



@app.route('/admin_add_teachers', methods=['post', 'get'])
def admin_add_teachers():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    data = {}
    db=Db()
    pp=session["uid"]
    print(pp,"--------------------")
    # qscr = "select * from department "
    # data['qscrview'] = db.select(qscr)
    # print(data['qscrview'])

    if "submit" in request.form:
        # cu = request.form['curs']
        fn = request.form['fname']
        ln = request.form['lname']
        ge = request.form['Gender']
        do = request.form['db']
        hn = request.form['hname']
        pl = request.form['place']
        pc = request.form['pcode']
        di = request.form['disrict']

        phone = request.form['phone']
        email = request.form['email']
        qualification = request.form['qualification']


        profile = request.files['photo']
        s=str(uuid.uuid4()) + ".jpg"
        path = r'C:\Users\HP\Desktop\uniqueid\static\teacher\\' +s
        

        profile.save(path)
        p1="/static/teacher/"+s



        qst = "insert into login values(null,'%s','%s','teacher')" % (email, phone)
        logid = db.insert(qst)

        qsd = "INSERT INTO `teacher`(`login_id`,`first_name`,`last_name`,`gender`,`dob`,`house_name`,`place`,`pincode`,`district`,`phone`,`email`,`qualification`,`photo`,clgid)VALUES('"+str(logid)+"','"+fn+"','"+ln+"','"+ge+"','"+do+"','"+hn+"','"+pl+"','"+pc+"','"+di+"','"+phone+"','"+email+"','"+qualification+"','"+p1+"','"+str(session["uid"])+"')"
        db.insert(qsd)
        return redirect(url_for('admin_add_teachers'))

    if "action" in request.args:
        action = request.args['action']
        sd = request.args['stid']

    else:
        action = None

    if action == 'delete':
        qds = "delete from teacher where login_id='%s'" % (sd)
        db.delete(qds)

        qdls = "delete from login where login_id='%s'" % (sd)
        db.delete(qdls)
        return redirect(url_for('admin_add_teachers'))

    if action == 'update':
        qss = "select * from teacher inner join login using (login_id) where login_id='%s' and clgid='%s'" % (sd,str(session["uid"]))
        data['sdview'] = db.select(qss)
        print(data["sdview"])
    if "updateS" in request.form:
        
        fna = request.form['fname']
        lna = request.form['lname']
        gen = request.form['Gender']
        d = request.form['db']
        hna = request.form['hname']
        pla = request.form['place']
        pco = request.form['pcod']
        dis = request.form['disrict']


        phone = request.form['phone']
        email = request.form['email']
        qualification = request.form['qualification']


        qul = "update login set username='%s' where login_id='%s' " % (email,  sd)
        db.insert(qul)
        if 'photo' in request.files:
            profile = request.files['photo']
            if profile.filename!="":
                s=str(uuid.uuid4()) + ".jpg"
                path = r'C:\\Users\\HP\\Desktop\\uniqueid\\static\\teacher\\' +s
                profile.save(path)
                p1="/static/teacher/"+s
                qus = "UPDATE `teacher` SET `first_name`='"+fna+"',`last_name`='"+lna+"',`gender`='"+gen+"',`dob`='"+d+"',`house_name`='"+hna+"',`place`='"+pla+"',`pincode`='"+pco+"',`district`='"+dis+"',`phone`='"+phone+"',`email`='"+email+"',`qualification`='"+qualification+"',`photo`='"+p1+"' WHERE `login_id`='"+sd+"'"
                db.insert(qus)
            else:
                qus = "UPDATE `teacher` SET `first_name`='" + fna + "',`last_name`='" + lna + "',`gender`='" + gen + "',`dob`='" + d + "',`house_name`='" + hna + "',`place`='" + pla + "',`pincode`='" + pco + "',`district`='" + dis + "',`phone`='" + phone + "',`email`='" + email + "',`qualification`='" + qualification + "' WHERE `login_id`='" + sd + "'"
                db.insert(qus)
        else:
            qus = "UPDATE `teacher` SET `first_name`='" + fna + "',`last_name`='" + lna + "',`gender`='" + gen + "',`dob`='" + d + "',`house_name`='" + hna + "',`place`='" + pla + "',`pincode`='" + pco + "',`district`='" + dis + "',`phone`='" + phone + "',`email`='" + email + "',`qualification`='" + qualification + "' WHERE `login_id`='" + sd + "'"
            db.insert(qus)
        return redirect(url_for('admin_add_teachers'))

    qstud = "SELECT *,CONCAT(teacher.first_name,' ',teacher.last_name)AS name,teacher.login_id as tlogin_id FROM `teacher` where  clgid='%s'" % (str(session["uid"]))

    data['stview'] = db.select(qstud)
    print(data["stview"])
    return render_template('admin_add_teachers.html', data=data)


@app.route('/clgvwnotif')
def clgvwnotif():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    qry = "select * from notifctn where clg='" + str(session["uid"]) + "'"
    print("qry333=" + qry)
    db = Db()
    re = db.select(qry)

    return render_template("College_View_Notification.html", data=re, m="0")

# Staff ----------------------

@app.route('/CollegeAddInternal')
def CollegeAddInternal():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    a = "select course.crsid,course.crs from coursealloc inner join course on coursealloc.crs = course.crsid where coursealloc.clgname='"+str(session["mcid"])+"'"
    print(a)
    print("a="+a)
    db=Db()
    re = db.select(a)

    b = "select crsid,batch,id from batch"
    print("b=" + b)


    re1 = db.select(b)


    d = "select subjectid,subject from subject"
    print("d=" + d)


    re3 = db.select(d)

    return render_template("staff_add_internal.html",data=re, data1=re1,data3=re3,id=id)


@app.route('/staff_view_internals')
def staff_view_internals():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    a = "select course.crsid,course.crs from coursealloc inner join course on coursealloc.crs = course.crsid where coursealloc.clgname='"+str(session["mcid"])+"'"
    print(a)
    print("a="+a)
    db=Db()
    re = db.select(a)

    b = "select crsid,batch,id from batch"
    print("b=" + b)


    re1 = db.select(b)


    d = "select subjectid,subject from subject"
    print("d=" + d)


    re3 = db.select(d)

    return render_template("staff_view_internal.html",data=re, data1=re1,data3=re3,id=id)


@app.route('/staff_view_internals_post',methods=['POST'])
def staff_view_internals_post():
    batch = request.form["batch"]
    course = request.form["course"]

    semester = request.form["semester"]
    subject=request.form['subject']

    session["batch"] = batch
    session["crs"] = course
    session["subject"] = subject
    session["sem"] = semester

    qry = "SELECT student.regno,NAME,`internalmk`.`internmrk`,`internalmk`.`attndnc` FROM student INNER JOIN `internalmk` ON `internalmk`.`regno`=`student`.`regno` inner join subject on subject.subjectid=internalmk.subjectid  WHERE student.crs='" + course + "' AND student.batch='" + batch + "' AND subject.sem='" + semester + "' AND clgid='" + str( session["mcid"]) + "' AND `internalmk`.`subjectid`='"+subject+"'"
    db=Db()
    print(qry)
    re=db.select(qry)
    print(re)
    print("hoiiiii")
    # if len(re)>0:
    return render_template("Staff_view_internalmrks2.html",data=re)

    # else:
    #     return '''<script>alert('No data');window.location='/staff_view_internals'</script>'''




@app.route('/CollegeAddInternal1', methods=['post'])
def CollegeAddInternal1():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    batch = request.form["batch"]
    course = request.form["course"]
    subject = request.form["subject"]
    semester = request.form["semester"]

    session["batch"] = batch
    session["crs"] = course
    session["subject"] = subject
    session["sem"] = semester

    qry = "select regno,name from student where crs='" + course + "' and batch='" + batch + "' and sem='" + semester + "' and clgid='" + str( session["mcid"]) + "'"
    db=Db()
    print(qry)
    re=db.select(qry)
   # return "ok"
    if len(re)>0:
        return render_template("Staff_Add_InternalmarkII.html", data=re)
    else:
        return '''<script>alert('No students found');window.location='/CollegeAddInternal'</script>'''






@app.route('/CollegeAddInternal2', methods=['post'])
def CollegeAddinternal2():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    batch = session["batch"]
    course = session["crs"]
    semester = session["sem"]

    qry = "select regno from student where crs='" + course + "' and batch='" + batch + "' and sem='" + semester + "' and clgid='" + str(session["mcid"]) + "' "
    print("mm=="+qry)
    db=Db()
    re=db.select(qry)
    stid = []
    for i in re:
        stid.append(i[0])
    attndnc=request.form.getlist("attnd")
    sz1=len(attndnc)
    mark = request.form.getlist("intmark")
    sz = len(mark)
    sz1==sz
    a = "select regno from student where crs='" + course + "' and batch='" + batch + "' and sem='" + semester + "' and clgid='"+str( session["mcid"])+"' "
    print("mm==" + a)

    re=db.select(a)

    print(str(re))
    if len(re)>0:
        print("haiiiii")
        callid=""
        print("size",len(mark))
        for r in range(sz):
            print("mark",mark[r])
            if int(mark[r])<= 40:
                b = "select regno,subjectid from internalmk where regno='" + str(stid[r]) + "'and subjectid='" +session["subject"] + "'"
                print("re1="+b)
                re1=db.selectOne(b)
                print("regno")
                print(re1)
                if re1 is not None:
                    print("mri")
                    pass
                    # return '''<script>alert('Data Already entered');</script>'''
                else:

                    qry = "insert into internalmk(regno,subjectid,internmrk,attndnc)values('" + str(stid[r]) + "','" + str(session["subject"]) + "','" + str( mark[r]) + "','" + str(attndnc[r]) + "')"
                    print(qry)
                    db.insert(qry)

        a = "update callinternal set status='updated' where clg='" + str(session["mcid"]) + "'"
        db.update(a)
        return '''<script>alert('Data saved');window.location='/CollegeAddInternal'</script>'''
       

    else:
        print("tst_mri")
        return '''<script>alert('Data already entered');window.location='/CollegeAddInternal'</script>'''



@app.route('/staff_view_profile')
def staff_view_profile():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    db=Db()
    qss = "select * from teacher inner join login using (login_id) where teacher_id='%s' " % ( str(session["uid"]))
    data = db.select(qss)

    return render_template("Staff_view_profile.html", data=data)


@app.route('/staff_view_crs_alloc')
def staff_view_crs_alloc():
    if  session["lid"] == "" :
        return '''<script>alert('Not Logged in ');window.location='/login'</script>'''


    qry = "SELECT * FROM coursealloc INNER JOIN `course` ON `course`.`crsid`=`coursealloc`.`crs` WHERE `clgname`='"+str(session["clgid"])+"' "
    print(qry)
    db=Db()
    re = db.select(qry)
    return render_template("staff_ViewAllocourse.html", data=re)



@app.route('/staff_view_batches/<id>')
def staff_view_batches(id):
    print()
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    session["crs"]=id
    qry = "SELECT * FROM `batch` WHERE `crsid`='"+id+"'"
    print(qry)
    db=Db()
    re = db.select(qry)
    return render_template("staff_view_batches.html", data=re)



@app.route('/staff_view_students/<id>')
def staff_view_students(id):
    print()
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    session["batch"]=id
    rr=session["clgid"]
    ii=session["crs"]
    
    print(rr)
    print(ii)
    print(id)
    
    qry = "SELECT * FROM `student` WHERE `clgid`='"+str(session["clgid"])+"' AND `crs`='"+str(session["crs"])+"' AND `batch`='"+id+"'"
    print(qry)
    db=Db()
    re = db.select(qry)
    print(re)
    return render_template("staff_View_Studet.html", data=re)


# =============================
@app.route('/staffvwnotif')
def staffvwnotif():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    qry = "select * from notifctn where clg='" + str(session["uid"]) + "' union (select * from notifctn where type='normal')"
    print("qry333=" + qry)
    db = Db()
    re = db.select(qry)

    return render_template("staff_View_Notification.html", data=re, m="0")


@app.route('/staffvwnotif_post', methods=['post'])
def staffvwnotif_post():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    type = request.form["notification"]
    if type == "normal":
        qry = "select * from notifctn WHERE  clg='%s'  union (select * from notifctn where type='normal')"%(session["uid"]) 
        db = Db()
        res = db.select(qry)
        return render_template("staff_view_Notification.html", data=res, m="1")
    elif type == "internal":
        aa = session["uid"]
        print("aa=" + str(aa))
        qry = "select * from notifctn,callinternal WHERE type='internal' and status='pending' and notifctn.callid=callinternal.callid"
        print(qry)
        db = Db()
        res = db.select(qry)

        return render_template("staff_view_Notification.html", data=res, m="1")

# ========================


# @app.route('/staffvwnotif')
# def staffvwnotif():
#     if session['lid']=="":
#         return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
#     qry = "select * from notifctn where clg='" + str(session["mcid"]) + "' union (select * from notifctn where type='normal')"
#     print("qry333=" + qry)
#     db = Db()
#     re = db.select(qry)

#     return render_template("staff_View_Notification.html", data=re, m="0")

@app.route('/staffvwnotif_post1', methods=['post'])
def staffvwnotif_post1():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    type = request.form["notification"]
    if type == "normal":
        qry = "select * from notifctn WHERE type='" + type + "' and clg='" + str(
            session["mcid"]) + "' union (select * from notifctn where type='normal')"
        db = Db()
        res = db.select(qry)
        return render_template("staff_view_Nnotif.html", data=res, m="1")
    elif type == "internal":
        aa = session["uid"]
        print("aa=" + str(aa))
        qry = "SELECT * FROM `callinternal` INNER JOIN `course` ON `course`.`crsid`=`callinternal`.`crsid` INNER JOIN `batch` ON `batch`.`id`=`callinternal`.`batch` WHERE clg='"+str(session["mcid"])+"'"

        db = Db()
        res = db.select(qry)
        return render_template("staff_View_Notification.html", data=re, m="0")
        return render_template("Colleges_View_Notification.html", data=res, m="1")


# @app.route('/staffvwnotif_post', methods=['post'])
# def staffvwnotif_post():
#     if session['lid']=="":
#         return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
#     type = request.form["notification"]
#     print(type,'0000000000000')
#     if type == "normal":
#         qry = "select * from notifctn WHERE type='" + type + "' and clg='" + str(
#             session["uid"]) + "' union (select * gtom notifctc where type='normal')"
#         db = Db()
#         res = db.select(qry)
#         return render_template("college_view_Nnotif.html", data=res, m="1")
#     elif type == "internal":
#         aa = session["uid"]
#         print("aa=" + str(aa))
#         qry = "select * from notifctn,callinternal WHERE type='" + type + "' and status='pending' and notifctn.callid=callinternal.callid"

#         db = Db()
#         res = db.select(qry)

#         return render_template("College_View_Notification.html", data=res, m="1")

@app.route('/college_view_marks')
def college_view_marks():
    if session['lid'] == "":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    a = "select course.crsid,course.crs from coursealloc inner join course on coursealloc.crs = course.crsid where coursealloc.clgname='" + str(
        session["uid"]) + "'"
    print(a)
    print("a=" + a)
    db = Db()
    re = db.select(a)

    b = "select crsid,batch,id from batch"
    print("b=" + b)

    re1 = db.select(b)

    d = "select subjectid,subject from subject"
    print("d=" + d)

    re3 = db.select(d)

    return render_template("college_view_internal.html", data=re, data1=re1, data3=re3, id=id)

@app.route('/college_view_marks_post', methods=['POST'])
def college_view_marks_post():
    batch = request.form["batch"]
    course = request.form["course"]

    semester = request.form["semester"]
    subject = request.form['subject']

    session["batch"] = batch
    session["crs"] = course
    session["subject"] = subject
    session["sem"] = semester

    qry = "SELECT student.regno,NAME,`internalmk`.`internmrk`,`internalmk`.`attndnc`,externalmk.mark FROM student INNER JOIN `internalmk` ON `internalmk`.`regno`=`student`.`regno` INNER JOIN SUBJECT ON subject.subjectid=internalmk.subjectid INNER JOIN `externalmk` ON `externalmk`.`inter_id`=`internalmk`.`subjectid` WHERE student.crs='" + course + "' AND student.batch='" + batch + "' AND subject.sem='" + semester + "' AND clgid='" + str(session["uid"]) + "' AND `internalmk`.`subjectid`='" + subject + "' AND `externalmk`.`regno`=`internalmk`.`regno`"
    db = Db()
    print(qry)
    re = db.select(qry)
    print(re)
    print("hoiiiii")
    # if len(re)>0:
    return render_template("college_view_internalmrks2.html", data=re)

    # else:
    #     return '''<script>alert('No data');window.location='/staff_view_internals'</script>'''


# --------------------
@app.route('/Student_view_reply')
def Student_view_reply():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    lid = session["uid"]

    db = Db()
    qry = "SELECT * FROM `complaint` WHERE `uid`='" + str(lid) + "' AND `from`='student'"
    res = db.select(qry)
    print(res)
    return render_template("Student_view_reply.html", data=res)


@app.route('/student_send_complaints')
def student_send_complaints():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    return render_template("Student_send_complaint.html")


@app.route('/student_send_complaints_p', methods=['POST'])
def student_send_complaintss():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    complaint = request.form["textarea"]
    qry = "insert into `complaint`(`complaint`,`date`,`reply`,`status`,`uid`,`from`)values('" + complaint + "',curdate(),'pending','pending','" + str(
        session["uid"]) + "','student')"
    db = Db()
    db.insert(qry)
    return '''<script>alert('Complaint send successfully');window.location='/student_send_complaints'</script>'''

@app.route('/Student_view_profile')
def Student_view_profile():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    db = Db()
    qry = "SELECT student.*,course.*,batch.batch AS bt FROM student INNER JOIN `course` ON `course`.`crsid`=`student`.`crs` INNER JOIN batch ON `batch`.`id`=`student`.`batch` WHERE `student`.`stdntid`='" + str(session["uid"]) + "'"
    db = Db()

    data = db.selectOne(qry)

    return render_template("Student_view_profile.html", data=data)


# =======================
@app.route('/student_view_marks_post',methods=['POST'])
def student_view_marks_post():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    db=Db()
    sem=request.form["semester"]
    qry1 = "select sem,course.crsid,batch ,name,course.crs,regno,photo from  student inner join course on course.crsid=student.crs where stdntid='" + str(session["uid"]) + "'"
    res22 = db.selectOne(qry1)
    print(qry1)
    # sem = res22[0]
    crs = res22[1]
    bat = res22[2]
    regno = res22[5]
    name = res22[3]
    photo = res22[6]
    crsname = res22[4]
    k = 0
    aa = 0
    sublen = 0
    l=[]

    qt1 = "SELECT * FROM `subject` WHERE `crs`='" + str(crs) + "' AND `batch`='" + str(bat) + "' AND `sem`='" + str(
        sem) + "'"
    dbn = Dbnew()
    rest1 = dbn.select(qt1)
    print(rest1)
    for j in rest1:
        subject = str(j["subjectid"]) 

        sub=j['subject']
        query1 = "SELECT `externalmk`.`mark` FROM   `externalmk` WHERE `inter_id`='" + str(
            subject) + "' AND `externalmk`.`regno`='" + str(regno) + "' "
        print(query1)
        res1 = dbn.selectOne(query1)
        print(res1)
        if res1 is not None:
            mark = int(res1['mark'])
        else:
            mark="Not Available"
        query2 = "SELECT `internalmk`.`internmrk` FROM `internalmk` INNER JOIN `subject` ON `subject`.`subjectid`=`internalmk`.`subjectid` INNER JOIN `externalmk` ON `externalmk`.`inter_id`=`subject`.`subjectid` WHERE `subject`.`subjectid`='" + str(
            subject) + "' AND   `internalmk`.`regno`='" + str(
            regno) + "'"
        res2 = dbn.selectOne(query2)
        if res2 is not None:
            mark2=res2['internmrk']
        else:
            mark2="Not Available"
        l.append({"subject":sub,"internal":mark2,"external":mark})
    return render_template("student_view_mark.html",l=l)


@app.route('/student_view_marks')
def student_view_marks():
    if session['lid']=="":
        return '''<script>alert('You havent logged in'); window.location='/login'</script>'''
    return render_template("student_view_mark.html")


@app.route('/and_login', methods=['get', 'post'])
def login_and():
    username = request.form['Username']
    password = request.form['Password']
    print(username,password)
    k="select * from login where username='%s' and pswd='%s'"%(username,password)
    db=Dbnew()
    res=db.selectOne(k)
    if res:
        lid=res['login_id']

        if res['type']=='verifier':
            y="select * from verifier where login_id='%s'"%(lid)
            h=db.selectOne(y)
            if h is not None:
                sid=h['verifier_id']

                return jsonify(status='ok',lid=lid,uid=sid,name=['Name'])
            else:
                return jsonify(status='no')
        else:
            return jsonify(status='no')
    else:
        return jsonify(status='no')



@app.route('/and_signup', methods=['get', 'post'])
def and_signup():
    name = request.form['name']
    phone = request.form['phone']
    mail = request.form['mail']
    passw = request.form['pass']
    qual = request.form['qual']

    db = Db()
    qry1 = "insert into login(Username,pswd,type) values('" + str(mail) + "','" + str(passw) + "','verifier')"

    i = db.insert(qry1)
    qry = "INSERT INTO `verifier` (`login_id`,`phone`,`Name`,`Email`,`Purpose`)VALUES('"+str(i)+"','"+phone+"','"+name+"','"+mail+"','"+qual+"')"

    db = Db()
    db.insert(qry)
    return jsonify(status='ok')
# def parse_scanned_content(scanned_content):
#     data = {}
#     lines = scanned_content.strip().split('\n')
#     for line in lines:
#         key, value = line.split(': ')
#         if key == 'Registration Number':
#             data['registration_number'] = value
#         # elif key == 'Face Features':
#             # Extract face features and convert them to numpy array
#             # data['face_features'] =value
#     return data
@app.route('/andro_qr', methods=['get', 'post'])
def andro_qr():
    name = request.form['content']
    pid=request.files["pic"]
    lid=request.form["lid"]
    import datetime
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    path=r"C:\Users\HP\Desktop\uniqueid\static\report\\"+now+".jpg"
    po="/static/report/"+now+".jpg"
    pid.save(path)
    pid.seek(0)

    print(name)
    db = Dbnew()

    select="SELECT * FROM `student` WHERE `regno`='"+name+"'"

    re=db.selectOne(select)
    if re is not None:
        p1=r"C:\\Users\\HP\\Desktop\\uniqueid\\static\\image\\"+re["photo"]
        picture_of_me = face_recognition.load_image_file(p1)
        my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

        picture_of_post = face_recognition.load_image_file(path)

        others_face_encoding = face_recognition.face_encodings(picture_of_post)

        totface = len(others_face_encoding)
        print(totface)
        m = 0
        for i in others_face_encoding:
            res = face_recognition.compare_faces([my_face_encoding], i, tolerance=0.5)
            print(res)

            l = 0


            if res[0]:
                m+=1
                return jsonify(status='ok', name="This is an original certificate of " + re["name"], photo=re['photo'])
        else:
            QRY = "INSERT INTO `report` (`file`,`date`,`verifier_lid`,`status`)VALUES('" + po + "',CURDATE(),'" + lid + "','pending')"
            db.insert(QRY)
            return jsonify(status="no",name="This is a Fake Certificate")



    else:
        QRY = "INSERT INTO `report` (`file`,`date`,`verifier_lid`,`status`)VALUES('" + po + "',CURDATE(),'" + lid + "','pending')"
        db.insert(QRY)
        return jsonify(status="no",name="This is a Fake Certificate")
if __name__ == "__main__":
    app.run(debug=True,port=5050,host='0.0.0.0')

