from django.test import TestCase
from .models import Location,Category,Image
# Create your tests here.
class LocationTestClass(TestCase):
    def setUp(self):
        self.calfornie= Location(photo_location="calfornie")
        self.calfornie.save_location()
       #Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.calfornie,Location)) 
    # Testing Save Method
    def test_save_method(self):
        self.calfornie.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)
    def test_updating_location(self):
        location = Location.get_location_id(self.calfornie.id)
        location.update_location('Kitengela')
        location = Location.get_location_id(self.calfornie.id)
        self.assertTrue(location.photo_location == 'Kitengela')
    def tearDown(self):
        self.calfornie.delete_location()
class CategoryTestClass(TestCase):
        #creating a new category and saving it
    def setUp(self):
        self.pic= Category(photo_category='pic')
        self.pic.save_category()
    def test_instance(self):
        self.assertTrue(isinstance(self.pic,Category))
    
    def tearDown(self):
        self.pic.delete_category()
    
    def test_updating_category(self):
        category = Category.get_category_id(self.pic.id)
        category.update_category('SUV')
        category = Category.get_category_id(self.pic.id)
        self.assertTrue(category.photo_category == 'SUV')

class ImageTestCase(TestCase):
    # Set Up Method
    def setUp(self):
        self.pic = Category(photo_category='pic')
        self.pic.save_category()

        self.calfornie = Location(photo_location='calfornie')
        self.calfornie.save_location()

        self.image = Image(name='Lamborghini', description='very first car', location=self.calfornie, category=self.pic)
        self.image.save_image()
    
    def tearDown(self):
        self.image.delete_image()
        self.pic.delete_category()
        self.calfornie.delete_location()
    
    def test_get_all_images(self):
        images = Image.get_all_images()
        self.assertTrue(len(images)>0)
    
    def test_get_image_by_id(self):
        images = Image.get_image_by_id(self.image.id)
        self.assertTrue(images == self.image)

    def test_search_image(self):
        images = Image.search_image('pic')
        self.assertTrue(len(images)>0)

