import cv2
from time import sleep
import face_recognition as fr

def facerecognizer(accno):
    key = cv2. waitKey(1)
    webcam = cv2.VideoCapture(0)
    sleep(2)
    while True:
        try:
            check, frame = webcam.read()
            print(check) #prints true as long as the webcam is running
            print(frame) #prints matrix values of each framecd 
            cv2.imshow("Capturing", frame)
            key = cv2.waitKey(1)
            if key == ord('s'): 
                cv2.imwrite(filename=str(accno)+'test.jpg', img=frame)
                webcam.release()
                print("Image saved!")
                cv2.destroyAllWindows()
                break
            elif key == ord('q'):
                webcam.release()
                cv2.destroyAllWindows()
                break
        except(KeyboardInterrupt):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break
    got_image = fr.load_image_file(str(accno)+'test.jpg')

    existing_image = fr.load_image_file(str(accno)+'.jpg')

    got_image_facialfeatures = fr.face_encodings(got_image)[0]

    existing_image_facialfeatures = fr.face_encodings(existing_image)[0]

    results= fr.compare_faces([existing_image_facialfeatures],got_image_facialfeatures)

    if(results[0]):
        face_match=1
    else:
        face_match=0
    return face_match

            
