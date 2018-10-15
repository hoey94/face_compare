from PIL import Image
import face_recognition

image = face_recognition.load_image_file("obama_and_biden.jpg");

face_locations = face_recognition.face_locations(image)

print("{} face".format(len(face_locations)))

for face_location in face_locations:
    top,right,bottom,left=face_location
    print("位置 Top:{},right:{},bottom:{},left:{}".format(top,right,bottom,left))
        
    #face_image = image[top:bottom,left:right]
    #pil_image = Image.formarray(face_image)
    #pil_image.show()
