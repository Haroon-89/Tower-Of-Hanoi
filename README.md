# 🏰 Tower of Hanoi – Flask Web App with Animation

A **Flask-based web application** that visualizes the **Tower of Hanoi** problem using **Matplotlib animations**.  
This interactive project demonstrates recursion with a beautiful GIF animation of each move.

---

## 🚀 Features

- 🌐 Built with **Flask** for the web interface  
- 🧠 Implements recursive **Tower of Hanoi** algorithm  
- 🖼️ Automatically generates animated **GIF visualization** using Matplotlib  
- 💡 Clean UI built with HTML + CSS  
- ⚙️ Input validation for disk range (1–6)

---

## 🧩 How It Works

The app uses the recursive algorithm to move disks between three rods (`A`, `B`, `C`) and captures each move as an image using **Matplotlib**.  
These frames are then combined into a GIF using **ImageIO**, which is displayed on the result page.

---

## 📁 Project Structure

```

Tower-Of-Hanoi/
│
├── static/
│   ├── animation.gif         # Output animation (auto-generated)
│   └── style.css             # Page styling
│
├── templates/
│   ├── index.html            # Input page (user enters number of disks)
│   └── result.html           # Displays final animation
│
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── .gitignore
└── README.md

````

---

## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Haroon-89/Tower-Of-Hanoi.git
cd Tower-Of-Hanoi
````

### 2️⃣ Create a virtual environment (recommended)

```bash
python -m venv venv
venv\Scripts\activate     # On Windows
source venv/bin/activate  # On Mac/Linux
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000/
```

---

## 🧮 Example

**Input:**

> Number of disks: 3

**Output:**

* Total moves = 7
* Animated GIF showing each step of the Tower of Hanoi solution

![Animation Preview](static/animation.gif)

---

## 📘 Technologies Used

* **Python 3**
* **Flask** (for web framework)
* **Matplotlib** (for disk visualization)
* **ImageIO** (for GIF generation)
* **HTML / CSS** (for front-end design)

---

## 🧠 Learning Outcome

* Understanding recursion and backtracking
* Generating animations dynamically using Python
* Integrating data visualization into a Flask web app

---
