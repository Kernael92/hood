from django.test import TestCase
from .models import Hood,Profile,Business,Comment,Post

# Create your tests here.
class HoodTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.kilimani= Hood(name='Kilimani',location="Ngong",occupants_count=245)
    
    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kilimani,Hood))
    
    #Testing save method
    def test_save_method(self):
        self.kilimani.save_hood()
        hoods = Hood.objects.all()
        self.assertTrue(len(hoods) > 0)
    
    #Testing delete method
    def tearDown(self):
        Hood.objects.all().delete()
    


