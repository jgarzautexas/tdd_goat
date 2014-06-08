from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page

# Create your tests here.
class HomePageTest(TestCase):
    def test_root_url(self):
        found = resolve('/')
	self.assertEqual(found.func, home_page)
#class SimpleTest(TestCase):
#    def test_basic_addition(self):
#        """
#	Tests that 1 + 1 always equals 2.
#	"""
#	self.assertEqual(1+1, 2)
#
#    def test_true(self):
#        """
#	Tests True
#	"""
#        self.assertTrue(True)
#


