
http://192.168.0.238:5000/heartbeat

How to Test the Heartbeat

Once the app is running, you can check the heartbeat by visiting:
?? http://localhost:5000/heartbeat

It should return:

{
  "status": "running",
  "service": "flask-backend"
}



Things to add:
1. Send these objects back to flask from react for mortality = 1 and save to file alive.csv
2. Send these objects back to flask from react for mortality = 1 and save to file dead.csv

3. Keep these names in memory and display count of alive and dead using client browser
4. store result in postgres and add another button to save to db
5. Write a client python file that keep generating these names and they can appear on the react page
6. 
  
