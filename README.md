# **Whiteboard – A Simple Drawing Application Using Tkinter**  

## **Overview**  
The **Whiteboard** is a Python-based drawing application built using **Tkinter**. It allows users to draw on a canvas, select different colors, adjust brush thickness, and use an eraser to clear parts of the drawing. The interface is simple and user-friendly, making it a great tool for quick sketches or notes.  

## **Features**  
✅ **Freehand Drawing** – Click and drag to draw on the canvas.  
✅ **Color Palette** – Choose from multiple colors.  
✅ **Eraser Tool** – Clear specific parts of the drawing.  
✅ **Reset Button** – Clears the entire canvas and resets settings.  
✅ **Adjustable Brush Size** – Use a slider to change the thickness of the brush.  
✅ **Interactive UI** – Designed with Tkinter for a smooth experience.  

---

## **Usage Instructions**  
🎨 **How to Use:**  
- Click and drag on the **canvas** to start drawing.  
- Select a **color** from the palette to change the brush color.  
- Use the **slider** to adjust brush thickness.  
- Click the **eraser** button to switch to eraser mode.  
- Click the **reset** button to clear the entire canvas.  

---

## **Code Structure**  
📂 **Project Structure:**  
```
/whiteboard
│── whiteboard.py     # Main application script
│── whiteboard.png    # App logo
│── eraser.png        # Eraser icon
│── reset.png         # Reset button icon
│── panel.png         # UI panel background
```

### **Key Components in `whiteboard.py`**  
📌 **Drawing Functions:**  
- `addline()` – Handles drawing lines on the canvas based on mouse movement.  
- `locate_xy()` – Tracks the initial mouse position.  

📌 **UI Elements:**  
- **Canvas (`tk.Canvas`)** – The main whiteboard where users draw.  
- **Color Palette (`tk.Canvas`)** – Allows users to pick colors.  
- **Eraser & Reset Buttons (`tk.Button`)** – Interactive buttons for clearing drawings.  
- **Brush Thickness Slider (`ttk.Scale`)** – Adjusts the brush size.  

📌 **Additional Features:**  
- Uses **PIL (Pillow)** for handling images.  
- **Custom icons** for the UI.  
- **Automatic UI updates** (slider label updates in real-time).


📌 **Images:** 

  <img width="1047" height="597" alt="wh1" src="https://github.com/user-attachments/assets/d6fe2795-e4d5-4074-9b25-c1b9becf94e4" />
  <img width="1055" height="599" alt="wh2" src="https://github.com/user-attachments/assets/f9e21762-fad0-476a-b38c-0fd4febc8b4e" />
  <img width="1051" height="602" alt="wh3" src="https://github.com/user-attachments/assets/f3e1b79e-218e-40b0-b937-8bf88f7e5e37" />
  <img width="1050" height="594" alt="wh4" src="https://github.com/user-attachments/assets/e5466e25-61b5-4a95-9d69-05b9ecab5589" />




