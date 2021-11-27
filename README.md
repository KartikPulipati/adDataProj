# adData 
## A project that gives useful data to small businesses!
### How to use this website!

**1. Make sure to have python installed in your computer**\
**2. Make folder for this project and *cd* into it**\
**3. Clone this repository into that folder(I personally use _Github Desktop_ because it is so much easier!)**
```
git clone https://github.com/<Username>/<Name of Repo>.git>
```
**4. Create a venv and activate it**

LINUX:
```
pip3 install virtualenv
virtualenv venv
source venv/bin/activate
```
WINDOWS:
```
pip install virtualenv
virtualenv myenv
cd myenv/Scripts
./activate
```
**5. Install all project dependencies**

LINUX:
```
pip3 install -r requirements.txt
```
WINDOWS:
```
pip install -r requirements.txt
```
**6. Create a file named .env in adData file and add the Secret Key to ths file(ignore < and >)**
```
SECRET_KEY=<some key>
```
**7. Create the database**

LINUX:
```
python3 manage.py migrate
```
WINDOWS:
```
py manage.py migrate
```
**8. Create a superuser and fill out the prompts, the password will be blank(it is for security)**

LINUX:
```
python3 manage.py createsuperuser
```
WINDOWS:
```
py manage.py createsuperuser
```

