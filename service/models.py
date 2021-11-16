from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Service(models.Model):
    service_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    employee = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    featured_image = CloudinaryField('image', default='placeholder')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    excerpt = models.TextField(blank=True)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    customer = models.ManyToManyField(
        User, related_name="customer_services", blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.service_name

