alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']

print(f"You just earned {new_points} points!")

# Adding New Key-Value Pairs

alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['speed'] = 'medium'
print(alien_0)

# Modifying values
alien_0['color'] = 'yellow'
print(f"The alien new color is {alien_0['color']}")

# Move the alien to the rigth
# Determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3
# The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

# Removing key-value pairs
del alien_0['points']
print(alien_0)

# Use get() to access value
point_value = alien_0.get('points', 'No point value assigned')
print(point_value)
