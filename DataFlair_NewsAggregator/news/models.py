from django.db import models

# Scrape data coming from websites 
# The posts will contain images, urls, and tites
# model will store 3 things :title, image, url

class Headline(models.Model):
  title = models.CharField(max_length=200)
  image = models.URLField(null=True, blank=True) # the image field can be blank
  url = models.TextField()

  def __str__(self): # method that will return the string representation of the object
    return self.title
