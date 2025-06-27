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
  Implemented login and registration functionality.

- **Templating** 
  Uses Jinja2 templating engine for rendering HTML pages.

- **Dynamic Routing**
  Supports dynamic URL routing for different pages.

- **Flask Blueprints for Modular Routing**  
  - Home routes: Handles simulation pages, running simulations, feedback submission, and about pages.  
  - Login routes: Manages user login, authentication, account creation, updating, and deletion.  
  - Stats routes: Displays statistics, AI prediction results, and various charts.  
  - Weather type routes: Shows charts categorized by weather simulation types (Winter, Summer, Normal).

## Charts Included

- Winter Charts — Various charts representing winter simulation data and flavor counts.  
- Summer Charts — Various charts representing summer simulation data and flavor counts.  
- Normal Charts — Various charts representing normal condition simulation data and flavor counts.  
- General Charts — Includes average purchases, average truck orders, purchases over time, and truck order charts.  


## AI Scripts Included

- Flavor Count AI — Predicts flavor purchase patterns using machine learning models.  
- Truck Order AI — Predicts truck order quantities using AI-based regression models.  

## UI Stylesheets Included

- About Us  
- Charts  
- Feedback  
- Home  
- Login UI  
- Navbar  
- Season Charts  
- Simulation  
- Statistics  
- Stats  

## Templates Included

- AI Stats Templates  
- Chart Templates  
- Home Templates  
- Login Templates  
- Stats Templates  


## Getting Started

Clone the repository:

```bash
git clone https://github.com/JeremyG9999/Capstone_Flask.git
cd Capstone_Flask
pip install -r requirements.txt
