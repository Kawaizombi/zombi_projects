import unittest, mine_sweeper
__author__ = 'Андрей'


class FieldTest(unittest.TestCase):
    # field = mine_sweeper.BattleField(3, 3, 'hard')

    def test_neighbours(self):
        field = mine_sweeper.BattleField(3, 3, 'hard')
        n = list(field._neighbour_cells(1, 1))
        self.assertSequenceEqual([(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)], n)

        n = list(field._neighbour_cells(0, 0))
        self.assertEqual([(0, 0), (0, 1), (1, 0), (1, 1)], n)

        n = list(field._neighbour_cells(2, 1))
        self.assertEqual([(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)], n)

    def test_right_click(self):
        field = mine_sweeper.BattleField(3, 3, 'hard')
        field.put_mine(1, 1)
        field.left_click(1, 1)
        self.assertTrue(field.game_over)
