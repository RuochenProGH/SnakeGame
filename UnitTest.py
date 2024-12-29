# Unit tests for SnakeGame
import unittest
from SnakeGame import SnakeGame

class TestSnakeGame(unittest.TestCase):
    def setUp(self):
        self.game = SnakeGame()

    def test_initial_state(self):
        self.assertEqual(len(self.game.snake), 3)
        self.assertEqual(self.game.direction, "RIGHT")
        self.assertGreaterEqual(self.game.food[0], 0)
        self.assertGreaterEqual(self.game.food[1], 0)

    def test_change_direction(self):
        self.game.change_direction("UP")
        self.assertEqual(self.game.direction, "UP")
        self.game.change_direction("LEFT")
        self.assertEqual(self.game.direction, "LEFT")
        # Should not allow reversing direction
        self.game.change_direction("RIGHT")
        self.assertEqual(self.game.direction, "LEFT")

    def test_move(self):
        initial_length = len(self.game.snake)
        self.assertTrue(self.game.move())  # Moving without collisions
        self.assertEqual(len(self.game.snake), initial_length)  # Snake moves without eating

    def test_collision_with_wall(self):
        # Simulate moving the snake into the wall
        self.game.snake = [(0, 0), (20, 0), (40, 0)]
        self.game.direction = "LEFT"
        self.assertFalse(self.game.move())  # Collision with wall

    def test_collision_with_self(self):
        # Simulate moving the snake into itself
        self.game.snake = [(100, 100), (80, 100), (80, 120), (100, 120)]
        self.game.direction = "DOWN"
        self.assertFalse(self.game.move())  # Collision with itself

    def test_food_consumption(self):
        # Place food directly in front of the snake
        self.game.food = (120, 100)
        self.game.snake = [(100, 100), (80, 100), (60, 100)]
        self.game.direction = "RIGHT"
        initial_length = len(self.game.snake)
        self.assertTrue(self.game.move())  # Move should succeed
        self.assertEqual(len(self.game.snake), initial_length + 1)  # Snake should grow

if __name__ == "__main__":
    unittest.main()
