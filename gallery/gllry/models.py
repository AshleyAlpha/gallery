from django.db import models

# Create your models here.

class Location(models.Model):
    photo_location = models.CharField(max_length=50)

    def save_location(self):
        self.save()
    
    def delete_location(self):
        self.delete()
    
    def update_location(self, update):
        self.photo_location = update
        self.save()
    
    @classmethod
    def get_location_id(cls, id):
        locate = Location.objects.get(pk = id)
        return locate

    def __str__(self):
        return self.photo_location

class Category(models.Model):
    photo_category = models.CharField(max_length=50)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()
    
    def update_category(self, update):
        self.photo_category = update
        self.save()

    @classmethod
    def get_category_id(cls, id):
        category = Category.objects.get(pk = id)
        return category

    def __str__(self):
        return self.photo_category
class Image(models.Model):
    image = models.ImageField(upload_to='media/Images/')
    name = models.CharField(max_length=30)
    description = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)

    class Meta:
        ordering = ('-id',)

    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()
    
    def __str__(self):
        return self.name
    
    @classmethod
    def get_all_images(cls):
        all_images = Image.objects.all()
        return all_images
    
    @classmethod
    def get_image_by_id(cls, id):
        an_image = Image.objects.get(id=id)
        return an_image
    
    @classmethod
    def search_image(cls,search_category):
        images_category = Image.objects.filter(category__photo_category__icontains=search_category)
        return images_category
    @classmethod
    def filter_by_location(cls, filter_location):
        location=Location.objects.filter(id=filter_location)
        images_location = Image.objects.filter(location=location)
        return images_location   