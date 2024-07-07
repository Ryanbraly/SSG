import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold", "none")
        node2 = TextNode("This is a text node", "bold", "none")
        self.assertEqual(node, node2)

    def test_ineq(self):
        node = TextNode("This is a text node", "bold", "none")
        node2 = TextNode("This is a Reese's Peanut Butter Cup", "bold", "none")
        self.assertNotEqual(node, node2)

    def test_texttype_diff(self):
        node = TextNode("This is a text node", "bold", "none")
        node2 = TextNode("This is a text node", "italic", "none")
        self.assertNotEqual(node, node2)

    def test_actual_none(self):
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold", None)
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()