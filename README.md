# OWASP-top-10-CTF-USW-Project


# Setup instructions:

## Run with docker:

``` 
git clone https://github.com/ErlendHoland/OWASP-top-10-CTF-USW-Project.git

cd OWASP-top-10-CTF-USW-Project

sudo docker build -t ctf .

sudo docker run -p 80:5000 -d ctf
```
Access in browser http://localhost/

## Run in virtual environment:
Windows:
```
git clone https://github.com/ErlendHoland/OWASP-top-10-CTF-USW-Project.git

cd OWASP-top-10-CTF-USW-Project

pip install virtualenv

.\env\Scripts\activate

python app.py
```
Access in browser http://localhost:5000/

Linux:
```
git clone https://github.com/ErlendHoland/OWASP-top-10-CTF-USW-Project.git

cd OWASP-top-10-CTF-USW-Project

pip install virtualenv

source env/Scripts/activate

python app.py
```
Access in browser http://localhost:5000/



## Run in virtual environment from scratch:

Windows:
1. git clone https://github.com/ErlendHoland/OWASP-top-10-CTF-USW-Project.git
2. cd OWASP-top-10-CTF-USW-Project
3. pip install virtualenv
4. python -m venv env
5. .\env\Scripts\activate
6. pip install -r requirements.txt
7. python app.py
8. Access in browser http://localhost:5000/

Linux:
1. git clone https://github.com/ErlendHoland/OWASP-top-10-CTF-USW-Project.git
2. cd OWASP-top-10-CTF-USW-Project
3. pip install virtualenv
4. python -m venv env
5. source env/Scripts/activate
6. pip install -r requirements.txt
7. python app.py
8. Access in browser http://localhost:5000/
