from django.contrib.auth.models import User
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files import File




# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='user_photos/', null=True, blank=True)

    def __str__(self):
        return self.user.username
    
class Product(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='product_photos/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='product_photos/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    PROVINCE_CHOICES = (
        ('Aceh', 'Aceh'),
        ('Bali', 'Bali'),
        ('Bangka Belitung', 'Bangka Belitung'),
        ('Banten', 'Banten'),
        ('Bengkulu', 'Bengkulu'),
        ('Gorontalo', 'Gorontalo'),
        ('DKI Jakarta', 'DKI Jakarta'),
        ('Jambi', 'Jambi'),
        ('Jawa Barat', 'Jawa Barat'),
        ('Jawa Tengah', 'Jawa Tengah'),
        ('Jawa Timur', 'Jawa Timur'),
        ('Kalimantan Barat', 'Kalimantan Barat'),
        ('Kalimantan Selatan', 'Kalimantan Selatan'),
        ('Kalimantan Tengah', 'Kalimantan Tengah'),
        ('Kalimantan Timur', 'Kalimantan Timur'),
        ('Kalimantan Utara', 'Kalimantan Utara'),
        ('Kepulauan Riau', 'Kepulauan Riau'),
        ('Lampung', 'Lampung'),
        ('Maluku', 'Maluku'),
        ('Maluku Utara', 'Maluku Utara'),
        ('Nusa Tenggara Barat', 'Nusa Tenggara Barat'),
        ('Nusa Tenggara Timur', 'Nusa Tenggara Timur'),
        ('Papua', 'Papua'),
        ('Papua Barat', 'Papua Barat'),
        ('Riau', 'Riau'),
        ('Sulawesi Barat', 'Sulawesi Barat'),
        ('Sulawesi Selatan', 'Sulawesi Selatan'),
        ('Sulawesi Tengah', 'Sulawesi Tengah'),
        ('Sulawesi Tenggara', 'Sulawesi Tenggara'),
        ('Sulawesi Utara', 'Sulawesi Utara'),
        ('Sumatera Barat', 'Sumatera Barat'),
        ('Sumatera Selatan', 'Sumatera Selatan'),
        ('Sumatera Utara', 'Sumatera Utara'),
        ('Yogyakarta', 'Yogyakarta')
    )
    
    location = models.CharField(max_length=100, choices=PROVINCE_CHOICES)
    

    class Meta:
        ordering = ('-date_added',)
    
    def __str__(self):
        return self.name
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''
    
    def make_thumbnail(self, image, size=(300, 200)):
        try:
            img = Image.open(image)
            img.convert('RGB')
            img.thumbnail(size)

            thumb_io = BytesIO()
            img.save(thumb_io, 'JPEG', quality=85)

            thumbnail = File(thumb_io, name=image.name)

            return thumbnail
        except Exception as e:
            # Log the exception or print it for debugging purposes
            print(f"Exception occurred while creating thumbnail: {e}")
            return None  # Return None or handle the exception as needed


    def save(self, *args, **kwargs):
        if self.pk:  # If the instance already exists (i.e., updating)
            # Retrieve the existing photo before saving changes
            orig = Product.objects.get(pk=self.pk)
            if self.image != orig.image:  # If a new photo is uploaded
                self.thumbnail = self.make_thumbnail(self.image)
        else:
            # For new instances, if there's an image, create a thumbnail
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)

        super(Product, self).save(*args, **kwargs)