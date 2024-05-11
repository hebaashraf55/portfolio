from django.db import models



class Person(models.Model):
    USER_CHOICES = [
        ('member' , 'member'),
        ('guest' , 'guest')
    ]
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    status= models.CharField(max_length=50, choices= USER_CHOICES)
    discribtion = models.TextField()
    image = models.ImageField(upload_to='images/',blank=True, null=True)
    
    userMail = models.EmailField(unique=True)
    userPhone = models.IntegerField()
    
    def __str__(self):
        return f"{self.firstName} {self.lastName}"
    
    
class Post(models.Model):
    postName = models.CharField(max_length=100)
    postDiscribtion = models.TextField()
    postDate = models.DateTimeField(auto_created=True)
    createdBy = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)

    def __str__(self):
       return f"{self.postName}"
   