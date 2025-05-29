import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
from scripts.DB_queries import total_flavor_counts_data

def generate_purchase_chart():
    data = total_flavor_counts_data()
    if not data:
        data = [0, 0, 0, 0, 0]
    lava, hot_fudge, blizzard, chocolate, vanilla = data

    plt.bar('Lava', lava)
    plt.bar('Hot Fudge', hot_fudge)
    plt.bar('Blizzard', blizzard)
    plt.bar('Chocolate', chocolate)
    plt.bar('Vanilla', vanilla)

    plt.xlabel('Flavor')
    plt.ylabel('Total Purchases')
    plt.title('Total Purchases per Flavor')
    plt.grid()
    plt.savefig('static/charts/purchase_chart.png')
    plt.close()