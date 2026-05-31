# 🏭 Smart Safety Factory Monitoring using YOLOv8

A real-time safety monitoring system built using **YOLOv8** to detect workers, machinery, and PPE compliance (helmets, vests, masks) inside factories and industrial environments.

This project helps improve workplace safety by automatically identifying safety rule violations and tracking worker activity.

---

## 🚀 Features
- ✔️ Real-time detection using YOLOv8  
- ✔️ Detects workers, helmets, vests, masks, machinery, and vehicles  
- ✔️ Flags safety rule violations (No-Helmet, No-Vest, No-Mask)  
- ✔️ Uses custom-trained dataset with 10 classes  
- ✔️ Supports image, video, and webcam detection  
- ✔️ Easy to deploy in safety monitoring systems  

---

## 🗂️ Dataset Classes
- Person  
- Helmet (Hardhat)  
- Safety Vest  
- Mask  
- NO-Helmet  
- NO-Vest  
- NO-Mask  
- Safety Cone  
- Machinery  
- Vehicle  

---

## 🛠️ Installation

### 1️⃣ Clone the Repository
git clone https://github.com/PVK-Nandan/Smart-Safety-Factory-Monitoring-using-Yolov8.git  
cd Smart-Safety-Factory-Monitoring-using-Yolov8

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
python -m venv venv  
venv\Scripts\activate  # Windows

### 3️⃣ Install Dependencies
pip install -r requirements.txt

---

## ▶️ Usage

### Run Inference on an Image
python test_yolo.py --source path/to/image.jpg

### Run on a Video
python test_yolo.py --source path/to/video.mp4

### Run Live Webcam Detection
python test_yolo.py --source 0

---

## 📂 Project Structure
├── data.yaml               # Dataset configuration  
├── models/                 # Trained YOLOv8 model weights  
├── datasets/               # Training dataset  
├── output/                 # Results and prediction images  
├── test_yolo.py            # Script for testing YOLOv8 model  
├── requirements.txt        # Dependencies  
└── README.md  

---

## 🧠 Training (Optional)
yolo train model=yolov8n.pt data=data.yaml epochs=100 imgsz=640

---

## 🤝 Contributing
Feel free to contribute or improve the project by opening a pull request.

---

## 📝 License
This project is open-source and free to use for research and development.

