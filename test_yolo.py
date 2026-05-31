from ultralytics import YOLO

model = YOLO("models/best.pt")  # Load your custom trained model

# Pick any file that exists
model.predict(source="source_files/hardhat.mp4", show=True)
