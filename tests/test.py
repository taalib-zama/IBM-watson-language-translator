'''Unit test for translator.py'''
import unittest
from translator import englishtofrench
from translator import englishtogerman
class TestTranslator(unittest.TestCase):
    '''Test class for translator'''
    def test_englishtofrench(self):
        '''Tests for french translation'''
        self.assertIsNone(None,"No input provided")
        self.assertEqual(englishtofrench("Hello"), "Bonjour")
        self.assertEqual(englishtofrench("How are you"), "Comment vous êtes")
        self.assertEqual(englishtofrench("Goodbye"), "Au revoir")

    def test_englishtogerman(self):
        '''Tests for german transalation'''
        self.assertIsNone(None, "No input provided")
        self.assertEqual(englishtogerman("Hello"), "Hallo")
        self.assertEqual(englishtogerman("How are you"), "Wie geht es Ihnen?")
        self.assertEqual(englishtogerman("Goodbye"), "Goodbye")

if __name__ == '__main__':
    unittest.main()
