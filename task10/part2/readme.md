# Завдання 10.2

Перевіримо підпис лектора на відповідне зображення ``` image.png ```. За умовою підпис виглядає таким чином:

```
-----BEGIN SSH SIGNATURE-----
U1NIU0lHAAAAAQAAADMAAAALc3NoLWVkMjU1MTkAAAAg5zLXqknUP9b21pGGC7L26LXu5n
W2zG15i0WExXmJac4AAAAMcm9ib3RfZHJlYW1zAAAAAAAAAAZzaGE1MTIAAABTAAAAC3Nz
aC1lZDI1NTE5AAAAQCabuXryeHf3RY7qFI/sACI+1ldE8INgrrFWpObWbLCjwvtvDBTfMT
aOHFN00UghzhkD+qmXLZZl1y2FkNtdhQM=
-----END SSH SIGNATURE-----
```

Публічний ключ:

```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOcy16pJ1D/W9taRhguy9ui17uZ1tsxteYtFhMV5iWnO ruslan.kiyanchuk@gmail.com
```

Збережемо публічний ключ у відповідні файли та виконаємо перевірку командою:

```
ssh-keygen -Y verify -f allowed_signers -I ruslan.kiyanchuk@gmail.com -n robot_dreams -s image.png.sig < image.png
```

Отримана відповідь:

```
Good "robot_dreams" signature for ruslan.kiyanchuk@gmail.com with ED25519 key SHA256:SBdGwvJ0qTZg9amDdXFvgSixDho7C0AtxhYyU2KDj+g
```