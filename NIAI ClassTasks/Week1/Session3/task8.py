import pandas as pd
import matplotlib.pyplot as plt



plt.style.use('dark_background')

PINK='#FF1493'
LIME = '#B8FF00'
CYAN = '#00E5FF'
MAGENTA = '#FF4FD8'
ORANGE = '#FF8C00'
WHITE = '#F5F5F5'
GRID = '#666666'

# Grammar of plot :data → pick a chart → label it → show it

# Data

df = pd.DataFrame({
    'Day':     ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    'Orders':  [45, 62, 58, 70, 95, 110, 80],
    'Revenue': [900, 1240, 1160, 1400, 1900, 2200, 1600]
})

cat_names = ['Electronics', 'Clothing', 'Home', 'Books']
cat_revenue = [4200, 3100, 2000, 1100]

# Dashboard(canvas & axis)

fig, axes = plt.subplots(2, 2, figsize=(13, 9))

# Main Dashboard Title
fig.suptitle(
    'E-Commerce Sales Performance Dashboard',
    fontsize=18,
    fontweight='bold',
    color=WHITE
)


# 1. Pick a chart: LINE CHART
# Why: To show the daily revenue trend across the week.

axes[0, 0].plot(
    df['Day'],
    df['Revenue'],
    marker='o',
    markersize=8,
    linewidth=2.5,
    color=LIME,
    label='Revenue'
)

# label
axes[0, 0].set_title(
    'Daily Revenue Trend',
    fontsize=13,
    fontweight='bold'
)

axes[0, 0].set_xlabel('Day')
axes[0, 0].set_ylabel('Revenue ($)')
axes[0, 0].grid(True, alpha=0.25, color=GRID)
axes[0, 0].legend()




# 2. BAR CHART
# Why: To compare the number of orders across different days.


bars = axes[0, 1].bar(
    df['Day'],
    df['Orders'],
    color=ORANGE,
    edgecolor=WHITE,
    linewidth=0.8
)

axes[0, 1].set_title(
    'Orders by Day',
    fontsize=13,
    fontweight='bold'
)

axes[0, 1].set_xlabel('Day')
axes[0, 1].set_ylabel('Orders')
axes[0, 1].grid(
    axis='y',
    alpha=0.25,
    color=GRID
)


'''
 3. SCATTER PLOT
 Why: To see whether there is a relationship between
 orders and revenue.
'''


axes[1, 0].scatter(
    df['Orders'],
    df['Revenue'],
    marker='D',
    s=90,
    color=MAGENTA,
    edgecolor=WHITE,
    linewidth=0.8
)

axes[1, 0].set_title(
    'Orders vs Revenue',
    fontsize=13,
    fontweight='bold'
)

axes[1, 0].set_xlabel('Orders')
axes[1, 0].set_ylabel('Revenue ($)')
axes[1, 0].grid(
    True,
    alpha=0.25,
    color=GRID
)


# 4. PIE CHART
# Why: There are only a few product categories, so a pie
# chart clearly shows each category's share of total revenue.


axes[1, 1].pie(
    cat_revenue,
    labels=cat_names,
    autopct='%1.1f%%',
    startangle=90,
    colors=[ ORANGE,CYAN, MAGENTA, PINK],
    explode=[0.08, 0, 0, 0],
    shadow=True,
    wedgeprops={'edgecolor': '#222222', 'linewidth': 1}
)

# 4200 + 3100 + 2000 + 1100 = 10400
# 4200 / 10400 × 100 = 40.38%

axes[1, 1].set_title(
    'Revenue Share by Category',
    fontsize=13,
    fontweight='bold'
)


# SPACING


plt.subplots_adjust(
    left=0.07,
    right=0.95,
    top=0.88,
    bottom=0.08,
    wspace=0.28,
    hspace=0.38
)

# show
plt.show()


# 🏆 SO WHAT?


'''
The founder should focus on the strong revenue and order performance on 
Friday and Saturday.
Electronics generated the largest share of category revenue,
while higher orders are strongly associated with higher revenue.

'''



# 🤔 Wrap-Up Reflection
'''
 1. For each task, did the question point you to the chart before you looked at the data?
   Yes, for most tasks, the question itself pointed me toward the correct chart
   before I looked at the data. This helped me understand that the question
   should guide the choice of chart.

2. In Task 3, why did the sorted bar chart beat the pie chart?
   The sorted bar chart beat the pie chart because it made it easier to
   compare values and see the ranking of categories. A pie chart shows
   parts of a whole, but comparing similar-sized slices is more difficult.

3. Name one chart from this worksheet where starting the y-axis at zero matters,
   and one where it doesn't.
   Starting the y-axis at zero matters in a bar chart, such as the
   "Orders by Day" chart, because the bar lengths represent the values.
   It matters less in a line chart, such as the "Daily Revenue Trend",
   where the main focus is the trend and changes over time.

4. In the capstone, which of your 4 charts was hardest to choose, and why?
   In the capstone, the scatter plot was the hardest to choose because
   I had to decide how to show the relationship between two numerical
   variables: orders and revenue. I chose a scatter plot because it
   clearly shows whether higher orders are associated with higher revenue.

'''