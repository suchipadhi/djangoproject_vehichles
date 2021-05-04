# Getting Started with Python app for collecting the location and then computing the navigation bearing (direction of vehicle expressed in angles).

Creating an application to collect the live position of all vehicles in its fleet and track its location.

## Prerequisites

You'll need the following:
* [Python (3.7.3)]
* [SQLite]
* [Django REST framework 3.2]
* [Docker]


## 1. Clone the sample app
You can clone the project from [Git repo].
   ```
https://github.com/suchipadhi/djangoproject_vehichles
  ```

## 2. Run the app locally

First, you have to install the dependencies listed in the [requirements.txt]to run it locally.

I prefer using a virtual environment [virtual environment] to avoid my dependencies clash with those of my other Python projects.
  ```
pip install -r requirements.txt
  ```

## 3. Run the contenarized app.
Run the app.
  ```
docker compose up
docker compose run
  ```

## 4. List of routes mentioned in the app

Below i have mentioned the list of routes used in the app:
* [http://127.0.0.1:8000/admin/]   (To check the admin view.)
* [http://127.0.0.1:8000/vehicles/]   (To register the vehicle.)
* [http://127.0.0.1:8000/vehicles/<uuid:pk>/locations/]   (To update the location.)
* [http://127.0.0.1:8000/vehicles/<uuid:pk>/]   (To de-register the vehicle.)

1. To register the vehicle:
INPUT JSON:
```
{ "id": "f8abc25c-33fa-40c2-9bc4-8867c2ba0c3d" }
  ``` 

RESPONSE JSON:
  ```
{
    "vehicle_id": "f8abc25c-33fa-40c2-9bc4-8867c2ba0c3d"
}
  ```
2. To update the vehicle's location:
INPUT JSON:
```
{
    "latitude": 10.0,
    "longitude": 20.0
}
  ``` 

RESPONSE JSON:
  ```
{}
  ```
3. TO delete the vehicle
