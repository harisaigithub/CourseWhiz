# CourseWhiz

**CourseWhiz** is a smart search tool designed to help users discover the most relevant free courses on Analytics Vidhya. Leveraging advanced NLP models like BERT, the tool offers a personalized and efficient search experience.

---

## 🔍 Topic
A smart course search and recommendation tool built using BERT embeddings and Retrieval-Augmented Generation (RAG) architecture to provide tailored course results for Analytics Vidhya users.

---

## 📚 About
CourseWhiz processes course data (titles, descriptions, and metadata) to create embeddings and calculate similarities using cosine similarity. The tool enables users to search using natural language queries and receive the most relevant course recommendations.

---

## 📊 Data
- **Source**: Free courses from Analytics Vidhya's platform.
- **Format**: JSON file containing course titles, descriptions, images, and links.

---

## 🎯 Objectives
- Provide accurate course recommendations using advanced embeddings.
- Allow natural language queries for a user-friendly experience.
- Enhance discoverability of Analytics Vidhya's free courses.

---

## 🖍️ Summary
CourseWhiz enables users to search for courses using keywords or natural language queries. It uses pre-trained BERT embeddings to compare the similarity of user queries with course titles and descriptions. The tool is built with Streamlit for an interactive user interface.

---

## 📚 Libraries Used
- `streamlit`: For building the interactive web application.
- `transformers`: To use pre-trained BERT models for embeddings.
- `torch`: For tensor computations with PyTorch.
- `numpy`: For numerical computations.
- `scikit-learn`: For cosine similarity calculations.

---

## 🌐 Data Source
Data is sourced from Analytics Vidhya's publicly available free course data.

---

## 📜 License
This project is licensed under the **MIT License**. Feel free to use, modify, and distribute this project as per the license terms.

---

## ⚙️ Dependencies
- Python 3.8 or higher
- Libraries: `streamlit`, `transformers`, `torch`, `numpy`, `scikit-learn`

---

## 🚀 Instructions to Deploy Locally

### Steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/CourseWhiz.git
   cd CourseWhiz
   ```

2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Scrape the course data**:
   ```bash
   python scripts/scrape_data.py
   ```

4. **Generate embeddings for the courses**:
   ```bash
   python scripts/generate_embeddings.py
   ```

5. **Run the application locally**:
   ```bash
   streamlit run app/app.py
   ```

6. **Open the link provided in the terminal** (typically `http://localhost:8501`) to access the application.

---

## 📷 Screenshots
### Homepage & Search Results

### Demo Video
[![Watch Demo](https://github.com/user-attachments/assets/ebdd2b9f-10d2-4c22-a814-4c5177a81d46)



---

## 🌐 Hosting Link
The hosting attempt on Huggingface Spaces was unsuccessful. Please deploy locally by following the steps provided above.

---

## 📆 Latest Version of README
This README is updated to reflect the latest project changes and deployment guidelines.

Enjoy using CourseWhiz to find the most relevant courses tailored to your learning needs!
