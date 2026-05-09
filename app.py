ChatGPT




已貼上文字 (1).txt
文件
[16:57:42] 🐍 Python dependencies were installed from /mount/src/fff0508/requirements.txt using uv.

Check if streamlit is installed

Streamlit is already installed

[16:57:43] 📦 Processed dependencies!

2026-05-07 16:57:45.175 Uvicorn server started on 0.0.0.0:8501




────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:129 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:689 in code_to_exec                                     

                                                                                

  /mount/src/fff0508/video_app.py:2 in <module>                                 

                                                                                

      1 import streamlit as st                                                  

  ❱   2 import cv2                                                              

      3 import math                                                             

      4 import av                                                               

      5 import time                                                             

                                                                                

  /home/adminuser/venv/lib/python3.14/site-packages/cv2/__init__.py:181 in      

  <module>                                                                      

                                                                                

    178 │   if DEBUG: print('OpenCV loader: DONE')                              

    179                                                                         

    180                                                                         

  ❱ 181 bootstrap()                                                             

    182                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.14/site-packages/cv2/__init__.py:153 in      

  bootstrap                                                                     

                                                                                

    150 │                                                                       

    151 │   py_module = sys.modules.pop("cv2")                                  

    152 │                                                                       

  ❱ 153 │   native_module = importlib.import_module("cv2")                      

    154 │                                                                       

    155 │   sys.modules["cv2"] = py_module                                      

    156 │   setattr(py_module, "_native", native_module)                        

                                                                                

  /usr/local/lib/python3.14/importlib/__init__.py:88 in import_module           

                                                                                

     85 │   │   │   if character != '.':                                        

     86 │   │   │   │   break                                                   

     87 │   │   │   level += 1                                                  

  ❱  88 │   return _bootstrap._gcd_import(name[level:], package, level)         

     89                                                                         

     90                                                                         

     91 _RELOADING = {}                                                         

────────────────────────────────────────────────────────────────────────────────

ImportError: libgthread-2.0.so.0: cannot open shared object file: No such file 

or directory

已思考 2 秒鐘
這個錯誤重點是：

ImportError: libgthread-2.0.so.0: cannot open shared object file
代表你的程式在這行出錯：

import cv2
也就是 OpenCV 需要的系統套件 libgthread-2.0.so.0 沒有被安裝。你的程式確實有用到 cv2 來畫框、顯示文字、處理即時影像畫面。


解法一：修改 requirements.txt
請確認你的 requirements.txt 不要放：

opencv-python
改成：

opencv-python-headless
建議你的 requirements.txt 可以改成這樣：

streamlit
ultralytics
opencv-python-headless
numpy<2
Pillow
torch
torchvision
streamlit-webrtc
streamlit-autorefresh
av
解法二：新增 packages.txt
因為現在錯的是 Linux 系統缺少 libgthread-2.0.so.0，所以你需要在 GitHub 專案裡新增一個檔案：

packages.txt
內容放：

libglib2.0-0
libsm6
libxext6
libxrender1
libgl1
也就是你的 GitHub 檔案應該至少有：

video_app.py
requirements.txt
packages.txt
alarm.mp3
最推薦做法
你的 requirements.txt：

streamlit
ultralytics
opencv-python-headless
numpy<2
Pillow
torch
torchvision
streamlit-webrtc
streamlit-autorefresh
av
你的 packages.txt：

libglib2.0-0
libsm6
libxext6
libxrender1
libgl1
改完後要做什麼？
改完 GitHub 上的檔案後，到 Streamlit Cloud：

進入你的 App

點右上角 Manage app

點 Reboot app

或重新部署一次

如果還是錯
你現在的環境顯示是：

Python 3.14
有些套件，尤其是 opencv、ultralytics、torch，在太新的 Python 版本可能比較容易出問題。

可以在專案裡新增：

runtime.txt
內容放：

python-3.11
所以最後建議你的 GitHub 專案有這四個重要檔案：

video_app.py
requirements.txt
packages.txt
runtime.txt
其中 runtime.txt 內容是：

python-3.11
這樣會比 Python 3.14 穩定很多。


❱ 181 bootstrap()這個是怎樣

❱ 181 bootstrap() 不是你自己程式寫錯的地方。

它的意思是：Python 在執行這行時：

import cv2
進入了 OpenCV 套件內部的載入流程，然後跑到 OpenCV 自己的檔案：

/home/adminuser/venv/lib/python3.14/site-packages/cv2/__init__.py
第 181 行：

bootstrap()
bootstrap() 可以理解成 OpenCV 啟動自己、載入底層系統函式庫 的動作。

真正錯誤在最後這句：

ImportError: libgthread-2.0.so.0: cannot open shared object file
意思是：

OpenCV 想啟動，但系統裡缺少 libgthread-2.0.so.0 這個 Linux 函式庫，所以 cv2 載入失敗。

所以不是 bootstrap() 要改，也不是 video_app.py 第 181 行要改。

你真正要改的是部署檔案：

1. requirements.txt
把：

opencv-python
改成：

opencv-python-headless
2. 新增 packages.txt
內容放：

libglib2.0-0
libsm6
libxext6
libxrender1
libgl1
3. 建議新增 runtime.txt
內容放：

python-3.11
簡單講，錯誤流程是：

你的程式 import cv2
↓
OpenCV 執行 bootstrap()
↓
OpenCV 要找系統函式庫 libgthread-2.0.so.0
↓
系統找不到
↓
App 掛掉
所以 ❱ 181 bootstrap() 只是告訴你「錯誤發生在 OpenCV 載入階段」，不用去改它。


import cv2為什麼不行

已思考 2 秒鐘
import cv2 不行，不是因為你程式語法錯，而是因為 OpenCV 這個套件在啟動時，需要一些 Linux 系統函式庫，但 Streamlit Cloud 的環境裡缺少它們。

你的程式一開始有這行：

import cv2
這行會載入 OpenCV。你的程式後面也確實有用到 cv2.rectangle()、cv2.putText() 來在即時影像上畫框和文字，所以它不是多餘的套件。


錯誤訊息真正的重點是這句：

ImportError: libgthread-2.0.so.0: cannot open shared object file
意思是：

cv2 要啟動
↓
需要 libgthread-2.0.so.0
↓
Streamlit Cloud 找不到這個系統檔案
↓
所以 import cv2 失敗
你可以把它想成：

你有安裝 OpenCV 這個 Python 套件，但它背後需要的「系統零件」沒有裝好。

最直接的解法是新增或修改這兩個檔案。

requirements.txt
請放：

streamlit
ultralytics
opencv-python-headless
numpy<2
Pillow
torch
torchvision
streamlit-webrtc
streamlit-autorefresh
av
重點是用：

opencv-python-headless
不要用：

opencv-python
packages.txt
在 GitHub 專案新增一個檔案叫：

packages.txt
內容放：

libglib2.0-0
libsm6
libxext6
libxrender1
libgl1
其中 libglib2.0-0 就是用來補你現在缺少的 libgthread-2.0.so.0。

另外你現在環境是 Python 3.14，對 torch、ultralytics、opencv 這類套件比較容易不穩。建議再新增：

runtime.txt
python-3.11
改完後，到 Streamlit Cloud 重新部署或 Reboot app。這樣 import cv2 通常就可以正常了。


我現在改用hugging face

已思考一秒鐘
可以，改用 Hugging Face Spaces 也可以跑 Streamlit，而且有時候比 Streamlit Cloud 更適合部署需要 opencv / ultralytics / torch 的專案。

你現在的錯誤本質還是一樣：import cv2 需要系統套件。
在 Hugging Face 上，建議這樣放檔案：

你的專案檔案結構
video_app.py
requirements.txt
packages.txt
alarm.mp3
如果 Hugging Face 的 Streamlit 入口需要固定叫 app.py，建議你直接把：

video_app.py
改名成：

app.py
requirements.txt 建議內容
streamlit
ultralytics
opencv-python-headless
numpy<2
Pillow
torch
torchvision
streamlit-webrtc
streamlit-autorefresh
av
重點一樣是：

opencv-python-headless
不要用：

opencv-python
packages.txt 建議內容
libglib2.0-0
libsm6
libxext6
libxrender1
libgl1
ffmpeg
這裡的 libglib2.0-0 就是解決：

libgthread-2.0.so.0: cannot open shared object file
Hugging Face Spaces 設定
建立 Space 時：

SDK 選 Streamlit
然後檔案名稱最好是：

app.py
不要叫 video_app.py，不然 Hugging Face 可能找不到主程式。

你現在最需要改的地方
你原本程式不用大改，主要改部署檔案：

1. 把 video_app.py 改名成 app.py
2. requirements.txt 改成：
streamlit
ultralytics
opencv-python-headless
numpy<2
Pillow
torch
torchvision
streamlit-webrtc
streamlit-autorefresh
av
3. 新增 packages.txt
libglib2.0-0
libsm6
libxext6
libxrender1
libgl1
ffmpeg
如果改完後還出現 cv2 錯誤，通常是 Hugging Face 還沒重新 build。
你可以到 Space 裡面按：

Settings → Restart this Space
或重新 commit 一次檔案，讓它重新安裝環境。



video_app.py
Python
可以把這段改成可以在hugging face spaces上面跑的程式碼

我會把它改成 Hugging Face Spaces 比較穩的版本：主程式改成 app.py，保留即時鏡頭、YOLO 姿勢偵測、警報秒數與聲音提醒，並補上部署需要的 requirements.txt / packages.txt。

已思考 43s
可以，我幫你改成 Hugging Face Spaces 可直接使用的版本。你原本的程式有用到 cv2、YOLO、streamlit-webrtc 做即時鏡頭與姿勢偵測，所以我保留這些功能，並把主程式改成 Hugging Face Spaces 常用的 app.py。


你可以直接下載這三個檔案放到 Hugging Face Space：

app.py

requirements.txt

packages.txt

另外我也附一個簡單說明檔：

README.md

你在 Hugging Face Spaces 要放的檔案
app.py
requirements.txt
packages.txt
alarm.mp3
alarm.mp3 可以先不放，程式還是能跑，只是觸發警報時不會有聲音。

requirements.txt 內容
streamlit
streamlit-webrtc
streamlit-autorefresh
ultralytics
opencv-python-headless
numpy<2
Pillow
torch
torchvision
av
重點是這個：

opencv-python-headless
不要用：

opencv-python
packages.txt 內容
libglib2.0-0
libsm6
libxext6
libxrender1
libgl1
ffmpeg
這個可以解決你前面遇到的：

libgthread-2.0.so.0: cannot open shared object file
我主要幫你改了這些地方
把主程式改成 Hugging Face Spaces 常用的 app.py

補上 import streamlit.components.v1 as components

把 st.components.v1.html() 改成比較穩定的 components.html()

讓 PoseVideoProcessor 繼承 VideoProcessorBase

修正 YOLO keypoints 座標轉換，避免 tensor 直接進 math.sqrt() 出錯

影片畫面上的文字改成英文，避免 cv2.putText() 顯示中文變亂碼

保留右側中文摘要、Start / Stop、秒數警報、警報確認按鈕

上傳到 Hugging Face Spaces 時
建立 Space 時選：

SDK: Streamlit
然後把檔案上傳上去。主程式檔名一定要叫：

app.py
不是 video_app.py。


app.py

直接生成完整的程式碼

已思考 2 秒鐘
下面這份可以直接存成 app.py 放到 Hugging Face Spaces。
Space 設定請選 Streamlit。

import streamlit as st
import streamlit.components.v1 as components

import cv2
import math
import av
import time
import threading
import base64
from pathlib import Path

from ultralytics import YOLO
from streamlit_webrtc import (
    webrtc_streamer,
    WebRtcMode,
    VideoProcessorBase,
)
from streamlit_autorefresh import st_autorefresh


# =========================
# Page config
# =========================
st.set_page_config(
    page_title="長照睡姿固定過久警報系統",
    page_icon="🛌",
    layout="wide"
)


# =========================
# Custom style
# =========================
st.markdown(
    """
<style>
.main-title {
    font-size: 2.2rem;
    font-weight: 700;
    color: #1f3c88;
    margin-bottom: 0.2rem;
}

.sub-text {
    color: #5f6b7a;
    font-size: 1rem;
    margin-bottom: 1.2rem;
}

.metric-card {
    background-color: #f8fbff;
    border: 1px solid #dfe8f3;
    border-radius: 14px;
    padding: 16px 20px;
    text-align: center;
}

.metric-label {
    font-size: 0.95rem;
    color: #6b7280;
}

.metric-value {
    font-size: 1.8rem;
    font-weight: 700;
    color: #1f3c88;
}

.alert-box {
    background-color: #fff1f2;
    border: 1px solid #fda4af;
    color: #b91c1c;
    border-radius: 12px;
    padding: 16px;
    font-size: 1.05rem;
    font-weight: 600;
}

.normal-box {
    background-color: #f0fdf4;
    border: 1px solid #86efac;
    color: #166534;
    border-radius: 12px;
    padding: 16px;
    font-size: 1.05rem;
    font-weight: 600;
}
</style>
""",
    unsafe_allow_html=True,
)


# =========================
# Title
# =========================
st.markdown(
    '<div class="main-title">🛌 長照睡姿固定過久警報系統</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="sub-text">使用影像分析臥床姿勢變化，協助照護員及早發現長時間未翻身狀況。</div>',
    unsafe_allow_html=True,
)


# =========================
# Load YOLO model
# =========================
@st.cache_resource
def load_model():
    return YOLO("yolov8n-pose.pt")


model = load_model()


# =========================
# Shared state
# =========================
class AppState:
    def __init__(self):
        self.lock = threading.Lock()

        self.current_posture = "無人躺著"
        self.last_posture = "無人躺著"

        self.start_time = time.time()
        self.duration = 0.0

        self.alarm = False
        self.alarm_acknowledged = False

        self.monitoring = False


if "shared_state" not in st.session_state:
    st.session_state.shared_state = AppState()

shared_state = st.session_state.shared_state

if "sound_enabled" not in st.session_state:
    st.session_state.sound_enabled = False


# =========================
# Helper functions
# =========================
def to_xy(point):
    """
    將 YOLO keypoint tensor 轉成一般 float tuple。
    Hugging Face / PyTorch 環境中，如果直接拿 tensor 算 math.sqrt，
    有時候會出錯，所以這裡先轉換。
    """
    return float(point[0]), float(point[1])


def dist(p1, p2):
    x1, y1 = to_xy(p1)
    x2, y2 = to_xy(p2)

    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# =========================
# 姿勢分類
# =========================
def classify_posture(results):
    current_posture = "無人躺著"

    if results is None or len(results) == 0:
        return current_posture

    result = results[0]

    if result.keypoints is None:
        return current_posture

    if result.keypoints.xy is None or len(result.keypoints.xy) == 0:
        return current_posture

    if result.keypoints.conf is None or len(result.keypoints.conf) == 0:
        return current_posture

    kps = result.keypoints.xy[0]
    conf = result.keypoints.conf[0]

    if len(kps) < 13:
        return current_posture

    if float(conf.max()) <= 0.5:
        return current_posture

    shoulder_width = dist(kps[5], kps[6])

    torso_length = (
        dist(kps[5], kps[11]) +
        dist(kps[6], kps[12])
    ) / 2

    left_shoulder_conf = float(conf[5])
    right_shoulder_conf = float(conf[6])

    is_side = (
        left_shoulder_conf < 0.4
        or right_shoulder_conf < 0.4
        or (
            torso_length > 0
            and (shoulder_width / torso_length) < 0.5
        )
    )

    if is_side:
        left_ear_conf = float(conf[3])
        right_ear_conf = float(conf[4])

        # 用耳朵與肩膀可見度粗略判斷左右側躺
        if (right_ear_conf + right_shoulder_conf) > (
            left_ear_conf + left_shoulder_conf
        ) + 0.2:
            current_posture = "左側躺"

        elif (left_ear_conf + left_shoulder_conf) > (
            right_ear_conf + right_shoulder_conf
        ) + 0.2:
            current_posture = "右側躺"

        else:
            # 若信心值差不多，用鼻子到左右耳距離輔助判斷
            if dist(kps[0], kps[3]) < dist(kps[0], kps[4]):
                current_posture = "右側躺"
            else:
                current_posture = "左側躺"

    else:
        current_posture = "仰躺"

    return current_posture


# =========================
# Alarm sound
# =========================
def render_loop_alarm():
    if not st.session_state.sound_enabled:
        st.warning("🔇 請先按左側『啟用警報聲』")
        return

    audio_file = Path("alarm.mp3")

    if not audio_file.exists():
        st.warning("⚠️ 找不到 alarm.mp3，請將音檔上傳到 Hugging Face Space。")
        return

    audio_bytes = audio_file.read_bytes()
    b64 = base64.b64encode(audio_bytes).decode()

    audio_html = f"""
    <audio autoplay loop>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    """

    components.html(audio_html, height=0)


# =========================
# Sidebar
# =========================
st.sidebar.header("⚙️ 分析設定")

alarm_threshold = st.sidebar.slider(
    "同姿勢維持幾秒觸發警報",
    min_value=3,
    max_value=60,
    value=10,
    step=1,
)

if st.sidebar.button("🔊 啟用警報聲"):
    st.session_state.sound_enabled = True
    st.sidebar.success("警報聲已啟用")

st.sidebar.markdown("---")

if st.sidebar.button("▶️ Start"):
    with shared_state.lock:
        shared_state.monitoring = True
        shared_state.start_time = time.time()
        shared_state.duration = 0.0
        shared_state.alarm = False
        shared_state.alarm_acknowledged = False
        shared_state.last_posture = shared_state.current_posture

if st.sidebar.button("⏹ Stop"):
    with shared_state.lock:
        shared_state.monitoring = False
        shared_state.duration = 0.0
        shared_state.alarm = False
        shared_state.alarm_acknowledged = False
        shared_state.current_posture = "無人躺著"
        shared_state.last_posture = "無人躺著"

st.sidebar.markdown("---")

st.sidebar.info("按下 Start 後開始監測；Stop 會停止並重新計算。")

st.sidebar.markdown("---")

st.sidebar.caption(
    "提醒：Hugging Face Spaces 使用即時鏡頭時，瀏覽器通常需要允許相機權限。"
)


# 每秒刷新右側資訊
st_autorefresh(interval=1000, key="refresh")


# =========================
# Video Processor
# =========================
class PoseVideoProcessor(VideoProcessorBase):
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")

        try:
            results = model(img, verbose=False)
            current_posture = classify_posture(results)
            annotated = results[0].plot()

        except Exception as e:
            annotated = img.copy()
            current_posture = "偵測錯誤"

            cv2.putText(
                annotated,
                f"Detection error: {str(e)[:80]}",
                (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 0, 255),
                2,
                cv2.LINE_AA,
            )

        now = time.time()

        with shared_state.lock:
            if shared_state.monitoring:
                if current_posture == shared_state.last_posture:
                    shared_state.duration = now - shared_state.start_time

                else:
                    shared_state.last_posture = current_posture
                    shared_state.current_posture = current_posture
                    shared_state.start_time = now
                    shared_state.duration = 0.0
                    shared_state.alarm = False
                    shared_state.alarm_acknowledged = False

                if (
                    shared_state.duration >= alarm_threshold
                    and current_posture != "無人躺著"
                    and current_posture != "偵測錯誤"
                    and not shared_state.alarm_acknowledged
                ):
                    shared_state.alarm = True

                else:
                    if (
                        current_posture == "無人躺著"
                        or current_posture == "偵測錯誤"
                        or shared_state.alarm_acknowledged
                    ):
                        shared_state.alarm = False

                shared_state.current_posture = current_posture

            else:
                shared_state.duration = 0.0
                shared_state.alarm = False
                shared_state.current_posture = current_posture

            monitor_text = "Monitoring" if shared_state.monitoring else "Stopped"

            # OpenCV 不支援直接顯示中文，所以影片畫面上用英文
            posture_map = {
                "無人躺著": "No person",
                "左側躺": "Left side",
                "右側躺": "Right side",
                "仰躺": "Supine",
                "偵測錯誤": "Error",
            }

            posture_en = posture_map.get(shared_state.current_posture, "Unknown")

            info_text = (
                f"{monitor_text} | "
                f"Posture: {posture_en} | "
                f"Time: {int(shared_state.duration)} sec"
            )

            cv2.rectangle(
                annotated,
                (20, 20),
                (900, 70),
                (0, 0, 0),
                -1,
            )

            cv2.putText(
                annotated,
                info_text,
                (30, 55),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                (255, 255, 255),
                2,
                cv2.LINE_AA,
            )

            if shared_state.alarm:
                cv2.rectangle(
                    annotated,
                    (0, 0),
                    (annotated.shape[1], annotated.shape[0]),
                    (0, 0, 255),
                    10,
                )

                cv2.putText(
                    annotated,
                    "ALARM",
                    (30, 115),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.7,
                    (0, 0, 255),
                    4,
                    cv2.LINE_AA,
                )

        return av.VideoFrame.from_ndarray(
            annotated,
            format="bgr24",
        )


# =========================
# Layout
# =========================
left_col, right_col = st.columns([1.15, 1.4])


# =========================
# Webcam
# =========================
with left_col:
    st.subheader("1. 即時影像監測")

    st.info(
        "請按下方 START，並允許瀏覽器開啟相機。若手機無法開啟，建議先用電腦瀏覽器測試。"
    )

    webrtc_streamer(
        key="pose-monitor",
        mode=WebRtcMode.SENDRECV,
        rtc_configuration={
            "iceServers": [
                {"urls": ["stun:stun.l.google.com:19302"]}
            ]
        },
        media_stream_constraints={
            "video": True,
            "audio": False,
        },
        video_processor_factory=PoseVideoProcessor,
        async_processing=True,
    )


# =========================
# Right Panel
# =========================
with right_col:
    st.subheader("2. 摘要資訊")

    with shared_state.lock:
        posture_now = shared_state.current_posture
        duration_now = int(shared_state.duration)
        alarm_now = shared_state.alarm
        monitoring_now = shared_state.monitoring

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-label">目前姿勢</div>
                <div class="metric-value">{posture_now}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-label">持續時間</div>
                <div class="metric-value">{duration_now} 秒</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c3:
        system_text = "監測中" if monitoring_now else "停止"

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-label">系統狀態</div>
                <div class="metric-value">{system_text}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader("3. 警報摘要")

    if alarm_now:
        st.markdown(
            f"""
            <div class="alert-box">
                🚨 偵測到姿勢持續超過 {alarm_threshold} 秒，
                請協助翻身。
            </div>
            """,
            unsafe_allow_html=True,
        )

        render_loop_alarm()

        if st.button("✅ 確認此資訊", type="primary"):
            with shared_state.lock:
                shared_state.alarm_acknowledged = True
                shared_state.alarm = False

            st.rerun()

    else:
        st.markdown(
            """
            <div class="normal-box">
                ✅ 目前尚未觸發警報
            </div>
            """,
            unsafe_allow_html=True,
        )
你還要另外放這兩個檔案。

requirements.txt

streamlit
streamlit-webrtc
streamlit-autorefresh
ultralytics
opencv-python-headless
numpy<2
Pillow
torch
torchvision
av
packages.txt

libglib2.0-0
libsm6
libxext6
libxrender1
libgl1
ffmpeg
檔案結構要像這樣：

app.py
requirements.txt
packages.txt
alarm.mp3
alarm.mp3 沒放也可以跑，只是警報聲不會播放。


TypeError: webrtc_streamer() got an unexpected keyword argument 'send_back_video'
Traceback:
File "/app/app.py", line 149, in <module>
    webrtc_streamer(

已思考幾秒鐘
這個錯誤代表：

send_back_video
這個參數在你目前 Hugging Face 安裝的 streamlit-webrtc 版本中 不支援。

所以你要做的事情很簡單：
把 webrtc_streamer() 裡面的這行刪掉：

send_back_video=True
或如果你有：

send_back_video=False
也一樣刪掉。

請把你的 webrtc_streamer() 改成這樣：

webrtc_streamer(
    key="pose-monitor",
    mode=WebRtcMode.SENDRECV,
    rtc_configuration={
        "iceServers": [
            {"urls": ["stun:stun.l.google.com:19302"]}
        ]
    },
    media_stream_constraints={
        "video": True,
        "audio": False,
    },
    video_processor_factory=PoseVideoProcessor,
    async_processing=True,
)
也就是不要寫成這樣：

webrtc_streamer(
    key="pose-monitor",
    mode=WebRtcMode.SENDRECV,
    video_processor_factory=PoseVideoProcessor,
    send_back_video=True,   # 這行會錯
    async_processing=True,
)
如果你想讓版本更穩，可以把 requirements.txt 裡的 streamlit-webrtc 固定版本：

streamlit-webrtc==0.47.9
所以 requirements.txt 可以改成：

streamlit
streamlit-webrtc==0.47.9
streamlit-autorefresh
ultralytics
opencv-python-headless
numpy<2
Pillow
torch
torchvision
av
改完後，Hugging Face Spaces 重新 Restart / Rebuild。


可以生成完整修改過的app.py嗎

已思考 2 秒鐘
可以，下面是已移除 send_back_video、適合 Hugging Face Spaces 使用的完整 app.py。

請直接把 Hugging Face Spaces 裡的 app.py 全部替換成這份。

import streamlit as st
import streamlit.components.v1 as components

import cv2
import math
import av
import time
import threading
import base64
from pathlib import Path

from ultralytics import YOLO
from streamlit_webrtc import (
    webrtc_streamer,
    WebRtcMode,
    VideoProcessorBase,
)
from streamlit_autorefresh import st_autorefresh


# =========================
# Page config
# =========================
st.set_page_config(
    page_title="長照睡姿固定過久警報系統",
    page_icon="🛌",
    layout="wide"
)


# =========================
# Custom style
# =========================
st.markdown(
    """
<style>
.main-title {
    font-size: 2.2rem;
    font-weight: 700;
    color: #1f3c88;
    margin-bottom: 0.2rem;
}

.sub-text {
    color: #5f6b7a;
    font-size: 1rem;
    margin-bottom: 1.2rem;
}

.metric-card {
    background-color: #f8fbff;
    border: 1px solid #dfe8f3;
    border-radius: 14px;
    padding: 16px 20px;
    text-align: center;
}

.metric-label {
    font-size: 0.95rem;
    color: #6b7280;
}

.metric-value {
    font-size: 1.8rem;
    font-weight: 700;
    color: #1f3c88;
}

.alert-box {
    background-color: #fff1f2;
    border: 1px solid #fda4af;
    color: #b91c1c;
    border-radius: 12px;
    padding: 16px;
    font-size: 1.05rem;
    font-weight: 600;
}

.normal-box {
    background-color: #f0fdf4;
    border: 1px solid #86efac;
    color: #166534;
    border-radius: 12px;
    padding: 16px;
    font-size: 1.05rem;
    font-weight: 600;
}
</style>
""",
    unsafe_allow_html=True,
)


# =========================
# Title
# =========================
st.markdown(
    '<div class="main-title">🛌 長照睡姿固定過久警報系統</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="sub-text">使用影像分析臥床姿勢變化，協助照護員及早發現長時間未翻身狀況。</div>',
    unsafe_allow_html=True,
)


# =========================
# Load YOLO model
# =========================
@st.cache_resource
def load_model():
    return YOLO("yolov8n-pose.pt")


model = load_model()


# =========================
# Shared state
# =========================
class AppState:
    def __init__(self):
        self.lock = threading.Lock()

        self.current_posture = "無人躺著"
        self.last_posture = "無人躺著"

        self.start_time = time.time()
        self.duration = 0.0

        self.alarm = False
        self.alarm_acknowledged = False

        self.monitoring = False


if "shared_state" not in st.session_state:
    st.session_state.shared_state = AppState()

shared_state = st.session_state.shared_state

if "sound_enabled" not in st.session_state:
    st.session_state.sound_enabled = False


# =========================
# Helper functions
# =========================
def to_xy(point):
    """
    將 YOLO keypoint tensor 轉成 float。
    避免 tensor 直接丟進 math.sqrt() 造成錯誤。
    """
    return float(point[0]), float(point[1])


def dist(p1, p2):
    x1, y1 = to_xy(p1)
    x2, y2 = to_xy(p2)

    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# =========================
# 姿勢分類
# =========================
def classify_posture(results):
    current_posture = "無人躺著"

    if results is None or len(results) == 0:
        return current_posture

    result = results[0]

    if result.keypoints is None:
        return current_posture

    if result.keypoints.xy is None or len(result.keypoints.xy) == 0:
        return current_posture

    if result.keypoints.conf is None or len(result.keypoints.conf) == 0:
        return current_posture

    kps = result.keypoints.xy[0]
    conf = result.keypoints.conf[0]

    if len(kps) < 13:
        return current_posture

    if float(conf.max()) <= 0.5:
        return current_posture

    shoulder_width = dist(kps[5], kps[6])

    torso_length = (
        dist(kps[5], kps[11])
        + dist(kps[6], kps[12])
    ) / 2

    left_shoulder_conf = float(conf[5])
    right_shoulder_conf = float(conf[6])

    is_side = (
        left_shoulder_conf < 0.4
        or right_shoulder_conf < 0.4
        or (
            torso_length > 0
            and (shoulder_width / torso_length) < 0.5
        )
    )

    if is_side:
        left_ear_conf = float(conf[3])
        right_ear_conf = float(conf[4])

        if (right_ear_conf + right_shoulder_conf) > (
            left_ear_conf + left_shoulder_conf
        ) + 0.2:
            current_posture = "左側躺"

        elif (left_ear_conf + left_shoulder_conf) > (
            right_ear_conf + right_shoulder_conf
        ) + 0.2:
            current_posture = "右側躺"

        else:
            if dist(kps[0], kps[3]) < dist(kps[0], kps[4]):
                current_posture = "右側躺"
            else:
                current_posture = "左側躺"

    else:
        current_posture = "仰躺"

    return current_posture


# =========================
# Alarm sound
# =========================
def render_loop_alarm():
    if not st.session_state.sound_enabled:
        st.warning("🔇 請先按左側『啟用警報聲』")
        return

    audio_file = Path("alarm.mp3")

    if not audio_file.exists():
        st.warning("⚠️ 找不到 alarm.mp3，請將音檔上傳到 Hugging Face Space。")
        return

    audio_bytes = audio_file.read_bytes()
    b64 = base64.b64encode(audio_bytes).decode()

    audio_html = f"""
    <audio autoplay loop>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    """

    components.html(audio_html, height=0)


# =========================
# Sidebar
# =========================
st.sidebar.header("⚙️ 分析設定")

alarm_threshold = st.sidebar.slider(
    "同姿勢維持幾秒觸發警報",
    min_value=3,
    max_value=60,
    value=10,
    step=1,
)

if st.sidebar.button("🔊 啟用警報聲"):
    st.session_state.sound_enabled = True
    st.sidebar.success("警報聲已啟用")

st.sidebar.markdown("---")

if st.sidebar.button("▶️ Start"):
    with shared_state.lock:
        shared_state.monitoring = True
        shared_state.start_time = time.time()
        shared_state.duration = 0.0
        shared_state.alarm = False
        shared_state.alarm_acknowledged = False
        shared_state.last_posture = shared_state.current_posture

if st.sidebar.button("⏹ Stop"):
    with shared_state.lock:
        shared_state.monitoring = False
        shared_state.duration = 0.0
        shared_state.alarm = False
        shared_state.alarm_acknowledged = False
        shared_state.current_posture = "無人躺著"
        shared_state.last_posture = "無人躺著"

st.sidebar.markdown("---")

st.sidebar.info("按下 Start 後開始監測；Stop 會停止並重新計算。")

st.sidebar.markdown("---")

st.sidebar.caption(
    "提醒：Hugging Face Spaces 使用即時鏡頭時，瀏覽器需要允許相機權限。"
)


# 每秒刷新右側資訊
st_autorefresh(interval=1000, key="refresh")


# =========================
# Video Processor
# =========================
class PoseVideoProcessor(VideoProcessorBase):
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")

        try:
            results = model(img, verbose=False)
            current_posture = classify_posture(results)
            annotated = results[0].plot()

        except Exception as e:
            annotated = img.copy()
            current_posture = "偵測錯誤"

            cv2.putText(
                annotated,
                f"Detection error: {str(e)[:80]}",
                (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 0, 255),
                2,
                cv2.LINE_AA,
            )

        now = time.time()

        with shared_state.lock:
            if shared_state.monitoring:
                if current_posture == shared_state.last_posture:
                    shared_state.duration = now - shared_state.start_time

                else:
                    shared_state.last_posture = current_posture
                    shared_state.current_posture = current_posture
                    shared_state.start_time = now
                    shared_state.duration = 0.0
                    shared_state.alarm = False
                    shared_state.alarm_acknowledged = False

                if (
                    shared_state.duration >= alarm_threshold
                    and current_posture != "無人躺著"
                    and current_posture != "偵測錯誤"
                    and not shared_state.alarm_acknowledged
                ):
                    shared_state.alarm = True

                else:
                    if (
                        current_posture == "無人躺著"
                        or current_posture == "偵測錯誤"
                        or shared_state.alarm_acknowledged
                    ):
                        shared_state.alarm = False

                shared_state.current_posture = current_posture

            else:
                shared_state.duration = 0.0
                shared_state.alarm = False
                shared_state.current_posture = current_posture

            monitor_text = "Monitoring" if shared_state.monitoring else "Stopped"

            posture_map = {
                "無人躺著": "No person",
                "左側躺": "Left side",
                "右側躺": "Right side",
                "仰躺": "Supine",
                "偵測錯誤": "Error",
            }

            posture_en = posture_map.get(shared_state.current_posture, "Unknown")

            info_text = (
                f"{monitor_text} | "
                f"Posture: {posture_en} | "
                f"Time: {int(shared_state.duration)} sec"
            )

            cv2.rectangle(
                annotated,
                (20, 20),
                (900, 70),
                (0, 0, 0),
                -1,
            )

            cv2.putText(
                annotated,
                info_text,
                (30, 55),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                (255, 255, 255),
                2,
                cv2.LINE_AA,
            )

            if shared_state.alarm:
                cv2.rectangle(
                    annotated,
                    (0, 0),
                    (annotated.shape[1], annotated.shape[0]),
                    (0, 0, 255),
                    10,
                )

                cv2.putText(
                    annotated,
                    "ALARM",
                    (30, 115),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.7,
                    (0, 0, 255),
                    4,
                    cv2.LINE_AA,
                )

        return av.VideoFrame.from_ndarray(
            annotated,
            format="bgr24",
        )


# =========================
# Layout
# =========================
left_col, right_col = st.columns([1.15, 1.4])


# =========================
# Webcam
# =========================
with left_col:
    st.subheader("1. 即時影像監測")

    st.info(
        "請按下方 START，並允許瀏覽器開啟相機。若手機無法開啟，建議先用電腦瀏覽器測試。"
    )

    webrtc_streamer(
        key="pose-monitor",
        mode=WebRtcMode.SENDRECV,
        rtc_configuration={
            "iceServers": [
                {"urls": ["stun:stun.l.google.com:19302"]}
            ]
        },
        media_stream_constraints={
            "video": True,
            "audio": False,
        },
        video_processor_factory=PoseVideoProcessor,
        async_processing=True,
    )


# =========================
# Right Panel
# =========================
with right_col:
    st.subheader("2. 摘要資訊")

    with shared_state.lock:
        posture_now = shared_state.current_posture
        duration_now = int(shared_state.duration)
        alarm_now = shared_state.alarm
        monitoring_now = shared_state.monitoring

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-label">目前姿勢</div>
                <div class="metric-value">{posture_now}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-label">持續時間</div>
                <div class="metric-value">{duration_now} 秒</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c3:
        system_text = "監測中" if monitoring_now else "停止"

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-label">系統狀態</div>
                <div class="metric-value">{system_text}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader("3. 警報摘要")

    if alarm_now:
        st.markdown(
            f"""
            <div class="alert-box">
                🚨 偵測到姿勢持續超過 {alarm_threshold} 秒，
                請協助翻身。
            </div>
            """,
            unsafe_allow_html=True,
        )

        render_loop_alarm()

        if st.button("✅ 確認此資訊", type="primary"):
            with shared_state.lock:
                shared_state.alarm_acknowledged = True
                shared_state.alarm = False

            st.rerun()

    else:
        st.markdown(
            """
            <div class="normal-box">
                ✅ 目前尚未觸發警報
            </div>
            """,
            unsafe_allow_html=True,
        )
同時請確認你的 requirements.txt 是這樣：

streamlit
streamlit-webrtc==0.47.9
streamlit-autorefresh
ultralytics
opencv-python-headless
numpy<2
Pillow
torch
torchvision
av
packages.txt 是這樣：

libglib2.0-0
libsm6
libxext6
libxrender1
libgl1
ffmpeg
這份 app.py 裡面已經沒有 send_back_video，所以不會再出現：

TypeError: webrtc_streamer() got an unexpected keyword argument 'send_back_video'

runtime error
Exit code: 2. Reason: Usage: streamlit run [OPTIONS] [TARGET] [ARGS]...
Try 'streamlit run --help' for help.

Error: Invalid value: File does not exist: app.py
Container logs:

===== Application Startup at 2026-05-07 18:47:25 =====

Usage: streamlit run [OPTIONS] [TARGET] [ARGS]...
Try 'streamlit run --help' for help.

Error: Invalid value: File does not exist: app.py
Usage: streamlit run [OPTIONS] [TARGET] [ARGS]...
Try 'streamlit run --help' for help.

Error: Invalid value: File does not exist: app.py

已思考 2 秒鐘
這個錯誤不是程式碼內容錯，而是 Hugging Face Spaces 找不到你的主程式檔案：

Error: Invalid value: File does not exist: app.py
意思是它啟動時執行：

streamlit run app.py
可是你的 Space 裡面沒有叫做：

app.py
你現在要檢查的地方
請到 Hugging Face Space 的 Files 看看你的檔案名稱是不是還叫：

video_app.py
如果是，請把它改名成：

app.py
Hugging Face Spaces 的 Streamlit 預設會找 app.py，所以檔名一定要對。

正確檔案結構
你的 Space 裡應該要長這樣：

app.py
requirements.txt
packages.txt
alarm.mp3
其中最重要的是：

app.py
不能是：

video_app.py
也不能是：

app.py.txt
常見錯誤
錯誤 1：檔名其實是 app.py.txt
有時候用記事本建立檔案，可能看起來叫 app.py，但實際上是：

app.py.txt
這樣 Hugging Face 也會找不到。

請確認檔名真的就是：

app.py
錯誤 2：檔案放在資料夾裡
如果你放成這樣：

fff0508/app.py
requirements.txt
packages.txt
Hugging Face 也可能找不到，因為它會在最外層找 app.py。

請改成：

app.py
requirements.txt
packages.txt
錯誤 3：Space 設定的啟動檔案還是錯的
到 Hugging Face Spaces：

Settings → App file
確認 App file 是：

app.py
如果你想保留檔名 video_app.py，那 App file 就要改成：

video_app.py
但我建議你直接改名成 app.py，最不容易出錯。

你現在最簡單的修法
把 Hugging Face 上原本的：

video_app.py
改名成：

app.py
然後重新 Restart Space。

如果你的 Files 裡已經有完整程式碼，但檔名不是 app.py，只要改檔名就好，不需要重寫程式。


Connection is taking longer than expected. Check your network or ask the developer for STUN/TURN settings if the problem persists.

已思考 2 秒鐘
這個錯誤不是 Python 語法錯，而是 WebRTC 即時鏡頭連線沒有成功建立。

Connection is taking longer than expected.
Check your network or ask the developer for STUN/TURN settings...
意思是：
你的網頁想把「使用者手機/電腦鏡頭」傳到 Hugging Face Space，但 WebRTC 需要透過 STUN/TURN 伺服器 建立連線。現在它連線太久，所以卡住。

最常見原因
1. Hugging Face Spaces 不一定穩定支援即時 WebRTC
streamlit-webrtc 在本機通常比較穩，但部署到 Hugging Face Spaces 時，可能因為網路、防火牆、伺服器轉發問題，導致鏡頭連不上。

2. 只有 STUN，不一定夠
你現在大概是這樣：

rtc_configuration={
    "iceServers": [
        {"urls": ["stun:stun.l.google.com:19302"]}
    ]
}
這只用了 STUN。
但有些網路環境需要 TURN 才能連線成功。

STUN 像是「幫你找路」，TURN 像是「真的幫你轉送影像」。
如果網路比較嚴格，只靠 STUN 可能失敗。

可以先試的修法
把 webrtc_streamer() 裡面的 rtc_configuration 改成這樣：

rtc_configuration={
    "iceServers": [
        {"urls": ["stun:stun.l.google.com:19302"]},
        {"urls": ["stun:stun1.l.google.com:19302"]},
        {"urls": ["stun:stun2.l.google.com:19302"]},
        {"urls": ["stun:stun3.l.google.com:19302"]},
        {"urls": ["stun:stun4.l.google.com:19302"]},
    ]
}
完整片段是：

webrtc_streamer(
    key="pose-monitor",
    mode=WebRtcMode.SENDRECV,
    rtc_configuration={
        "iceServers": [
            {"urls": ["stun:stun.l.google.com:19302"]},
            {"urls": ["stun:stun1.l.google.com:19302"]},
            {"urls": ["stun:stun2.l.google.com:19302"]},
            {"urls": ["stun:stun3.l.google.com:19302"]},
            {"urls": ["stun:stun4.l.google.com:19302"]},
        ]
    },
    media_stream_constraints={
        "video": True,
        "audio": False,
    },
    video_processor_factory=PoseVideoProcessor,
    async_processing=True,
)
但如果還是不行
那就不是你的程式錯，而是 Hugging Face + WebRTC 即時鏡頭連線不穩。

這時候我建議你改成比較穩的版本：

改成「拍照上傳 / camera_input」版本
Hugging Face Spaces 上，這種方式通常比 WebRTC 穩很多：

img_file = st.camera_input("請拍攝病床畫面")

if img_file is not None:
    image = Image.open(img_file)
    img = np.array(image)

    results = model(img)
    annotated = results[0].plot()

    st.image(annotated, caption="偵測結果", channels="BGR")
這種方式不是即時連續影像，但優點是：

比較穩
比較容易部署成功
不需要 STUN / TURN
手機也比較容易開啟
比較適合期末專案展示
我的建議
如果你只是要做期末專案展示，我會建議：

Hugging Face Spaces：用上傳圖片 + camera_input 拍照偵測
本機電腦：再用 streamlit-webrtc 做即時影像版本
因為 WebRTC 在雲端部署很常卡連線，不一定是程式碼能完全解決。

你現在這個錯誤可以先改多個 STUN 試試看；如果還是卡住，就改成 st.camera_input() 版本會最穩。


完整程式碼

已思考 5s
下面這份是 Hugging Face Spaces 比較穩定的版本，改成：

上傳圖片 + 使用相機拍照偵測
不使用 streamlit-webrtc，所以不會再出現：

Connection is taking longer than expected
請直接把下面內容存成 app.py。

import streamlit as st
import streamlit.components.v1 as components

import cv2
import math
import time
import base64
from pathlib import Path

import numpy as np
from PIL import Image
from ultralytics import YOLO


# =========================
# Page config
# =========================
st.set_page_config(
    page_title="長照睡姿固定過久警報系統",
    page_icon="🛌",
    layout="wide"
)


# =========================
# Custom style
# =========================
st.markdown(
    """
<style>
.main-title {
    font-size: 2.2rem;
    font-weight: 700;
    color: #1f3c88;
    margin-bottom: 0.2rem;
}

.sub-text {
    color: #5f6b7a;
    font-size: 1rem;
    margin-bottom: 1.2rem;
}

.metric-card {
    background-color: #f8fbff;
    border: 1px solid #dfe8f3;
    border-radius: 14px;
    padding: 16px 20px;
    text-align: center;
}

.metric-label {
    font-size: 0.95rem;
    color: #6b7280;
}

.metric-value {
    font-size: 1.8rem;
    font-weight: 700;
    color: #1f3c88;
}

.alert-box {
    background-color: #fff1f2;
    border: 1px solid #fda4af;
    color: #b91c1c;
    border-radius: 12px;
    padding: 16px;
    font-size: 1.05rem;
    font-weight: 600;
}

.normal-box {
    background-color: #f0fdf4;
    border: 1px solid #86efac;
    color: #166534;
    border-radius: 12px;
    padding: 16px;
    font-size: 1.05rem;
    font-weight: 600;
}
</style>
""",
    unsafe_allow_html=True,
)


# =========================
# Title
# =========================
st.markdown(
    '<div class="main-title">🛌 長照睡姿固定過久警報系統</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="sub-text">使用影像分析臥床姿勢，協助照護員及早發現長時間未翻身狀況。</div>',
    unsafe_allow_html=True,
)


# =========================
# Load model
# =========================
@st.cache_resource
def load_model():
    return YOLO("yolov8n-pose.pt")


model = load_model()


# =========================
# Session state
# =========================
if "last_posture" not in st.session_state:
    st.session_state.last_posture = "尚未偵測"

if "current_posture" not in st.session_state:
    st.session_state.current_posture = "尚未偵測"

if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()

if "duration" not in st.session_state:
    st.session_state.duration = 0

if "alarm" not in st.session_state:
    st.session_state.alarm = False

if "alarm_acknowledged" not in st.session_state:
    st.session_state.alarm_acknowledged = False

if "sound_enabled" not in st.session_state:
    st.session_state.sound_enabled = False

if "monitoring" not in st.session_state:
    st.session_state.monitoring = False


# =========================
# Helper functions
# =========================
def to_xy(point):
    return float(point[0]), float(point[1])


def dist(p1, p2):
    x1, y1 = to_xy(p1)
    x2, y2 = to_xy(p2)

    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# =========================
# 姿勢分類
# =========================
def classify_posture(results):
    current_posture = "無人躺著"

    if results is None or len(results) == 0:
        return current_posture

    result = results[0]

    if result.keypoints is None:
        return current_posture

    if result.keypoints.xy is None or len(result.keypoints.xy) == 0:
        return current_posture

    if result.keypoints.conf is None or len(result.keypoints.conf) == 0:
        return current_posture

    kps = result.keypoints.xy[0]
    conf = result.keypoints.conf[0]

    if len(kps) < 13:
        return current_posture

    if float(conf.max()) <= 0.5:
        return current_posture

    shoulder_width = dist(kps[5], kps[6])

    torso_length = (
        dist(kps[5], kps[11])
        + dist(kps[6], kps[12])
    ) / 2

    left_shoulder_conf = float(conf[5])
    right_shoulder_conf = float(conf[6])

    is_side = (
        left_shoulder_conf < 0.4
        or right_shoulder_conf < 0.4
        or (
            torso_length > 0
            and (shoulder_width / torso_length) < 0.5
        )
    )

    if is_side:
        left_ear_conf = float(conf[3])
        right_ear_conf = float(conf[4])

        if (right_ear_conf + right_shoulder_conf) > (
            left_ear_conf + left_shoulder_conf
        ) + 0.2:
            current_posture = "左側躺"

        elif (left_ear_conf + left_shoulder_conf) > (
            right_ear_conf + right_shoulder_conf
        ) + 0.2:
            current_posture = "右側躺"

        else:
            if dist(kps[0], kps[3]) < dist(kps[0], kps[4]):
                current_posture = "右側躺"
            else:
                current_posture = "左側躺"

    else:
        current_posture = "仰躺"

    return current_posture


# =========================
# Alarm sound
# =========================
def render_loop_alarm():
    if not st.session_state.sound_enabled:
        st.warning("🔇 請先按左側『啟用警報聲』")
        return

    audio_file = Path("alarm.mp3")

    if not audio_file.exists():
        st.warning("⚠️ 找不到 alarm.mp3，請將音檔上傳到 Hugging Face Space。")
        return

    audio_bytes = audio_file.read_bytes()
    b64 = base64.b64encode(audio_bytes).decode()

    audio_html = f"""
    <audio autoplay loop>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    """

    components.html(audio_html, height=0)


# =========================
# 更新姿勢狀態
# =========================
def update_posture_state(current_posture, alarm_threshold):
    now = time.time()

    if not st.session_state.monitoring:
        st.session_state.current_posture = current_posture
        st.session_state.duration = 0
        st.session_state.alarm = False
        return

    if current_posture == st.session_state.last_posture:
        st.session_state.duration = int(now - st.session_state.start_time)

    else:
        st.session_state.last_posture = current_posture
        st.session_state.current_posture = current_posture
        st.session_state.start_time = now
        st.session_state.duration = 0
        st.session_state.alarm = False
        st.session_state.alarm_acknowledged = False

    st.session_state.current_posture = current_posture

    if (
        st.session_state.duration >= alarm_threshold
        and current_posture != "無人躺著"
        and not st.session_state.alarm_acknowledged
    ):
        st.session_state.alarm = True
    else:
        if current_posture == "無人躺著" or st.session_state.alarm_acknowledged:
            st.session_state.alarm = False


# =========================
# 偵測圖片
# =========================
def detect_image(image_pil, alarm_threshold):
    image_rgb = np.array(image_pil.convert("RGB"))

    results = model(image_rgb, verbose=False)

    current_posture = classify_posture(results)

    update_posture_state(current_posture, alarm_threshold)

    annotated = results[0].plot()

    annotated_rgb = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)

    return annotated_rgb, current_posture


# =========================
# Sidebar
# =========================
st.sidebar.header("⚙️ 分析設定")

alarm_threshold = st.sidebar.slider(
    "同姿勢維持幾秒觸發警報",
    min_value=3,
    max_value=60,
    value=10,
    step=1,
)

st.sidebar.markdown("---")

if st.sidebar.button("▶️ Start"):
    st.session_state.monitoring = True
    st.session_state.start_time = time.time()
    st.session_state.duration = 0
    st.session_state.alarm = False
    st.session_state.alarm_acknowledged = False
    st.session_state.last_posture = st.session_state.current_posture
    st.sidebar.success("已開始監測")

if st.sidebar.button("⏹ Stop"):
    st.session_state.monitoring = False
    st.session_state.duration = 0
    st.session_state.alarm = False
    st.session_state.alarm_acknowledged = False
    st.session_state.current_posture = "尚未偵測"
    st.session_state.last_posture = "尚未偵測"
    st.sidebar.warning("已停止監測")

st.sidebar.markdown("---")

if st.sidebar.button("🔊 啟用警報聲"):
    st.session_state.sound_enabled = True
    st.sidebar.success("警報聲已啟用")

st.sidebar.info(
    "這個版本使用拍照或上傳圖片偵測，適合 Hugging Face Spaces，較不容易出現 WebRTC 連線問題。"
)


# =========================
# Layout
# =========================
left_col, right_col = st.columns([1.15, 1.4])


# =========================
# Left Panel
# =========================
with left_col:
    st.subheader("1. 輸入影像")

    input_method = st.radio(
        "選擇影像來源",
        ["使用相機拍照", "上傳圖片"],
        horizontal=True,
    )

    image_file = None

    if input_method == "使用相機拍照":
        image_file = st.camera_input("請拍攝病床畫面")

    else:
        image_file = st.file_uploader(
            "請上傳病床影像",
            type=["jpg", "jpeg", "png"],
        )

    if image_file is not None:
        image_pil = Image.open(image_file)

        st.image(
            image_pil,
            caption="原始影像",
            use_container_width=True,
        )

        if st.button("開始分析這張影像", type="primary"):
            with st.spinner("正在分析姿勢..."):
                annotated_img, posture = detect_image(
                    image_pil,
                    alarm_threshold,
                )

            st.image(
                annotated_img,
                caption=f"偵測結果：{posture}",
                use_container_width=True,
            )

    else:
        st.info("請先拍照或上傳一張病床影像。")


# =========================
# Right Panel
# =========================
with right_col:
    st.subheader("2. 摘要資訊")

    posture_now = st.session_state.current_posture
    duration_now = int(st.session_state.duration)
    alarm_now = st.session_state.alarm
    monitoring_now = st.session_state.monitoring

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-label">目前姿勢</div>
                <div class="metric-value">{posture_now}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-label">持續時間</div>
                <div class="metric-value">{duration_now} 秒</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c3:
        system_text = "監測中" if monitoring_now else "停止"

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-label">系統狀態</div>
                <div class="metric-value">{system_text}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader("3. 警報摘要")

    if alarm_now:
        st.markdown(
            f"""
            <div class="alert-box">
                🚨 偵測到同一姿勢持續超過 {alarm_threshold} 秒，
                請協助病人翻身。
            </div>
            """,
            unsafe_allow_html=True,
        )

        render_loop_alarm()

        if st.button("✅ 確認此資訊", type="primary"):
            st.session_state.alarm_acknowledged = True
            st.session_state.alarm = False
            st.rerun()

    else:
        st.markdown(
            """
            <div class="normal-box">
                ✅ 目前尚未觸發警報
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")

    st.subheader("4. 使用說明")

    st.markdown(
        """
        1. 先按左側 **Start** 開始監測。  
        2. 使用相機拍照，或上傳病床圖片。  
        3. 按下 **開始分析這張影像**。  
        4. 系統會判斷目前姿勢，例如：仰躺、左側躺、右側躺。  
        5. 若同一姿勢超過設定秒數，就會出現警報提醒。  

        注意：這個版本不是連續即時影像，而是「拍照／上傳圖片後分析」，比較適合部署在 Hugging Face Spaces。
        """
    )
requirements.txt
請改成這樣，這個版本不需要 streamlit-webrtc：

streamlit
ultralytics
opencv-python-headless
numpy<2
Pillow
torch
torchvision
packages.txt
libglib2.0-0
libsm6
libxext6
libxrender1
libgl1
ffmpeg
Hugging Face Spaces 檔案結構
請確認 Files 裡面長這樣：

app.py
requirements.txt
packages.txt
alarm.mp3
alarm.mp3 可以不放，不會影響主要偵測功能，只是沒有警報聲。


RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0 libsm6 libxext6 libxrender-dev libgomp1 && rm -rf /var/lib/apt/lists/*
4s
Hit:1 http://deb.debian.org/debian trixie InRelease
Get:2 http://deb.debian.org/debian trixie-updates InRelease [47.3 kB]
Get:3 http://deb.debian.org/debian-security trixie-security InRelease [43.4 kB]
Get:4 http://deb.debian.org/debian trixie/main amd64 Packages [9671 kB]
Get:5 http://deb.debian.org/debian trixie-updates/main amd64 Packages [5412 B]
Get:6 http://deb.debian.org/debian-security trixie-security/main amd64 Packages [154 kB]
Fetched 9921 kB in 1s (7662 kB/s)
Reading package lists...
Reading package lists...
Package libgl1-mesa-glx is not available, but is referred to by another package.
This may mean that the package is missing, has been obsoleted, or
is only available from another source
E: Package 'libgl1-mesa-glx' has no installation candidate
Build Failed: build daemon returned an error < failed to solve: process "/bin/sh -c apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0 libsm6 libxext6 libxrender-dev libgomp1 && rm -rf /var/lib/apt/lists/*" did not complete successfully: exit code: 100 >

這個錯誤是因為 Hugging Face 現在用的是 Debian trixie，裡面已經沒有：

libgl1-mesa-glx
所以 build 失敗。

把它改成：

libgl1
就好。

如果你是用 packages.txt
請把 packages.txt 改成這樣：

libgl1
libglib2.0-0
libsm6
libxext6
libxrender1
libgomp1
ffmpeg
不要放：

libgl1-mesa-glx
如果你是用 Dockerfile
把原本這行：

RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0 libsm6 libxext6 libxrender-dev libgomp1 && rm -rf /var/lib/apt/lists/*
改成：

RUN apt-get update && apt-get install -y libgl1 libglib2.0-0 libsm6 libxext6 libxrender1 libgomp1 ffmpeg && rm -rf /var/lib/apt/lists/*
簡單說
錯的是這個套件名稱：

libgl1-mesa-glx
現在請改成：

libgl1
改完後重新 Build / Restart Space。


我現在用railway

可以，Railway 也能部署 Streamlit，但設定方式跟 Hugging Face 不一樣。重點會變成：啟動指令、Port 參數、系統套件、以及是否還要用即時鏡頭。

已思考 8s
可以，Railway 的設定跟 Hugging Face 不太一樣。你現在可以用 Railway + Streamlit + Nixpacks 部署，重點是新增 nixpacks.toml，並讓 Streamlit 使用 Railway 提供的 $PORT。Railway 的 Streamlit 範例也是用 Nixpacks 部署；Nixpacks 可以用 nixpacks.toml 自訂 build 設定，包含安裝 apt 套件。

你的 Railway 檔案結構
請讓 GitHub 專案最外層長這樣：

app.py
requirements.txt
nixpacks.toml
如果你要警報聲，再加：

alarm.mp3
1. app.py
你可以先沿用我上一版給你的 拍照 / 上傳圖片版本。
Railway 上也比較建議先用這版，因為 WebRTC 即時鏡頭在雲端平台常會卡 STUN/TURN 連線。

2. requirements.txt
Railway 用這份：

streamlit
ultralytics
opencv-python-headless
numpy<2
Pillow
torch
torchvision
不要放：

streamlit-webrtc
av
因為你現在建議先不用即時 WebRTC 版本。

3. nixpacks.toml
新增一個檔案叫：

nixpacks.toml
內容放這個：

[phases.setup]
aptPkgs = [
  "...",
  "libgl1",
  "libglib2.0-0",
  "libsm6",
  "libxext6",
  "libxrender1",
  "libgomp1",
  "ffmpeg"
]

[start]
cmd = "streamlit run app.py --server.address=0.0.0.0 --server.port=$PORT --server.headless=true"
這裡不要用 libgl1-mesa-glx，因為你前面遇到的 Debian trixie 環境已經沒有這個套件，改用 libgl1。

Railway 設定
在 Railway 專案中：

連接你的 GitHub repo

確認根目錄有 app.py

到 Settings / Deploy 檢查 Start Command
如果 Railway 有讓你填 Start Command，可以填：

streamlit run app.py --server.address=0.0.0.0 --server.port=$PORT --server.headless=true
Streamlit 在雲端部署時要綁到 0.0.0.0，不然外部可能連不到；雲端平台也通常會透過環境變數 PORT 指定服務要監聽的 port。

如果又出現 $PORT 相關錯誤
例如：

Invalid value for '--server.port'
那就把 nixpacks.toml 的 start command 改成這個比較保險的寫法：

[start]
cmd = "sh -c 'streamlit run app.py --server.address=0.0.0.0 --server.port=${PORT:-8080} --server.headless=true'"
最推薦你現在用的版本
Railway 目前先用：

拍照 / 上傳圖片偵測版本
不要先用：

即時 WebRTC 鏡頭版本
因為 Railway 部署即時鏡頭一樣可能遇到 STUN/TURN 連線問題；先把專案成功跑起來，期末展示會比較穩。


RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0 libsm6 libxext6 libxrender-dev libgomp1 && rm -rf /var/lib/apt/lists/*
4s
Hit:1 http://deb.debian.org/debian trixie InRelease
Get:2 http://deb.debian.org/debian trixie-updates InRelease [47.3 kB]
Get:3 http://deb.debian.org/debian-security trixie-security InRelease [43.4 kB]
Get:4 http://deb.debian.org/debian trixie/main amd64 Packages [9671 kB]
Get:5 http://deb.debian.org/debian trixie-updates/main amd64 Packages [5412 B]
Get:6 http://deb.debian.org/debian-security trixie-security/main amd64 Packages [154 kB]
Fetched 9921 kB in 1s (7662 kB/s)
Reading package lists...
Reading package lists...
Package libgl1-mesa-glx is not available, but is referred to by another package.
This may mean that the package is missing, has been obsoleted, or
is only available from another source
E: Package 'libgl1-mesa-glx' has no installation candidate
Build Failed: build daemon returned an error < failed to solve: process "/bin/sh -c apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0 libsm6 libxext6 libxrender-dev libgomp1 && rm -rf /var/lib/apt/lists/*" did not complete successfully: exit code: 100 >

這是目前的問題

已思考 5s
你目前的問題很明確：Railway build 時還在安裝 libgl1-mesa-glx，但 Debian trixie 已經找不到這個套件，所以失敗。

錯誤重點是這句：

E: Package 'libgl1-mesa-glx' has no installation candidate
解法：把 libgl1-mesa-glx 改成 libgl1
你現在這行：

RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0 libsm6 libxext6 libxrender-dev libgomp1 && rm -rf /var/lib/apt/lists/*
改成：

RUN apt-get update && apt-get install -y libgl1 libglib2.0-0 libsm6 libxext6 libxrender1 libgomp1 ffmpeg && rm -rf /var/lib/apt/lists/*
重點是：

libgl1-mesa-glx ❌
libgl1 ✅
如果你有 Dockerfile
請直接把 Dockerfile 改成這樣：

FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    libgomp1 \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD streamlit run app.py --server.address=0.0.0.0 --server.port=${PORT:-8080} --server.headless=true
如果你用的是 nixpacks.toml
請改成這樣：

[phases.setup]
aptPkgs = [
  "...",
  "libgl1",
  "libglib2.0-0",
  "libsm6",
  "libxext6",
  "libxrender1",
  "libgomp1",
  "ffmpeg"
]

[start]
cmd = "sh -c 'streamlit run app.py --server.address=0.0.0.0 --server.port=${PORT:-8080} --server.headless=true'"
你現在要做的事
到你的 GitHub 專案裡搜尋：

libgl1-mesa-glx
只要看到這個，就全部改成：

libgl1
它可能出現在：

Dockerfile
nixpacks.toml
packages.txt
README.md
Railway 目前的 build log 顯示它一定還在某個設定檔裡，所以才會繼續跑這行：

apt-get install -y libgl1-mesa-glx ...
requirements.txt 建議保持這樣
如果你現在用的是「拍照 / 上傳圖片」版本：

streamlit
ultralytics
opencv-python-headless
numpy<2
Pillow
torch
torchvision
如果你不是用即時 WebRTC，先不要放：

streamlit-webrtc
av
簡單講：
你的 Python 程式目前不是主要問題，是 Railway 的系統套件安裝清單還有舊的 libgl1-mesa-glx。把它改成 libgl1 後再重新 Deploy。


FROM python:3.11-slim

# 安裝系統依賴
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

# 先升級 pip
RUN pip install --no-cache-dir --upgrade pip

# 安裝依賴
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

已思考 4s
你的問題就在這一行：

libgl1-mesa-glx
Railway 目前的 Debian 環境找不到它，所以要改成：

libgl1
另外 Railway 不建議固定用 8501，最好改成使用 Railway 自動提供的 $PORT。

請把你的 Dockerfile 改成這份：

FROM python:3.11-slim

# 安裝系統依賴
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    libgomp1 \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

# 先升級 pip
RUN pip install --no-cache-dir --upgrade pip

# 安裝 Python 依賴
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Railway 會自動提供 PORT，不要固定只用 8501
EXPOSE 8080

CMD streamlit run app.py --server.address=0.0.0.0 --server.port=${PORT:-8080} --server.headless=true
你的 requirements.txt 如果是「拍照 / 上傳圖片版本」，建議用：

streamlit
ultralytics
opencv-python-headless
numpy<2
Pillow
torch
torchvision
重點改動是：

libgl1-mesa-glx ❌
libgl1 ✅
以及：

--server.port=8501 ❌
--server.port=${PORT:-8080} ✅
改完後重新 push 到 GitHub，Railway 重新 deploy。



已思考 2 秒鐘
看起來已經 部署成功了 🎉

畫面上有顯示：

Deployment successful
Active
Online
代表 Railway 已經成功 build 並啟動你的服務。

你現在下一步是找 公開網址 來打開你的 Streamlit 網頁。

接下來怎麼開網站
在 Railway 專案裡找：

Settings / Networking / Public Networking
或找類似：

Generate Domain
按下後 Railway 會產生一個網址，例如：

https://你的專案名稱.up.railway.app
點那個網址就可以開你的 app。

如果網址打開後是空白或錯誤
先去看：

Deploy Logs
如果有看到類似：

You can now view your Streamlit app in your browser.
Local URL: http://localhost:8080
Network URL: http://0.0.0.0:8080
通常代表程式有正常啟動。

你目前狀態判斷
你前面 Dockerfile 的問題應該已經解掉了，因為這張圖已經顯示：

Build ✓
Deploy ✓
Deployment successful ✓
所以現在不是 build 問題了，而是要去 Railway 產生或打開公開連結。


是這邊嗎

已思考 2 秒鐘
不是這邊喔。你現在打開的是 Project Settings → Webhooks，這是拿來設定 Discord / Slack 通知用的，不是網站網址。

你要找的是 服務本身的 Networking / Domains。

請照這樣找：

回到 Railway 專案首頁

點左邊或中間那個服務卡片：fff0508

進入服務後，找上方或側邊的 Settings

找 Networking

找 Public Networking

按 Generate Domain

產生後會出現類似：

https://你的專案名稱.up.railway.app
那個才是你的 Streamlit 網頁網址。

你現在這頁的 Webhook URL 不用填，也不用建立 Webhook。



對，這邊是正確位置。

你現在在 Networking，請按：

Generate Domain
按下後 Railway 會幫你產生一個公開網址，通常長得像：

https://你的服務名稱-production.up.railway.app
產生後，你就可以用那個網址打開你的 Streamlit App。

下面的這個：

fff0508.railway.internal
是 Private Networking，只能在 Railway 內部服務之間使用，外面瀏覽器不能直接打開。

所以你現在要做的是：

按 Generate Domain

等它產生網址

點網址打開

如果打不開，再去看 Deploy Logs 有沒有 Streamlit 啟動錯誤



對，這裡要填你的 Streamlit 實際監聽的 port。

因為我前面建議你的 Dockerfile 是用：

CMD streamlit run app.py --server.address=0.0.0.0 --server.port=${PORT:-8080} --server.headless=true
所以這裡填：

8080
然後按 Generate Domain。

如果你 Dockerfile 還是這樣：

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
那這裡就要填：

8501
但我建議你統一改成 8080 版本，比較適合 Railway：

EXPOSE 8080

CMD streamlit run app.py --server.address=0.0.0.0 --server.port=${PORT:-8080} --server.headless=true
所以現在這個畫面請填：

8080
再按 Generate Domain。



已思考 6s
這個畫面代表：Railway 網址有連到服務，但你的 Streamlit App 沒有正常回應。

最常見原因是：Domain 填 8080，但 Dockerfile 裡 Streamlit 實際跑在 8501 或其他 port。

建議你現在直接把 Dockerfile 改成「固定 8080」版本，最簡單。

請把 Dockerfile 改成這樣
FROM python:3.11-slim

# 安裝系統依賴
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    libgomp1 \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8080", "--server.headless=true"]
然後 Railway 這裡填 8080
你剛剛 Generate Domain 那邊：

Enter the port your app is listening on
填：

8080
這樣 Dockerfile 和 Railway 網址才會對到。

requirements.txt 確認是這樣
如果你現在用的是「拍照 / 上傳圖片版本」，請用這份：

streamlit
ultralytics
opencv-python-headless
numpy<2
Pillow
torch
torchvision
不要先放：

streamlit-webrtc
av
因為你目前不是用即時 WebRTC 版本。

改完後流程
修改 Dockerfile

Push 到 GitHub

Railway 會自動重新 Deploy

Deploy 成功後，回到 Networking

確認 Public Domain 的 port 是 8080

再打開網址

如果還是出現這個畫面，請點 Railway 的 Deploy Logs，把最後 20 行錯誤貼給我。那時候就不是 port 問題，而是 app.py 執行時出錯。


目前都還行，但手機換成後置相機的時候跑不出來

已思考 5s
可以，這種情況很常見。
手機前鏡頭可以，但切到後置相機跑不出來，通常不是程式壞掉，而是後鏡頭拍出來的照片解析度太高，例如 3000×4000 以上，YOLO 在 Railway 上處理會太慢或記憶體不夠。

解法是：在送進 YOLO 前先把圖片縮小。

你可以在 app.py 裡加這個函式：

from PIL import ImageOps
然後新增這段：

def resize_for_detection(image_pil, max_size=960):
    """
    手機後鏡頭照片解析度通常很大，先縮小再丟進 YOLO。
    也順便處理手機照片旋轉方向問題。
    """
    image_pil = ImageOps.exif_transpose(image_pil)
    image_pil = image_pil.convert("RGB")

    w, h = image_pil.size

    if max(w, h) > max_size:
        scale = max_size / max(w, h)
        new_w = int(w * scale)
        new_h = int(h * scale)
        image_pil = image_pil.resize((new_w, new_h))

    return image_pil
然後把你原本的 detect_image() 改成這樣：

def detect_image(image_pil, alarm_threshold):
    # 先縮小圖片，避免手機後鏡頭解析度太高造成 Railway 跑不動
    image_pil = resize_for_detection(image_pil, max_size=960)

    image_rgb = np.array(image_pil)

    results = model(
        image_rgb,
        verbose=False,
        imgsz=640
    )

    current_posture = classify_posture(results)

    update_posture_state(current_posture, alarm_threshold)

    annotated = results[0].plot()

    annotated_rgb = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)

    return annotated_rgb, current_posture
也建議把顯示原始影像那段改一下
原本可能是：

image_pil = Image.open(image_file)

st.image(
    image_pil,
    caption="原始影像",
    use_container_width=True,
)
改成：

image_pil = Image.open(image_file)
image_pil = resize_for_detection(image_pil, max_size=960)

st.image(
    image_pil,
    caption="原始影像",
    use_container_width=True,
)
這樣後置相機拍出來的超大圖片會先被縮小，Railway 比較跑得動。

如果你想更穩，可以把 max_size 再調小
目前：

max_size=960
如果 Railway 還是卡，可以改成：

max_size=640
例如：

image_pil = resize_for_detection(image_pil, max_size=640)
這樣速度會更快，但偵測精細度會稍微下降。

簡單講
你現在的問題大概是：

手機前鏡頭照片小 → 可以跑
手機後鏡頭照片太大 → YOLO 處理太慢或記憶體不足 → 跑不出來
所以最重要的修法就是：

後鏡頭照片先 resize，再丟進模型


已貼上文字 (1).txt
文件
這是我目前的程式碼

已思考 9s
我看你的程式目前還是 即時 WebRTC 版本，而且 media_stream_constraints 只有寫：

"video": True
所以手機瀏覽器通常會先用預設鏡頭，切到後置鏡頭時可能因為解析度太高、鏡頭切換不穩，或 Railway 處理太吃資源而卡住。你的程式目前確實是用 streamlit-webrtc 接即時影像，並把每一幀丟進 YOLO 做偵測。

 另外你現在的 webrtc_streamer() 設定也在 media_stream_constraints 裡只有 "video": True，沒有指定手機後鏡頭與解析度限制。


建議你先改兩個地方。

1. 在 PoseVideoProcessor.recv() 裡縮小影像
找到這段：

img = frame.to_ndarray(format="bgr24")
改成下面這樣：

img = frame.to_ndarray(format="bgr24")

# 手機後鏡頭解析度通常很高，先縮小再丟進 YOLO，避免 Railway 跑不動
max_width = 640
h, w = img.shape[:2]

if w > max_width:
    scale = max_width / w
    new_h = int(h * scale)
    img = cv2.resize(img, (max_width, new_h))
然後找到：

results = model(img, verbose=False)
改成：

results = model(img, verbose=False, imgsz=640)
這樣後鏡頭即使拍出很大的畫面，也會先縮小。

2. 修改 webrtc_streamer() 的 media_stream_constraints
你現在是這樣：

media_stream_constraints={
    "video": True,
    "audio": False
},
請改成：

media_stream_constraints={
    "video": {
        "facingMode": {"ideal": "environment"},
        "width": {"ideal": 640, "max": 960},
        "height": {"ideal": 480, "max": 720},
        "frameRate": {"ideal": 10, "max": 15},
    },
    "audio": False
},
這段意思是：
優先使用手機後鏡頭，但不要開太高解析度，也限制 FPS，讓 Railway 比較跑得動。

你的 PoseVideoProcessor 建議改成這段
你可以直接把原本的 class PoseVideoProcessor(VideoProcessorBase): 整段替換成下面這段：

class PoseVideoProcessor(VideoProcessorBase):
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")

        # =========================
        # 降低手機後鏡頭解析度
        # =========================
        max_width = 640
        h, w = img.shape[:2]

        if w > max_width:
            scale = max_width / w
            new_h = int(h * scale)
            img = cv2.resize(img, (max_width, new_h))

        try:
            results = model(img, verbose=False, imgsz=640)
            current_posture = classify_posture(results)
            annotated = results[0].plot()

        except Exception as e:
            current_posture = "偵測錯誤"
            annotated = img.copy()

            cv2.putText(
                annotated,
                f"Detection error: {str(e)[:80]}",
                (30, 55),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 0, 255),
                2,
                cv2.LINE_AA
            )

        now = time.time()

        with shared_state.lock:
            if shared_state.monitoring:
                if current_posture == shared_state.last_posture:
                    shared_state.duration = now - shared_state.start_time

                else:
                    shared_state.last_posture = current_posture
                    shared_state.current_posture = current_posture
                    shared_state.start_time = now
                    shared_state.duration = 0.0
                    shared_state.alarm = False
                    shared_state.alarm_acknowledged = False

                if (
                    shared_state.duration >= alarm_threshold
                    and current_posture != "無人躺著"
                    and current_posture != "偵測錯誤"
                    and not shared_state.alarm_acknowledged
                ):
                    shared_state.alarm = True

                else:
                    if (
                        current_posture == "無人躺著"
                        or current_posture == "偵測錯誤"
                        or shared_state.alarm_acknowledged
                    ):
                        shared_state.alarm = False

                shared_state.current_posture = current_posture

            else:
                shared_state.duration = 0.0
                shared_state.alarm = False
                shared_state.current_posture = current_posture

            monitor_text = (
                "Monitoring"
                if shared_state.monitoring
                else "Stopped"
            )

            posture_map = {
                "無人躺著": "No person",
                "左側躺": "Left side",
                "右側躺": "Right side",
                "仰躺": "Supine",
                "偵測錯誤": "Error"
            }

            posture_en = posture_map.get(
                shared_state.current_posture,
                "Unknown"
            )

            info_text = (
                f"{monitor_text} | "
                f"Posture: {posture_en} | "
                f"Time: {int(shared_state.duration)} sec"
            )

            cv2.rectangle(
                annotated,
                (20, 20),
                (min(900, annotated.shape[1] - 20), 70),
                (0, 0, 0),
                -1
            )

            cv2.putText(
                annotated,
                info_text,
                (30, 55),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255, 255, 255),
                2,
                cv2.LINE_AA
            )

            if shared_state.alarm:
                cv2.rectangle(
                    annotated,
                    (0, 0),
                    (annotated.shape[1], annotated.shape[0]),
                    (0, 0, 255),
                    10
                )

                cv2.putText(
                    annotated,
                    "ALARM",
                    (30, 110),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.5,
                    (0, 0, 255),
                    4,
                    cv2.LINE_AA
                )

        return av.VideoFrame.from_ndarray(
            annotated,
            format="bgr24"
        )
你的 webrtc_streamer() 改成這段
把原本 webrtc_streamer(...) 整段替換成：

webrtc_streamer(
    key="pose-monitor",
    mode=WebRtcMode.SENDRECV,
    rtc_configuration={
        "iceServers": [
            {"urls": ["stun:stun.l.google.com:19302"]},
            {"urls": ["stun:stun1.l.google.com:19302"]},
            {"urls": ["stun:stun2.l.google.com:19302"]},
            {"urls": ["stun:stun3.l.google.com:19302"]},
            {"urls": ["stun:stun4.l.google.com:19302"]}
        ]
    },
    media_stream_constraints={
        "video": {
            "facingMode": {"ideal": "environment"},
            "width": {"ideal": 640, "max": 960},
            "height": {"ideal": 480, "max": 720},
            "frameRate": {"ideal": 10, "max": 15},
        },
        "audio": False
    },
    video_processor_factory=PoseVideoProcessor,
    async_processing=True,
)
如果你想保留前鏡頭 / 後鏡頭切換
目前這版是「優先使用後鏡頭」。
如果你想讓使用者自己選，可以之後再加：

camera_mode = st.radio("選擇鏡頭", ["前鏡頭", "後鏡頭"])
但先建議你用上面版本測試，因為你現在的問題主要是後鏡頭跑不出來。


我想要可以選擇鏡頭

已思考幾秒鐘
可以，你現在的程式可以加一個「前鏡頭 / 後鏡頭」選擇。你目前 webrtc_streamer() 的 media_stream_constraints 是固定 "video": True，所以瀏覽器會自己決定鏡頭，手機切後鏡頭時容易不穩。


請改這兩個地方。

1. 在 Sidebar 加上鏡頭選擇
找到這段：

st.sidebar.header("⚙️ 分析設定")

alarm_threshold = st.sidebar.slider(
    "同姿勢維持幾秒觸發警報",
    min_value=3,
    max_value=60,
    value=10,
    step=1
)
改成：

st.sidebar.header("⚙️ 分析設定")

camera_choice = st.sidebar.radio(
    "選擇鏡頭",
    ["前鏡頭", "後鏡頭"],
    index=1
)

if camera_choice == "前鏡頭":
    facing_mode = "user"
else:
    facing_mode = "environment"

alarm_threshold = st.sidebar.slider(
    "同姿勢維持幾秒觸發警報",
    min_value=3,
    max_value=60,
    value=10,
    step=1
)
2. 把 webrtc_streamer() 改成可選鏡頭版本
找到你原本這段：

webrtc_streamer(
    key="pose-monitor",
    mode=WebRtcMode.SENDRECV,
    rtc_configuration={
        "iceServers": [
            {"urls": ["stun:stun.l.google.com:19302"]},
            {"urls": ["stun:stun1.l.google.com:19302"]},
            {"urls": ["stun:stun2.l.google.com:19302"]},
            {"urls": ["stun:stun3.l.google.com:19302"]},
            {"urls": ["stun:stun4.l.google.com:19302"]}
        ]
    },
    media_stream_constraints={
        "video": True,
        "audio": False
    },
    video_processor_factory=PoseVideoProcessor,
    async_processing=True,
)
改成這段：

webrtc_streamer(
    key=f"pose-monitor-{facing_mode}",
    mode=WebRtcMode.SENDRECV,
    rtc_configuration={
        "iceServers": [
            {"urls": ["stun:stun.l.google.com:19302"]},
            {"urls": ["stun:stun1.l.google.com:19302"]},
            {"urls": ["stun:stun2.l.google.com:19302"]},
            {"urls": ["stun:stun3.l.google.com:19302"]},
            {"urls": ["stun:stun4.l.google.com:19302"]}
        ]
    },
    media_stream_constraints={
        "video": {
            "facingMode": {"ideal": facing_mode},
            "width": {"ideal": 640, "max": 960},
            "height": {"ideal": 480, "max": 720},
            "frameRate": {"ideal": 10, "max": 15},
        },
        "audio": False
    },
    video_processor_factory=PoseVideoProcessor,
    async_processing=True,
)
這裡最重要的是：

key=f"pose-monitor-{facing_mode}"
因為切換前鏡頭 / 後鏡頭時，streamlit-webrtc 需要重新建立連線。如果 key 不變，它有時候會沿用舊鏡頭，導致切換失敗。

3. 建議同時縮小影像，避免後鏡頭太大跑不動
在你的 PoseVideoProcessor.recv() 裡面，找到：

img = frame.to_ndarray(format="bgr24")
改成：

img = frame.to_ndarray(format="bgr24")

# 手機後鏡頭解析度通常較高，先縮小再偵測，避免 Railway 跑不動
max_width = 640
h, w = img.shape[:2]

if w > max_width:
    scale = max_width / w
    new_h = int(h * scale)
    img = cv2.resize(img, (max_width, new_h))
然後把：

results = model(img, verbose=False)
改成：

results = model(img, verbose=False, imgsz=640)
改完後使用方式
使用者在左邊或側邊選：

前鏡頭 / 後鏡頭
切換後如果畫面沒有立刻變，請重新按一次瀏覽器重新整理，或關閉再開鏡頭權限。手機瀏覽器切換鏡頭本來就比較容易卡，所以用不同 key 讓它重新連線會穩很多。


我想改成可以連線其他裝置攝影機的版本

已思考 14s
可以改，但要先注意一件很重要的事：

你現在的版本是 WebRTC 使用「開啟網頁那台裝置」的鏡頭，也就是誰打開 Railway 網頁，就用誰的手機/電腦鏡頭。你的程式目前就是用 streamlit-webrtc 的 webrtc_streamer() 接收瀏覽器鏡頭畫面。


如果你想「連線其他裝置攝影機」，通常會改成下面這種：

手機 / IP 攝影機 / 另一台電腦
        ↓
提供一個串流網址，例如 http://.../video 或 rtsp://...
        ↓
Railway 上的 Streamlit 用 OpenCV 讀取這個網址
        ↓
YOLO 偵測姿勢
但是要注意：Railway 在雲端，不能直接讀取你家裡或學校區網的 192.168.x.x 攝影機網址。
例如這種通常不行：

http://192.168.1.23:8080/video
因為 Railway 不在你的 Wi-Fi 裡。

最適合你的做法
我建議你改成 兩種模式都保留：

模式一：使用目前裝置鏡頭
模式二：輸入其他裝置攝影機串流網址
這樣在展示時可以彈性切換。

先加這段：攝影機來源選擇
在你的 Sidebar 這段下面：

st.sidebar.header("⚙️ 分析設定")
加入：

camera_source = st.sidebar.radio(
    "選擇攝影機來源",
    ["目前裝置鏡頭", "其他裝置攝影機 URL"],
    index=0
)

camera_url = ""

if camera_source == "其他裝置攝影機 URL":
    camera_url = st.sidebar.text_input(
        "請輸入攝影機串流網址",
        placeholder="例如：http://你的公開網址/video 或 rtsp://..."
    )
再加這個函式：讀取其他裝置攝影機
放在 class PoseVideoProcessor 前面：

def process_image_frame(img):
    """
    統一處理單張影像：
    1. 縮小影像
    2. YOLO 偵測
    3. 姿勢判斷
    4. 更新警報狀態
    5. 回傳畫好結果的影像
    """

    max_width = 640
    h, w = img.shape[:2]

    if w > max_width:
        scale = max_width / w
        new_h = int(h * scale)
        img = cv2.resize(img, (max_width, new_h))

    try:
        results = model(img, verbose=False, imgsz=640)
        current_posture = classify_posture(results)
        annotated = results[0].plot()

    except Exception as e:
        current_posture = "偵測錯誤"
        annotated = img.copy()

        cv2.putText(
            annotated,
            f"Detection error: {str(e)[:80]}",
            (30, 55),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 0, 255),
            2,
            cv2.LINE_AA
        )

    now = time.time()

    with shared_state.lock:
        if shared_state.monitoring:
            if current_posture == shared_state.last_posture:
                shared_state.duration = now - shared_state.start_time
            else:
                shared_state.last_posture = current_posture
                shared_state.current_posture = current_posture
                shared_state.start_time = now
                shared_state.duration = 0.0
                shared_state.alarm = False
                shared_state.alarm_acknowledged = False

            if (
                shared_state.duration >= alarm_threshold
                and current_posture != "無人躺著"
                and current_posture != "偵測錯誤"
                and not shared_state.alarm_acknowledged
            ):
                shared_state.alarm = True
            else:
                if (
                    current_posture == "無人躺著"
                    or current_posture == "偵測錯誤"
                    or shared_state.alarm_acknowledged
                ):
                    shared_state.alarm = False

            shared_state.current_posture = current_posture
        else:
            shared_state.duration = 0.0
            shared_state.alarm = False
            shared_state.current_posture = current_posture

        monitor_text = "Monitoring" if shared_state.monitoring else "Stopped"

        posture_map = {
            "無人躺著": "No person",
            "左側躺": "Left side",
            "右側躺": "Right side",
            "仰躺": "Supine",
            "偵測錯誤": "Error"
        }

        posture_en = posture_map.get(shared_state.current_posture, "Unknown")

        info_text = (
            f"{monitor_text} | "
            f"Posture: {posture_en} | "
            f"Time: {int(shared_state.duration)} sec"
        )

        cv2.rectangle(
            annotated,
            (20, 20),
            (min(900, annotated.shape[1] - 20), 70),
            (0, 0, 0),
            -1
        )

        cv2.putText(
            annotated,
            info_text,
            (30, 55),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2,
            cv2.LINE_AA
        )

        if shared_state.alarm:
            cv2.rectangle(
                annotated,
                (0, 0),
                (annotated.shape[1], annotated.shape[0]),
                (0, 0, 255),
                10
            )

            cv2.putText(
                annotated,
                "ALARM",
                (30, 110),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.5,
                (0, 0, 255),
                4,
                cv2.LINE_AA
            )

    return annotated
把你的 PoseVideoProcessor 簡化成這樣
把原本整個 class PoseVideoProcessor(VideoProcessorBase): 換成：

class PoseVideoProcessor(VideoProcessorBase):
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")

        annotated = process_image_frame(img)

        return av.VideoFrame.from_ndarray(
            annotated,
            format="bgr24"
        )
這樣之後 WebRTC 和外部攝影機都可以共用同一套 YOLO 偵測邏輯。

把 Webcam 區塊改成可選來源
找到你的這段：

with left_col:
    st.subheader("1. 即時影像監測")

    webrtc_streamer(
        key="pose-monitor",
        ...
    )
整段改成下面這樣：

with left_col:
    st.subheader("1. 即時影像監測")

    if camera_source == "目前裝置鏡頭":

        st.info("目前使用開啟此網頁的裝置鏡頭。")

        webrtc_streamer(
            key="pose-monitor",
            mode=WebRtcMode.SENDRECV,
            rtc_configuration={
                "iceServers": [
                    {"urls": ["stun:stun.l.google.com:19302"]},
                    {"urls": ["stun:stun1.l.google.com:19302"]},
                    {"urls": ["stun:stun2.l.google.com:19302"]},
                    {"urls": ["stun:stun3.l.google.com:19302"]},
                    {"urls": ["stun:stun4.l.google.com:19302"]}
                ]
            },
            media_stream_constraints={
                "video": {
                    "width": {"ideal": 640, "max": 960},
                    "height": {"ideal": 480, "max": 720},
                    "frameRate": {"ideal": 10, "max": 15},
                },
                "audio": False
            },
            video_processor_factory=PoseVideoProcessor,
            async_processing=True,
        )

    else:

        st.info("目前使用其他裝置攝影機 URL。")

        if camera_url == "":
            st.warning("請先在左側輸入攝影機串流網址。")

        else:
            run_ip_camera = st.button("▶️ 讀取其他裝置攝影機")

            frame_placeholder = st.empty()

            if run_ip_camera:
                cap = cv2.VideoCapture(camera_url)

                if not cap.isOpened():
                    st.error("無法連線到攝影機，請確認網址是否正確，且 Railway 可以連到該網址。")
                else:
                    for _ in range(150):
                        ret, frame = cap.read()

                        if not ret:
                            st.warning("讀取不到影像，串流可能中斷。")
                            break

                        annotated = process_image_frame(frame)
                        annotated_rgb = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)

                        frame_placeholder.image(
                            annotated_rgb,
                            channels="RGB",
                            use_container_width=True
                        )

                        time.sleep(0.1)

                    cap.release()
這個版本會讀取大約 150 幀，約 15 秒。
如果你想更久，可以把：

for _ in range(150):
改成：

for _ in range(300):
其他裝置攝影機要怎麼提供網址？
方法一：手機安裝 IP Webcam 類 App
手機開啟 IP Camera App 後，可能會給你：

http://192.168.1.23:8080/video
但這種 只適合本機或同 Wi-Fi，Railway 通常不能讀。

方法二：用公開網址
Railway 可以讀的網址要像這樣：

https://xxxx.ngrok-free.app/video
或：

https://xxxx.trycloudflare.com/video
也就是你需要把手機或電腦的攝影機串流透過 ngrok / Cloudflare Tunnel 暴露成公開網址。

最簡單判斷
如果攝影機網址是這種：

192.168.x.x
10.x.x.x
localhost
127.0.0.1
部署在 Railway 上通常讀不到。

如果是這種：

https://...
rtsp://公開IP...
Railway 才比較可能讀得到。

我建議你先加「其他裝置攝影機 URL」模式，但展示時如果只是要用另一支手機當攝影機，最穩的方式其實是：直接用那支手機打開 Railway 網頁，讓它變成攝影機端。


可以先給我完整程式碼嗎

已思考 2 秒鐘
可以，下面這份是整合版完整 app.py，功能包含：

目前裝置鏡頭

可選前鏡頭 / 後鏡頭

其他裝置攝影機 URL

YOLO 姿勢偵測

姿勢維持過久警報

警報聲測試與播放

自動縮小影像，避免手機後鏡頭解析度太高跑不動

我保留你原本的主要架構、警報邏輯、畫面樣式與音效功能，再加上「攝影機來源選擇」和「外部攝影機 URL」模式。你的原本程式是用 streamlit-webrtc 讀取目前裝置鏡頭並把每一幀送進 YOLO 偵測，這版是在這個基礎上改的。


請直接把整份存成 app.py。

import streamlit as st
import streamlit.components.v1 as components

import cv2
import math
import av
import time
import threading
import base64
from pathlib import Path

from ultralytics import YOLO
from streamlit_webrtc import webrtc_streamer, WebRtcMode, VideoProcessorBase
from streamlit_autorefresh import st_autorefresh


# =========================
# Page config
# =========================
st.set_page_config(
    page_title="長照睡姿固定過久警報系統",
    page_icon="🛌",
    layout="wide"
)


# =========================
# Custom style
# =========================
st.markdown("""
<style>

.main-title {
    font-size: 2.2rem;
    font-weight: 700;
    color: #1f3c88;
    margin-bottom: 0.2rem;
}

.sub-text {
    color: #5f6b7a;
    font-size: 1rem;
    margin-bottom: 1.2rem;
}

.metric-card {
    background-color: #f8fbff;
    border: 1px solid #dfe8f3;
    border-radius: 14px;
    padding: 16px 20px;
    text-align: center;
}

.metric-label {
    font-size: 0.95rem;
    color: #6b7280;
}

.metric-value {
    font-size: 1.8rem;
    font-weight: 700;
    color: #1f3c88;
}

.alert-box {
    background-color: #fff1f2;
    border: 1px solid #fda4af;
    color: #b91c1c;
    border-radius: 12px;
    padding: 16px;
    font-size: 1.05rem;
    font-weight: 600;
}

.normal-box {
    background-color: #f0fdf4;
    border: 1px solid #86efac;
    color: #166534;
    border-radius: 12px;
    padding: 16px;
    font-size: 1.05rem;
    font-weight: 600;
}

.sound-box {
    background-color: #fff7ed;
    border: 1px solid #fdba74;
    color: #9a3412;
    border-radius: 12px;
    padding: 14px;
    font-size: 1rem;
    font-weight: 600;
    margin-top: 10px;
    margin-bottom: 10px;
}

</style>
""", unsafe_allow_html=True)


# =========================
# Title
# =========================
st.markdown(
    '<div class="main-title">🛌 長照睡姿固定過久警報系統</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-text">使用影像分析臥床姿勢變化，協助照護員及早發現長時間未翻身狀況。</div>',
    unsafe_allow_html=True
)


# =========================
# Load YOLO model
# =========================
@st.cache_resource
def load_model():
    return YOLO("yolov8n-pose.pt")


model = load_model()


# =========================
# Shared state
# =========================
class AppState:
    def __init__(self):
        self.lock = threading.Lock()

        self.current_posture = "無人躺著"
        self.last_posture = "無人躺著"

        self.start_time = time.time()
        self.duration = 0.0

        self.alarm = False
        self.alarm_acknowledged = False

        self.monitoring = False


if "shared_state" not in st.session_state:
    st.session_state.shared_state = AppState()

shared_state = st.session_state.shared_state

if "sound_enabled" not in st.session_state:
    st.session_state.sound_enabled = False

if "test_alarm_sound" not in st.session_state:
    st.session_state.test_alarm_sound = False

if "external_camera_running" not in st.session_state:
    st.session_state.external_camera_running = False


# =========================
# Helper
# =========================
def to_xy(point):
    return float(point[0]), float(point[1])


def dist(p1, p2):
    x1, y1 = to_xy(p1)
    x2, y2 = to_xy(p2)

    return math.sqrt(
        (x1 - x2) ** 2 +
        (y1 - y2) ** 2
    )


def resize_frame(img, max_width=640):
    """
    手機後鏡頭或外部攝影機解析度可能太高，
    先縮小再丟進 YOLO，避免 Railway 跑太慢或卡住。
    """
    h, w = img.shape[:2]

    if w > max_width:
        scale = max_width / w
        new_h = int(h * scale)
        img = cv2.resize(img, (max_width, new_h))

    return img


# =========================
# 姿勢分類
# =========================
def classify_posture(results):
    current_posture = "無人躺著"

    if results is None or len(results) == 0:
        return current_posture

    result = results[0]

    if result.keypoints is None:
        return current_posture

    if result.keypoints.xy is None or len(result.keypoints.xy) == 0:
        return current_posture

    if result.keypoints.conf is None or len(result.keypoints.conf) == 0:
        return current_posture

    kps = result.keypoints.xy[0]
    conf = result.keypoints.conf[0]

    if len(kps) < 13:
        return current_posture

    if float(conf.max()) <= 0.5:
        return current_posture

    shoulder_width = dist(kps[5], kps[6])

    torso_length = (
        dist(kps[5], kps[11]) +
        dist(kps[6], kps[12])
    ) / 2

    left_shoulder_conf = float(conf[5])
    right_shoulder_conf = float(conf[6])

    is_side = (
        left_shoulder_conf < 0.4
        or right_shoulder_conf < 0.4
        or (
            torso_length > 0
            and (shoulder_width / torso_length) < 0.5
        )
    )

    if is_side:
        left_ear_conf = float(conf[3])
        right_ear_conf = float(conf[4])

        if (right_ear_conf + right_shoulder_conf) > (
            left_ear_conf + left_shoulder_conf
        ) + 0.2:
            current_posture = "左側躺"

        elif (left_ear_conf + left_shoulder_conf) > (
            right_ear_conf + right_shoulder_conf
        ) + 0.2:
            current_posture = "右側躺"

        else:
            if dist(kps[0], kps[3]) < dist(kps[0], kps[4]):
                current_posture = "右側躺"
            else:
                current_posture = "左側躺"

    else:
        current_posture = "仰躺"

    return current_posture


# =========================
# Alarm sound
# =========================
def render_loop_alarm():
    audio_file = Path("alarm.mp3")

    if not audio_file.exists():
        st.warning("⚠️ 找不到 alarm.mp3，請確認 alarm.mp3 有放在 app.py 同一層。")
        return

    audio_bytes = audio_file.read_bytes()
    b64 = base64.b64encode(audio_bytes).decode()

    st.markdown(
        """
        <div class="sound-box">
            🔊 警報聲已觸發。若瀏覽器沒有自動播放，請按下方「播放警報聲」按鈕。
        </div>
        """,
        unsafe_allow_html=True
    )

    audio_html = f"""
    <div style="margin-top: 12px;">
        <audio id="alarmAudio" loop>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            你的瀏覽器不支援音訊播放。
        </audio>

        <button onclick="playAlarm()" 
            style="
                background-color:#dc2626;
                color:white;
                border:none;
                border-radius:10px;
                padding:12px 20px;
                font-size:18px;
                font-weight:700;
                cursor:pointer;
                margin-right:10px;
            ">
            🔊 播放警報聲
        </button>

        <button onclick="stopAlarm()" 
            style="
                background-color:#4b5563;
                color:white;
                border:none;
                border-radius:10px;
                padding:12px 20px;
                font-size:18px;
                font-weight:700;
                cursor:pointer;
            ">
            ⏹ 停止警報聲
        </button>

        <script>
            const audio = document.getElementById("alarmAudio");

            function playAlarm() {{
                audio.currentTime = 0;
                audio.play();
            }}

            function stopAlarm() {{
                audio.pause();
                audio.currentTime = 0;
            }}

            audio.play().catch(function(error) {{
                console.log("Autoplay was blocked by browser.");
            }});
        </script>
    </div>
    """

    components.html(audio_html, height=100)


# =========================
# Sidebar
# =========================
st.sidebar.header("⚙️ 分析設定")

camera_source = st.sidebar.radio(
    "選擇攝影機來源",
    ["目前裝置鏡頭", "其他裝置攝影機 URL"],
    index=0
)

camera_choice = "後鏡頭"
facing_mode = "environment"

if camera_source == "目前裝置鏡頭":
    camera_choice = st.sidebar.radio(
        "選擇鏡頭",
        ["前鏡頭", "後鏡頭"],
        index=1
    )

    if camera_choice == "前鏡頭":
        facing_mode = "user"
    else:
        facing_mode = "environment"

camera_url = ""

if camera_source == "其他裝置攝影機 URL":
    camera_url = st.sidebar.text_input(
        "請輸入攝影機串流網址",
        placeholder="例如：https://xxxx.ngrok-free.app/video 或 rtsp://..."
    )

st.sidebar.markdown("---")

alarm_threshold = st.sidebar.slider(
    "同姿勢維持幾秒觸發警報",
    min_value=3,
    max_value=60,
    value=10,
    step=1
)

if st.sidebar.button("🔊 啟用警報聲"):
    st.session_state.sound_enabled = True
    st.sidebar.success("警報聲已啟用")

if st.sidebar.button("🔔 測試警報聲"):
    st.session_state.sound_enabled = True
    st.session_state.test_alarm_sound = True

st.sidebar.markdown("---")


# =========================
# Start button
# =========================
if st.sidebar.button("▶️ Start"):
    with shared_state.lock:
        shared_state.monitoring = True
        shared_state.start_time = time.time()
        shared_state.duration = 0.0
        shared_state.alarm = False
        shared_state.alarm_acknowledged = False
        shared_state.last_posture = shared_state.current_posture


# =========================
# Stop button
# =========================
if st.sidebar.button("⏹ Stop"):
    with shared_state.lock:
        shared_state.monitoring = False
        shared_state.duration = 0.0
        shared_state.alarm = False
        shared_state.alarm_acknowledged = False
        shared_state.current_posture = "無人躺著"
        shared_state.last_posture = "無人躺著"

    st.session_state.test_alarm_sound = False
    st.session_state.external_camera_running = False

st.sidebar.markdown("---")

st.sidebar.info(
    "按下 Start 後開始監測；Stop 會停止並重新計算。"
)

if camera_source == "其他裝置攝影機 URL":
    st.sidebar.warning(
        "提醒：Railway 無法直接連到 192.168.x.x、localhost 這類區網網址。"
    )


# 每秒刷新右側資訊
st_autorefresh(interval=1000, key="refresh")


# =========================
# 共用影像處理邏輯
# =========================
def process_image_frame(img):
    """
    WebRTC 和其他裝置攝影機 URL 共用這個函式。
    """
    img = resize_frame(img, max_width=640)

    try:
        results = model(img, verbose=False, imgsz=640)
        current_posture = classify_posture(results)
        annotated = results[0].plot()

    except Exception as e:
        current_posture = "偵測錯誤"
        annotated = img.copy()

        cv2.putText(
            annotated,
            f"Detection error: {str(e)[:80]}",
            (30, 55),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 0, 255),
            2,
            cv2.LINE_AA
        )

    now = time.time()

    with shared_state.lock:
        if shared_state.monitoring:
            if current_posture == shared_state.last_posture:
                shared_state.duration = now - shared_state.start_time

            else:
                shared_state.last_posture = current_posture
                shared_state.current_posture = current_posture
                shared_state.start_time = now
                shared_state.duration = 0.0
                shared_state.alarm = False
                shared_state.alarm_acknowledged = False

            if (
                shared_state.duration >= alarm_threshold
                and current_posture != "無人躺著"
                and current_posture != "偵測錯誤"
                and not shared_state.alarm_acknowledged
            ):
                shared_state.alarm = True

            else:
                if (
                    current_posture == "無人躺著"
                    or current_posture == "偵測錯誤"
                    or shared_state.alarm_acknowledged
                ):
                    shared_state.alarm = False

            shared_state.current_posture = current_posture

        else:
            shared_state.duration = 0.0
            shared_state.alarm = False
            shared_state.current_posture = current_posture

        monitor_text = (
            "Monitoring"
            if shared_state.monitoring
            else "Stopped"
        )

        posture_map = {
            "無人躺著": "No person",
            "左側躺": "Left side",
            "右側躺": "Right side",
            "仰躺": "Supine",
            "偵測錯誤": "Error"
        }

        posture_en = posture_map.get(
            shared_state.current_posture,
            "Unknown"
        )

        info_text = (
            f"{monitor_text} | "
            f"Posture: {posture_en} | "
            f"Time: {int(shared_state.duration)} sec"
        )

        cv2.rectangle(
            annotated,
            (20, 20),
            (min(900, annotated.shape[1] - 20), 70),
            (0, 0, 0),
            -1
        )

        cv2.putText(
            annotated,
            info_text,
            (30, 55),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2,
            cv2.LINE_AA
        )

        if shared_state.alarm:
            cv2.rectangle(
                annotated,
                (0, 0),
                (annotated.shape[1], annotated.shape[0]),
                (0, 0, 255),
                10
            )

            cv2.putText(
                annotated,
                "ALARM",
                (30, 110),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.5,
                (0, 0, 255),
                4,
                cv2.LINE_AA
            )

    return annotated


# =========================
# Video Processor
# =========================
class PoseVideoProcessor(VideoProcessorBase):
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")

        annotated = process_image_frame(img)

        return av.VideoFrame.from_ndarray(
            annotated,
            format="bgr24"
        )


# =========================
# Layout
# =========================
left_col, right_col = st.columns([1.15, 1.4])


# =========================
# Camera Panel
# =========================
with left_col:
    st.subheader("1. 即時影像監測")

    if camera_source == "目前裝置鏡頭":
        st.info(f"目前使用：{camera_choice}")

        webrtc_streamer(
            key=f"pose-monitor-{facing_mode}",
            mode=WebRtcMode.SENDRECV,
            rtc_configuration={
                "iceServers": [
                    {"urls": ["stun:stun.l.google.com:19302"]},
                    {"urls": ["stun:stun1.l.google.com:19302"]},
                    {"urls": ["stun:stun2.l.google.com:19302"]},
                    {"urls": ["stun:stun3.l.google.com:19302"]},
                    {"urls": ["stun:stun4.l.google.com:19302"]}
                ]
            },
            media_stream_constraints={
                "video": {
                    "facingMode": {"ideal": facing_mode},
                    "width": {"ideal": 640, "max": 960},
                    "height": {"ideal": 480, "max": 720},
                    "frameRate": {"ideal": 10, "max": 15},
                },
                "audio": False
            },
            video_processor_factory=PoseVideoProcessor,
            async_processing=True,
        )

    else:
        st.info("目前使用：其他裝置攝影機 URL")

        st.markdown(
            """
            可輸入其他攝影機串流網址，例如 IP Camera、ngrok、Cloudflare Tunnel 或公開 RTSP/HTTP 串流。
            
            注意：如果網址是 `192.168.x.x`、`localhost`、`127.0.0.1`，
            Railway 通常無法讀取，因為那是你的本地區網。
            """
        )

        if camera_url.strip() == "":
            st.warning("請先在左側輸入攝影機串流網址。")

        else:
            col_a, col_b = st.columns(2)

            with col_a:
                if st.button("▶️ 讀取其他裝置攝影機", type="primary"):
                    st.session_state.external_camera_running = True

            with col_b:
                if st.button("⏹ 停止讀取外部攝影機"):
                    st.session_state.external_camera_running = False

            frame_placeholder = st.empty()

            if st.session_state.external_camera_running:
                cap = cv2.VideoCapture(camera_url)

                if not cap.isOpened():
                    st.error("無法連線到攝影機。請確認網址是否正確，且 Railway 可以連到該網址。")
                    st.session_state.external_camera_running = False

                else:
                    st.success("已連線到外部攝影機，正在讀取影像。")

                    # 每次執行讀取一小段，避免 Streamlit 長時間卡死
                    for _ in range(80):
                        if not st.session_state.external_camera_running:
                            break

                        ret, frame = cap.read()

                        if not ret:
                            st.warning("讀取不到影像，串流可能中斷。")
                            st.session_state.external_camera_running = False
                            break

                        annotated = process_image_frame(frame)
                        annotated_rgb = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)

                        frame_placeholder.image(
                            annotated_rgb,
                            channels="RGB",
                            use_container_width=True
                        )

                        time.sleep(0.08)

                    cap.release()


# =========================
# Right Panel
# =========================
with right_col:
    st.subheader("2. 摘要資訊")

    with shared_state.lock:
        posture_now = shared_state.current_posture
        duration_now = int(shared_state.duration)
        alarm_now = shared_state.alarm
        monitoring_now = shared_state.monitoring

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">目前姿勢</div>
            <div class="metric-value">{posture_now}</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">持續時間</div>
            <div class="metric-value">{duration_now} 秒</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        system_text = (
            "監測中"
            if monitoring_now
            else "停止"
        )

        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">系統狀態</div>
            <div class="metric-value">{system_text}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)


    # =========================
    # 測試警報聲
    # =========================
    if st.session_state.test_alarm_sound:
        st.subheader("🔔 警報聲測試")
        render_loop_alarm()

        if st.button("停止測試警報聲"):
            st.session_state.test_alarm_sound = False
            st.rerun()


    # =========================
    # Alarm 區
    # =========================
    st.subheader("3. 警報摘要")

    if alarm_now:
        st.markdown(f"""
        <div class="alert-box">
            🚨 偵測到姿勢持續超過 {alarm_threshold} 秒，
            請協助翻身。
        </div>
        """, unsafe_allow_html=True)

        render_loop_alarm()

        if st.button("✅ 確認此資訊", type="primary"):
            with shared_state.lock:
                shared_state.alarm_acknowledged = True
                shared_state.alarm = False

            st.rerun()

    else:
        st.markdown("""
        <div class="normal-box">
            ✅ 目前尚未觸發警報
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.subheader("4. 使用提醒")

    st.markdown(
        """
        **目前裝置鏡頭模式：**
        - 適合直接用手機或電腦打開網頁。
        - 可選擇前鏡頭或後鏡頭。
        - 後鏡頭解析度較高，程式已自動縮小影像以提升穩定度。

        **其他裝置攝影機 URL 模式：**
        - 可輸入公開的攝影機串流網址。
        - Railway 通常無法讀取 `192.168.x.x` 這種區網網址。
        - 如果要用另一支手機當攝影機，通常需要 ngrok 或 Cloudflare Tunnel 轉成公開網址。
        """
    )
你的 requirements.txt 建議要包含：

streamlit
streamlit-webrtc==0.47.9
streamlit-autorefresh
ultralytics
opencv-python-headless
numpy<2
Pillow
torch
torchvision
av
你的 Dockerfile 仍然建議用這種：

FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    libgomp1 \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8080", "--server.headless=true"]
最穩的展示方式：用「目前裝置鏡頭」模式；如果要真的接其他裝置攝影機，記得 URL 不能是 192.168.x.x，Railway 需要連得到公開網址。


如果要用另一支手機當攝影機，通常需要 ngrok 或 Cloudflare Tunnel 轉成公開網址。

這個部分要怎麼用

已思考 6s
可以，我建議你用 Cloudflare Tunnel，比較適合你現在的情境，因為可以不用先處理 ngrok 帳號、token，比較快測試。Cloudflare 官方也有提供 Quick Tunnel，主要是給測試與開發使用。

概念是這樣：

另一支手機當攝影機
↓
手機產生一個本地攝影機網址，例如 http://192.168.x.x:8080/video
↓
電腦用 Cloudflare Tunnel 把這個網址轉成公開網址
↓
Railway App 輸入公開網址
↓
你的系統讀取這支手機的鏡頭畫面
方法一：用 Android 手機當攝影機，最簡單
Step 1：手機安裝 IP Camera App
另一支手機安裝類似這種 App：

IP Webcam
DroidCam
Iriun Webcam
以 IP Webcam 為例，打開 App 後按：

Start server / 開始伺服器
它會顯示一個網址，通常長這樣：

http://192.168.1.23:8080
影像串流網址通常會是：

http://192.168.1.23:8080/video
請先用你的電腦瀏覽器打開這個網址測試。
如果電腦可以看到畫面，代表手機攝影機已經成功在區網內開啟。

Step 2：電腦安裝 Cloudflare Tunnel
到 Cloudflare 官方下載 cloudflared。Cloudflare Tunnel 是用 cloudflared 這個程式把本機或內網服務連到 Cloudflare 網路。

如果你是 Windows，可以下載 cloudflared.exe，放在一個資料夾，例如：

C:\cloudflared\
Step 3：用 Cloudflare Tunnel 轉成公開網址
在電腦打開 CMD 或 PowerShell，進到 cloudflared.exe 所在資料夾：

cd C:\cloudflared
假設手機 IP Camera 的網址是：

http://192.168.1.23:8080
執行：

cloudflared tunnel --url http://192.168.1.23:8080
成功後會出現一個公開網址，長得像：

https://xxxx-xxxx-xxxx.trycloudflare.com
這時候你的攝影機公開串流網址就是：

https://xxxx-xxxx-xxxx.trycloudflare.com/video
把這個網址貼到你的 Railway App 的：

其他裝置攝影機 URL
就可以測試。

你要貼進 App 的格式
如果 Cloudflare 給你的網址是：

https://abc-test.trycloudflare.com
那你通常要貼：

https://abc-test.trycloudflare.com/video
不是只貼主網址。

方法二：用 ngrok
ngrok 也是同樣概念：安裝 agent，讓它把本地服務轉成公開網址。ngrok 官方文件說 ngrok agent 會把它建立的雲端 endpoint 轉發到你的本地 upstream service。

假設手機攝影機網址是：

http://192.168.1.23:8080
你可以在電腦執行：

ngrok http http://192.168.1.23:8080
它會給你一個：

https://xxxx.ngrok-free.app
貼到 App 時一樣加 /video：

https://xxxx.ngrok-free.app/video
ngrok 需要先安裝 agent，通常還要設定 authtoken；官方 Quickstart 有安裝與設定步驟。

最容易成功的測試流程
先用這個順序：

1. 另一支手機開 IP Webcam
2. 電腦瀏覽器測試 http://手機IP:8080/video
3. 電腦開 cloudflared tunnel --url http://手機IP:8080
4. 拿到 https://xxxx.trycloudflare.com
5. 在 Railway App 貼 https://xxxx.trycloudflare.com/video
6. 按「讀取其他裝置攝影機」
注意事項
手機和電腦要先在同一個 Wi-Fi，因為電腦要能讀到：

http://192.168.x.x:8080
Cloudflare Tunnel 的那個 CMD 視窗不能關掉，關掉後公開網址就會失效。

如果你的手機攝影機 App 顯示的串流路徑不是 /video，要依 App 顯示為準。有些可能是：

/video
/mjpeg
/shot.jpg
你可以先用電腦瀏覽器測試哪個網址會顯示即時畫面。


我只有iphone手機

已思考 9s
可以，只有 iPhone 也可以，但做法會有兩種情況：

最簡單做法：直接用 iPhone 打開 Railway 網頁
如果你的需求只是「用 iPhone 的鏡頭當攝影機」，其實不用 Cloudflare Tunnel。

你直接用 iPhone Safari 或 Chrome 打開你的 Railway 網址：

https://你的app.up.railway.app
然後在系統裡選：

目前裝置鏡頭 → 後鏡頭
這樣 iPhone 本身就是攝影機。
這是最穩、最簡單的展示方式。

如果你是要「另一支 iPhone 當攝影機」
那你需要讓那支 iPhone 變成一台「IP Camera」。iPhone 可以用支援 HTTP / RTSP / MJPEG 的 App，例如 IP Camera Lite，它的 App Store 說明有提到可以把 iOS 裝置變成無線 IP Camera，並支援內建 RTSP 與 HTTP Server。

也可以找類似 SimpleIPCamera 這種 App，它的說明是讓 iPhone 建立 MJPEG streaming server，並在同 Wi-Fi 的其他裝置用瀏覽器打開顯示的網址觀看。

iPhone 當外部攝影機的流程
你需要：

iPhone A：當攝影機
電腦：開 Cloudflare Tunnel
Railway App：讀取公開網址
流程如下：

1. iPhone 安裝 IP Camera 類 App
在 iPhone 上安裝：

IP Camera Lite
或搜尋：

MJPEG IP Camera
IP Camera Server
SimpleIPCamera
開啟 App 後，按類似：

Start Server
Start Camera
Start Streaming
它通常會給你一個區網網址，例如：

http://192.168.1.35:8080
串流網址可能是：

http://192.168.1.35:8080/video
或：

http://192.168.1.35:8080/mjpeg
每個 App 不一定一樣，要看 App 顯示的 URL。

2. 先用電腦測試 iPhone 攝影機網址
你的電腦和 iPhone 要連同一個 Wi-Fi。

在電腦瀏覽器打開：

http://192.168.1.35:8080
或：

http://192.168.1.35:8080/video
如果電腦看得到 iPhone 畫面，就代表區網串流成功。

3. 電腦開 Cloudflare Tunnel
假設你的 iPhone 攝影機主網址是：

http://192.168.1.35:8080
電腦執行：

cloudflared tunnel --url http://192.168.1.35:8080
成功後會出現一個公開網址，例如：

https://abc-123.trycloudflare.com
4. 貼到你的 Railway App
如果 iPhone App 的串流路徑是 /video，那你在 Railway App 裡貼：

https://abc-123.trycloudflare.com/video
如果 iPhone App 的串流路徑是 /mjpeg，就貼：

https://abc-123.trycloudflare.com/mjpeg
也就是：

Cloudflare 給你的網址 + 原本 iPhone App 的串流路徑
但我要提醒你
只有 iPhone 的話，最簡單、最穩的方式還是：直接用 iPhone 打開 Railway App。

因為「另一支 iPhone → Cloudflare Tunnel → Railway → YOLO」會比較複雜，而且需要：

1. iPhone 開 IP Camera App
2. 電腦和 iPhone 同 Wi-Fi
3. 電腦執行 cloudflared
4. Railway 讀公開串流網址
如果你只是期末展示，我建議先用：

iPhone Safari 打開 Railway 網頁 → 選後鏡頭
這樣最不容易出錯。


iPhone Safari 打開 Railway 網頁 → 選後鏡頭

怎麼用

已思考 2 秒鐘
可以，這個方式就是：用 iPhone 自己當攝影機，不需要另一台手機、不需要 ngrok。

iPhone Safari 使用步驟
1. 用 iPhone 打開你的 Railway 網址
在 iPhone 的 Safari 打開你的 Railway App 網址，例如：

https://你的專案名稱.up.railway.app
建議用 Safari，不要用 LINE 內建瀏覽器或 Instagram 內建瀏覽器，因為相機權限比較容易出問題。

2. 允許相機權限
打開網頁後，如果跳出：

是否允許使用相機？
請按：

允許
如果沒有跳出，或之前按到拒絕，可以到 iPhone 設定改：

設定 → Safari → 相機 → 允許
或：

設定 → 隱私權與安全性 → 相機 → Safari → 開啟
3. 在你的 App 左側選後鏡頭
你的新版程式如果有我前面加的選項，側邊欄會有：

選擇攝影機來源
請選：

目前裝置鏡頭
然後下面的：

選擇鏡頭
請選：

後鏡頭
4. 按 Start
接著按左側：

▶️ Start
然後 WebRTC 畫面應該會開始顯示 iPhone 後鏡頭畫面。

如果後鏡頭沒有出來
請依序試這幾個方法：

方法 1：重新整理網頁
切換成後鏡頭後，按 Safari 重新整理。

因為手機切換前後鏡頭時，WebRTC 有時候需要重新建立連線。

方法 2：關掉分頁重新開
關掉 Safari 這個 Railway App 分頁

重新開 Railway 網址

選「目前裝置鏡頭」

選「後鏡頭」

按 Start

方法 3：確認網址是 HTTPS
iPhone Safari 使用相機通常需要安全網址，也就是要長這樣：

https://...
Railway 產生的網址通常是 HTTPS，所以這點通常沒問題。

方法 4：先不要開太高解析度
你的程式裡這段要有：

media_stream_constraints={
    "video": {
        "facingMode": {"ideal": facing_mode},
        "width": {"ideal": 640, "max": 960},
        "height": {"ideal": 480, "max": 720},
        "frameRate": {"ideal": 10, "max": 15},
    },
    "audio": False
},
這樣 iPhone 後鏡頭才不會解析度太高，導致 Railway 跑不動。

展示時最穩的操作順序
1. 用 iPhone Safari 打開 Railway 網址
2. 允許相機
3. 選「目前裝置鏡頭」
4. 選「後鏡頭」
5. 按 Start
6. 對準病床或模擬畫面
如果你要展示給老師看，建議先在同一台 iPhone 上測一次，確認 Safari 的相機權限已經開好。


2026-05-09 01:30:32.600 Uvicorn server started on 0.0.0.0:8080

已思考 2 秒鐘
這行代表 Railway 上的 Streamlit 服務已經成功啟動：

2026-05-09 01:30:32.600 Uvicorn server started on 0.0.0.0:8080
意思是：

你的 app.py 有跑起來
伺服器正在 0.0.0.0:8080 等待連線
所以這不是錯誤，是好消息。

你現在可以做這幾件事：

到 Railway 的 Networking

確認 Public Domain 對應的 port 是：

8080
打開 Railway 產生的公開網址

如果網頁能開，就代表部署成功。

如果你接下來是要用 iPhone Safari：

用 iPhone Safari 打開 Railway 網址

允許相機權限

在 App 左側選：

攝影機來源：目前裝置鏡頭
鏡頭：後鏡頭
按 Start

等畫面連線

如果畫面卡在連線，可以先重新整理 Safari，或先切成前鏡頭測試，再切回後鏡頭。


File "/app/app.py", line 13, in <module>
    from streamlit_webrtc import webrtc_streamer, WebRtcMode, VideoProcessorBase
File "/usr/local/lib/python3.11/site-packages/streamlit_webrtc/__init__.py", line 9, in <module>
    from .component import (
File "/usr/local/lib/python3.11/site-packages/streamlit_webrtc/component.py", line 44, in <module>
    from .webrtc import (
File "/usr/local/lib/python3.11/site-packages/streamlit_webrtc/webrtc.py", line 15, in <module>
    from .eventloop import get_global_event_loop
File "/usr/local/lib/python3.11/site-packages/streamlit_webrtc/eventloop.py", line 5, in <module>
    from tornado.platform.asyncio import BaseAsyncIOLoop

已思考 2 秒鐘
這個錯誤卡在：

from tornado.platform.asyncio import BaseAsyncIOLoop
代表 streamlit-webrtc 在載入時，跟你目前安裝到的 tornado 版本不相容。

你的程式第 13 行有用：

from streamlit_webrtc import webrtc_streamer, WebRtcMode, VideoProcessorBase
所以 Railway 一啟動就會先載入 streamlit-webrtc，如果版本不合就會直接掛掉。你的程式目前確實還是使用 streamlit-webrtc 做即時影像。


解法：固定 streamlit-webrtc 和 tornado 版本
請把你的 requirements.txt 改成這樣：

streamlit==1.37.1
streamlit-webrtc==0.47.9
streamlit-autorefresh
tornado==6.4.1
ultralytics
opencv-python-headless
numpy<2
Pillow
torch
torchvision
av
重點是加上：

tornado==6.4.1
不要讓它自動裝到太新的版本。

然後重新部署 Railway
流程：

1. 修改 requirements.txt
2. Push 到 GitHub
3. Railway 自動重新 Deploy
4. 看 Deploy Logs
如果 Railway 沒有自動重裝，可以在 Railway 裡按：

Redeploy
或：

Clear build cache / Rebuild
如果還是不行
把 requirements.txt 改成更保守的版本：

streamlit==1.35.0
streamlit-webrtc==0.47.7
streamlit-autorefresh
tornado==6.4.1
ultralytics
opencv-python-headless
numpy<2
Pillow
torch
torchvision
av
你現在的問題不是 app.py 邏輯錯
這次錯誤不是 YOLO、OpenCV 或相機設定，而是套件版本問題：

streamlit-webrtc
↓
需要 tornado 某些舊版 API
↓
目前環境 tornado 版本不合
↓
ImportError / 啟動失敗
所以先改 requirements.txt，通常就會解。


如果要使用其他裝置，可不可以生成一個網址或QR code，讓裝置去連接

已思考 9s
可以，可以在你的 App 裡產生一個 QR Code，讓另一台手機掃描後直接打開 Railway 網頁。

但要先分清楚兩種情況：

情況 1：另一支手機掃 QR code → 打開 Railway App → 用那支手機自己的鏡頭
✅ 可以，最簡單

情況 2：另一支手機掃 QR code → 只當攝影機 → 畫面回傳到你電腦上的同一個 Dashboard
⚠️ 比較複雜，需要另外做 WebRTC 房間或串流伺服器
你現在最適合做的是 情況 1：在 App 裡顯示 QR Code，手機掃描後直接開啟系統，然後選「目前裝置鏡頭 → 後鏡頭」。

要新增的功能
可以在側邊欄加入：

📱 手機連線 QR Code
掃描後用手機開啟此系統
手機掃描後就會進到你的 Railway App。

1. requirements.txt 加一行
請在 requirements.txt 加上：

qrcode[pil]
你的 requirements.txt 可以變成：

streamlit
streamlit-webrtc==0.47.9
streamlit-autorefresh
tornado==6.4.1
ultralytics
opencv-python-headless
numpy<2
Pillow
torch
torchvision
av
qrcode[pil]
2. app.py 最上面新增 import
在你的 app.py 上方 import 區加入：

import os
import qrcode
from io import BytesIO
3. 加入 QR Code 產生函式
放在 Helper 區附近即可：

def generate_qr_code(url):
    qr = qrcode.QRCode(
        version=1,
        box_size=8,
        border=2
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    return buffer
4. 在 Sidebar 加入 QR Code 區塊
可以放在：

st.sidebar.header("⚙️ 分析設定")
下面。

st.sidebar.markdown("### 📱 手機連線")

default_app_url = os.getenv("PUBLIC_APP_URL", "")

app_url = st.sidebar.text_input(
    "Railway 公開網址",
    value=default_app_url,
    placeholder="請貼上你的 Railway 網址，例如 https://xxx.up.railway.app"
)

if app_url:
    qr_buffer = generate_qr_code(app_url)

    st.sidebar.image(
        qr_buffer,
        caption="用手機掃描開啟系統",
        use_container_width=True
    )

    st.sidebar.caption("掃描後請選：目前裝置鏡頭 → 後鏡頭 → Start")
else:
    st.sidebar.info("貼上 Railway 網址後，這裡會產生 QR Code。")

st.sidebar.markdown("---")
5. Railway 可以設定環境變數
如果你不想每次手動貼網址，可以到 Railway 設定環境變數：

PUBLIC_APP_URL=https://你的railway網址.up.railway.app
然後程式裡這行就會自動讀到：

default_app_url = os.getenv("PUBLIC_APP_URL", "")
使用方式
你的電腦打開 Railway App 後，左側會出現 QR Code。

另一支 iPhone：

1. 打開相機掃 QR Code
2. 開啟 Railway 網頁
3. 選「目前裝置鏡頭」
4. 選「後鏡頭」
5. 按 Start
6. 允許 Safari 使用相機
這樣那支 iPhone 就可以直接當攝影機使用。

重要提醒
這個 QR Code 的作用是：

讓其他裝置快速打開你的系統
不是把手機鏡頭傳回你電腦上的原本頁面。

也就是說：

手機掃 QR Code → 手機自己開一個 App 畫面 → 手機自己偵測
如果你想要：

手機當攝影機
電腦看 Dashboard
那就要做「手機端上傳影像 / WebRTC 房間 / 外部串流 URL」，會比現在複雜很多。建議期末展示先用 QR Code 版本，最穩。


情況 2：另一支手機掃 QR code → 只當攝影機 → 畫面回傳到你電腦上的同一個 Dashboard
⚠️ 比較複雜，需要另外做 WebRTC 房間或串流伺服器

已思考 6s
可以做，而且可以設計成：

電腦開 Dashboard
↓
Dashboard 顯示 QR Code
↓
另一支 iPhone 掃 QR Code
↓
iPhone 開啟「攝影機上傳頁面」
↓
iPhone 後鏡頭畫面持續傳到 Railway
↓
電腦 Dashboard 顯示 iPhone 畫面並做 YOLO 偵測
這樣就符合你說的：

另一支手機掃 QR code → 只當攝影機 → 畫面回傳到電腦上的同一個 Dashboard
但這不能只靠 Streamlit 原本的 webrtc_streamer
你現在的 Streamlit WebRTC 是：

誰打開網頁，就用誰的鏡頭
如果要「手機當攝影機、電腦看結果」，需要多一個機制：

手機端：負責拍攝與上傳影像
伺服器端：接收手機影像
電腦端：讀取最新影像並顯示結果
所以比較適合改成：

FastAPI + Streamlit
或乾脆改成：

FastAPI 網頁版 Dashboard
我建議你用這種架構
電腦 Dashboard
顯示：

QR Code
目前姿勢
持續秒數
警報狀態
iPhone 傳回來的畫面
iPhone 攝影端
掃 QR Code 後進入一個簡單頁面：

開啟後鏡頭
每 0.5 秒截一張畫面
傳到 Railway
Railway 伺服器
收到 iPhone 傳來的畫面後：

儲存最新畫面
YOLO 偵測姿勢
更新 Dashboard
優點
這種方式比外部 IP Camera、ngrok、Cloudflare Tunnel 更適合展示，因為：

不用裝 iPhone IP Camera App
不用設定 ngrok
不用 Cloudflare Tunnel
手機只要掃 QR Code
老師看到會覺得比較完整
缺點
它不是純 Streamlit 小改而已，需要我幫你把程式改成比較像：

app.py
templates/camera.html
requirements.txt
Dockerfile
或一個完整的：

FastAPI + HTML + YOLO
版本。

最推薦做法
我建議下一步直接幫你做一個 Railway 可部署版本：

電腦端：
/dashboard

手機端：
/camera

手機掃描 QR Code 後會打開 /camera
然後手機後鏡頭會把畫面傳回 /dashboard
這樣你的展示流程會變成：

1. 電腦打開 Railway Dashboard
2. 畫面出現 QR Code
3. iPhone 掃 QR Code
4. iPhone 按「開始傳送鏡頭」
5. 電腦 Dashboard 看到 iPhone 畫面與姿勢偵測結果
這是可以做的，只是程式會從目前的 Streamlit 即時鏡頭版，改成「手機上傳影像到伺服器」版。


最推薦做法

我建議下一步直接幫你做一個 Railway 可部署版本：

電腦端：
/dashboard

手機端：
/camera

手機掃描 QR Code 後會打開 /camera
然後手機後鏡頭會把畫面傳回 /dashboard

這樣你的展示流程會變成：

1. 電腦打開 Railway Dashboard
2. 畫面出現 QR Code
3. iPhone 掃 QR Code
4. iPhone 按「開始傳送鏡頭」
5. 電腦 Dashboard 看到 iPhone 畫面與姿勢偵測結果

這是可以做的，只是程式會從目前的 Streamlit 即時鏡頭版，改成「手機上傳影像到伺服器」版。

以我現在的程式碼'要怎麼修改

已思考 17s
可以，但這個功能不是在你原本 Streamlit 裡加幾行就好，因為你現在的程式是「誰打開網頁，就使用誰的鏡頭」的 streamlit-webrtc 架構。你目前程式中有 streamlit_webrtc、VideoProcessorBase、webrtc_streamer()，所以它是目前裝置鏡頭模式。


如果要變成：

電腦開 Dashboard
iPhone 掃 QR Code
iPhone 只負責拍攝
畫面回傳到電腦 Dashboard
建議把程式改成 FastAPI 版本。核心的 YOLO 姿勢判斷邏輯可以沿用，但要移除 streamlit-webrtc。

下面給你一組 Railway 可部署的完整版本。

1. app.py
把原本的 app.py 全部替換成這份：

import os
import cv2
import math
import time
import base64
import threading
from io import BytesIO

import numpy as np
import qrcode
from ultralytics import YOLO

from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse, JSONResponse, Response, FileResponse
from fastapi.middleware.cors import CORSMiddleware


# =========================
# FastAPI app
# =========================
app = FastAPI(title="長照睡姿固定過久警報系統")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================
# Load YOLO model
# =========================
model = YOLO("yolov8n-pose.pt")


# =========================
# Shared state
# =========================
class AppState:
    def __init__(self):
        self.lock = threading.Lock()

        self.current_posture = "尚未偵測"
        self.last_posture = "尚未偵測"

        self.start_time = time.time()
        self.duration = 0.0

        self.alarm = False
        self.alarm_acknowledged = False

        self.monitoring = False
        self.alarm_threshold = 10

        self.latest_image_base64 = ""
        self.last_update_time = ""


state = AppState()


# =========================
# Helper functions
# =========================
def get_base_url(request: Request):
    """
    Railway 通常會透過反向代理轉發，所以用 header 判斷公開網址。
    如果你有在 Railway 設定 PUBLIC_APP_URL，也會優先使用。
    """
    public_url = os.getenv("PUBLIC_APP_URL", "").strip()

    if public_url:
        return public_url.rstrip("/")

    proto = request.headers.get("x-forwarded-proto", request.url.scheme)
    host = request.headers.get("host", "")

    return f"{proto}://{host}".rstrip("/")


def to_xy(point):
    return float(point[0]), float(point[1])


def dist(p1, p2):
    x1, y1 = to_xy(p1)
    x2, y2 = to_xy(p2)
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def resize_frame(img, max_width=640):
    h, w = img.shape[:2]

    if w > max_width:
        scale = max_width / w
        new_h = int(h * scale)
        img = cv2.resize(img, (max_width, new_h))

    return img


# =========================
# 姿勢分類
# =========================
def classify_posture(results):
    current_posture = "無人躺著"

    if results is None or len(results) == 0:
        return current_posture

    result = results[0]

    if result.keypoints is None:
        return current_posture

    if result.keypoints.xy is None or len(result.keypoints.xy) == 0:
        return current_posture

    if result.keypoints.conf is None or len(result.keypoints.conf) == 0:
        return current_posture

    kps = result.keypoints.xy[0]
    conf = result.keypoints.conf[0]

    if len(kps) < 13:
        return current_posture

    if float(conf.max()) <= 0.5:
        return current_posture

    shoulder_width = dist(kps[5], kps[6])

    torso_length = (
        dist(kps[5], kps[11]) +
        dist(kps[6], kps[12])
    ) / 2

    left_shoulder_conf = float(conf[5])
    right_shoulder_conf = float(conf[6])

    is_side = (
        left_shoulder_conf < 0.4
        or right_shoulder_conf < 0.4
        or (
            torso_length > 0
            and (shoulder_width / torso_length) < 0.5
        )
    )

    if is_side:
        left_ear_conf = float(conf[3])
        right_ear_conf = float(conf[4])

        if (right_ear_conf + right_shoulder_conf) > (
            left_ear_conf + left_shoulder_conf
        ) + 0.2:
            current_posture = "左側躺"

        elif (left_ear_conf + left_shoulder_conf) > (
            right_ear_conf + right_shoulder_conf
        ) + 0.2:
            current_posture = "右側躺"

        else:
            if dist(kps[0], kps[3]) < dist(kps[0], kps[4]):
                current_posture = "右側躺"
            else:
                current_posture = "左側躺"

    else:
        current_posture = "仰躺"

    return current_posture


# =========================
# Process image
# =========================
def process_image_frame(img):
    img = resize_frame(img, max_width=640)

    try:
        results = model(img, verbose=False, imgsz=640)
        current_posture = classify_posture(results)
        annotated = results[0].plot()

    except Exception as e:
        current_posture = "偵測錯誤"
        annotated = img.copy()

        cv2.putText(
            annotated,
            f"Detection error: {str(e)[:80]}",
            (30, 55),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 0, 255),
            2,
            cv2.LINE_AA
        )

    now = time.time()

    with state.lock:
        if state.monitoring:
            if current_posture == state.last_posture:
                state.duration = now - state.start_time

            else:
                state.last_posture = current_posture
                state.current_posture = current_posture
                state.start_time = now
                state.duration = 0.0
                state.alarm = False
                state.alarm_acknowledged = False

            if (
                state.duration >= state.alarm_threshold
                and current_posture != "無人躺著"
                and current_posture != "偵測錯誤"
                and not state.alarm_acknowledged
            ):
                state.alarm = True

            else:
                if (
                    current_posture == "無人躺著"
                    or current_posture == "偵測錯誤"
                    or state.alarm_acknowledged
                ):
                    state.alarm = False

            state.current_posture = current_posture

        else:
            state.duration = 0.0
            state.alarm = False
            state.current_posture = current_posture

        monitor_text = "Monitoring" if state.monitoring else "Stopped"

        posture_map = {
            "無人躺著": "No person",
            "左側躺": "Left side",
            "右側躺": "Right side",
            "仰躺": "Supine",
            "偵測錯誤": "Error",
            "尚未偵測": "Not detected"
        }

        posture_en = posture_map.get(state.current_posture, "Unknown")

        info_text = (
            f"{monitor_text} | "
            f"Posture: {posture_en} | "
            f"Time: {int(state.duration)} sec"
        )

        cv2.rectangle(
            annotated,
            (20, 20),
            (min(900, annotated.shape[1] - 20), 70),
            (0, 0, 0),
            -1
        )

        cv2.putText(
            annotated,
            info_text,
            (30, 55),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2,
            cv2.LINE_AA
        )

        if state.alarm:
            cv2.rectangle(
                annotated,
                (0, 0),
                (annotated.shape[1], annotated.shape[0]),
                (0, 0, 255),
                10
            )

            cv2.putText(
                annotated,
                "ALARM",
                (30, 115),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.7,
                (0, 0, 255),
                4,
                cv2.LINE_AA
            )

    return annotated


def image_to_base64(img):
    ok, buffer = cv2.imencode(".jpg", img)

    if not ok:
        return ""

    return base64.b64encode(buffer).decode("utf-8")


def generate_qr_png(url):
    qr = qrcode.QRCode(
        version=1,
        box_size=8,
        border=2
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    return buffer.getvalue()


# =========================
# Routes
# =========================
@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
        <head>
            <meta http-equiv="refresh" content="0; url=/dashboard">
        </head>
        <body>
            <p>Redirecting to dashboard...</p>
        </body>
    </html>
    """


@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    base_url = get_base_url(request)
    camera_url = f"{base_url}/camera"

    return f"""
    <!DOCTYPE html>
    <html lang="zh-Hant">
    <head>
        <meta charset="UTF-8">
        <title>長照睡姿固定過久警報系統 Dashboard</title>
        <style>
            body {{
                margin: 0;
                font-family: Arial, "Microsoft JhengHei", sans-serif;
                background: #f5f7fb;
                color: #1f2937;
            }}

            .container {{
                max-width: 1200px;
                margin: 0 auto;
                padding: 24px;
            }}

            .title {{
                font-size: 32px;
                font-weight: 800;
                color: #1f3c88;
                margin-bottom: 6px;
            }}

            .subtitle {{
                color: #64748b;
                margin-bottom: 24px;
            }}

            .grid {{
                display: grid;
                grid-template-columns: 1.2fr 0.8fr;
                gap: 24px;
            }}

            .card {{
                background: white;
                border-radius: 18px;
                padding: 20px;
                box-shadow: 0 10px 25px rgba(15, 23, 42, 0.08);
                border: 1px solid #e5e7eb;
            }}

            .video-box {{
                width: 100%;
                background: #111827;
                border-radius: 16px;
                min-height: 420px;
                display: flex;
                align-items: center;
                justify-content: center;
                overflow: hidden;
            }}

            #latestImage {{
                max-width: 100%;
                width: 100%;
                border-radius: 16px;
            }}

            .metrics {{
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 12px;
                margin-bottom: 18px;
            }}

            .metric {{
                background: #f8fbff;
                border: 1px solid #dfe8f3;
                border-radius: 14px;
                padding: 16px;
                text-align: center;
            }}

            .metric-label {{
                color: #64748b;
                font-size: 14px;
                margin-bottom: 8px;
            }}

            .metric-value {{
                color: #1f3c88;
                font-size: 24px;
                font-weight: 800;
            }}

            button {{
                border: none;
                border-radius: 12px;
                padding: 12px 18px;
                font-size: 16px;
                font-weight: 700;
                cursor: pointer;
                margin: 4px;
            }}

            .start {{
                background: #2563eb;
                color: white;
            }}

            .stop {{
                background: #475569;
                color: white;
            }}

            .ack {{
                background: #16a34a;
                color: white;
            }}

            .alert {{
                background: #fff1f2;
                border: 1px solid #fda4af;
                color: #b91c1c;
                border-radius: 12px;
                padding: 16px;
                font-size: 18px;
                font-weight: 700;
                margin-top: 14px;
            }}

            .normal {{
                background: #f0fdf4;
                border: 1px solid #86efac;
                color: #166534;
                border-radius: 12px;
                padding: 16px;
                font-size: 18px;
                font-weight: 700;
                margin-top: 14px;
            }}

            .qr {{
                width: 220px;
                border: 1px solid #e5e7eb;
                border-radius: 14px;
                padding: 8px;
                background: white;
            }}

            input {{
                padding: 10px;
                border: 1px solid #cbd5e1;
                border-radius: 10px;
                font-size: 16px;
                width: 80px;
            }}

            .hint {{
                color: #64748b;
                font-size: 14px;
                line-height: 1.6;
            }}

            @media (max-width: 900px) {{
                .grid {{
                    grid-template-columns: 1fr;
                }}

                .metrics {{
                    grid-template-columns: 1fr;
                }}
            }}
        </style>
    </head>

    <body>
        <div class="container">
            <div class="title">🛌 長照睡姿固定過久警報系統</div>
            <div class="subtitle">電腦端 Dashboard：顯示 iPhone 傳回的畫面與姿勢偵測結果</div>

            <div class="grid">
                <div class="card">
                    <h2>1. 即時影像</h2>
                    <div class="video-box">
                        <img id="latestImage" src="" alt="尚未收到手機影像">
                    </div>
                    <p class="hint">請用 iPhone 掃描右側 QR Code，進入攝影機頁面後按「開始傳送」。</p>
                </div>

                <div class="card">
                    <h2>2. 手機攝影機連線</h2>
                    <img class="qr" src="/qr.png" alt="QR Code">
                    <p class="hint">
                        掃描後會開啟：<br>
                        <b>{camera_url}</b>
                    </p>

                    <hr>

                    <h2>3. 控制面板</h2>

                    <label>警報秒數：</label>
                    <input id="thresholdInput" type="number" min="3" max="120" value="10">
                    <button onclick="updateThreshold()" class="start">更新秒數</button>

                    <br><br>

                    <button onclick="startMonitoring()" class="start">▶️ Start</button>
                    <button onclick="stopMonitoring()" class="stop">⏹ Stop</button>
                    <button onclick="ackAlarm()" class="ack">✅ 確認警報</button>

                    <hr>

                    <h2>4. 摘要資訊</h2>

                    <div class="metrics">
                        <div class="metric">
                            <div class="metric-label">目前姿勢</div>
                            <div id="posture" class="metric-value">尚未偵測</div>
                        </div>

                        <div class="metric">
                            <div class="metric-label">持續時間</div>
                            <div id="duration" class="metric-value">0 秒</div>
                        </div>

                        <div class="metric">
                            <div class="metric-label">系統狀態</div>
                            <div id="monitoring" class="metric-value">停止</div>
                        </div>
                    </div>

                    <div id="alarmBox" class="normal">✅ 目前尚未觸發警報</div>

                    <audio id="alarmAudio" src="/alarm.mp3" loop></audio>
                </div>
            </div>
        </div>

        <script>
            async function fetchState() {{
                try {{
                    const res = await fetch("/state");
                    const data = await res.json();

                    document.getElementById("posture").innerText = data.current_posture;
                    document.getElementById("duration").innerText = data.duration + " 秒";
                    document.getElementById("monitoring").innerText = data.monitoring ? "監測中" : "停止";
                    document.getElementById("thresholdInput").value = data.alarm_threshold;

                    if (data.latest_image_base64) {{
                        document.getElementById("latestImage").src =
                            "data:image/jpeg;base64," + data.latest_image_base64;
                    }}

                    const alarmBox = document.getElementById("alarmBox");
                    const alarmAudio = document.getElementById("alarmAudio");

                    if (data.alarm) {{
                        alarmBox.className = "alert";
                        alarmBox.innerText = "🚨 偵測到同一姿勢維持過久，請協助翻身";

                        alarmAudio.play().catch(() => {{
                            console.log("Autoplay blocked.");
                        }});
                    }} else {{
                        alarmBox.className = "normal";
                        alarmBox.innerText = "✅ 目前尚未觸發警報";
                        alarmAudio.pause();
                        alarmAudio.currentTime = 0;
                    }}

                }} catch (err) {{
                    console.log(err);
                }}
            }}

            async function startMonitoring() {{
                await fetch("/control", {{
                    method: "POST",
                    headers: {{ "Content-Type": "application/json" }},
                    body: JSON.stringify({{ action: "start" }})
                }});
                fetchState();
            }}

            async function stopMonitoring() {{
                await fetch("/control", {{
                    method: "POST",
                    headers: {{ "Content-Type": "application/json" }},
                    body: JSON.stringify({{ action: "stop" }})
                }});
                fetchState();
            }}

            async function ackAlarm() {{
                await fetch("/control", {{
                    method: "POST",
                    headers: {{ "Content-Type": "application/json" }},
                    body: JSON.stringify({{ action: "ack" }})
                }});
                fetchState();
            }}

            async function updateThreshold() {{
                const threshold = parseInt(document.getElementById("thresholdInput").value);

                await fetch("/control", {{
                    method: "POST",
                    headers: {{ "Content-Type": "application/json" }},
                    body: JSON.stringify({{
                        action: "threshold",
                        alarm_threshold: threshold
                    }})
                }});

                fetchState();
            }}

            setInterval(fetchState, 1000);
            fetchState();
        </script>
    </body>
    </html>
    """


@app.get("/camera", response_class=HTMLResponse)
async def camera_page():
    return """
    <!DOCTYPE html>
    <html lang="zh-Hant">
    <head>
        <meta charset="UTF-8">
        <title>手機攝影機端</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, "Microsoft JhengHei", sans-serif;
                background: #0f172a;
                color: white;
                text-align: center;
            }

            .container {
                padding: 20px;
            }

            h1 {
                font-size: 28px;
                margin-bottom: 8px;
            }

            p {
                color: #cbd5e1;
                line-height: 1.6;
            }

            video {
                width: 100%;
                max-width: 520px;
                border-radius: 18px;
                background: black;
                margin-top: 16px;
            }

            button {
                border: none;
                border-radius: 14px;
                padding: 14px 22px;
                font-size: 18px;
                font-weight: 800;
                cursor: pointer;
                margin: 8px;
            }

            .start {
                background: #22c55e;
                color: white;
            }

            .stop {
                background: #ef4444;
                color: white;
            }

            .status {
                margin-top: 16px;
                padding: 14px;
                border-radius: 12px;
                background: #1e293b;
                color: #e2e8f0;
            }
        </style>
    </head>

    <body>
        <div class="container">
            <h1>📱 手機攝影機端</h1>
            <p>
                請允許使用相機，並將手機後鏡頭對準病床或模擬畫面。<br>
                這個頁面會定時把影像傳回電腦 Dashboard。
            </p>

            <video id="video" autoplay playsinline muted></video>

            <br>

            <button class="start" onclick="startCamera()">▶️ 開始傳送</button>
            <button class="stop" onclick="stopCamera()">⏹ 停止傳送</button>

            <div id="status" class="status">尚未開始</div>

            <canvas id="canvas" style="display:none;"></canvas>
        </div>

        <script>
            let video = document.getElementById("video");
            let canvas = document.getElementById("canvas");
            let statusBox = document.getElementById("status");

            let stream = null;
            let sending = false;
            let timer = null;

            async function startCamera() {
                try {
                    stream = await navigator.mediaDevices.getUserMedia({
                        video: {
                            facingMode: { ideal: "environment" },
                            width: { ideal: 640, max: 960 },
                            height: { ideal: 480, max: 720 },
                            frameRate: { ideal: 10, max: 15 }
                        },
                        audio: false
                    });

                    video.srcObject = stream;
                    sending = true;

                    statusBox.innerText = "✅ 已開啟相機，正在傳送影像到 Dashboard";

                    timer = setInterval(captureAndSend, 800);

                } catch (err) {
                    statusBox.innerText = "❌ 無法開啟相機：" + err;
                }
            }

            function stopCamera() {
                sending = false;

                if (timer) {
                    clearInterval(timer);
                    timer = null;
                }

                if (stream) {
                    stream.getTracks().forEach(track => track.stop());
                    stream = null;
                }

                video.srcObject = null;
                statusBox.innerText = "已停止傳送";
            }

            async function captureAndSend() {
                if (!sending || !video.videoWidth) {
                    return;
                }

                const maxWidth = 640;
                const scale = maxWidth / video.videoWidth;
                const width = maxWidth;
                const height = Math.round(video.videoHeight * scale);

                canvas.width = width;
                canvas.height = height;

                const ctx = canvas.getContext("2d");
                ctx.drawImage(video, 0, 0, width, height);

                canvas.toBlob(async function(blob) {
                    if (!blob) return;

                    const formData = new FormData();
                    formData.append("file", blob, "frame.jpg");

                    try {
                        const res = await fetch("/upload", {
                            method: "POST",
                            body: formData
                        });

                        if (res.ok) {
                            statusBox.innerText = "✅ 影像傳送中：" + new Date().toLocaleTimeString();
                        } else {
                            statusBox.innerText = "⚠️ 傳送失敗";
                        }

                    } catch (err) {
                        statusBox.innerText = "❌ 傳送錯誤：" + err;
                    }

                }, "image/jpeg", 0.7);
            }
        </script>
    </body>
    </html>
    """


@app.get("/qr.png")
async def qr_png(request: Request):
    base_url = get_base_url(request)
    camera_url = f"{base_url}/camera"

    png = generate_qr_png(camera_url)

    return Response(content=png, media_type="image/png")


@app.post("/upload")
async def upload_frame(file: UploadFile = File(...)):
    image_bytes = await file.read()

    img_array = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    if img is None:
        return JSONResponse(
            {"ok": False, "message": "無法讀取影像"},
            status_code=400
        )

    annotated = process_image_frame(img)
    img_b64 = image_to_base64(annotated)

    with state.lock:
        state.latest_image_base64 = img_b64
        state.last_update_time = time.strftime("%Y-%m-%d %H:%M:%S")

    return {"ok": True}


@app.get("/state")
async def get_state():
    with state.lock:
        return {
            "current_posture": state.current_posture,
            "last_posture": state.last_posture,
            "duration": int(state.duration),
            "alarm": state.alarm,
            "alarm_acknowledged": state.alarm_acknowledged,
            "monitoring": state.monitoring,
            "alarm_threshold": state.alarm_threshold,
            "latest_image_base64": state.latest_image_base64,
            "last_update_time": state.last_update_time,
        }


@app.post("/control")
async def control(payload: dict):
    action = payload.get("action", "")

    with state.lock:
        if action == "start":
            state.monitoring = True
            state.start_time = time.time()
            state.duration = 0.0
            state.alarm = False
            state.alarm_acknowledged = False
            state.last_posture = state.current_posture

        elif action == "stop":
            state.monitoring = False
            state.duration = 0.0
            state.alarm = False
            state.alarm_acknowledged = False
            state.current_posture = "尚未偵測"
            state.last_posture = "尚未偵測"

        elif action == "ack":
            state.alarm_acknowledged = True
            state.alarm = False

        elif action == "threshold":
            threshold = int(payload.get("alarm_threshold", 10))
            threshold = max(3, min(120, threshold))
            state.alarm_threshold = threshold

    return {"ok": True}


@app.get("/alarm.mp3")
async def alarm_mp3():
    path = "alarm.mp3"

    if os.path.exists(path):
        return FileResponse(path, media_type="audio/mpeg")

    return Response(status_code=404)
2. requirements.txt
這版不要再用 Streamlit，所以你的 requirements.txt 改成：

fastapi
uvicorn[standard]
python-multipart
ultralytics
opencv-python-headless
numpy<2
Pillow
torch
torchvision
qrcode[pil]
請把這些刪掉：

streamlit
streamlit-webrtc
streamlit-autorefresh
av
tornado
3. Dockerfile
Railway 的 Dockerfile 改成：

FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    libgomp1 \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
4. Railway 檔案結構
你的 GitHub 專案最後應該長這樣：

app.py
requirements.txt
Dockerfile
alarm.mp3
alarm.mp3 可以不放，不影響影像功能，只是警報聲不會播放。

5. 使用方式
部署成功後：

1. 電腦打開：
   https://你的railway網址/dashboard

2. Dashboard 右側會出現 QR Code

3. iPhone 用相機掃 QR Code

4. iPhone 會打開：
   https://你的railway網址/camera

5. iPhone 按「開始傳送」

6. 電腦 Dashboard 就會看到 iPhone 傳回的畫面與姿勢偵測結果
6. 你原本程式要怎麼對應修改？
可以這樣理解：

原本：
Streamlit + streamlit-webrtc
誰開網頁，就用誰的鏡頭

改成：
FastAPI + HTML/JavaScript
iPhone /camera 負責拍攝並上傳
電腦 /dashboard 負責顯示結果
你的這些部分可以沿用：

YOLO 模型載入
classify_posture()
dist()
警報秒數邏輯
alarm.mp3
但是這些要移除：

streamlit
streamlit-webrtc
st.sidebar
st.columns
VideoProcessorBase
webrtc_streamer()
st_autorefresh
因為這版已經不是 Streamlit 介面，而是用 /dashboard 和 /camera 兩個網頁來分工。


為什麼apple手機沒法即時撥聲音

已思考幾秒鐘
因為 iPhone / iPad 的 Safari 對「自動播放聲音」限制很嚴格。
簡單說：Apple 不允許網頁在使用者沒有主動操作前，自動播放有聲音的音訊。

所以你的警報聲在電腦、Android 可能可以自動響，但在 iPhone 上常常不會自動播放。

為什麼 Apple 手機不讓它自動播放？
主要原因是 Apple 的瀏覽器政策：

網頁不能在沒有使用者互動的情況下，自動播放有聲音的 audio
也就是說，這種寫法在 iPhone 很可能會被擋：

<audio autoplay loop>
  <source src="alarm.mp3" type="audio/mp3">
</audio>
即使你用 JavaScript：

audio.play()
如果不是在使用者按按鈕、點擊畫面後觸發，iPhone Safari 也可能會擋掉。

你的 App 為什麼會遇到？
你的警報邏輯是：

系統偵測到姿勢太久
↓
自動觸發 alarm
↓
網頁自動播放 alarm.mp3
但在 iPhone 看來，這個播放動作不是使用者主動點擊，所以它會阻止播放。

最穩解法：一定要先讓使用者按一次「啟用警報聲」
你現在已經有類似這個按鈕：

🔊 啟用警報聲
這是正確方向。

但在 iPhone 上，這個按鈕不能只是把：

st.session_state.sound_enabled = True
改成 True 而已。

它最好要在使用者按下時，真的播放一次很短的聲音，讓 Safari 知道：

這個使用者允許這個網頁播放聲音
最推薦的設計
在手機端或 Dashboard 上放一個明顯按鈕：

🔊 啟用警報聲 / 測試警報聲
使用者一開始要先按一次。

流程變成：

1. 開啟 App
2. 按「🔊 啟用警報聲」
3. 系統播放一次測試音
4. 之後警報觸發時，才比較有機會播放聲音
但要注意
就算使用者按過一次，iPhone 還是可能在某些情況下擋掉，例如：

手機靜音模式開啟
音量太小
Safari 分頁在背景
低耗電模式
網頁重新整理後音訊權限狀態重置
所以 iPhone 上不能保證 100% 自動播放警報聲。

最實際的做法
你的系統建議設計成：

主要警報：畫面紅框、文字警示
輔助警報：聲音播放
備用方式：手動播放警報聲按鈕
也就是警報觸發時，畫面一定要顯示：

🚨 偵測到姿勢持續過久，請協助翻身
同時顯示一個按鈕：

🔊 播放警報聲
這樣即使 iPhone 擋掉自動播放，使用者還是可以手動按。

如果你現在用 FastAPI Dashboard 版本
可以在 Dashboard 裡把警報音改成這種概念：

<button onclick="enableSound()">🔊 啟用警報聲</button>
<audio id="alarmAudio" src="/alarm.mp3" loop></audio>

<script>
let soundEnabled = false;

function enableSound() {
    const audio = document.getElementById("alarmAudio");
    audio.play().then(() => {
        audio.pause();
        audio.currentTime = 0;
        soundEnabled = true;
        alert("警報聲已啟用");
    }).catch(() => {
        alert("瀏覽器阻擋音訊，請確認手機音量與 Safari 權限");
    });
}

function playAlarmIfAllowed() {
    const audio = document.getElementById("alarmAudio");

    if (soundEnabled) {
        audio.play().catch(() => {
            console.log("iPhone Safari blocked autoplay.");
        });
    }
}
</script>
然後當警報觸發時，不是直接 audio.play()，而是呼叫：

playAlarmIfAllowed();
結論
Apple 手機不能即時自動播放聲音，不是你程式壞掉，而是 iOS Safari 的安全與使用者體驗限制。

最穩的展示方式是：

進入 App 後先按「🔊 啟用警報聲」
警報觸發時畫面一定要紅色提示
聲音能播就播
如果被擋，就提供「手動播放警報聲」按鈕
所以你的警報系統在 iPhone 上應該設計成「聲音輔助」，不要只依賴自動聲音。


import streamlit as st
import streamlit.components.v1 as components

import cv2
import math
import av
import time
import threading
import base64
from pathlib import Path

from ultralytics import YOLO
from streamlit_webrtc import webrtc_streamer, WebRtcMode, VideoProcessorBase
from streamlit_autorefresh import st_autorefresh

=========================
Page config
=========================
st.set_page_config(
page_title="長照睡姿固定過久警報系統",
page_icon="🛌",
layout="wide"
)

=========================
Custom style
=========================
st.markdown("""

""", unsafe_allow_html=True)

=========================
Title
=========================
st.markdown(
'🛌 長照睡姿固定過久警報系統',
unsafe_allow_html=True
)

st.markdown(
'使用影像分析臥床姿勢變化，協助照護員及早發現長時間未翻身狀況。',
unsafe_allow_html=True
)

=========================
Load YOLO model
=========================
@st.cache_resource
def load_model():
return YOLO("yolov8n-pose.pt")

model = load_model()

=========================
Shared state
=========================
class AppState:
def init(self):
self.lock = threading.Lock()

    self.current_posture = "無人躺著"
    self.last_posture = "無人躺著"

    self.start_time = time.time()
    self.duration = 0.0

    self.alarm = False
    self.alarm_acknowledged = False

    self.monitoring = False
if "shared_state" not in st.session_state:
st.session_state.shared_state = AppState()

shared_state = st.session_state.shared_state

if "sound_enabled" not in st.session_state:
st.session_state.sound_enabled = False

if "test_alarm_sound" not in st.session_state:
st.session_state.test_alarm_sound = False

=========================
Helper
=========================
def to_xy(point):
return float(point[0]), float(point[1])

def dist(p1, p2):
x1, y1 = to_xy(p1)
x2, y2 = to_xy(p2)

return math.sqrt(
    (x1 - x2) ** 2 +
    (y1 - y2) ** 2
)
=========================
姿勢分類
=========================
def classify_posture(results):
current_posture = "無人躺著"

if results is None or len(results) == 0:
    return current_posture

result = results[0]

if result.keypoints is None:
    return current_posture

if result.keypoints.xy is None or len(result.keypoints.xy) == 0:
    return current_posture

if result.keypoints.conf is None or len(result.keypoints.conf) == 0:
    return current_posture

kps = result.keypoints.xy[0]
conf = result.keypoints.conf[0]

if len(kps) < 13:
    return current_posture

if float(conf.max()) <= 0.5:
    return current_posture

shoulder_width = dist(kps[5], kps[6])

torso_length = (
    dist(kps[5], kps[11]) +
    dist(kps[6], kps[12])
) / 2

left_shoulder_conf = float(conf[5])
right_shoulder_conf = float(conf[6])

is_side = (
    left_shoulder_conf < 0.4
    or right_shoulder_conf < 0.4
    or (
        torso_length > 0
        and (shoulder_width / torso_length) < 0.5
    )
)

if is_side:
    left_ear_conf = float(conf[3])
    right_ear_conf = float(conf[4])

    if (right_ear_conf + right_shoulder_conf) > (
        left_ear_conf + left_shoulder_conf
    ) + 0.2:
        current_posture = "左側躺"

    elif (left_ear_conf + left_shoulder_conf) > (
        right_ear_conf + right_shoulder_conf
    ) + 0.2:
        current_posture = "右側躺"

    else:
        if dist(kps[0], kps[3]) < dist(kps[0], kps[4]):
            current_posture = "右側躺"
        else:
            current_posture = "左側躺"

else:
    current_posture = "仰躺"

return current_posture
=========================
Alarm sound
=========================
def render_loop_alarm():
audio_file = Path("alarm.mp3")

if not audio_file.exists():
    st.warning("⚠️ 找不到 alarm.mp3，請確認 alarm.mp3 有放在 app.py 同一層。")
    return

audio_bytes = audio_file.read_bytes()
b64 = base64.b64encode(audio_bytes).decode()

st.markdown(
    """
    <div class="sound-box">
        🔊 警報聲已觸發。若瀏覽器沒有自動播放，請按下方「播放警報聲」按鈕。
    </div>
    """,
    unsafe_allow_html=True
)

audio_html = f"""
<div style="margin-top: 12px;">
    <audio id="alarmAudio" loop>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        你的瀏覽器不支援音訊播放。
    </audio>

    <button onclick="playAlarm()" 
        style="
            background-color:#dc2626;
            color:white;
            border:none;
            border-radius:10px;
            padding:12px 20px;
            font-size:18px;
            font-weight:700;
            cursor:pointer;
            margin-right:10px;
        ">
        🔊 播放警報聲
    </button>

    <button onclick="stopAlarm()" 
        style="
            background-color:#4b5563;
            color:white;
            border:none;
            border-radius:10px;
            padding:12px 20px;
            font-size:18px;
            font-weight:700;
            cursor:pointer;
        ">
        ⏹ 停止警報聲
    </button>

    <script>
        const audio = document.getElementById("alarmAudio");

        function playAlarm() {{
            audio.currentTime = 0;
            audio.play();
        }}

        function stopAlarm() {{
            audio.pause();
            audio.currentTime = 0;
        }}

        audio.play().catch(function(error) {{
            console.log("Autoplay was blocked by browser.");
        }});
    </script>
</div>
"""

components.html(audio_html, height=100)
=========================
Sidebar
=========================
st.sidebar.header("⚙️ 分析設定")

alarm_threshold = st.sidebar.slider(
"同姿勢維持幾秒觸發警報",
min_value=3,
max_value=60,
value=10,
step=1
)

if st.sidebar.button("🔊 啟用警報聲"):
st.session_state.sound_enabled = True
st.sidebar.success("警報聲已啟用")

if st.sidebar.button("🔔 測試警報聲"):
st.session_state.sound_enabled = True
st.session_state.test_alarm_sound = True

st.sidebar.markdown("---")

=========================
Start button
=========================
if st.sidebar.button("▶️ Start"):
with shared_state.lock:
shared_state.monitoring = True
shared_state.start_time = time.time()
shared_state.duration = 0.0
shared_state.alarm = False
shared_state.alarm_acknowledged = False
shared_state.last_posture = shared_state.current_posture

=========================
Stop button
=========================
if st.sidebar.button("⏹ Stop"):
with shared_state.lock:
shared_state.monitoring = False
shared_state.duration = 0.0
shared_state.alarm = False
shared_state.alarm_acknowledged = False
shared_state.current_posture = "無人躺著"
shared_state.last_posture = "無人躺著"

st.session_state.test_alarm_sound = False
st.sidebar.markdown("---")

st.sidebar.info(
"按下 Start 後開始監測；Stop 會停止並重新計算。"
)

每秒刷新
st_autorefresh(interval=1000, key="refresh")

=========================
Video Processor
=========================
class PoseVideoProcessor(VideoProcessorBase):
def recv(self, frame):
img = frame.to_ndarray(format="bgr24")

    try:
        results = model(img, verbose=False)
        current_posture = classify_posture(results)
        annotated = results[0].plot()

    except Exception as e:
        current_posture = "偵測錯誤"
        annotated = img.copy()

        cv2.putText(
            annotated,
            f"Detection error: {str(e)[:80]}",
            (30, 55),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 0, 255),
            2,
            cv2.LINE_AA
        )

    now = time.time()

    with shared_state.lock:
        if shared_state.monitoring:
            if current_posture == shared_state.last_posture:
                shared_state.duration = now - shared_state.start_time

            else:
                shared_state.last_posture = current_posture
                shared_state.current_posture = current_posture
                shared_state.start_time = now
                shared_state.duration = 0.0
                shared_state.alarm = False
                shared_state.alarm_acknowledged = False

            if (
                shared_state.duration >= alarm_threshold
                and current_posture != "無人躺著"
                and current_posture != "偵測錯誤"
                and not shared_state.alarm_acknowledged
            ):
                shared_state.alarm = True

            else:
                if (
                    current_posture == "無人躺著"
                    or current_posture == "偵測錯誤"
                    or shared_state.alarm_acknowledged
                ):
                    shared_state.alarm = False

            shared_state.current_posture = current_posture

        else:
            shared_state.duration = 0.0
            shared_state.alarm = False
            shared_state.current_posture = current_posture

        monitor_text = (
            "Monitoring"
            if shared_state.monitoring
            else "Stopped"
        )

        posture_map = {
            "無人躺著": "No person",
            "左側躺": "Left side",
            "右側躺": "Right side",
            "仰躺": "Supine",
            "偵測錯誤": "Error"
        }

        posture_en = posture_map.get(
            shared_state.current_posture,
            "Unknown"
        )

        info_text = (
            f"{monitor_text} | "
            f"Posture: {posture_en} | "
            f"Time: {int(shared_state.duration)} sec"
        )

        cv2.rectangle(
            annotated,
            (20, 20),
            (900, 70),
            (0, 0, 0),
            -1
        )

        cv2.putText(
            annotated,
            info_text,
            (30, 55),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (255, 255, 255),
            2,
            cv2.LINE_AA
        )

        if shared_state.alarm:
            cv2.rectangle(
                annotated,
                (0, 0),
                (annotated.shape[1], annotated.shape[0]),
                (0, 0, 255),
                10
            )

            cv2.putText(
                annotated,
                "ALARM",
                (30, 110),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.5,
                (0, 0, 255),
                4,
                cv2.LINE_AA
            )

    return av.VideoFrame.from_ndarray(
        annotated,
        format="bgr24"
    )
=========================
Layout
=========================
left_col, right_col = st.columns([1.15, 1.4])

=========================
Webcam
=========================
with left_col:
st.subheader("1. 即時影像監測")

webrtc_streamer(
    key="pose-monitor",
    mode=WebRtcMode.SENDRECV,
    rtc_configuration={
        "iceServers": [
            {"urls": ["stun:stun.l.google.com:19302"]},
            {"urls": ["stun:stun1.l.google.com:19302"]},
            {"urls": ["stun:stun2.l.google.com:19302"]},
            {"urls": ["stun:stun3.l.google.com:19302"]},
            {"urls": ["stun:stun4.l.google.com:19302"]}
        ]
    },
    media_stream_constraints={
        "video": True,
        "audio": False
    },
    video_processor_factory=PoseVideoProcessor,
    async_processing=True,
)
=========================
Right Panel
=========================
with right_col:
st.subheader("2. 摘要資訊")

with shared_state.lock:
    posture_now = shared_state.current_posture
    duration_now = int(shared_state.duration)
    alarm_now = shared_state.alarm
    monitoring_now = shared_state.monitoring

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">目前姿勢</div>
        <div class="metric-value">{posture_now}</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">持續時間</div>
        <div class="metric-value">{duration_now} 秒</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    system_text = (
        "監測中"
        if monitoring_now
        else "停止"
    )

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">系統狀態</div>
        <div class="metric-value">{system_text}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# =========================
# 測試警報聲
# =========================
if st.session_state.test_alarm_sound:
    st.subheader("🔔 警報聲測試")
    render_loop_alarm()

    if st.button("停止測試警報聲"):
        st.session_state.test_alarm_sound = False
        st.rerun()


# =========================
# Alarm 區
# =========================
st.subheader("3. 警報摘要")

if alarm_now:
    st.markdown(f"""
    <div class="alert-box">
        🚨 偵測到姿勢持續超過 {alarm_threshold} 秒，
        請協助翻身。
    </div>
    """, unsafe_allow_html=True)

    render_loop_alarm()

    if st.button("✅ 確認此資訊", type="primary"):
        with shared_state.lock:
            shared_state.alarm_acknowledged = True
            shared_state.alarm = False

        st.rerun()

else:
    st.markdown("""
    <div class="normal-box">
        ✅ 目前尚未觸發警報
    </div>
    """, unsafe_allow_html=True)

關閉
