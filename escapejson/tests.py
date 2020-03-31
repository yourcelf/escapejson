import unittest

from escapejson import escapejson

class TestEscapeJSON(unittest.TestCase):
    def test_escape_script(self):
        bad =  '''{"msg": "</script><script>alert('Bad!')</script>"}'''
        good = '''{"msg": "<\/script><script>alert('Bad!')<\/script>"}'''
        self.assertEqual(escapejson(bad), good)

    def test_escape_problematic_unicode(self):
        bad =  '{"msg": "\u2028This is a problem\u2029"}'
        good = r'{"msg": "\u2028This is a problem\u2029"}'
        self.assertEqual(escapejson(bad), good)

    def test_inoccuous_passthrough(self):
        fine = '{"msg": "\u0028What the hey"}'
        self.assertEqual(escapejson(fine), fine)

if __name__ == "__main__":
    unittest.main()
