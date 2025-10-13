players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("--- All ---")
print(players)
print("--- 0:3 ---")
print(players[0:3])
print("--- :4 ---")
print(players[:4])
print("--- 2: ---")
print(players[2:])
print("--- -3: (Last Three) ---")
print(players[-3:])

print("\nHere are the first three players on my team:")
for player in players[:3]:
    print(f"\t{player.title()}")
