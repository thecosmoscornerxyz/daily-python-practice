#!/usr/bin/env python3

import request

response = requests.get("https://httpbin.org/get")

print(response.status_code)
print(response.text)
