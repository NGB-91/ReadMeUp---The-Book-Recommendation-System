# 📚 ReadMeUp  
### A Multi-Level Book Recommendation System

ReadMeUp is an end-to-end **book recommendation system** designed to showcase applied **Data Science, Machine Learning, and NLP** skills through a complete product pipeline — from raw data processing to model-driven recommendations and a functional web interface.

The project explores **three levels of personalization**, allowing users to discover books using progressively more advanced recommendation strategies.


## 🎯 Project Goals

- Design and compare multiple recommendation approaches
- Apply NLP techniques to textual book data
- Build reusable, modular ML pipelines
- Deploy a functional web application to demonstrate real-world usability
- Communicate technical decisions clearly to non-technical users


## 🧠 Recommendation Levels

### 1. Quick Pick (Baseline)
A lightweight recommendation approach based on:
- Genre filtering
- Popularity metrics
- Simple user constraints  

Designed for fast and intuitive discovery.


### 2. Smart Match (Content-Based)
A semantic recommendation system using:
- Text embeddings
- Cosine similarity
- Feature-based filtering  

This model focuses on **matching books by meaning**, not just metadata.


### 3. Deep Dive (Advanced NLP)
The most advanced level, combining:
- Transformer-based embeddings
- FAISS similarity search
- Multi-dimensional ranking logic  

Optimized for users seeking **highly personalized and semantically rich recommendations**.


## 🗂️ Project Structure

```text
├── app/                     # Flask web application
│   ├── main/                # Routes and views
│   ├── models/              # Recommendation logic
│   ├── utils/               # Text processing & helpers
│   ├── static/              # CSS, JS, images
│   └── templates/           # HTML templates
│
├── data/
│   ├── raw/                 # Original datasets
│   ├── interim/             # Intermediate processed data
│   ├── processed/           # Cleaned and enriched datasets
│   └── final/               # Embeddings, FAISS index, final tables
│
├── models/notebooks/        # Model experimentation notebooks
├── notebooks/               # EDA and analysis
├── filling_data/            # Data enrichment & preprocessing scripts
│
├── run.py                   # Application entry point
├── requirements.txt         # Python dependencies
└── README.md
## 🛠️ Tech Stack

### Languages & Frameworks
- Python  
- Flask  

### Data Science & Machine Learning
- NumPy, Pandas  
- Scikit-learn, SciPy  
- PyTorch  
- FAISS  

### NLP
- spaCy  
- NLTK  
- Hugging Face Transformers  
- Sentence-Transformers  

### Visualization & Frontend
- HTML / CSS / JavaScript  
- Matplotlib, Seaborn  

### Data Storage
- CSV-based datasets  
- Vector indexes (FAISS)  


## 🚀 Deployment

The application is deployed on **Hugging Face Spaces** and can be accessed via a public link.

It runs as a Flask-based web application listening on port **7860**, following Hugging Face deployment requirements.


## 📱 Responsive Design & Future Improvements

ReadMeUp has been designed as a **desktop-first web application**.

This was an intentional decision:
- The platform focuses on rich exploration, multi-step forms, and dense recommendation results  
- These interactions are more effective on larger screens  

Planned future improvements include:
- A mobile-first layout redesign  
- Simplified interaction flows for smaller screens  
- Progressive UX optimization for touch-based devices  

This reflects a common real-world product approach:  
**prioritizing model quality and core functionality before full UI optimization**.


## 🧪 Dataset Notes

The project works with large datasets and vector embeddings.  
Due to size constraints:
- Heavy files are handled using **Git LFS**  
- Some datasets are preprocessed before deployment  


## 👩‍💻 Authors

Created by:

Noemí Gómez Bouzada — Data Science

LinkedIn: https://www.linkedin.com/in/noemigomezbouzada/

Elena Sánchez — Data Science

LinkedIn: https://www.linkedin.com/in/elenasanchez25/

Sami Amarante — Data Science

LinkedIn: https://www.linkedin.com/in/samillyamarante/


## 📌 Final Note

ReadMeUp is not intended as a production-ready commercial product, but as a **portfolio project** demonstrating:
- Strong data reasoning  
- Applied machine learning  
- NLP-driven recommendation systems  
- The ability to take a project from data to deployment  

It reflects a **Data Science–first mindset**, with engineering and UX choices made to support that goal.
