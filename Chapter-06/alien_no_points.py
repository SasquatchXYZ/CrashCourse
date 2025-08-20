alien_0 = {'color': 'green', 'speed': 'slow'}

# Throws a KeyError
# print(alien_0['points'])

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
