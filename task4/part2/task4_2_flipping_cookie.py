import requests
import json


def check_admin(cookie, iv):
    url = "http://aes.cryptohack.org/flipping_cookie/check_admin/" + cookie + "/" + iv;
    r = requests.get(url);
    return (json.loads(r.text));

def get_cookie():
    url = "http://aes.cryptohack.org/flipping_cookie/get_cookie/";
    r = requests.get(url);
    return (json.loads(r.text));


#print(get_cookie());

#                   000000000000000000000000000000001111111111111111111111111111111100000000000000000000000000000000
#print(check_admin("2779375700aaca10aab8e54aefef44b1332f5aaa9fb906c8f57a0adda8678372", "9554db47ed8263270c952bc8043967ad"));

#     IV: "9554db47ed8263270c952bc8043967ad"
#      XOR
#     PT: "61646d696e3d46616c73653b65787069"   | hex("admin=False;expi")
#     RESULT
#         "f430b62e83bf254660e64ef3614117c4"
# 
#     PT: "61646d696e3d547275653b3b65787069"   | hex("admin=True;;expi")
#      XOR
#     RESULT
#         "f430b62e83bf254660e64ef3614117c4"
# NEW IV: "9554db47ed827134158375c8043967ad"
# 
# 

print(check_admin("2779375700aaca10aab8e54aefef44b1332f5aaa9fb906c8f57a0adda8678372", "9554db47ed827134158375c8043967ad"));