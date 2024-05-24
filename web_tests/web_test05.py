# 應用 Session 來模擬 API 測試流程
import requests
import json

# 建立一個 Session
session = requests.session()

# Login
url = "https://restful-booker.herokuapp.com/auth"
body = {
    "username": "admin",
    "password": "password123"
}

response = session.request("post", url, json=body)
print(f"Create Token Response: {response.json()}")

# 把取得的 token 存入 headers 的 cookie
session.headers["Cookie"] = f"token={response.json()['token']}"
print(f"Cookie: {session.headers['Cookie']}")

# 預訂房間
create_booking_api = "https://restful-booker.herokuapp.com/booking"
create_booking_body = {
    "firstname": "Jim",
    "lastname": "Brown",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2018-01-01",
        "checkout": "2019-01-01"
    },
    "additionalneeds": "Breakfast"
}

response = session.request("post", create_booking_api, json=create_booking_body)
print(f"Create Booking Response: {json.dumps(response.json(), indent=4)}")

# 取得 Booking ID
booking_id = response.json()["bookingid"]

# 更改預訂內容
update_booking_api = f"https://restful-booker.herokuapp.com/booking/{booking_id}"
update_body = {
    "firstname": "James"
}
# 繼續運用同一個 session 會帶之前存的 token
response = session.request("patch", update_booking_api, json=update_body)
print(f"Partial Update Booking Response: {json.dumps(response.json(), indent=4)}")

# 刪除預訂
delete_booking_api = f"https://restful-booker.herokuapp.com/booking/{booking_id}"
response = session.request("delete", delete_booking_api)
print(f"Delete Booking Response status code: {response.status_code}")