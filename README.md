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
 pip install Flask
~~~


### Run
~~~terminal
 python app.py
~~~
    
Open the url localhost:5000/<city>

Replace <city> with the name of your city


