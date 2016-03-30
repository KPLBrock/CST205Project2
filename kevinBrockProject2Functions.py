folderPath = "c:/Users/Kevin/Documents/CSTMultimediaProgramming/bit_photos/"
imageFinal = makePicture(folderPath + "1.jpg")

def recolorImage(myImage, imageType):
  for i in range(0, getWidth(myImage)):
    for j in range(0, getHeight(myImage)):
      testPixel = getPixel(myImage, i, j)
      newRed = getRed(testPixel)
      newGreen = getGreen(testPixel)
      newBlue = getBlue(testPixel)
      if(imageType == 0):
        newRed *= 1.75
      else: 
        if (imageType == 1):
          newGreen *= 1.75
        if (imageType == 2):
          newBlue *= 1.75
      newColor = makeColor(newRed, newGreen, newBlue)
      setColor(getPixel(myImage, i, j), newColor)
      
      
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
       


recolorImage(imageFinal, 2)
repaint(imageFinal)      
show(imageFinal)     