import os

SERVICE_KEY = os.environ.get("BUS_SERVICE_KEY")
BUS_API_URL = f"http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRouteAll?serviceKey={SERVICE_KEY}"
