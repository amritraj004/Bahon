## Bahon
A dead simple URL redirector using Flask

### Steps
```shell
https://github.com/lap00zza/Bahon.git
cd Bahon
docker-compose build
docker-compose up
```
Note: Depending on how your docker/docker compose is set up, you might need to use **sudo**.

### Prerequisites
1. **Docker**
2. **Docker Compose**

### What is it actually doing?
1. The main app is a simple flask app (**/web**).
2. This app is being served with gunicorn. Gunicorn is running on port 8000.
3. The webserver we are using is nginx (**/nginx**) which proxies incoming requests to our gunicorn.

If you want to work on the repo, then you will need python3 installed. I used `python 3.6.1`.
