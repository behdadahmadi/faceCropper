#!/usr/bin/python
#faceCroper
#by Behdad Ahmadi
#Twitter:behdadahmadi
#https://logicalcoders.com
import cv2
import argparse
import os, sys

def banner():
    dotname = "-" * 31
    print " "
    print dotname.center(16, '-')
    print (".:: " + 'Face Cropper' + " ::.").center(30)
    print "by Behdad Ahmadi".center(30)
    print "Twitter:behdadahmadi".center(30)
    print dotname.center(20, '-')


def main():
    banner()
    parser = argparse.ArgumentParser()
    parser.add_argument('image',help='Image to be cropped')
    args = parser.parse_args()
    cropped_name = args.image.split('.')[0] + '-' + 'cropped.jpg'
    if not os.path.exists(args.image):
        print 'File is not existed'
        sys.exit()
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    img = cv2.imread(args.image)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for idx,(x,y,w,h) in enumerate(faces):
        cropped = img[x:x + w, y:y + h]
        cv2.imshow(cropped_name, cropped)
        if os.path.exists(cropped_name):
            file_name = cropped_name.split('.')[0] + str(idx) + '.jpg'
        else:
            file_name = cropped_name
        cv2.imwrite(file_name, cropped)
        print 'Saved as {0}'.format(file_name)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
