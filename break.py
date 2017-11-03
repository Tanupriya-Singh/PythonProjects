import time
import webbrowser

total=3
count=0
print("This program strated on"+time.ctime())
while(count<total):
    time.sleep(10)
    print ("time:"+time.ctime())
    webbrowser.open("https://www.youtube.com/watch?v=lpdRqn6xwiM")
    count=count+1
