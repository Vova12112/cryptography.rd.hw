# Завдання 10.1

Відповідно до умови, створимо нову ключову пару SSH:

```
   ssh-keygen -t ed25519 -C vladimiranikin01@gmail.com
```

Виконаємо підпис файлу ``` image.png ``` згенерованим приватним ключем:

```
   ssh-keygen -Y sign -f task-10-1.pem -n telegram image.png
```

В результаті отримали підпис:

```
-----BEGIN SSH SIGNATURE-----
U1NIU0lHAAAAAQAAADMAAAALc3NoLWVkMjU1MTkAAAAgY13QxtErWd7r+oqbbRYBCN25km
1unzMAKfqqiqNn230AAAAIdGVsZWdyYW0AAAAAAAAABnNoYTUxMgAAAFMAAAALc3NoLWVk
MjU1MTkAAABAB6/K28iSMIcaO2HFp3qNOopxZ4Rk5w6jXBDuiy6PtiNVhWAnOOd5x0XIpC
uHQh2JxrfZfoQnmAnrpj+uj+MyAw==
-----END SSH SIGNATURE-----
```