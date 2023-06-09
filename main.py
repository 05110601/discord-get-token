import requests

mail = "example@example.com"
password = "PassWord"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "X-Debug-Options":"bugReporterEnabled",
            "X-Discord-Locale":"ja",
            "X-Discord-Timezone":"Asia/Tokyo",
            "Content-Type":"application/json"
            }

payload = {"login": mail, "password": password, "undelete": "false"}

data = requests.post("https://discord.com/api/v9/auth/login",headers=headers,json=payload)

print(data.status_code)
print(data.text)
print(data.encoding)
