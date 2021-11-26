# adData 
##A project that gives useful data to small businesses!
### How to use this website!
###### *This is done with Mac commands*

1. Make sure to have python installed in your computer
2. Make folder for this project and *cd* into it
3. Clone this repository into that folder(I personally use _Github Desktop_ because it is so much easier!)
```
git clone https://github.com/<Username>/<Name of Repo>.git>
```
6. Create a venv and activate it
```
pip3 install virtualenv
virtualenv venv
source venv/bin/activate
```
7. Install all project dependencies
```
pip3 install -r requirements.txt
```
8. Be sure to add your own Secret Key and Email credentials in Settings.py
9. Create the database
```
python3 manage.py migrate
```
10. Create a superuser and fill out the prompts, the password will be blank(it is for security)
```
python3 manage.py createsuperuser
```
11. Create a file named .env in adData file and add the Secret Key to ths file(ignore < and >)
```
SECRET_KEY=<some key>
```
 
