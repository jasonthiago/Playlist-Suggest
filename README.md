# Playlist Suggest

This simple API suggest a playlist in Deezer based on the actual real temperaturte in your city. 


|Temperature     |Playlist                          |
|----------------|-------------------------------|
|Temperature > 25ºC|`Pop`            |'Isn't this fun?'            |
|Temperature < 25ºC and >10ºC           |`Rock`            |"Isn't this fun?"            |
|Temperature < 10ºC         |`Classic`|-- is en-dash, --- is em-dash|

## Running Locally - Linux Debian

### Cloning the repository
~~~terminal
 git glone
~~~

### Adding Dependencies
~~~terminal
 sudo apt-install python
 pip install Flesk
~~~

### Setting-up OpenWeather

This API uses OpenWeather,you will need to creat an account on openweather.com and put your key in the config.

### Finally Run
~~~terminal
 python app.py
~~~
    



## Running on heroku

