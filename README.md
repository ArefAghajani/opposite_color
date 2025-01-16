### OPPOSITE COLOR GENERATOR
---
## what it does
this program genrate the oppsite color using the color hex code.
example ==> opposite of color #FFFFFF (white) is #000000 (black)

## how it works
every 2 charcter of this code can be converted to an int between 0 to 255.

#2f4ab2 ==> red: 2f, green: 4a, blue:b2 ==> conver hex to 10 base int.

after calculating the main number int we find its complementary int.

after that convert that int into hex and concatenate them.

**how to run** :
1. clone the code locally in your device.
2. channge your directory to the project dirctory
3. install flask using pip `pip install flask`
4. set the enviroment var `set FLASK_APP=app.py` in windows and `export FLASK_APP=app.py`
5. run the server `flask run`
6. open browser and go to `localhost:5000`(you can see the right url after running the server)
