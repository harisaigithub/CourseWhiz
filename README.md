# CourseWhiz

**CourseWhiz** is a smart search tool designed to help users discover the most relevant free courses on Analytics Vidhya. Leveraging advanced NLP models like BERT, the tool offers a personalized and efficient search experience.

---

## 🔍 Topic
A smart course search and recommendation tool built using BERT embeddings and RAG architecture to provide tailored course results for Analytics Vidhya users.

---

## 📖 About
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

## 📝 Summary
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
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/CourseWhiz.git
   cd CourseWhiz
Install the required dependencies:
bash
Copy code
pip install -r requirements.txt
Run the application locally:
bash
Copy code
streamlit run app.py
Open the link provided in the terminal to access the application.
Note:
Hosting the tool on Huggingface Spaces has encountered issues. For now, the tool can only be run on localhost by following the instructions above.

## 📷 Screenshots
Homepage & Search Results
[Watch Demo Video](/Recording%202024-12-30%20234723.mp4)


## 🌐 Hosting Link
The hosting attempt on Huggingface Spaces was unsuccessful. Please deploy locally by following the steps provided above.

## 📦 Latest Version of README
This README is updated to reflect the latest project changes and deployment guidelines.

Enjoy using CourseWhiz to find the most relevant courses tailored to your learning needs!

