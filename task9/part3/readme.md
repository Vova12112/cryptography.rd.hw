# Завдання 9.3

Відповідно до умови, згенеруємо самопідписаний сертифікат:

```
   openssl x509 -req -sha256 -in ../part2/task-9-2.csr -signkey ../part2/task-9-2.key -out task-9-3.crt
```


Перевіримо вміст сертифікату:

```
   openssl x509 -text -noout -in task-9-3.crt
```

Результат:

```
   Certificate:
    Data:
        Version: 1 (0x0)
        Serial Number:
            12:6f:b1:8f:af:5f:68:13:cf:35:c8:f7:8d:cf:99:1b:21:d3:d3:42
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: C = UA, L = Kyiv, O = Robot_dreams, CN = www.robotdreams.cc, emailAddress = vladimiranikin01@gmail.com
        Validity
            Not Before: Oct 20 18:57:57 2025 GMT
            Not After : Nov 19 18:57:57 2025 GMT
        Subject: C = UA, L = Kyiv, O = Robot_dreams, CN = www.robotdreams.cc, emailAddress = vladimiranikin01@gmail.com
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (2048 bit)
                Modulus:
                    00:9f:8d:ad:d3:cc:9d:e7:20:ea:aa:d4:f4:ab:76:
                    6c:49:4b:44:ca:04:e0:67:b7:fa:c9:fb:e5:c3:77:
                    65:26:f9:dc:a1:05:97:99:84:4c:c4:42:ed:50:11:
                    29:44:8d:84:c1:09:62:fd:ef:d1:f6:5f:e6:b3:21:
                    92:bf:de:31:a7:67:5d:3b:5d:57:5f:7f:ec:22:89:
                    a3:83:81:c5:73:25:9c:69:c4:12:cd:0d:ba:65:bb:
                    d6:1b:8e:cf:80:3b:51:46:36:fd:4f:7c:95:a7:93:
                    22:f6:8d:c0:33:2a:43:6f:7f:4e:3f:0d:50:fd:3b:
                    5b:2b:d4:df:6b:21:d8:d9:6e:3c:cd:b6:10:15:f2:
                    da:e2:d9:e1:06:8c:a9:4e:38:db:4b:58:5c:2f:14:
                    19:43:bc:a6:82:6f:fa:29:e8:5e:58:06:d9:10:a1:
                    51:a3:6f:ec:7b:34:a8:36:62:4f:0e:1b:bd:03:e4:
                    7c:20:9b:de:4a:4c:4d:c9:b6:a4:52:5a:4d:15:68:
                    fa:f8:68:ca:20:1a:ca:f5:fe:5a:c7:16:e2:86:ba:
                    a7:42:94:6b:e4:a8:c5:d8:87:a7:a0:44:c7:97:eb:
                    57:a1:4b:2e:58:9a:68:b8:b4:4f:bb:ff:ac:d5:90:
                    17:f4:53:f0:c2:78:f5:04:33:2f:e8:ad:09:6b:bb:
                    6e:bb
                Exponent: 65537 (0x10001)
    Signature Algorithm: sha256WithRSAEncryption
    Signature Value:
        33:0e:c4:71:56:8a:94:25:64:2b:70:32:75:74:26:c9:44:1b:
        6d:0d:95:b0:17:96:7c:2e:c5:21:57:11:6c:5e:b0:32:96:6b:
        87:59:d4:3c:48:97:d7:c7:fd:e2:1b:5e:91:8c:fe:f3:b6:2d:
        60:5c:9d:3e:fe:b0:cd:5e:f6:b9:74:ff:7d:b2:d0:29:cb:13:
        be:53:1c:70:a2:3b:0f:92:bf:88:00:82:78:1b:07:a0:12:bc:
        0a:23:63:05:eb:9b:9d:e6:74:65:f8:77:b3:70:e1:c5:3a:eb:
        85:01:4d:9d:9b:3e:46:b8:33:8a:a6:b8:05:55:4b:18:86:16:
        7d:5a:20:44:e8:f4:c5:55:3d:63:f7:36:4d:9b:c6:22:6d:41:
        d3:7e:90:15:7f:57:15:26:b9:d5:bf:b9:1e:f4:a8:3e:26:5b:
        b9:a0:d0:ab:c5:b3:cb:ec:f3:07:60:0e:53:ab:82:45:ad:70:
        81:89:8b:96:65:a5:98:49:95:f4:16:c8:26:fb:1a:97:38:f2:
        39:cf:26:22:da:71:bd:7a:25:40:85:fb:32:e7:f3:f0:c1:9f:
        01:77:88:a1:66:44:76:3e:f3:88:07:fa:d3:96:3c:a9:12:76:
        b2:b3:9a:fe:90:70:25:12:03:fc:38:17:39:6f:5b:b3:93:19:
        72:72:9e:87
```