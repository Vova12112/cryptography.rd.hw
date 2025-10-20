# Завдання 9.1

Відповідно до умови, згенеруємо новий RSA ключ, за допомогою команди:

```
   openssl genpkey -algorithm RSA -out task-9-1-rsa.key -pkeyopt rsa_keygen_bits:2048
```

Перевіримо згенерований результат:

```
   openssl rsa -text -in task-9-1-rsa.key
```

Отриманий результат:

```
   Private-Key: (2048 bit, 2 primes)
modulus:
    00:c1:5a:b2:7d:f2:3d:cd:78:aa:76:9d:bc:57:da:
    b9:bf:28:09:bb:52:75:1a:11:07:5e:e7:00:d2:88:
    59:b0:9c:dc:d3:74:a4:e8:1a:d0:6f:a2:eb:7f:15:
    f0:5a:c9:3a:e0:fe:c8:b0:5c:e1:c9:65:8b:00:16:
    e3:44:2b:60:d0:2e:d1:57:45:08:37:48:fc:52:6f:
    02:fb:b6:63:2f:2e:4e:10:e6:aa:b8:7e:7f:98:52:
    c3:3c:c3:04:15:45:8e:c5:59:b6:98:af:2d:ed:34:
    2c:d1:67:ff:81:9a:e0:b5:d9:67:3a:7a:94:cc:43:
    05:c2:43:ee:3e:fa:fe:c9:51:7e:a6:93:d3:ee:e2:
    bd:d2:ed:33:0d:88:a0:8b:d5:c0:74:3b:13:05:87:
    0a:06:66:d8:5e:dc:7f:27:99:13:51:8f:6c:b1:93:
    dc:8b:da:b2:e4:26:cb:10:46:c2:c3:2b:47:84:ae:
    7c:81:22:f5:14:9b:b3:83:3a:dc:ea:b2:a5:39:c7:
    a1:ae:c5:aa:24:ed:12:fc:9c:10:03:01:e8:e3:0e:
    57:e9:41:63:b0:48:24:6f:a5:ec:e4:ba:6c:91:e8:
    6c:72:12:68:7d:f4:49:26:f8:58:4c:08:c9:5d:61:
    53:a5:db:fe:d7:4a:5c:1c:0a:8d:36:45:c1:22:ba:
    1b:67
publicExponent: 65537 (0x10001)
privateExponent:
    2c:44:94:1e:12:c2:84:92:ee:50:26:ef:f2:9b:50:
    b0:8b:bd:a2:a6:0f:ca:6e:80:a6:01:34:66:7f:32:
    2d:a5:d4:47:13:6b:17:fa:df:a2:d7:85:9c:3c:8d:
    21:73:f5:e7:82:5d:b7:47:24:a8:83:f7:8d:87:2f:
    f4:31:0c:42:cd:9d:3f:22:3e:6d:cd:e7:7b:06:10:
    84:49:af:2e:a3:a6:da:e6:bc:ca:6d:a7:cf:db:8e:
    f8:8f:db:94:f5:2e:69:4f:8f:67:28:a0:56:b0:fd:
    db:d9:b8:1d:57:b4:bf:dd:ac:ed:2e:18:78:25:96:
    21:72:85:0e:e5:4f:45:0e:dd:85:00:ed:03:cb:de:
    c8:69:61:18:06:3f:bc:5f:49:96:19:f4:56:a5:5d:
    8e:6d:fd:25:99:4c:e3:95:72:b4:ce:0a:28:85:01:
    1d:00:8f:35:a2:16:52:11:19:d4:4f:92:66:4b:6a:
    36:f5:c0:77:22:b5:14:e2:94:94:7b:fc:02:c3:74:
    45:92:14:f8:2f:9e:e2:f1:68:8b:5a:15:20:dc:29:
    f1:63:01:81:78:d4:a4:c5:b9:ca:b8:2f:15:5d:f7:
    74:c6:e9:a3:ba:4c:a6:64:a6:e5:7a:60:53:dd:ec:
    3c:3b:05:3f:c6:77:f2:bf:c6:d1:5d:99:ca:0a:af:
    8d
prime1:
    00:c8:51:70:cd:55:63:c0:9d:09:58:fa:29:74:be:
    4c:d6:47:1b:9a:e6:b3:28:24:91:16:f6:b7:cd:0d:
    58:cf:04:08:a5:98:26:da:ce:1d:2c:15:d8:a0:88:
    e2:3a:e7:bb:0f:2c:9c:64:64:72:ae:33:fc:e9:69:
    f1:34:0a:a3:2d:54:3c:6c:26:5a:51:2a:36:86:a7:
    46:4c:d0:c3:4b:59:e6:17:e5:a6:ab:9b:58:b8:46:
    2e:9a:d5:9b:75:dd:f3:23:81:4c:99:fb:ea:9b:c1:
    a8:e2:ee:cd:26:5a:25:dc:14:85:5f:ed:9e:4b:6c:
    0b:79:c6:0f:90:69:21:da:e3
prime2:
    00:f7:19:b6:5e:76:78:7c:bf:d2:45:14:2d:24:67:
    95:48:fb:0b:ed:1e:47:39:37:17:3c:85:7d:77:97:
    89:69:ca:90:fd:5c:d0:ef:1c:1f:33:49:4c:06:93:
    db:85:0b:24:e5:f6:f1:44:82:23:1a:34:24:62:dd:
    c6:37:d5:35:4b:3b:db:d7:65:37:1f:1a:1d:02:93:
    ca:d4:9c:96:49:56:87:d7:3a:ce:d1:7e:ce:10:b1:
    79:75:ee:91:63:eb:ed:7d:a5:e4:4c:0d:8f:45:76:
    48:0e:ad:52:e0:be:e5:82:5d:75:57:25:98:db:cd:
    2f:53:29:29:06:53:19:10:ad
exponent1:
    00:a0:2f:77:eb:ca:e7:bc:e4:16:d0:7f:23:5d:86:
    bb:bc:f2:19:e2:11:af:9c:5f:39:62:ca:a2:0a:28:
    2d:27:46:0b:80:18:1e:a2:04:06:91:f5:5a:48:6d:
    8d:b3:1b:11:9b:bd:c9:c6:02:09:2e:c2:c5:f1:05:
    55:eb:8e:c2:14:02:73:5a:ec:84:76:b9:31:e7:15:
    a6:82:d0:c2:0a:e4:75:ba:10:5b:ea:88:8c:36:b7:
    70:97:42:4f:51:be:cd:aa:4b:c0:2c:b6:a5:52:2e:
    57:d6:38:ad:f6:88:4a:14:26:98:cd:30:1f:d0:22:
    33:3f:0a:a1:f1:92:10:8f:8f
exponent2:
    4d:f2:05:6d:fc:ce:fb:03:03:50:19:12:38:56:98:
    67:c2:11:3c:05:fe:0f:95:4a:36:24:21:b4:d4:cf:
    5a:d8:b4:2d:c7:d6:7c:66:91:8c:fb:05:09:5a:20:
    b7:f2:10:fc:9d:8d:f3:bf:5d:55:49:b7:64:9c:72:
    87:70:30:f4:7f:78:54:94:af:f3:96:a8:2a:04:f6:
    c9:64:6f:9f:c8:b4:e6:f6:bd:00:a6:90:58:01:b3:
    bf:b8:b6:92:1f:7c:f5:d2:9b:96:45:fc:b8:bb:9b:
    f5:4d:45:44:71:d3:31:f1:4b:2f:67:43:b5:aa:1e:
    d0:8b:be:4e:29:6e:51:ad
coefficient:
    00:97:c2:05:b9:05:48:63:9b:c6:56:7a:ef:e3:42:
    92:3f:e7:7f:88:5f:54:15:b3:4e:6a:86:37:e6:5b:
    e5:f3:55:12:35:40:b7:2d:dc:01:73:4c:cf:2c:28:
    0d:e5:41:db:61:bf:7f:f2:10:31:c5:f3:f5:6f:e8:
    47:35:83:0a:a6:cf:ef:63:ca:b1:39:83:99:4f:87:
    01:04:7f:19:e0:4e:76:68:6a:50:90:93:fb:5e:08:
    f5:49:8b:53:9d:73:db:f5:51:dc:90:ec:eb:fd:54:
    37:94:0c:7c:2f:07:67:73:61:39:ad:58:78:e4:98:
    94:fb:00:9a:09:f8:11:95:c5
writing RSA key
-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDBWrJ98j3NeKp2
nbxX2rm/KAm7UnUaEQde5wDSiFmwnNzTdKToGtBvout/FfBayTrg/siwXOHJZYsA
FuNEK2DQLtFXRQg3SPxSbwL7tmMvLk4Q5qq4fn+YUsM8wwQVRY7FWbaYry3tNCzR
Z/+BmuC12Wc6epTMQwXCQ+4++v7JUX6mk9Pu4r3S7TMNiKCL1cB0OxMFhwoGZthe
3H8nmRNRj2yxk9yL2rLkJssQRsLDK0eErnyBIvUUm7ODOtzqsqU5x6Guxaok7RL8
nBADAejjDlfpQWOwSCRvpezkumyR6GxyEmh99Ekm+FhMCMldYVOl2/7XSlwcCo02
RcEiuhtnAgMBAAECggEALESUHhLChJLuUCbv8ptQsIu9oqYPym6ApgE0Zn8yLaXU
RxNrF/rfoteFnDyNIXP154Jdt0ckqIP3jYcv9DEMQs2dPyI+bc3newYQhEmvLqOm
2ua8ym2nz9uO+I/blPUuaU+PZyigVrD929m4HVe0v92s7S4YeCWWIXKFDuVPRQ7d
hQDtA8veyGlhGAY/vF9Jlhn0VqVdjm39JZlM45VytM4KKIUBHQCPNaIWUhEZ1E+S
ZktqNvXAdyK1FOKUlHv8AsN0RZIU+C+e4vFoi1oVINwp8WMBgXjUpMW5yrgvFV33
dMbpo7pMpmSm5XpgU93sPDsFP8Z38r/G0V2ZygqvjQKBgQDIUXDNVWPAnQlY+il0
vkzWRxua5rMoJJEW9rfNDVjPBAilmCbazh0sFdigiOI657sPLJxkZHKuM/zpafE0
CqMtVDxsJlpRKjaGp0ZM0MNLWeYX5aarm1i4Ri6a1Zt13fMjgUyZ++qbwaji7s0m
WiXcFIVf7Z5LbAt5xg+QaSHa4wKBgQD3GbZednh8v9JFFC0kZ5VI+wvtHkc5Nxc8
hX13l4lpypD9XNDvHB8zSUwGk9uFCyTl9vFEgiMaNCRi3cY31TVLO9vXZTcfGh0C
k8rUnJZJVofXOs7Rfs4QsXl17pFj6+19peRMDY9FdkgOrVLgvuWCXXVXJZjbzS9T
KSkGUxkQrQKBgQCgL3fryue85BbQfyNdhru88hniEa+cXzliyqIKKC0nRguAGB6i
BAaR9VpIbY2zGxGbvcnGAgkuwsXxBVXrjsIUAnNa7IR2uTHnFaaC0MIK5HW6EFvq
iIw2t3CXQk9Rvs2qS8AstqVSLlfWOK32iEoUJpjNMB/QIjM/CqHxkhCPjwKBgE3y
BW38zvsDA1AZEjhWmGfCETwF/g+VSjYkIbTUz1rYtC3H1nxmkYz7BQlaILfyEPyd
jfO/XVVJt2SccodwMPR/eFSUr/OWqCoE9slkb5/ItOb2vQCmkFgBs7+4tpIffPXS
m5ZF/Li7m/VNRURx0zHxSy9nQ7WqHtCLvk4pblGtAoGBAJfCBbkFSGObxlZ67+NC
kj/nf4hfVBWzTmqGN+Zb5fNVEjVAty3cAXNMzywoDeVB22G/f/IQMcXz9W/oRzWD
CqbP72PKsTmDmU+HAQR/GeBOdmhqUJCT+14I9UmLU51z2/VR3JDs6/1UN5QMfC8H
Z3NhOa1YeOSYlPsAmgn4EZXF
-----END PRIVATE KEY-----
```
