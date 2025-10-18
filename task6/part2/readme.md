# Завдання 6.2

Таємне повідомлення було зашифровано з використанням паддингу:

padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

Код наведено у файлі [task6.2.py](task6.2.py)

Результат шифрування збережено у файлі [task-2-message.txt](task-2-message.txt)