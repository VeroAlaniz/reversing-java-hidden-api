import base64

url_ofuscada = "aHR0cDovL2FwaS1jYWxjdWxhZG9yYS5zb2Z0d2FyZXNlZ3Vyby5jb20uYXIvdmVyaWZpY2FyLWNvZGlnby1jYWxjdWxhZG9yYS8/dD0="
url = base64.b64decode(url_ofuscada).decode()
print(url)