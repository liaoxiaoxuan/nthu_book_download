import os
import img2pdf
from PIL import Image, ImageFile
#ImageFile.LOAD_TRUNCATED_IMAGES = True

list    = os.listdir(".")
#print(list)
newList = [x for x in list if x.endswith(".jpg")]
#for image in newList :
#    im = Image.open(image)
#    im.save('png/'+image+'.png')
#    image = 'png/'+image+'.png'
#print(newList)
pdf     = img2pdf.convert(newList)
file    = open("book.pdf", "wb")
file.write(pdf)
file.close