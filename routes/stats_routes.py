from flask import Blueprint, render_template
from scripts.simulation_script import *
from scripts.DB_queries import *
from database_layer import *
from scripts.AI_scripts.flavor_count_ai import *
from scripts.AI_scripts.truck_order_ai import *
from scripts.insert_DB_script import *
from scripts.charts.truck_AI_chart import *
from scripts.charts.truck_chart import *
from scripts.charts.purchases_chart import *
from scripts.charts.normal_charts.customer_simulation_chart import *
from scripts.charts.purchases_over_time_chart import *
from scripts.charts.average_purchases_chart import *
from scripts.charts.average_truck_order_chart import *
from scripts.charts.summer_charts.summer_simulation_chart import *
from scripts.charts.winter_charts.winter_simulation_chart import *

stats_routes = Blueprint('statistics', __name__)

@stats_routes.route('/flavor_count_data', methods=['GET'])
def flavor_count_data():
    flavor_data = flavor_counts_data()
    return render_template('stats_templates/flavor_count_display.html', flavor_data=flavor_data)

@stats_routes.route('/truck_report')  
def truck_report(): 
    flavor_totals = truck_report_logic()
    return render_template('stats_templates/truck_report.html', flavor_totals=flavor_totals)

@stats_routes.route('/flavor_count_AI', methods=['GET'])
def predict():
    results, mse = PredictionResults.run_prediction()
    return render_template('ai_stats_templates/flavor_count_AI.html', results=results, mse=mse)

@stats_routes.route('/truck_order_AI', methods=['GET'])
def predict_truck():
    results, mse = Truck_Prediction.run_prediction()
    return render_template('ai_stats_templates/truck_order_AI.html', results=results, mse=mse)

@stats_routes.route('/total_purchases', methods=['GET'])
def save_total_purchase():
    total_purchases = total_purchases_data()
    return render_template('stats_templates/total_purchases.html', total_purchases=total_purchases)

@stats_routes.route('/truck_chart_AI')
def truck_chart_AI():
    generate_combined_chart()  
    return render_template('chart_templates/truck_chart_AI.html', truck_chart='static/charts/truck_ai_chart.png') 

@stats_routes.route('/truck_chart')
def truck_chart():
    generate_truck_chart()
    return render_template('chart_templates/truck_chart.html', truck_chart='static/charts/truck_chart.png')

@stats_routes.route('/purchase_chart')
def purchase_chart():
    generate_purchase_chart()
    return render_template('chart_templates/purchase_chart.html', purchase_chart='static/charts/purchase_chart.png')

@stats_routes.route('/customer_simulation_chart')
def customer_simulation_charts():
    customer_simulation_chart()  
    return render_template('chart_templates/customer_simulation_chart.html', chart='static/charts/simulation_chart_Customer.png')

@stats_routes.route('/summer_simulation_chart')
def summer_simulation_charts():
    summer_simulation_chart()  
    return render_template('chart_templates/summer_simulation_chart.html', chart='static/charts/simulation_chart_Summer.png')

@stats_routes.route('/winter_simulation_chart')
def winter_simulation_charts():
    winter_simulation_chart()  
    return render_template('chart_templates/winter_simulation_chart.html', chart='static/charts/simulation_chart_Winter.png')

@stats_routes.route('/purchases_over_time')
def purchase_over_time():
    purchases_over_time()  
    return render_template('chart_templates/purchases_over_time_chart.html', chart='static/charts/purchases_over_time.png')

@stats_routes.route('/average_purchases')
def average_purchase_route():
    average_purchase_charts() 
    return render_template('chart_templates/average_purchases_chart.html', chart='static/charts/average_purchases_chart.png')

@stats_routes.route('/average_truck_order')
def average_truck_order_route():
    average_truck_order_chart()  
    return render_template('chart_templates/average_truck_order_chart.html', chart='static/charts/average_truck_order_chart.png')