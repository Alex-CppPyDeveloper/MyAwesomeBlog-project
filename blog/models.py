from django.db import models

# Create your models here.
class PostModel(models.Model):
	post_title = models.CharField(max_length = 300)
	post_date = models.DateTimeField()
	post_text = models.TextField()
	post_image = models.ImageField(upload_to='blog_images/')


	def __str__(self):
		return self.post_title