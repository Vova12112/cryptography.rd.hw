# Завдання 9.4

Відповідно до умови, перевіримо сертифікат robotdreams.cc:

```
   openssl s_client -showcerts -connect robotdreams.cc:443
```


Результат:

```
   CONNECTED(00000003)
depth=2 C = US, O = Google Trust Services LLC, CN = GTS Root R4
verify return:1
depth=1 C = US, O = Google Trust Services, CN = WE1
verify return:1
depth=0 CN = robotdreams.cc
verify return:1
---
Certificate chain
 0 s:CN = robotdreams.cc
   i:C = US, O = Google Trust Services, CN = WE1
   a:PKEY: id-ecPublicKey, 256 (bit); sigalg: ecdsa-with-SHA256
   v:NotBefore: Sep 27 12:12:48 2025 GMT; NotAfter: Dec 26 13:11:21 2025 GMT
-----BEGIN CERTIFICATE-----
MIIDrTCCA1SgAwIBAgIQT9cvWNympSoN5OB51GO4LjAKBggqhkjOPQQDAjA7MQsw
CQYDVQQGEwJVUzEeMBwGA1UEChMVR29vZ2xlIFRydXN0IFNlcnZpY2VzMQwwCgYD
VQQDEwNXRTEwHhcNMjUwOTI3MTIxMjQ4WhcNMjUxMjI2MTMxMTIxWjAZMRcwFQYD
VQQDEw5yb2JvdGRyZWFtcy5jYzBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABHR9
jfNUbZXjhD/8fq74NPNUXA0O0NiaSWwghg9fKQXfnGXId71NTn/3RdfKK/r52Gzd
IDb5Gmzt+LeleKPOdKmjggJaMIICVjAOBgNVHQ8BAf8EBAMCB4AwEwYDVR0lBAww
CgYIKwYBBQUHAwEwDAYDVR0TAQH/BAIwADAdBgNVHQ4EFgQUL1nQ6bXftjI+/1d8
SRoRF0Qko4YwHwYDVR0jBBgwFoAUkHeSNWfE/6jMqeZ72YB5e8yT+TgwXgYIKwYB
BQUHAQEEUjBQMCcGCCsGAQUFBzABhhtodHRwOi8vby5wa2kuZ29vZy9zL3dlMS9U
OWMwJQYIKwYBBQUHMAKGGWh0dHA6Ly9pLnBraS5nb29nL3dlMS5jcnQwKwYDVR0R
BCQwIoIOcm9ib3RkcmVhbXMuY2OCECoucm9ib3RkcmVhbXMuY2MwEwYDVR0gBAww
CjAIBgZngQwBAgEwNgYDVR0fBC8wLTAroCmgJ4YlaHR0cDovL2MucGtpLmdvb2cv
d2UxLzF5SkZjY0IxMWQwLmNybDCCAQUGCisGAQQB1nkCBAIEgfYEgfMA8QB2ABLx
TjS9U3JMhAYZw48/ehP457Vih4icbTAFhOvlhiY6AAABmYtN/y0AAAQDAEcwRQIh
ALdKnjF9zyoeuEQFFG5OLYprrh78VIOoLQ754tEg952CAiB41HHVdmoeqeh9Rnvu
TSwccvS/M43OoFaLcZqpB+BMeQB3ABmG1Mcoqm/+ugNveCpNAZGqzi1yMQ+uzl1w
QS0lTMfUAAABmYtOAywAAAQDAEgwRgIhAJkuE5r/LK3R0KlCxNRdAcy5onB6UT7X
eWt96+cYmELtAiEAw9KbSmbk2Oi320vs3vyThLxDTNEaSfBiDT1TYgd/+tswCgYI
KoZIzj0EAwIDRwAwRAIgIxg0d1QinBOPWXNtY/VVgyifMbjVr2+KdZUQ2aMEbJ8C
IBgsQjmngJYH5O8MHP0JXag1zdMUoqpg2ClF4fkepCqu
-----END CERTIFICATE-----
 1 s:C = US, O = Google Trust Services, CN = WE1
   i:C = US, O = Google Trust Services LLC, CN = GTS Root R4
   a:PKEY: id-ecPublicKey, 256 (bit); sigalg: ecdsa-with-SHA384
   v:NotBefore: Dec 13 09:00:00 2023 GMT; NotAfter: Feb 20 14:00:00 2029 GMT
-----BEGIN CERTIFICATE-----
MIICnzCCAiWgAwIBAgIQf/MZd5csIkp2FV0TttaF4zAKBggqhkjOPQQDAzBHMQsw
CQYDVQQGEwJVUzEiMCAGA1UEChMZR29vZ2xlIFRydXN0IFNlcnZpY2VzIExMQzEU
MBIGA1UEAxMLR1RTIFJvb3QgUjQwHhcNMjMxMjEzMDkwMDAwWhcNMjkwMjIwMTQw
MDAwWjA7MQswCQYDVQQGEwJVUzEeMBwGA1UEChMVR29vZ2xlIFRydXN0IFNlcnZp
Y2VzMQwwCgYDVQQDEwNXRTEwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAARvzTr+
Z1dHTCEDhUDCR127WEcPQMFcF4XGGTfn1XzthkubgdnXGhOlCgP4mMTG6J7/EFmP
LCaY9eYmJbsPAvpWo4H+MIH7MA4GA1UdDwEB/wQEAwIBhjAdBgNVHSUEFjAUBggr
BgEFBQcDAQYIKwYBBQUHAwIwEgYDVR0TAQH/BAgwBgEB/wIBADAdBgNVHQ4EFgQU
kHeSNWfE/6jMqeZ72YB5e8yT+TgwHwYDVR0jBBgwFoAUgEzW63T/STaj1dj8tT7F
avCUHYwwNAYIKwYBBQUHAQEEKDAmMCQGCCsGAQUFBzAChhhodHRwOi8vaS5wa2ku
Z29vZy9yNC5jcnQwKwYDVR0fBCQwIjAgoB6gHIYaaHR0cDovL2MucGtpLmdvb2cv
ci9yNC5jcmwwEwYDVR0gBAwwCjAIBgZngQwBAgEwCgYIKoZIzj0EAwMDaAAwZQIx
AOcCq1HW90OVznX+0RGU1cxAQXomvtgM8zItPZCuFQ8jSBJSjz5keROv9aYsAm5V
sQIwJonMaAFi54mrfhfoFNZEfuNMSQ6/bIBiNLiyoX46FohQvKeIoJ99cx7sUkFN
7uJW
-----END CERTIFICATE-----
 2 s:C = US, O = Google Trust Services LLC, CN = GTS Root R4
   i:C = BE, O = GlobalSign nv-sa, OU = Root CA, CN = GlobalSign Root CA
   a:PKEY: id-ecPublicKey, 384 (bit); sigalg: RSA-SHA256
   v:NotBefore: Nov 15 03:43:21 2023 GMT; NotAfter: Jan 28 00:00:42 2028 GMT
-----BEGIN CERTIFICATE-----
MIIDejCCAmKgAwIBAgIQf+UwvzMTQ77dghYQST2KGzANBgkqhkiG9w0BAQsFADBX
MQswCQYDVQQGEwJCRTEZMBcGA1UEChMQR2xvYmFsU2lnbiBudi1zYTEQMA4GA1UE
CxMHUm9vdCBDQTEbMBkGA1UEAxMSR2xvYmFsU2lnbiBSb290IENBMB4XDTIzMTEx
NTAzNDMyMVoXDTI4MDEyODAwMDA0MlowRzELMAkGA1UEBhMCVVMxIjAgBgNVBAoT
GUdvb2dsZSBUcnVzdCBTZXJ2aWNlcyBMTEMxFDASBgNVBAMTC0dUUyBSb290IFI0
MHYwEAYHKoZIzj0CAQYFK4EEACIDYgAE83Rzp2iLYK5DuDXFgTB7S0md+8Fhzube
Rr1r1WEYNa5A3XP3iZEwWus87oV8okB2O6nGuEfYKueSkWpz6bFyOZ8pn6KY019e
WIZlD6GEZQbR3IvJx3PIjGov5cSr0R2Ko4H/MIH8MA4GA1UdDwEB/wQEAwIBhjAd
BgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwDwYDVR0TAQH/BAUwAwEB/zAd
BgNVHQ4EFgQUgEzW63T/STaj1dj8tT7FavCUHYwwHwYDVR0jBBgwFoAUYHtmGkUN
l8qJUC99BM00qP/8/UswNgYIKwYBBQUHAQEEKjAoMCYGCCsGAQUFBzAChhpodHRw
Oi8vaS5wa2kuZ29vZy9nc3IxLmNydDAtBgNVHR8EJjAkMCKgIKAehhxodHRwOi8v
Yy5wa2kuZ29vZy9yL2dzcjEuY3JsMBMGA1UdIAQMMAowCAYGZ4EMAQIBMA0GCSqG
SIb3DQEBCwUAA4IBAQAYQrsPBtYDh5bjP2OBDwmkoWhIDDkic574y04tfzHpn+cJ
odI2D4SseesQ6bDrarZ7C30ddLibZatoKiws3UL9xnELz4ct92vID24FfVbiI1hY
+SW6FoVHkNeWIP0GCbaM4C6uVdF5dTUsMVs/ZbzNnIdCp5Gxmx5ejvEau8otR/Cs
kGN+hr/W5GvT1tMBjgWKZ1i4//emhA1JG1BbPzoLJQvyEotc03lXjTaCzv8mEbep
8RqZ7a2CPsgRbuvTPBwcOMBBmuFeU88+FSBX6+7iP0il8b4Z0QFqIwwMHfs/L6K1
vepuoxtGzi4CZ68zJpiq1UvSqTbFJjtbD4seiMHl
-----END CERTIFICATE-----
---
Server certificate
subject=CN = robotdreams.cc
issuer=C = US, O = Google Trust Services, CN = WE1
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: ECDSA
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 2834 bytes and written 396 bytes
Verification: OK
---
New, TLSv1.3, Cipher is TLS_AES_256_GCM_SHA384
Server public key is 256 bit
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 0 (ok)
---
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: 017EA58C9C249AE8F0C78F9C80E99343854B92AB61284FA1ACF46118A37ED9A7
    Session-ID-ctx: 
    Resumption PSK: 4524727D7765FC00C9ACAD613B1274E76CC4361F43C443384BD8ABB0C96E6B781E9FDD1C4EBA9A2403E4C741ECB44FDA
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 64800 (seconds)
    TLS session ticket:
    0000 - 32 6f 97 8b e0 20 b2 3a-4a 91 e7 17 15 54 59 cd   2o... .:J....TY.
    0010 - da e3 8b df 7f bc 81 da-21 5b f6 98 04 a9 52 cf   ........![....R.
    0020 - ff 60 69 96 09 59 cc b2-d8 45 44 8d 6b d9 ad c7   .`i..Y...ED.k...
    0030 - ee c2 7b 5c 0b c8 0a 6c-6f e5 a4 dc 97 17 da 7a   ..{\...lo......z
    0040 - 12 a6 bc 36 ad 2f c5 cd-39 cf 48 a2 7e 31 c1 d7   ...6./..9.H.~1..
    0050 - c6 91 a6 6e 9f 76 fe 79-dc ee bc fd 58 06 9a 93   ...n.v.y....X...
    0060 - e7 bc 09 00 03 77 85 3e-14 ee 38 e0 3c df d7 ea   .....w.>..8.<...
    0070 - 17 d8 82 af b5 d6 cb b9-9d 76 83 30 73 8e d6 bd   .........v.0s...
    0080 - 39 54 0d 3b 70 25 68 ba-50 eb e6 f6 df e8 d5 e4   9T.;p%h.P.......
    0090 - b4 1c dc e5 09 c2 db f0-d8 ba c1 7c f5 3f 01 02   ...........|.?..
    00a0 - 4d 0e aa 4e 1f 38 a1 d9-da e2 f4 f2 73 96 e0 02   M..N.8......s...
    00b0 - ed d8 05 b6 96 1c 26 9f-4f 32 f3 65 9d 06 a5 bc   ......&.O2.e....

    Start Time: 1760987055
    Timeout   : 7200 (sec)
    Verify return code: 0 (ok)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: F8E0958FF4C676822877A089B3453ED652CEE945C464415FA81DC5418BA3615D
    Session-ID-ctx: 
    Resumption PSK: D5CA5A4118BC233E50661166850B7967B34D5EBB9CD034A033458FF0A17AA52F1D81E88B1578B9DF0A8BD86BD9C603D0
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 64800 (seconds)
    TLS session ticket:
    0000 - 32 6f 97 8b e0 20 b2 3a-4a 91 e7 17 15 54 59 cd   2o... .:J....TY.
    0010 - 98 7a a8 32 47 d5 bc 82-b0 36 b6 7f 26 82 6a 9b   .z.2G....6..&.j.
    0020 - d5 0b 0a 3f 76 6e 49 71-73 55 59 2b 24 e3 fd d4   ...?vnIqsUY+$...
    0030 - 04 55 6e 77 1f 09 7f 5b-f7 e4 ce 12 79 21 39 66   .Unw...[....y!9f
    0040 - b0 1b 1b 77 23 36 16 84-44 bf 7d 68 35 4e a5 40   ...w#6..D.}h5N.@
    0050 - ba 95 71 12 17 68 55 e6-f0 4a 6f 15 99 d8 c3 a7   ..q..hU..Jo.....
    0060 - d6 39 9c 27 b2 c3 ff 81-3b 7e f4 c1 82 d2 bc 16   .9.'....;~......
    0070 - 18 49 10 e9 57 65 69 4f-53 da 7f 3b bc e9 bc fa   .I..WeiOS..;....
    0080 - c8 7a 42 5e fe ee 05 2c-f2 a6 9c 7a 7f 49 5f 36   .zB^...,...z.I_6
    0090 - b1 06 b8 59 58 cd db 5b-93 f2 4b 9d bd 41 61 da   ...YX..[..K..Aa.
    00a0 - ff cb ba a6 5a 8e 93 2d-87 0d 0c 56 84 76 22 36   ....Z..-...V.v"6
    00b0 - e8 4c 92 2e de 36 a7 7f-d4 3f c7 40 c3 1c 10 4f   .L...6...?.@...O

    Start Time: 1760987055
    Timeout   : 7200 (sec)
    Verify return code: 0 (ok)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
closed
```

Відповідно до даного результату:

Сертифікат видав: Google Trust Services

Найдовший термін дії має сертифікат «WE1»
Видавець: Google Trust Services LLC
Період дії: 13 грудня 2023 — 20 лютого 2029р.

Розмір ключа: 256 біт
Еліптична крива: NIST P-256 / secp256r1