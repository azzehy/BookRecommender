# 📚 Book Recommender System

> A Machine Learning-powered book recommendation system built with **Streamlit**, **Scikit-learn**, and **Pickle**.

![Book Recommender System](https://via.placeholder.com/800x400?text=Book+Recommender+System)

---

## 🌟 Overview
This project is an **AI-powered book recommendation system** that suggests books based on user preferences using **Machine Learning (KNN Algorithm)**. The web application is built using **Streamlit** for an interactive user experience.

---

## 🏗 Project Structure
```
book_recommender_system/
│-- artifacts/        # Contains trained ML models and datasets
│-- data/             # Raw & Processed Data
│-- env/              # Virtual Environment (optional)
│-- src/              # Source code directory
│-- app.py            # Main Streamlit application
│-- recommend.py      # Recommendation logic
│-- requirements.txt  # Required dependencies
│-- setup.py          # Setup for packaging
│-- README.md         # Project documentation
```

---

## 🛠 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/book-recommender.git
cd book-recommender
```

### 2️⃣ Create a Virtual Environment (Optional)
```bash
python -m venv env
source env/bin/activate   # For macOS/Linux
env\Scripts\activate      # For Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application
```bash
streamlit run app.py
```

---

## 🚀 How It Works
1. **Select a book** from the dropdown.  
2. **Click "Show Recommendations"** to see book suggestions.  
3. The system **displays 5 recommended books** with cover images.  
4. Uses **K-Nearest Neighbors (KNN) algorithm** for recommendations.  

---

## 📂 Artifacts & Data
- `artifacts/model.pkl` → Pre-trained ML model  
- `artifacts/book_names.pkl` → List of book names  
- `artifacts/book_pivot.pkl` → Transformed data for KNN  
- `artifacts/ratingsGeneralInfo.pkl` → Contains book ratings & image URLs  

---

## 🖼 Screenshots
| ![Screenshot 1](https://github.com/user-attachments/assets/134735f7-ffd3-4ac1-96ac-d030bdbe856a) | ![Screenshot 2](https://github.com/user-attachments/assets/7b5bcfa0-c9d5-4f25-99b7-d469e652dd94) |
|:-------------------------:|:-------------------------:|
| **Home Page** | **Book Recommendations** |

---

## 🧑‍💻 Technologies Used
- **Python** 🐍  
- **Machine Learning (KNN)** 🤖  
- **Streamlit (Web UI)** 🎨  
- **Pandas & NumPy (Data Processing)** 📊  
- **Scikit-Learn (ML Model)** 🔍  

---

## 🤝 Contributing
1. **Fork the repository**  
2. **Create a feature branch** (`git checkout -b feature-branch`)  
3. **Commit changes** (`git commit -m "Added new feature"`)  
4. **Push to GitHub** (`git push origin feature-branch`)  
5. **Open a Pull Request** 🚀  

---

## 📜 License
This project is licensed under the **MIT License**. Feel free to use and modify it! 📖  

---

## 🔗 Connect With Me
- **GitHub**: [azzehy](https://github.com/azzehy)  
- **LinkedIn**: [yazzzeh](https://www.linkedin.com/in/yazzzeh/)

---


## 🎯 Future Improvements
✅ Implement **Neural Collaborative Filtering (NCF) with TensorFlow**
✅ Improve **UI with a web interface (Flask/React)**
✅ Add **Content-Based Filtering** for better recommendations

---
📌 *Contributions & feedback are welcome!* 😃

