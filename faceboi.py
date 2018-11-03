#test : Hayato Nakamura

from face_recognition.cli import image_files_in_folder

known_image = face_recognition.load_image_file("rick1.jpg")
unknown_image = face_recognition.load_image_file("rick.jpg")

biden_encoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces([biden_encoding], unknown_encoding)

