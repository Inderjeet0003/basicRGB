import cv2
import numpy as np

def ef():
    pass
def main():
   img=np.zeros((512,512,3),np.uint8)
   windowName = 'OpenCV BGR Color Pal'
   cv2.namedWindow(windowName)
   cv2.createTrackbar('b',windowName,0,255,ef)
   cv2.createTrackbar('g',windowName,0,255,ef)
   cv2.createTrackbar('r',windowName,0,255,ef)
   while(True):
       cv2.imshow(windowName,img)
       
       if cv2.waitKey(1) ==27:
           break;
    
                  
       blue=cv2.getTrackbarPos('b',windowName)
       green=cv2.getTrackbarPos('g',windowName)
       red=cv2.getTrackbarPos('r',windowName)
       img[:]=[blue,green,red]
       print(blue,green,red)
        
   cv2.destroyAllWindows()

if __name__=="__main__":
    main()