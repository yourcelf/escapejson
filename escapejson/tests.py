# -*- coding: utf-8 -*-
import unittest

from escapejson import escapejson

class TestEscapeJSON(unittest.TestCase):
    def test_escape_script(self):
        bad =  '''{"msg": "</script><script>alert('Bad!')</script>"}'''
        good = '''{"msg": "<\/script><script>alert('Bad!')<\/script>"}'''
        self.assertEquals(escapejson(bad), good)

    def test_escape_problematic_unicode(self):
        bad =  u'{"msg": "\u2028This is a problem\u2029"}'
        good = r'{"msg": "\u2028This is a problem\u2029"}'
        self.assertEquals(escapejson(bad), good)

    def test_inoccuous_passthrough(self):
        fine = u'{"msg": "\u0028What the hey"}'
        self.assertEquals(escapejson(fine), fine)

if __name__ == "__main__":
    unittest.main()
