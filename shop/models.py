

from pyexpat import model
import uuid
from django.db import models
from course.models import *
from django.contrib.auth.models import User

from user_profile.models import slug_generator
# Create your models here.
class product_detail(models.Model):
    product_img=models.ImageField(upload_to='image/shop/')
    product_title=models.CharField(max_length=100)
    slug=models.SlugField(unique=True,max_length=1000)
    product_price=models.IntegerField()
    about_product=models.TextField()
    product_description=models.TextField()
    product_tag=models.CharField(max_length=100)
    quntity=models.IntegerField()
    product_sku=models.IntegerField()
    category=models.CharField(max_length=100)
    discount=models.IntegerField(default=0)
    rating=models.FloatField(default=0.0)
    created_date=models.DateField(auto_now_add=True)
    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slug_generator(product_detail,self.product_title)
        super(product_detail, self).save(*args, **kwargs)
  
    def __str__(self):
        return self.product_title

class shop_review(models.Model):
    shop=models.ForeignKey(product_detail,on_delete=models.CASCADE)
    review=models.TextField()
    rate=models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.shop.product_title[:20] +' - '+self.review[:20]
 

class coupon_code(models.Model):
    code=models.IntegerField()
    valid_date=models.DateField()
    discount=models.IntegerField(null=True)
class cart(models.Model):
    userid=models.IntegerField()
    slug=models.SlugField(null=True)
    prod_id=models.IntegerField()
    prod_name=models.CharField(max_length=100)
    quntity=models.IntegerField()
    coupon=models.IntegerField(default=0)
    total=models.IntegerField(default=0)


class products_purchase_order(models.Model):
    product=models.ForeignKey(product_detail,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True, verbose_name="prod_pyment")
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    company=models.CharField(max_length=100,blank=True)
    country=models.CharField(max_length=50)
    address=models.TextField()
    city=models.CharField(max_length=50)
    province=models.CharField(max_length=100)
    postal_code=models.IntegerField()
    phone=models.IntegerField()
    email=models.EmailField()
    quntity=models.IntegerField()
    payment=models.CharField(max_length=100)
    amount=models.IntegerField()
    order_notes=models.TextField(blank=True)
    status = models.CharField(max_length=50,default='pending')
    order_date=models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        if self.order_id is None and self.order_date and self.id:
            self.order_id = self.order_date.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)
    def __str__(self):
        return self.product.product_title[:10]+' '+self.fname+' '+self.lname
 



class courses_purchase_order(models.Model):
    course=models.ForeignKey(course_detail,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True, verbose_name="crs_pyment")
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    company=models.CharField(max_length=100,blank=True)
    country=models.CharField(max_length=50)
    address=models.TextField()
    city=models.CharField(max_length=50)
    province=models.CharField(max_length=100)
    postal_code=models.IntegerField()
    phone=models.IntegerField()
    email=models.EmailField()
    quntity=models.IntegerField()
    payment=models.CharField(max_length=100)
    amount=models.IntegerField()
    status = models.CharField(max_length=50,default='pending')
    order_notes=models.TextField(blank=True)
    order_date=models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        if self.order_id is None and self.order_date and self.id:
            self.order_id = self.order_date.strftime('PAYTM%Y%m%dOD') + str(self.id)
        return super().save(*args, **kwargs)
 
    def __str__(self):
        return self.course.course_title[:10]+' '+self.fname+' '+self.lname
 
class payment_done_detail(models.Model):

    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    amount = models.FloatField()
    gatewayname = models.CharField(max_length=100)
    bnk_name=models.CharField(max_length=200)
    MID=models.CharField(max_length=200)
    txn_id=models.IntegerField()
    order_id=models.CharField(max_length=200)
    bnk_txn_id=models.IntegerField()
    txn_status = models.CharField(max_length=20,default="pending")
    txn_time = models.DateTimeField()
    # def msgtime(self):
    #     return datetime_from_utc_to_local(self.time).strftime('%I:%M')
    def __str__(self) -> str:
        return self.user.username


class update_order(models.Model):
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    prod_orders=models.ManyToManyField(products_purchase_order)
    crs_orders=models.ManyToManyField(courses_purchase_order)
    updt_id=models.CharField(unique=True, max_length=1000, null=True, blank=True,  verbose_name="updt_pyment")
    updt_date=models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        if self.updt_id is None and self.updt_date and self.id:
            self.updt_id = self.updt_date.strftime('PAYMENT%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)
