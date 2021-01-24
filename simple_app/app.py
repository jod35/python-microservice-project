''' How to build a simple Flask App '''

from flask import Flask,jsonify,request,g,request_finished,abort
from flask.signals import signals_available
from werkzeug.exceptions import HTTPException,default_exceptions
#import necessary tools





app=Flask(__name__)

app.testing =True  #necessary when testing

#registering a blueprint called 'team_bp' located in teams.py
from simple_app.teams import team_bp
app.register_blueprint(team_bp)

#create a view with a route '/'
@app.route('/api')
def my_simple_microservice():
    print("Info about the request\n")
    print(request)
    print("The request environment\n")
    print(request.environ)
    
    response=jsonify({"message":"Hello"})

    print(response)

    return response

@app.route('/api/<name>',methods=['GET','DELETE','POST'])
def greet(name):
    return jsonify({"Hello":name})

#The way we pass variables is by using the <variable> format
#Flask enables us to specify HTTP methods within the route decorator

@app.before_request
def authentication():
    if request.authorization:
        g.user=request.authorization['username']
    else:
        g.user='Anonymous'
        

@app.route('/api/user')
def hello_user():
    return jsonify({"Hello":g.user}) 
'''
    returns {
        "Hello": "Anonymous"
    } 
    or 
    {
        "Hello": <user>
    }
    if a user is specified in the authentication header

'''

#checking if flask signals are available 
if not signals_available:
    raise RuntimeError("Blinker is not installed \n run 'pip3 install blnker'")

def finished(sender,response,**extra):
    # print("About to send a request")
    print(response)

request_finished.connect(finished)

@app.route('/api/signal')
def signal():
    return jsonify({"hello":g.user})




# creating a custom error handler view
@app.errorhandler(404) #handling a 404 error this time
def not_found(error):
    return jsonify({"error":str(error)}),404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"message":str(error)}),500









if __name__ == "__main__":
    # print(app.url_map)

    '''
        Each time we create a route with the @app.route decorator, Flask uses werkzeug to create 
        various rules associated for the endpoints of our app.
        
        These can all be found within the app.url_app
    ''' 
    app.run(debug=True) #run the app


'''
    The __name__ has the to have the value of __main__ so as to make the app run. It is used by Flask
    to locate the root directory of the app. (aids in locating static and template folders)
'''