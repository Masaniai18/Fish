def setup():
    size(400,400)
    background(0,0,255)
    Nemo(150,150,50,30)
    Tim(250,200,60,30)
    Gary(235,115,65,30)
    


def Nemo(xCoord,yCoord,NemoW,NemoH):
    setColor("orange")
    ellipse(xCoord,yCoord,NemoW,NemoH)
    setColor("orange")
    rect(rectX-95,125,20,50)
    setColor("black")
    rect(rectX-125,135,10,30)
    setColor("black")
    ellipse(133,145,5,5)
    
def Tim(eCoord,tCoord,TimW,TimH):
    setColor("black")
    ellipse(eCoord,tCoord,TimW,TimH)
    setColor("black")
    rect(rectX,175,20,50)
    setColor("pink")
    ellipse(230,195,5,5)

def Gary(bCoord,cCoord,GarW,GarH):
    setColor("green")
    ellipse(bCoord,cCoord,GarW,GarH)
    setColor("green")
    rect(rectX-3,92,20,50)
    setColor("black")
    ellipse(210,110,5,5)
    
         




def setColor(colorName):
    if colorName == "orange":
        fill(255,100,0)
    elif colorName == "black":
        fill(0)
    elif colorName == "green":
        fill(0,255,0)
    elif colorName == "pink":
        fill(255,255,255)
