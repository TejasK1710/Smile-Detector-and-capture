import cv2
import time

# Load Haar Cascade Classifiers for face and smile detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")

# Open the webcam
cap = cv2.VideoCapture(0)

# Counter to manage multiple photo captures
photo_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Error: Unable to read frame from webcam.")
        break

    # Convert the frame to grayscale for better performance
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        # Draw rectangle around the detected face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Define Region of Interest (ROI) for smile detection
        roi_gray = gray_frame[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Detect smiles in the ROI
        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.8, minNeighbors=20)

        for (sx, sy, sw, sh) in smiles:
            # Draw rectangle around the detected smile
            cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 2)

            # Display smile detection message
            cv2.putText(frame, "Smile Detected!", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

            # Capture and save the photo
            photo_count += 1
            photo_name = f"smile_photo_{photo_count}.jpg"
            cv2.imwrite(photo_name, frame)
            print(f"Photo captured: {photo_name}")

            # Optional: Add a small delay to prevent multiple captures for the same smile
            time.sleep(2)
            break  # Break to avoid capturing multiple photos for the same smile

    # Display the frame
    cv2.imshow("Smile Detector", frame)

    # Exit loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
