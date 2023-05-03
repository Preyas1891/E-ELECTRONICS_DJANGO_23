from django.db import models

class UserRegistration(models.Model):
    full_name = models.CharField(max_length = 50)
    mobile_num = models.IntegerField()
    email_id = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    is_approved=models.BooleanField(default=False)

    def __str__(self):
        return self.email_id

class ListingAppliances(models.Model):
    #details
    email_id = models.CharField(max_length=50,blank=True, null=True)
    view_count = models.IntegerField(default = 0)
    title = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to = "images/")
    video=models.FileField(upload_to="video/",default='',null=True,blank=True)
    description = models.TextField(max_length=500)
    country = models.CharField("Area",max_length=50)
    appliance_type = models.CharField(max_length=50)
    #appliance
    appliance_id = models.IntegerField(default=0)
    appliance_size=models.IntegerField(default=0)
    appliance_weight=models.IntegerField(default=0)
    appliance_batterylife=models.IntegerField(default=0)
    appliance_powerconsumptions=models.IntegerField(default=0)
    #appliance_name=models.CharField(max_length=50, null=True)
    #Inclusions
    OriginalCharger = models.BooleanField(default=False)
    box = models.BooleanField(default=False)
    OriginalBill = models.BooleanField(default=False)
    warranty = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    

    def __str__(self):
        return self.title


Product_Raings = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
)

class ProperFeedback(models.Model):
    Appliance_name = models.ForeignKey("ListingAppliances", on_delete=models.CASCADE,blank=True, null=True)
    cust_data = models.ForeignKey("UserRegistration", on_delete=models.CASCADE,blank=True, null=True)
    date_time = models.DateTimeField(auto_now=True)
    rating = models.CharField(max_length=20,choices=Product_Raings,default = '1')
    feedback = models.TextField()
    feed_pos = models.FloatField(default=0.0)
    feed_neg = models.FloatField(default=0.0)

    def __str__(self):
        return self.Appliance_name



class OwnerDetails(models.Model):
    Ownername=models.CharField(max_length=50)
    Owneremail=models.EmailField(unique=True)
    Ownerphone=models.PositiveIntegerField()
    Ownerstate=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    Amount=models.IntegerField(default=50)
    Approved=models.BooleanField(default=False)

    def __str__(self):
        return self.Owneremail


class Orders(models.Model):
    user_id=models.ForeignKey(UserRegistration,on_delete=models.CASCADE)
    owner_id=models.ForeignKey(OwnerDetails,on_delete=models.CASCADE,null=True)
    app_id=models.ForeignKey(ListingAppliances,on_delete=models.CASCADE)
    document=models.FileField(upload_to='file/')
    booked=models.BooleanField(default=False)
    date=models.DateField(null=True)
    payment=models.BooleanField(default=False)

    def __str__(self):
        return str(self.date)


class paymentdetails(models.Model):
    user_id=models.CharField(max_length=50,default="")
    owner_id=models.CharField(max_length=50,default="")
    user=models.CharField(max_length=50)
    Owner=models.CharField(max_length=50)
    appliance_name=models.CharField(max_length=50)
    PaymentVia=models.CharField(max_length=50)
    PaymentMethod=models.CharField(max_length=50)
    Amount=models.CharField(max_length=50)
    transactionId = models.TextField(default=None)
    orderDate = models.DateTimeField(auto_created=True,auto_now=True)

    def __str__(self):
        return self.appliance_name

    