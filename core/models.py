from django.db import models 

# Create your models here.

class Test(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    phone_no = models.IntegerField()
    address = models.CharField(max_length=100, null=False)

    def get_details(self):
        data = {
            "id" : self.id,
            "first_name" : self.first_name,
            "last_name" : self.last_name,
            "email" : self.email,
            "phone_no" : self.phone_no,
            "address" : self.address,
        }
        return data
