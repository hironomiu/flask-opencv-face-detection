# flask-opencv-face-detection

Flask + OpenCVでカメラ映像から顔を検出

## SetUp

pytnon3.8.9 を利用
パッケージ管理はpipenvを利用

```
pipenv install
```

pipenv を利用しない場合

```
pip install flask
pip install opencv-python
```

### カスケード型識別器

`./static`配下には[OpenCV](https://github.com/opencv/opencv)の[カスケード型識別器](https://github.com/opencv/opencv/tree/4.x/data/haarcascades)にある`haarcascade_frontalface_alt.xml`を今回は利用するため適時`git clone`し配置

## Run

起動後ブラウザで`localhost:3333`を開く

```
pipenv shell
python main.py
```