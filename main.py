import time
from flask import Flask

app=Flask(__name__)

Start=time.time()

def elapsed():
    running=time.time()-Start
    minutes,seconds=divmod(running,60)
    hours,minutes=divmod(minutes,60)
    
    return "%d:%02d:%02d" %(hours,minutes,seconds)


@app.route("/")
def root():
    return f"Hello Everyone!! App is running at {elapsed()}"

if __name__=='__main__':
    app.run(debug=True,host="0.0.0.0",port=8070)

