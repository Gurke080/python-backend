from pydantic import BaseModel, Field

from flask_openapi3 import Info, Tag
from flask_openapi3 import OpenAPI
from database import create_connection, close_connection

info = Info(title="book API", version="1.0.0")
app = OpenAPI(__name__, info=info)

room_tag = Tag(name="room", description="Room")
device_tag = Tag(name="devices", description="Devices")
connection = create_connection()


class RoomRoute(BaseModel):
    rid: int = Field(..., title="Room ID", description="Room ID")

class Devices(BaseModel):
    Dvalue:int = Field(...,title="Devices Value", description="Devices Value")

class RoomControlDeviceRoute(BaseModel):
    rid: int = Field(..., title="Room ID", description="Room ID")
    did: int = Field(..., title="Device ID", description="Device ID")
    
@app.get("/room/<int:rid>", summary="get data from room", tags=[room_tag])
def get_room(path: RoomRoute):
    """
    to get rooms
    """
    return {
        "code": 0,
        "message": "ok",
        "data": {
            "id": str(path.rid)
        }
    }

@app.get("/room", summary="get all data from all rooms", tags=[room_tag])
def get_all_room():
    """
    to get rooms
    """
    command = "SELECT * FROM Room LEFT JOIN SensorData USING (RoomID)"
    data = connection.cmd_query(command)
    return {
        "code": 0,
        "message": "ok",
        "data": data
    }

@app.post("/room/<int:rid>/device/<int:did>", summary="get device  from room", tags=[device_tag])
def controll_device(path: RoomControlDeviceRoute, body: Devices):
    """
    to get rooms
    """
    return {
        "value": 0,
        "": "ok",
        "data": {
            "id": str(path.rid)
        }
    }



                         
if __name__ == "__main__":
    app.run(debug=True)