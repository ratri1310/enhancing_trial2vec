# Trial2Vec Demo: README

This repository demonstrates the use of the enhancement of Trial2Vec model for evaluation on sample data (`demo_data`). The final implementation is provided in `DL_project_driver_final.ipynb`.

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/RyanWangZf/Trial2Vec.git
cd Trial2Vec
2. Create and Activate a Virtual Environment (Recommended)
We recommend using venv or conda to manage dependencies.

Using venv:

bash
Always show details

Copy
python3 -m venv trial2vec_env
source trial2vec_env/bin/activate
Using conda:

bash
Always show details

Copy
conda create -n trial2vec_env python=3.8
conda activate trial2vec_env
3. Install Dependencies
bash
Always show details

Copy
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt || true  # install if requirements.txt exists
pip install -e .  # install Trial2Vec in editable mode
4. (Optional) Force CPU Mode
If running without GPU, you can enforce CPU usage before importing torch or related libraries.

Running the Final Notebook
Open DL_project_driver_final.ipynb

Execute all cells under the #Main section

You should see evaluation results similar to the following:

Method	Prec@1	Prec@2	Prec@5	Rec@1	Rec@2	Rec@5	nDCG@5
TF-IDF	0.5455	0.5833	0.5515	0.4455	0.5095	0.7410	0.6791
SBERT	0.6700	0.8000	0.6700	0.5455	0.6870	0.7812	0.8016
Trial2Vec	1.0000	1.0000	1.0000	0.7818	0.8545	0.9812	1.0000
Proposed A	1.0000	1.0000	1.0000	0.7818	0.8545	0.7810	0.9266

Sanity Check with Trial2Vec Embeddings
To perform a sanity check on Trial2Vec embeddings, run the sanity.py script:

bash

Copy
python sanity.py
"""

📌 Acknowledgements
This project builds upon the [Trial2Vec repository](https://github.com/RyanWangZf/Trial2Vec) by [Ryan Wang](https://github.com/RyanWangZf).  
We adapted core modules from the [`trial2vec` directory](https://github.com/RyanWangZf/Trial2Vec/tree/main/trial2vec) for our contrastive learning experiments.

