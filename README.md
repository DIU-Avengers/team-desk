

Step 1 : Start docker containers.

```
docker compose up -d
```

Step 2 : (if first time) :
```
python3 -m venv .venv
```

Step 3 : active the virtual environment
```
source .venv/bin/activate
.\venv\Scripts\activate.bat # for windows

```

Step 4: install the requirements
```
pip3 install -r requirements.txt
```

Step 6 : set up the .env file  
```
create a duplicate file of .env.example and replace the port numbers with avaiable ones.
```

Step 6 : run the app
```
python3 app.py
```



### Important docs
1. Flask Documentation:  https://flask.palletsprojects.com/en/stable/
2. Live Production Link :  https://avergers-app.dev.shagato.me/ 
