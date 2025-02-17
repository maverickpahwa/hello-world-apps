
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
  
how to add an app to github from local computer


Run the Flask Tests
Inside backend/, run:pytest test_app.py
It should output:
2 passed in X seconds

Install Dependencies (if not installed)
Inside frontend/, run: npm install --save-dev jest @testing-library/react @testing-library/jest-dom

Run React Tests
Inside frontend/, run: npm test
Expected output:
? renders API response message (Xms)

added 1481 packages, and audited 1482 packages in 7m
268 packages are looking for funding
  run `npm fund` for details
8 vulnerabilities (2 moderate, 6 high)
To address all issues (including breaking changes), run:
  npm audit fix --force
