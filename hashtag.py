from bottle import run,route,get,post,request,template,static_file
from twarc import Twarc
import pandas as pd
t=Twarc("JNaw7CRIGnQWxHH3C6tcpF0fP","1opF4IfXrtzcUPOJUvnSr4wXbYpVGEJ8J4oBHAzEqRxV1p9FVO","1055391684354203648-bmiuojBuJ8S0a4cQEGErobfaPVMIQV","5R457jy32zTCVtwlQkZCKUtM9mMjgod9fw02g6zNWCOzW")										
twdata = None
@get('/get_details')
def get_detail():
        
        return '''<!doctype html>
        <html>
        <head>
        <title>twitter</title>
        <style>
        body{
        background-image:url("https://thetrendingprof.com/wp-content/uploads/2013/11/twitter.jpg");
        background-size: 1300px 800px;
        background-repeat:no-repeat;
        } 
        #rcorners3{
        border-radius: 80px 0px;
        background-image:url("http://www.hdwallpapers10.com/wp-content/uploads/2017/05/Black%20and%20White%20abstract%20Background%20Full%20HD-623x623.png");
        padding: 20px; 
        width: 500px;
        height: 200px;
        opacity:0.8; 
        }
        </style>
        </head>
        <body><b>
        <h1 align="center" style="color:royalblue">Hashtag Analysis</h1></b>
        <form id=rcorners3 method="post" action="/get_details">
												
        <img src="http://realmomentsphotography.com.au/wp-content/uploads/2016/07/twitter.png" height="100px" width="100px">
        <p align="center" style="color:deeppink"><b>Hashtag:</b>
        <input type="text" placeholder="enter hashtag" name="hashtag" ><br>
        <br>
        <input type="submit" value="Search"></p>
        </form>
        </body>
        </html>
        '''

@route("/<hashtag>")
def search(has):
	global twdata,data2,data4,data6
	c=0
	news=[]
	print("in hashtag")
	for tweet in t.search(has):
		tweet['followers_count'] = tweet['user']['followers_count']
		#print(tweet['followers_count'] )
		news.append(tweet)
		if c>100:
			break
		c=c+1
	data = pd.DataFrame(news)
	data['favorite_count'] = data['favorite_count'].apply(pd.to_numeric)
	data = data.sort_values(by='favorite_count', ascending=False)
	twdata = data
	data1 = data.sort_values(by='followers_count', ascending=False)
	data2 = data1
	data3 = data.sort_values(by='retweet_count', ascending=False)
	data4 = data3
	data5 = data.sort_values(by='full_text', ascending=False)
	data6 = data5
	#print("im fine till here")
	return template('temp', data=twdata)
#@route('/favs')
@route('/favs')

def favs():
	global twdata
	print("i am in favs")
	count = twdata.sort_values(by='favorite_count',ascending=False)
	return template('favs',data=twdata)
@route('/user')
def user():
	global data2
	print("i am in user")
	user = twdata.sort_values(by='followers_count',ascending=False)
	return template('favs',data=data2)
@route('/retweets')
def retweets():
	global data4
	print("i am in retweets")
	user = twdata.sort_values(by='retweet_count',ascending=False)
	return template('favs',data=data4)
@route('/fulltext')
def fulltext(): 											
	global data6
	print("i am in fulltext")
	user = twdata.sort_values(by='full_text',ascending=False)
	return template('favs',data=data6)
#@get("/get_details")
#def hello():
#	return template("proj", data=twdata)
@post('/get_details')
def do_get():
	has = request.forms.get("hashtag")
	print(has)
	return search(has)
#run(host="localhost",reloader="True",port="8002")
run(host = 'Localhost',port=8080,debug=True)

