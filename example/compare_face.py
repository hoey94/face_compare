import face_recognition

songning_image = face_recognition.load_image_file("songning.jpg")
songning_encoding = face_recognition.face_encodings(songning_image)[0]

unknown_image = face_recognition.load_image_file("unknow2.jpg")
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

result = face_recognition.compare_faces([songning_encoding],unknown_encoding)

if result[0] == True:
    print("is songning")
else:
    print("isn't songning")
