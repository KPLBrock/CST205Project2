
def recolorImage(myImageName, imageType):
  im = Image.open(myImageName)
  pix = im.load()
  for i in xrange(im.size[0]):
    for j in xrange(im.size[1]):
      newRed =  pix[x, y][0]
      newGreen = pix[x, y][1]
      newBlue =  pix[x, y][2]
      if(imageType == 0):
        newRed *= 1.75
      else: 
        if (imageType == 1):
          newGreen *= 1.75
        if (imageType == 2):
          newBlue *= 1.75
      return, newRed, newGreen, newBlue

      
      
def pickMusic(redValue, greenValue, blueValue):
    if (redValue > greenValue):
      if(redValue > blueValue):
        return 1
    if (greenValue > redValue):
      if(greenValue > blueValue):
        return 2
    if (blueValue > greenValue):
      if(blueValue > redValue):
        return 3    
       

  