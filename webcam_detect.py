import cv2
from ultralytics import YOLO

# Load your trained model (best.pt)
model = YOLO("models/best.pt")   # Change to yolov8n.pt if needed

def main():
    cap = cv2.VideoCapture(0)  # 0 = default webcam

    if not cap.isOpened():
        print("❌ Error: Could not access the webcam")
        return

    print("✅ Webcam is running... Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Failed to grab frame")
            break

        results = model.predict(frame, conf=0.5)  # confidence threshold
        annotated_frame = results[0].plot()  # draw bounding boxes

        cv2.imshow("PPE Detection - Webcam", annotated_frame)

        # Quit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
