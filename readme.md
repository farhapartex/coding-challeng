## Coding Challenge

### Project Setup
* Clone from the repository
* Move to the root folder
* Create virtual environment (You can use `python3 -m venv venv`)
* Active virtual environment
* Install packages from requirements file (`pip install -r requirements.txt`)
* Run the project by (`python run.py`)

The development server will be run

Open your postman and do followings

* Use this API endpoint for both GET & POST request: `http://127.0.0.1:8080/api/v1/post-data/`

### GET request response:
`
{
    "status": true
}
`

### POST request body:
```
{
    "is_malicious": false,
    "name": "Nazmul Hasan",
    "position": "Python Developer"
}
```
### POST request response:
if is_malicious is true
```
{
    "error": "Data unauthorized"
}
```
status code: 401

if is_malicious is false
```
{
    "is_malicious": false,
    "name": "Nazmul Hasan",
    "position": "Python Developer"
}
```
status code: 200

### Log file
When server will be run, logger file named as `errors.log` will be created and all information will be logged

Te have a look on log data, open errors.log file
