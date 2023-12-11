class Alien:
    total_aliens_created = 0

    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self):
        self.health -= 1

    def is_alive(self):
        return self.health > 0

    def teleport(self, new_x_coordinate, new_y_coordinate):
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection(self, other_object):
        pass  # Placeholder for future implementation

def new_aliens_collection(start_positions):
    return [Alien(x, y) for x, y in start_positions]

# Example usage
alien_start_positions = [(4, 7), (-1, 0)]
aliens = new_aliens_collection(alien_start_positions)

for alien in aliens:
    print(alien.x_coordinate, alien.y_coordinate)
