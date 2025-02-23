# Book Recommendation System

## 📌 Project Overview
This project is a **Book Recommendation System** that suggests books to users based on their reading history and preferences of similar users. It utilizes **Item-Based Collaborative Filtering** with the **K-Nearest Neighbors (KNN) algorithm** to find books similar to the ones a user has liked.

## 🛠️ Technologies Used
- **Python**
- **Pandas & NumPy** (for data processing)
- **Scikit-learn** (for KNN-based recommendations)
- **Seaborn & Matplotlib** (for data visualization)
- **Pickle** (for model persistence)
- **Jupyter Notebook** (for development & testing)

## 📂 Project Structure
```
📂 book-recommender-system
│── 📂 artifacts          # Stores trained models & processed data
│── 📂 data               # Raw dataset files
│── 📂 env                # Virtual environment (if applicable)
│── recommendation.ipynb  # Jupyter notebook with the recommendation model
│── README.md             # Project documentation
```

## 🚀 How It Works
1. **Data Preprocessing**:
   - Load book ratings dataset.
   - Remove duplicates and filter low-rated books.
   - Create a pivot table mapping users to books.

2. **Model Training (Collaborative Filtering - KNN)**:
   - Convert data into a sparse matrix.
   - Train a **KNN model** using **Brute Force Search**.
   - Find similar books based on the nearest neighbors.

3. **Generating Recommendations**:
   - For a given book, find its closest books based on cosine similarity.
   - Return a list of recommended books with their covers (image URLs).

## 📌 How to Run the Project
### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Train the Model & Save It
Run the **recommendation.ipynb** notebook to train the model and save it using **Pickle**.

### 3️⃣ Load the Model & Make Predictions
You can use the trained model to generate recommendations like this:
```python
import pickle
import numpy as np

# Load model
model = pickle.load(open('artifacts/model.pkl', 'rb'))
book_names = pickle.load(open('artifacts/book_names.pkl', 'rb'))
book_pivot = pickle.load(open('artifacts/book_pivot.pkl', 'rb'))

# Get recommendations for a book
def recommend_book(book_title, n_recommendations=5):
    book_index = np.where(book_pivot.index == book_title)[0][0]
    distances, indices = model.kneighbors(book_pivot.iloc[book_index, :].values.reshape(1, -1), n_neighbors=n_recommendations + 1)
    recommendations = [book_pivot.index[i] for i in indices[0][1:]]
    return recommendations

print(recommend_book("Harry Potter and the Sorcerer's Stone (Book 1)"))
```

## 🎯 Future Improvements
✅ Implement **Neural Collaborative Filtering (NCF) with TensorFlow**
✅ Improve **UI with a web interface (Flask/React)**
✅ Add **Content-Based Filtering** for better recommendations

---
### 📌 Notes
- If you want to switch to **TensorFlow-based recommendation models**, we need to implement **Neural Collaborative Filtering (NCF)**.
- The system currently **compares books based on user interactions**, making it an **item-based collaborative filtering system**.
- **Feel free to improve and extend this project!** 🚀

---
📌 *Contributions & feedback are welcome!* 😃

