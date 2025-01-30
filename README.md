# Bioinformatics Lab Project 2024/2025

## Overview

This project focuses on the bioinformatic analysis of genes from microorganisms in the human gut microbiome. The goal is to analyze gene sequences, study their structure, and interpret their potential functions, interactions, and relationships to health and disease.

## Project Objectives

- Select and analyze genes from microorganisms in the human microbiome.
- Use bioinformatics tools to study gene sequences (DNA, RNA, proteins).
- Investigate homologous sequences and related data from literature and databases.
- Interpret results to infer gene functions and interactions.

## Workflow

1. **Gene Selection**: This group selected *Faecalibacterium prausnitzii* as the microorganism in study and a gene per group member.
   - *Genes*:
     - FAEPRAM212_RS11550
     - ptsP
     - FAEPRAM212_03428
2. **Data Collection and Analysis**:
   - Retrieve gene sequences from NCBI and other databases.
   - Perform homology searches (BLAST) and functional annotations.
   - Analyze protein properties using UniProt, PDB, and conserved domain databases.
3. **Multiple Sequence Alignment and Phylogeny**:
   - Perform alignments and build phylogenetic trees to identify conserved regions.
4. **Regulation and Variant Analysis**:
   - Investigate regulatory interactions and gene variants.
Aqui está um **README.md** completo e bem estruturado em inglês:  

---  
This project provides a **Jupyter Notebook** environment using **Docker** and **Docker Compose**.  

## 📦 Prerequisites  

- [Docker](https://www.docker.com/get-started) installed  
- [Docker Compose](https://docs.docker.com/compose/install/) installed  

## 🚀 How to Run  

### 1️⃣ Clone the Repository  
```sh
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

### 2️⃣ Build and Start the Container  
```sh
docker-compose up -d
```

### 3️⃣ Access Jupyter Notebook  
Once the container is running, open your browser and go to:  
👉 **http://127.0.0.1:8888**  

A token will be displayed in the terminal. Copy and paste it into the browser to access Jupyter Notebook.

## 🛑 How to Stop the Container  
To stop and remove the container, run:  
```sh
docker-compose down
```

## 📂 Persistent Data  
All files and notebooks inside the project folder will be saved, as the directory is mapped as a **volume** in the container.

## 🛠️ Compatibility (Windows, macOS, Linux)  
This project works on any OS with **Docker** and **Docker Compose** installed.

### ⚠️ Notes for Windows  
- If using **PowerShell**, some commands may need the `./` prefix:
  ```sh
  ./docker-compose up -d
  ```
- If running the project inside **OneDrive**, you may face permission issues. It's recommended to move it to `C:\Projects`.

### ⚠️ Notes for macOS/Linux  
- If you encounter permission errors, try running:
  ```sh
  sudo docker-compose up -d
  ```

## 🛠️ Customizing the Jupyter Notebook Configuration  
If you want to disable the token authentication or set a password, edit the `CMD` command in **Dockerfile** or **docker-compose.yml**.

For example, to remove token authentication, update **docker-compose.yml**:
```yaml
command: ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''"]
```
This will allow direct access to Jupyter Notebook without a token.

## 🐳 Useful Docker Commands  
Check running containers:  
```sh
docker ps
```
Stop a specific container:  
```sh
docker stop <container_id>
```
Remove all stopped containers:  
```sh
docker system prune -f
```

---

## Team Contributions

Each group member is responsible for analyzing one gene. The portfolio includes a credits section detailing individual contributions. The main branch was developed by Catarina and Maria. The branch protein_analysis was developed by Muneeb.

