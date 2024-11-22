# data-mining-weather

### Openweather API Data Collection

### To install

##### Create virtualenv
```bash
pip install virtualenv
virtualenv venv
```
##### Activate venv
```bash
source venv/Scripts/activate
```
##### Build
```bash
pip install -r requirements.txt
```

---

## Running via Docker:

### Build:
```bash
docker build -t weather-app . 
```

### Run:
```bash
docker run -d --name weather-container weather-app
```

### View the logs:
```bash
docker exec weather-container cat /var/log/cron.log
```