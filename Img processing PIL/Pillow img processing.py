#Displaying the image using pillow
from PIL import Image
img=Image.open("mycode.png")
img.show()

#Tilting the image by a certain angle
from PIL import Image
img=Image.open("mycode.png")
rotated=img.rotate(60)#mention the angle here
rotated.show()

#Bluring an image:
from PIL import Image
from PIL import ImageFilter
img=Image.open("mycode.png")#original
blurred=img.filter(ImageFilter.BLUR)#slightly blurred
blurred=blurred.filter(ImageFilter.BLUR)
blurred.show()#blurred

#Sharpen an image:
from PIL import Image
from PIL import ImageFilter
img=Image.open("happy.jpg")
sharpen=img.filter(ImageFilter.EDGE_ENHANCE)
sharpen=sharpen.filter(ImageFilter.EDGE_ENHANCE)
sharpen.show()
sharpen.save("sharp happy.jpg")

#Find edges(changes the image to black background with white lines
from PIL import Image
from PIL import ImageFilter
img=Image.open("mycode.png")
edges=img.filter(ImageFilter.FIND_EDGES)
edges.show()
edges.save("hey_code.png")

#Emboss filter(replacing each pixel by a highlight or shadow depending on the light dark boundaries
from PIL import Image
from PIL import ImageFilter
img=Image.open("happy.jpg")
emboss=img.filter(ImageFilter.EMBOSS)
emboss.show()
emboss.save("Emboss_happy.jpg")

#Contour filter
from PIL import Image
from PIL import ImageFilter
img=Image.open("happy.jpg")
contour=img.filter(ImageFilter.CONTOUR)
contour.show()
contour.save("happy_con.jpg")


