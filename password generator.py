import random

# znaki podzielone na grupy, aby upewnić się, że w każdym haśle znajdzie się mała litera, wielka litera, cyfra i znak specjalny
table = ["abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "1234567890", "!@#$%^&*()[];':\""]

p_counter = int(input("Ile chcesz wygenerować haseł? "))
if p_counter == 1: syntax = "jego hasła"
if p_counter > 1: syntax = "ich haseł"
p_length = int(input(f"Jaka ma być długość Two{syntax}? (ilość znaków) "))

for i in range(p_counter):
    p = [random.choice(table[i%4]) for i in range(p_length)]
    random.shuffle(p)
    print("".join(p))