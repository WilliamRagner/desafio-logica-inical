nome = input("Qual é o nome do seu herói? ")
xp = int(input("Quantos pontos de experiência ele tem? "))

if xp < 1000:
    rank = "Ferro"
elif xp <= 2000:
    rank = "Bronze"
elif xp <= 5000:
    rank = "Prata"
elif xp <= 7000:
    rank = "Ouro"
elif xp <= 8000:
    rank = "Platina"
elif xp <= 9000:
    rank = "Diamante"
elif xp <= 10000:
    rank = "Ascendente"
else:
    rank = "Imortal"

print(f"\nO Herói de nome {nome} está no nível de {rank}")

if xp < 1000:
    print("Dica: Continue jogando para subir de nível!")