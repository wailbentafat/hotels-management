from django.db import models

class client(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    start_date=models.DateField()
    end_date=models.DateField()
    
    def __str__(self) :
        return self.name
    
    
class room(models.Model):
    price = models.IntegerField()
    number = models.IntegerField()
    type = models.CharField(max_length=100)
    free=models.BooleanField (default=True) 
    
    def __str__(self) :
        return self.number
      
      
      
class booking(models.Model):
    start_date=models.DateField()
    end_date=models.DateField()
    client=models.ForeignKey(client,on_delete=models.CASCADE)
    room=models.ForeignKey(room,on_delete=models.CASCADE)
    total_price=models.IntegerField()
    
   
        
          
    