# Capstone Flask 🍦

A simulation-driven ice cream flavor purchase prediction and analysis system built with Flask and SQLite. 🐍🗃️

## Features ✨

- **Database Setup** 💾  
  Initializes SQLite tables for users, purchases, flavor counts, simulation types, truck reports, total purchases, simulation references, and feedback messages.

- **Customer Simulations** 🎲  
  Multiple classes simulate customer flavor choices with seasonal and probabilistic variations (Winter ❄️, Summer ☀️, Normal variants with different times and probabilities).

- **Data Persistence** 📊  
  Functions to save simulation data, flavor counts, truck reports, total purchases, and user feedback to the database with conflict resolution.

- **Visualization** 📈  
  Generates bar charts of total flavor purchases from simulation results and saves them as static images.

- **User Authentication** 🔐  
  Implements login and registration functionality with session management.

- **Templating and Routing** 🛣️  
  Uses Jinja2 templating engine and Flask Blueprints for modular routing including dynamic URL handling.

## Advanced Features 🚀

- **Charts** 📊  
  (Matplotlib) Various charts for winter, summer, normal conditions, and general analytics such as average purchases, truck orders, and purchases over time.

- **AI Scripts** 🤖  
  (Ski-Kit-Learn) Machine learning models for predicting flavor purchases and truck orders.

## Getting Started 🏁

Clone the repository:

```bash
git clone https://github.com/JeremyG9999/Capstone_Flask.git
cd Capstone_Flask
pip install -r requirements.txt
