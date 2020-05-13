from flask import Flask, render_template, request
app = Flask(__name__)
import sqlite3

@app.route('/')
def home():
   return render_template('Home.html')

@app.route('/faculty')
def faculty():
   return render_template('Faculty.html')

@app.route('/student')
def student():
   return render_template('Student.html')

@app.route('/facspace1',methods = ['POST', 'GET'])
def facultyspace1():
    if request.method == 'POST':
        result = request.form.to_dict()
        conn = sqlite3.connect('marks1.db')
        c = conn.cursor()
        c.execute("select username from faculty where username=:username",{'username':result['username']})
        s1=c.fetchall()
        c.execute("select username from faculty where password=:password",{'password':result['password']})
        s2 = c.fetchall()
        if(len(s1)!=0)&(len(s2)!=0):
            c.execute("select subject from faculty where username=:password",{'password':result['password']})
            s3 = c.fetchall()
            conn.commit()
            conn.close()
            return render_template('Entermark.html')
        else:
            conn.commit()
            conn.close()
            return render_template('Faculty.html')

@app.route('/afterenter',methods = ['POST', 'GET'])
def facultyspace2():
    if request.method == 'POST':
        result = request.form.to_dict()
        conn = sqlite3.connect('marks1.db')
        c = conn.cursor()
        c.execute("INSERT INTO '{}' VALUES('{}','{}','{}','{}','{}','{}')".format(result['subject'],result['subject'],result['roll'],result['p1'],result['p2'],result['ca'],result['sem']))
        c.execute("select * from '{}' ".format(result['subject']))
        print(c.fetchall())
        conn.commit()
        conn.close()
        return render_template('Entermark.html')

@app.route('/studspace1',methods = ['POST', 'GET'])
def studentspace1():
    if request.method == 'POST':
        result = request.form.to_dict()
        conn = sqlite3.connect('marks1.db')
        c = conn.cursor()
        c.execute("select username from students where username=:username", {'username': result['username']})
        s1 = c.fetchall()
        c.execute("select username from students where password=:password", {'password': result['password']})
        s2 = c.fetchall()
        if(len(s1)!=0)&(len(s2)!=0):
            c.execute("select rollno from students where username=:username", {'username': result['username']})
            s3=c.fetchall()
            z1 = str(s3[0])
            print(z1)
            z2 = z1[2:len(z1) - 3]
            if(len(s3)!=0):
                result1 = {}
                c.execute("select * from Openlab where rollno=:rollno", {'rollno': z2})
                p=c.fetchall()
                p1=str(p)
                q1 = p1[3:len(p1) - 2]
                print(q1)
                a = []
                temp = 0
                i = 0
                while i < (len(q1)):
                    if (q1[i] == ','):
                        if (q1[i - 1] == "'"):
                            a.append(q1[temp:i - 1])
                            temp = i + 2
                            i = i + 1
                        else:
                            a.append(q1[temp:i])
                            temp = i + 2
                            i = i + 1
                    i = i + 1
                a.append(q1[temp:len(q1)])
                fin1 = {}
                fin1['subject'] = a[0]
                fin1['periodical1'] = a[2]
                fin1['periodical2'] = a[3]
                fin1['Continuous assesment'] = a[4]
                fin1['End sem'] = a[5]
                fin1['Grade'] = 'A'
########################################3
                q = c.execute("select * from Network where rollno=:rollno", {'rollno': z2})
                q = c.fetchall()
                p1=str(q)
                q1 = p1[3:len(p1) - 2]
                print(q1)
                a = []
                temp = 0
                i = 0
                while i < (len(q1)):
                    if (q1[i] == ','):
                        if (q1[i - 1] == "'"):
                            a.append(q1[temp:i - 1])
                            temp = i + 2
                            i = i + 1
                        else:
                            a.append(q1[temp:i])
                            temp = i + 2
                            i = i + 1
                    i = i + 1
                a.append(q1[temp:len(q1)])
                fin2 = {}
                fin2['subject'] = a[0]
                fin2['periodical1'] = a[2]
                fin2['periodical2'] = a[3]
                fin2['Continuous assesment'] = a[4]
                fin2['End sem'] = a[5]
                fin2['Grade'] = 'B'
####################################
                r = c.execute("select * from MachineLearning where rollno=:rollno", {'rollno': z2})
                r = c.fetchall()
                p1 = str(r)
                q1 = p1[3:len(p1) - 2]
                print(q1)
                a = []
                temp = 0
                i = 0
                while i < (len(q1)):
                    if (q1[i] == ','):
                        if (q1[i - 1] == "'"):
                            a.append(q1[temp:i - 1])
                            temp = i + 2
                            i = i + 1
                        else:
                            a.append(q1[temp:i])
                            temp = i + 2
                            i = i + 1
                    i = i + 1
                a.append(q1[temp:len(q1)])
                fin3 = {}
                fin3['subject'] = a[0]
                fin3['periodical1'] = a[2]
                fin3['periodical2'] = a[3]
                fin3['Continuous assesment'] = a[4]
                fin3['End sem'] = a[5]
                fin3['Grade'] = 'A+'
###################################
                s = c.execute("select * from Software where rollno=:rollno", {'rollno': z2})
                s = c.fetchall()
                p1 = str(s)
                q1 = p1[3:len(p1) - 2]
                print(q1)
                a = []
                temp = 0
                i = 0
                while i < (len(q1)):
                    if (q1[i] == ','):
                        if (q1[i - 1] == "'"):
                            a.append(q1[temp:i - 1])
                            temp = i + 2
                            i = i + 1
                        else:
                            a.append(q1[temp:i])
                            temp = i + 2
                            i = i + 1
                    i = i + 1
                a.append(q1[temp:len(q1)])
                fin4 = {}
                fin4['subject'] = a[0]
                fin4['periodical1'] = a[2]
                fin4['periodical2'] = a[3]
                fin4['Continuous assesment'] = a[4]
                fin4['End sem'] = a[5]
                fin4['Grade'] = 'O'
            result1=[]
            result1.append(fin1)
            result1.append(fin2)
            result1.append(fin3)
            result1.append(fin4)
            conn.commit()
            conn.close()
            return render_template('Displayscore.html',result=result1)
        else:
            conn.commit()
            conn.close()
            return render_template('Student.html')

# conn = sqlite3.connect('marks1.db')
# c = conn.cursor()
# c.execute("""CREATE TABLE faculty (
#                       name text ,
#                       subject text ,
#                       facultyid numeric ,
#                       username text ,
#                        password text )""")
# 
# c.execute("INSERT INTO faculty VALUES('Dhanya','Openlab',12341,'Dhanya9','openlab')");
# c.execute("INSERT INTO faculty VALUES('Narayan','Network',12342,'Natayan3','netintowork')");
# c.execute("INSERT INTO faculty VALUES('Gowtham','MachineLearning',12343,'gowthang9','myml')");
# c.execute("INSERT INTO faculty VALUES('Senthil','Software',12344,'mesenthil7','agile')");
#
# c.execute("""CREATE TABLE students (
#                       name text,
#                       rollno text ,
#                       username text ,
#                        password text ,
#                        primary key(rollno))""")
#
# c.execute("INSERT INTO students VALUES('satvik','cse17334','satvik99','12345')");
# c.execute("INSERT INTO students VALUES('jaya vamshhi','cse17367','vamshhiv9','cse67651')");
# c.execute("INSERT INTO students VALUES('manikanta','cse17327','mani','javaji')");
# c.execute("INSERT INTO students VALUES('jaya bharath','cse17363','jayabha','12346')");
# c.execute("INSERT INTO students VALUES('abhiram','cse17347','abhii','navy')");
# c.execute("INSERT INTO students VALUES('mahesh','cse17357','mahi','kathi')");
#
# c.execute("""CREATE TABLE Openlab (
#                       subject text,
#                       rollno text,
#                       p1 numeric ,
#                       p2 numeric ,
#                       contiass numeric ,
#                        sem numeric )""")
#
# c.execute("""CREATE TABLE Network (
#                    subject text,
#                       rollno text,
#                       p1 numeric ,
#                       p2 numeric ,
#                       contiass numeric ,
#                        sem numeric )""")
#
# c.execute("""CREATE TABLE MachineLearning (
#                   subject text,
#                       rollno text,
#                       p1 numeric ,
#                       p2 numeric ,
#                       contiass numeric ,
#                        sem numeric )""")
#
# c.execute("""CREATE TABLE Software (
#                     subject text,
#                       rollno text,
#                       p1 numeric ,
#                       p2 numeric ,
#                       contiass numeric ,
#                        sem numeric )""")
# conn.commit()
# conn.close()

if __name__ == '__main__':
   app.run(debug = True)