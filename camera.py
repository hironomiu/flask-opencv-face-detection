import cv2

face_cascade = cv2.CascadeClassifier()
# 顔認識はOpenCVのカスケード型識別器を利用 https://github.com/opencv/opencv/tree/4.x/data/haarcascades
face_cascade.load(cv2.samples.findFile("static/haarcascade_frontalface_alt.xml"))

def gen(video):
    detected_message = "Undetected"
    while True:
        success, image = video.read()

        if success != True:
            break

        frame_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        frame_gray = cv2.equalizeHist(frame_gray)
        # 顔が検知された場合facesにx,y,w,hのnumpy.ndarrayが返る、検知されない場合は空のtupleが返る
        faces = face_cascade.detectMultiScale(frame_gray)

        if type(faces) is tuple:
            detected_message = "Undetected"
        else:
            detected_message = "Detected"

        # 顔の検知状況を表示
        cv2.putText(image, detected_message , (300, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

        for (x, y, w, h) in faces:
            center = (x + w//2, y + h//2)
            # 顔のX,Y座標を表示
            cv2.putText(image, "X: " + str(center[0]) + " Y: " + str(center[1]), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
            # 顔認識の範囲を長方形で表示 color(0, 255, 0) 最後の2をマイナス値(-1)にすると塗りつぶしになる
            image = cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

        #     faceROI = frame_gray[y:y+h, x:x+w]
        ret, jpeg = cv2.imencode('.jpg', image)

        frame = jpeg.tobytes()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')