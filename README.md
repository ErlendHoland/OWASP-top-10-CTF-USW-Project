# OWASP-top-10-CTF-USW-Project


![#c5f015](https://via.placeholder.com/15/c5f015/000000?text=+) `FLAG{Welcome_and_enjoy!}`


# Setup instructions:
## Run with docker compose: (Required for challenge 6)

``` 
sudo apt-get install docker-compose -y
```
``` 
sudo apt-get install curl -y
```
``` 
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```
```
sudo chmod +x /usr/local/bin/docker-compose
```
```
git clone https://github.com/ErlendHoland/OWASP-top-10-CTF-USW-Project.git
```
``` 
cd OWASP-top-10-CTF-USW-Project
```
```
sudo docker-compose up -d
```
Access in browser http://localhost/

## Run with docker:

``` 
git clone https://github.com/ErlendHoland/OWASP-top-10-CTF-USW-Project.git
```
```
cd OWASP-top-10-CTF-USW-Project
```
```
sudo docker build -t ctf .
```
```
sudo docker run -p 80:5000 -d ctf
```
Access in browser http://localhost/

## Run in virtual environment:
### Windows:
```
git clone https://github.com/ErlendHoland/OWASP-top-10-CTF-USW-Project.git
```
```
cd OWASP-top-10-CTF-USW-Project
```
```
pip install virtualenv
```
```
.\env\Scripts\activate
```
```
python app.py
```
Access in browser http://localhost:5000/

### Linux:
```
git clone https://github.com/ErlendHoland/OWASP-top-10-CTF-USW-Project.git
```
```
cd OWASP-top-10-CTF-USW-Project
```
```
pip install virtualenv
```
```
source env/Scripts/activate
```
```
python app.py
```
Access in browser http://localhost:5000/


## Run in virtual environment from scratch:

### Windows:
```
git clone https://github.com/ErlendHoland/OWASP-top-10-CTF-USW-Project.git
```
```
cd OWASP-top-10-CTF-USW-Project
```
```
pip install virtualenv
```
```
python -m venv env
```
```
.\env\Scripts\activate
```
```
pip install -r requirements.txt
```
```
python app.py
```
Access in browser http://localhost:5000/

### Linux:
```
git clone https://github.com/ErlendHoland/OWASP-top-10-CTF-USW-Project.git
```
```
cd OWASP-top-10-CTF-USW-Project
```
```
pip install virtualenv
```
```
python -m venv env
```
```
source env/Scripts/activate
```
```
pip install -r requirements.txt
```
```
python app.py
```
Access in browser http://localhost:5000/

## Run without virtual environment:
```
git clone https://github.com/ErlendHoland/OWASP-top-10-CTF-USW-Project.git
```
```
cd OWASP-top-10-CTF-USW-Project
```
```
pip install -r requirements.txt
```
```
python app.py
```
Access in browser http://localhost:5000/
