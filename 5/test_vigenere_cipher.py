"""Tests for 5"""
import unittest
from vigenere_cipher import VigenereCipher
from vigenere_cipher import combine_character
from vigenere_cipher import separate_character
from unittest import TestCase

class TestVigenereCipher(TestCase):
    """TestVigenereCipher"""
    def test_encode(self):
        """Test 1"""
        cipher = VigenereCipher("TRAIN")
        encoded = cipher.encode("ENCODEDINPYTHON")
        self.assertEqual(encoded, "XECWQXUIVCRKHWA")
    def test_encode_character(self):
        """Test 2"""
        cipher = VigenereCipher("TRAIN")
        encoded = cipher.encode("E")
        self.assertEqual(encoded, "X")
    def test_encode_spaces(self):
        """Test 3"""
        cipher = VigenereCipher("TRAIN")
        encoded = cipher.encode("ENCODED IN PYTHON")
        self.assertEqual(encoded, "XECWQXUIVCRKHWA")
    def test_encode_lowercase(self):
        """Test 4"""
        cipher = VigenereCipher("TRain")
        encoded = cipher.encode("encoded in Python")
        self.assertEqual(encoded, "XECWQXUIVCRKHWA")
    def test_combine_character(self):
        """Test 5"""
        self.assertEqual(combine_character("E", "T"), "X")
        self.assertEqual(combine_character("N", "R"), "E")
    def test_combine_character1(self):
        """Test 6"""
        self.assertNotEqual(combine_character("E", "T"), "L")
        self.assertNotEqual(combine_character("N", "R"), "G")
    def test_extend_keyword(self):
        """Test 7"""
        cipher = VigenereCipher("TRAIN")
        extended = cipher.extend_keyword(16)
        self.assertEqual(extended, "TRAINTRAINTRAINT")
    def test_separate_character(self):
        """Test 8"""
        self.assertEqual(separate_character("X", "T"), "E")
        self.assertEqual(separate_character("E", "R"), "N")
    def test_decode(self):
        """Test 9"""
        cipher = VigenereCipher("TRAIN")
        decoded = cipher.decode("XECWQXUIVCRKHWA")
        self.assertEqual(decoded, "ENCODEDINPYTHON")
# if __name__ == "__main__":
#     unittest.main()
