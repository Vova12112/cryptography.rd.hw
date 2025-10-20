# Завдання 9.2

Відповідно до умови, згенеруємо запит на формування сертифікату:

```
   openssl req -new -keyout task-9-2.key -out task-9-2.csr \
      -subj "/C=UA/L=Kyiv/O=Robot_dreams/CN=www.robotdreams.cc/emailAddress=vladimiranikin01@gmail.com" \
      -nodes
```

