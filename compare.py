import face_recognition
import picamera
import numpy as np
import os

def compare_face(compare_lib):

    camera = picamera.PiCamera()
    camera.resolution = (320,240)
    output = np.empty((240,320,3),dtype=np.uint8)
    #images = tuple({"zyh.jpg","obama_small.jpg"})

    while True:
        print("caputing image...")
        camera.capture(output,format="rgb")
        face_locs = face_recognition.face_locations(output)
        print("found {} faces in image...".format(len(face_locs)))
        face_encodings = face_recognition.face_encodings(output,face_locs)
        
    
        print("load image...")
        #compare_lib = "/home/pi/picamera/comparelib"
        #for image in images:
        
        exit_flag = False
        #files = os.listdir(r"/home/pi/picamera/comparelib")
        files = os.listdir(compare_lib)
        out_last_pos = len(files) - 1
        for filename in files:
            if exit_flag:
                break

            out_index = files.index(filename)
            file_full_path = compare_lib + os.sep + filename
            loaded_file = face_recognition.load_image_file(file_full_path)
            loaded_file_encoding = face_recognition.face_encodings(loaded_file)[0]
            
            name = "<Unknown Person>"
            in_last_pos = len(face_encodings) - 1
            for face_encoding in face_encodings:
                in_index = face_encodings.index(face_encoding)
                match = face_recognition.compare_faces([loaded_file_encoding],face_encoding)
                if match[0]:
                    exit_flag = True
                    
                    filename_arr = ".".join(filename.split(".")[:-1]).split("_")
                    name = filename_arr[0]
                    department = filename_arr[1]
                    position = filename_arr[2]
                    phone = filename_arr[3]
                    email = filename_arr[4]
                    print("I see someone name {},department {},position {},phone {},email {}".format(name,department,position,phone,email))
                    break
                elif out_last_pos == out_index and in_last_pos == in_index:
                    print("I see someone name {}".format(name))
                    break
                else :
                    continue

if __name__=='__main__':
    compare_lib = '/home/pi/picamera/comparelib'
    compare_face(compare_lib)