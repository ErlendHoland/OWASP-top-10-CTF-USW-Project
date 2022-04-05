# OWASP-top-10-CTF-USW-Project


Run with docker:

1. git clone https://github.com/ErlendHoland/OWASP-top-10-CTF-USW-Project.git
2. cd OWASP-top-10-CTF-USW-Project
3. sudo docker build -t ctf .
4. sudo docker run -p 80:5000 -d ctf
5. Access in browser http://localhost/

##Run in virtual environment:

Windows:
1. git clone https://github.com/ErlendHoland/OWASP-top-10-CTF-USW-Project.git
2. cd OWASP-top-10-CTF-USW-Project
3. pip install virtualenv
4. python -m venv env
5. .\env\Scripts\activate

Linux:
1. git clone https://github.com/ErlendHoland/OWASP-top-10-CTF-USW-Project.git
2. cd OWASP-top-10-CTF-USW-Project
3. pip install virtualenv
4. python -m venv env
5. source env/Scripts/activate
6. pip install -r requirements.txt
7. python app.py
 
