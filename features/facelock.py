# import cv2
#
# # Load the cascade classifier
# face_cascade = cv2.CascadeClassifier('path/to/haarcascade_frontalface_default.xml')
#
# # Read the image
# image = cv2.imread('C:\\Users\\chatu\\OneDrive\\Desktop\\LiNa\\database\\WIN_20230113_13_20_46_Pro.jpg')
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# # Detect faces
# faces = face_cascade.detectMultiScale(gray, 1.1, 4)
#
# # Draw a rectangle around the faces
# for (x, y, w, h) in faces:
#     cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
#
# # Show the image
# cv2.imshow('image', image)
# cv2.waitKey()
# cv2.destroyAllWindows()
