# Getting Started with Python app for collecting the location and then computing the navigation bearing (direction of vehicle expressed in angles).

To get started, we'll build a Python-D app which helps to format the input JSON-formatted opening hours of a restaurant
as an input payload and outputs hours in more human-readable format with response as Output JSON.

## Prerequisites

You'll need the following:
* [Python (3.7.3)]
* [SQLite]
* [Django REST framework 3.2]
* [WebSockets (via Django Channels)]


## 1. Clone the sample app
You can clone the project from [Git repo].
   ```

  ```

## 2. Run the app locally

First, you have to install the dependencies listed in the [requirements.txt]to run it locally.

I prefer using a virtual environment [virtual environment] to avoid my dependencies clash with those of my other Python projects.
  ```
pip install -r requirements.txt
  ```
Run the app.
  ```

  ```
View your app at:
  ``` 

  ```
## 3. Run the contenarized app.


## 4. List of routes mentioned in the app

Below i have mentioned the list of routes used in the app:
* [http://127.0.0.1:8000/admin/]   (To check the admin view.)
* [http://127.0.0.1:8000/vehicles/]   (To register the vehicle.)
* [http://127.0.0.1:8000/vehicles/<uuid:pk>/locations/]   (To update the location.)
* [http://127.0.0.1:8000/vehicles/<uuid:pk>/]   (To de register the vehicle.)


INPUT JSON:
```

  ``` 

RESPONSE JSON:
  ```

  ```

