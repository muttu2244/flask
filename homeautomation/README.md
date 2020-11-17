#Device API Services

#Resources

#Get list of Devices
# Request: ("GET /devices")
# Response: '200 OK ' on Success

''' Json
[
    {
        "identifier": "floor-lamp",
        "name": "Floor Lamp",
        "device_type": "switch",
        "controller_gateway": "192.1.68.0.2"
    },
    {
        "identifier": "samsung-tv",
        "name": "Living Room TV",
        "device_type": "tv",
        "controller_gateway": "192.168.0.9"
    }
]
'''

#Adding a new Device
# Request: 'POST /device'
# Response: '201 OK' on Success

''' Json

   {
    "identifier": "floor-lamp",
    "name": "Floor Lamp",
    "device_type": "switch",
    "controller_gateway": "192.1.68.0.2"
}
 
 
 '''

#Getting a specific device details
#Request: 'GET /device/<id>'
#Response: '200 OK' on success, '404 Not Found' if the device doesnt exist

'''Json
{
    "identifier": "floor-lamp",
    "name": "Floor Lamp",
    "device_type": "switch",
    "controller_gateway": "192.1.68.0.2"
}


'''

#Deleting a device
#Request: 'DELETE /device/<id>'
#Response: '204 No Content ' on Success, '404 Not Found' if the device doesnt exist




Run "Docker-compose up "
    If you modify "docker-compose.yml" file , then we have to rebuild it with this cmd
    
Run "docker-compose build" ... rebuilds the docker image again, and then AGAIN run 

Run "docker-compose up" (to run the container)

OR

Run "docker run -it -d -p 5000:80 <ImageName>" (80 is the exposed port in the docker-compose file, so you cannot change it)
Access it using "http://localhost:5000"
    
    Now if you want to run one more container with another port
    
Run "docker run -it -d -p 5001:80 <ImageName>" (80 is the exposed port in the docker-compose file, so you cannot change it)
Access it using "http://localhost:5001"

Note: Creating ENTRYPOINT into docker " ENTRYPOINT [ "python"]"

Note: Run "docker ps" to see all the running containers

Note: Run "docker stop <Container ID" --- to stop the running containers


    


