from fastapi import FastAPI, File, UploadFile
from ultralytics import YOLO
from PIL import Image
import io

app = FastAPI(title="YOLOv11 Object Detection API")


model = YOLO("best.pt")

@app.get("/")
def home():
    return {"message": "API is online and ready for prediction!"}

@app.post("/predict")
async def predict_image(file: UploadFile = File(...)):
   
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes))

   
    results = model.predict(source=image, conf=0.5)

   
    detections = []
    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])
            class_name = model.names[class_id]
            confidence = float(box.conf[0])
            
            detections.append({
                "object": class_name,
                "confidence_score": round(confidence * 100, 2)
            })

    return {
        "filename": file.filename,
        "total_objects": len(detections),
        "results": detections
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)