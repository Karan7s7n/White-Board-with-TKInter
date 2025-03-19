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
