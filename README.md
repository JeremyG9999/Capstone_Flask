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

- **User Authentication**  
  Implements login and registration functionality with session management.

- **Templating and Routing**  
  Uses Jinja2 templating engine and Flask Blueprints for modular routing including dynamic URL handling.

- **Modular Flask Blueprints**  
  - Home routes: Manage simulation pages, running simulations, feedback submission, and about pages.  
  - Login routes: Handle user login, authentication, account creation, updates, and deletion.  
  - Stats routes: Display statistics, AI prediction results, and various charts.  
  - Weather type routes: Present charts categorized by weather simulation types (Winter, Summer, Normal).

- **Charts**  
  Various charts for winter, summer, normal conditions, and general analytics such as average purchases, truck orders, and purchases over time.

- **AI Scripts**  
  Machine learning models for predicting flavor purchases and truck orders.

- **Templates**  
  Organized templates for AI stats, charts, home, login, and general statistics views.

## Getting Started

Clone the repository:

```bash
git clone https://github.com/JeremyG9999/Capstone_Flask.git
cd Capstone_Flask
pip install -r requirements.txt
