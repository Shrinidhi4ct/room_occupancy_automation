from sensordata.models import SensorData
from occupancy.models import Rooms

def get_room_status_data():
    """
        Room status data
    """

    room_data = Rooms.objects.all()
    total_rooms = room_data.count()
    # get latest sensor data for each room
    data = []
    occupied, available = 0, 0
    if room_data:
        for room in room_data:
            sensor_data = SensorData.objects.filter(room_id=room.room_identifier).order_by('-created_at')
            if sensor_data:
                if sensor_data[0].data['status'] == "true" or sensor_data[0].data['status'] == True:
                    occupied += 1
                else:
                    available += 1
                data.append(
                    {
                        "room": room.room_identifier,
                        "room_name": room.name,
                        "status": sensor_data[0].data['status'],
                        "room_coords" : str(room.room_coords),
                        "created_at": sensor_data[0].created_at,
                    }
                )

        response = {
            "data" : data,
            "room_data" : room_data,
            "floor" : room_data[0].floor_id.image,
            "occupied": occupied,
            "available": available,
            "total_rooms": total_rooms,
        }

        return response
    else:
        response = {
            "data" : data,
            "floor" : None
        }

        return response