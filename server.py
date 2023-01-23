import os
import string
import random
import numpy as np
import cv2
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory

from model import mnist_pred

# ---------------------------------------------------
# 画像のアップロード先のディレクトリ
UPLOAD_DIR = './uploads'
if not os.path.isdir(UPLOAD_DIR):
    os.mkdir(UPLOAD_DIR)
# 推論結果のアップロード先のディレクトリ
PRED_DIR = './preds'
if not os.path.isdir(PRED_DIR):
    os.mkdir(PRED_DIR)

# Applicationの起動
app = Flask(__name__, static_url_path="")

def random_str(n):
    return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(n)])

@app.route('/')
def index():
    pred_list = os.listdir(PRED_DIR)[::-1]
    pred_classes = []
    for path in pred_list:
        with open(os.path.join(PRED_DIR,path)) as f:
            pred_class = f.read()
        pred_classes.append(str(pred_class))
    print(pred_classes)
    return render_template('indexes.html', images=os.listdir(UPLOAD_DIR)[::-1], prediction_classes=pred_classes)

@app.route('/uploads/<path:path>')
def send_js(path):
    return send_from_directory(UPLOAD_DIR, path)

# 参考: https://qiita.com/yuuuu3/items/6e4206fdc8c83747544b
@app.route('/upload', methods=['POST'])
def upload():
    if request.files['image']:
        # 画像として読み込み
        stream = request.files['image'].stream
        img_array = np.asarray(bytearray(stream.read()), dtype=np.uint8)
        img = cv2.imdecode(img_array, 1)
        img = 0.299 * img[:, :, 2] + 0.587 * img[:, :, 1] + 0.114 * img[:, :, 0] ## gray画像に変換

        # 保存
        dt_now = datetime.now().strftime("%Y_%m_%d%_H_%M_%S_") + random_str(5)
        # Raw画像の保存
        upload_path = os.path.join(UPLOAD_DIR, dt_now+"_raw.png")
        cv2.imwrite(upload_path, img)
        
        # 推論結果の保存
        pred = mnist_pred(img[None,...])
        with open(os.path.join(PRED_DIR, dt_now+"_pred.txt"), mode='w') as f:
            f.write(str(pred.to('cpu').detach().numpy().copy()))
        
        return redirect('/')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)