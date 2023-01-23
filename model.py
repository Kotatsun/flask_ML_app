import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import datasets, transforms

#----------------------------------------------------------
# ニューラルネットワークモデルの定義
class Net(nn.Module):
    def __init__(self, input_size, output_size):
        super(Net, self).__init__()

        # 各クラスのインスタンス（入出力サイズなどの設定）
        self.fc1 = nn.Linear(input_size, 100)
        self.fc2 = nn.Linear(100, output_size)

    def forward(self, x):
        # 順伝播の設定（インスタンスしたクラスの特殊メソッド(__call__)を実行）
        x = self.fc1(x)
        x = torch.sigmoid(x)
        x = self.fc2(x)
        return F.log_softmax(x, dim=1) 

# モデルによる推論
def mnist_pred(inputs):
  #----------------------------------------------------------
  # モデルの読み込み
  device = 'cuda' if torch.cuda.is_available() else 'cpu'  # GPU(CUDA)が使えるかどうか？
  image_size = 28*28                                       # 画像の画素数(幅x高さ)
  model = Net(input_size=image_size, output_size=10).to(device)
  model.load_state_dict(torch.load('./weights/model_weights.pth'))
  # 評価
  model.eval()  # モデルを評価モードにする

  inputs = torch.from_numpy(inputs.astype(np.float32)).clone()
  with torch.no_grad():
    # GPUが使えるならGPUにデータを送る
    inputs = inputs.to(device)
    # ニューラルネットワークの処理を行う
    inputs = inputs.view(-1, image_size) # 画像データ部分を一次元へ並び変える
    # 正解の値を取得
    outputs = model(inputs)
    pred = outputs.argmax(1)[0]
    print(pred)
  
  return pred

