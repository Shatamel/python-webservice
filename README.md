##General information
It's a simple [Bottle](https://bottlepy.org/) based web service with the main purpose of checking URLs from an imaginary proxy.
The web service returns policy value from DB for the requested URL or HTTP 204 (No Content) if such URL is not in the DB.
This value can be changed to anything else if needed. 
##Requirements 
This service is running on python 3.9.5 and MongoDB 5.0. 
Also, it uses bottle 0.12.19 for web service and pymongo 4.0.1 to access the database.

## Setting up your environment
Assuming you have MacOS please do the following to install python3 and MongoDB on your laptop
* Install python3 and required libraries with the following commands:
```
brew install python3
pip3 install -r /path/to/project/requirements.txt
```  
* Install and launch MongoDB with the following commands:
```
brew tap mongodb/brew
brew install mongodb-community@5.0
brew services start mongodb-community@5.0
```
* Then update your MongoDB using command `python3 /path/to/project/db/mongodb.py` with  a sample data

##Usage
When all requirements are installed and MongoDB is running you can launch the script as a service using systemctl/systemd or manually with `python3 /path/to/project/main.py` command.

##Testing 
There are two ways to test the web service - manually and with UTs. 
 * You can run unit tests using command ```python3 unittests.py```
 These tests check both successful and "No Content" cases.
 * Or manually query web service with `curl localhost:8080/urlinfo/1/google.com/search?query` where **google.com/search?query** is the URL we are going to check.
