import unittest
from translator import french_to_english, english_to_french

class TestTranslator(unittest.TestCase):
    def test_french_to_english_equal(self):
        self.assertEqual(french_to_english(None), '')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
    
    def test_french_to_english_not_equal(self):
        self.assertNotEqual(french_to_english('au revoir'), 'Hello')
    
    def test_english_to_french_equal(self):
        self.assertEqual(english_to_french(None), '')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    
    def test_english_to_french_not_equal(self):
        self.assertNotEqual(english_to_french('Goodbye'), 'Bonjour')

unittest.main()
