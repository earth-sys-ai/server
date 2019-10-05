# server
Flask webserver to serve data from database to frontend in json format.

---
## Usage

To start the the server run the script with the only arguement being the cache directory as created by [datacacher](https://github.com/earth-sys-ai/datacacher).

Ex:
`> python3 server.py cacheDir`

---
## Setup

To setup install the necessary requirements through pip.
```
flask
flask_cors
```
---
## API
To interact with the server, url parameters are used. The `com` parameter tells the server which action you wish to execute. Available commands are listed below.

<br>

**listLevels**   
This command returns a list of cached levels.   
No additional parameters are needed.

```c
levelCount: int     // number of levels cached
levels: array       // array of level numbers cached
```
<br>


**transect**  
This command is used to get the values within givin polygons.
A `line` parameter is needed to specify the coordinates of the line to transect.
Each coordinate is contained as such `(lat, lng)`, and are to be concatenated together.

```c
count: int          // amount of values returned
values: array       // array of values for each coordinate
```

<br>

**getData**   
This command returns the cached data with a given amount of levels.   
A `level` parameter is needed to specify which level cache to return.
The response is the same as that from the output of the [datacacher](https://github.com/earth-sys-ai/datacacher#api).

<br>
If an error occurs, the server will respond with the following format:

```c
error: string       // string explaining the error
```


