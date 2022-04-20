#Importing Libaries
import cv2
import pandas as pd


#Reading the image 
img = cv2.imread("Heading.jpg")


#Initializing Variables
clicked = False
r = g = b = xpos = ypos = 0

#Reading csv file and naming the columns
index=["color","color_name","hex","R","G","B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

#function to choose the most matching color
def getColorName(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname

#function to get the coordinates upon left-clicking
def show_color(event, x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)
       
cv2.namedWindow('color detection')
cv2.setMouseCallback('color detection',show_color)

while(1):
    #displaying window
    cv2.imshow("color detection",img)
    if (clicked):
   
        #Creating a rectangle to fill with the color chosen and write in
        cv2.rectangle(img,(20,20), (600,60), (b,g,r), -1)

        #Creating text string to display color name and RGB values.
        text = getColorName(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)
        
        #Putting the color name on the output picture 
        cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)

        #If the color is very light, the text is written in black.
        if(r+g+b>=600):
            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
            
        clicked=False

    #Break the loop when user hits 'esc' key    
    if cv2.waitKey(20) & 0xFF ==27:
        break
    
cv2.destroyAllWindows()
