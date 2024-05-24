import json
import requests

url = "https://automationintesting.online/message/"

request_body = {
    "description": "012345678901234567890",
    "email": "abc@abc.com",
    "name": "Tester",
    "phone": "09123456789",
    "subject": "Booking"
}

headers = {
    "Content-Type": "application/json"
}

# 以 post method 發出 request
# 由於 Content-Type 為 application/json，會使用 json 參數傳入 request body
response = requests.request("post", url, json=request_body, headers=headers)

# 可列印 Requests 的 headers
print("Requests:", response.request.headers)

# 由於知道 response 的 Content-Type 是 application/json
# 可用 json() 讀取 Response 內容
# 應用 json 套件作排版顯示，不然資料量大的時候，閱讀會比較困難
# 使用 indent 參數設定縮排為 4 個空格
print("Response:", json.dumps(response.json(), indent=4))

# 可列印 Response 的 Status Code, 若成功會顯示 201
print("Status Code:", response.status_code)
