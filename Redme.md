---
title: Hardware Component Detection API
colorFrom: blue
colorTo: green
sdk: docker
app_port: 7860
short_description: FastAPI based YOLOv11 API for detecting 24 hardware components with 99% accuracy.
web site link: https://hardware-component-detector.netlify.app/
---

# 🛠️ 24-Class Hardware Component Detection API

Welcome to the **Hardware Component Detection API**! Built with **YOLOv11** and **FastAPI**, this high-performance API accurately detects, classifies, and locates **24 different types of everyday hardware tools and components** in real-time with an impressive **99% accuracy**.

---

## 📊 Dataset & Model Highlights

* **Architecture:** YOLOv11 (Object Detection)
* **API Framework:** FastAPI
* **Dataset Size:** 5,000 High-Quality Custom Annotated Images
* **Accuracy:** 99%
* **Classes:** 24 Unique Hardware Tool Categories

### Supported Tool Classes:
1. Adjustable Wrench
2. Allen Key
3. Allen Key Set
4. Bolts
5. Brush
6. Cutting Pliers
7. Cutting Saw
8. Hammer
9. Knife
10. Measuring Tape
11. Niddle Pliers
12. Non-Adjustable Wrench
13. Nuts
14. Perek (Nails)
15. Plumbing Tape
16. Regular Pliers
17. Scale
18. Scissor
19. Screw
20. Screwdriver Minus
21. Screwdriver Plus
22. Slide Callipers
23. Tester
24. Utility Cutter

---

## ⚡ API Endpoint Details

### **Predict Endpoint:** `/predict` `[POST]`

Send an image containing hardware tools via `POST` request. The API processes the image using the trained YOLOv11 model and returns object names, confidence scores, bounding box coordinates, and detection statistics.

* **URL Path:** `/predict`
* **Method:** `POST`
* **Content-Type:** `multipart/form-data`
* **Form Field Key:** `file`

---

## 📄 Comprehensive Sample Output (JSON)

When an image containing detected objects (e.g., a screwdriver and pliers) is uploaded, the FastAPI backend returns a structured response like this:

```json
{
  "status": "success",
  "filename": "sample_hardware_tools.jpg",
  "image_size": {
    "width": 1920,
    "height": 1080
  },
  "total_objects_found": 2,
  "detections": [
    {
      "class_id": 20,
      "class_name": "screwdriver plus",
      "confidence": 0.99,
      "bounding_box": {
        "xmin": 245.5,
        "ymin": 120.0,
        "xmax": 510.2,
        "ymax": 890.4
      }
    },
    {
      "class_id": 5,
      "class_name": "cutting pliers",
      "confidence": 0.98,
      "bounding_box": {
        "xmin": 600.1,
        "ymin": 300.8,
        "xmax": 950.0,
        "ymax": 750.3
      }
    }
  ]
}