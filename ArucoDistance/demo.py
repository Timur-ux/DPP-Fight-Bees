import cv2  
from PIL import Image  
import os

def recordImages(video_name, camera_index, framesN = 600, folder = "."):
    cap = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)

    _, img = cap.read()
    width, height, layers = img.shape
    for i in range(framesN):
        _, img = cap.read()
        cv2.imwrite(f"{folder}/demoImages/{i}.jpg", img)

    cv2.destroyAllWindows()
    # video.release()

def showVideo(video_name):
    cap = cv2.VideoCapture(video_name)
    while True:
        ret, img = cap.read()
        if ret == True:
            cv2.imshow(video_name, img)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()
  
  
def prepare_images(folder = '.'):
    mean_height = 0
    mean_width = 0
      
    num_of_images = len(os.listdir(folder)) 
      
    for file in os.listdir(folder): 
        im = Image.open(os.path.join(folder, file)) 
        width, height = im.size 
        mean_width += width 
        mean_height += height 
      
    mean_width = int(mean_width / num_of_images) 
    mean_height = int(mean_height / num_of_images) 
      
    for file in os.listdir(folder): 
        if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith("png"): 
            im = Image.open(os.path.join(folder, file))  
       
            # im.size includes the height and width of image 
            width, height = im.size    
      
            # resizing  
            imResize = im.resize((mean_width, mean_height), Image.LANCZOS)  
            imResize.save(os.path.join(folder, file), 'JPEG', quality = 95) # setting quality 
      
  
# Video Generating function 
def generate_video(video_name, fps, image_folder  = "."): 
    images = [img for img in os.listdir(image_folder) 
              if img.endswith(".jpg") or
                 img.endswith(".jpeg") or
                 img.endswith("png")] 
     
    frame = cv2.imread(os.path.join(image_folder, images[0])) 
  
    # setting the frame width, height width 
    # the width, height of first image 
    height, width, layers = frame.shape   
  
    video = cv2.VideoWriter(video_name, 0, fps, (width, height))  
  
    # Appending the images to the video one by one 
    for i in range(len(images)):  
        image = f"{i}.jpg"
        # print(image)
        video.write(cv2.imread(os.path.join(image_folder, image)))  
      
    # Deallocating memories taken for window creation 
    cv2.destroyAllWindows()  
    video.release()  # releasing the video generated 

if __name__ == "__main__":
    video_name = "demo.avi"
    # print('Start')
    recordImages(video_name, 1, 600)
    # print('End')
    prepare_images('./demoImages')
    generate_video(video_name, 30, './demoImages')
    # showVideo(video_name)

