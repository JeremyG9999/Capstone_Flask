# Capstone Flask

A simulation-driven ice cream flavor purchase prediction and analysis system built with Flask and SQLite.

## Features

- **Database Setup**  
  Initializes SQLite tables for users, purchases, flavor counts, simulation types, truck reports, total purchases, simulation references, and feedback messages.

- **Customer Simulations**  
  Multiple classes simulate customer flavor choices with seasonal and probabilistic variations (Winter, Summer, Normal variants with different times and probabilities).

- **Data Persistence**  
  Functions to save simulation data, flavor counts, truck reports, total purchases, and user feedback to the database with conflict resolution.

- **Prediction Model**  
  Random Forest regression model predicts future flavor purchase patterns based on historical simulation data.

- **Visualization**  
  Generates bar charts of total flavor purchases from simulation results and saves them as static images.

## Getting Started

Clone the repository:

```bash
git clone https://github.com/JeremyG9999/Capstone_Flask.git
cd Capstone_Flask
pip install -r requirements.txt
