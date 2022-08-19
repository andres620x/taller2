python3 -m venv .venv   //isolate libraries for this application

source .venv/bin/activate  //activate virtual env

pip install fastapi

pip install "uvicorn[standard]"


pip3 freeze > requirements.txt // transportar dependiencias

touch main.py //crear archivo vacio main.py
  
Charm .   //abrir PyCharm el contenido del directorio actual

