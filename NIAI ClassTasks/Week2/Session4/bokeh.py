import pandas as pd

from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.models import HoverTool, ColumnDataSource

output_notebook()


# Grammar of plot:
# data → pick a chart → label it → show it


# =========================
# DATA
# =========================

df = pd.DataFrame({
    'Day':     ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    'Orders':  [45, 62, 58, 70, 95, 110, 80],
    'Revenue': [900, 1240, 1160, 1400, 1900, 2200, 1600]
})

cat_names = ['Electronics', 'Clothing', 'Home', 'Books']
cat_revenue = [4200, 3100, 2000, 1100]


# =========================
# 1. LINE CHART
# =========================
# Why:
# To show the daily revenue trend across the week.


source_line = ColumnDataSource(data=dict(
    x=list(range(len(df))),
    revenue=df['Revenue'],
    day=df['Day']
))

p1 = figure(
    title='Daily Revenue Trend',
    x_axis_label='Day',
    y_axis_label='Revenue ($)',
    height=350,
    width=650
)

p1.line(
    'x',
    'revenue',
    source=source_line,
    line_width=3
)

p1.circle(
    'x',
    'revenue',
    source=source_line,
    size=8
)

p1.add_tools(
    HoverTool(
        tooltips=[
            ('Day', '@day'),
            ('Revenue', '@revenue')
        ]
    )
)

show(p1)


# =========================
# 2. BAR CHART
# =========================
# Why:
# To compare the number of orders across different days.


source_bar = ColumnDataSource(data=dict(
    day=df['Day'],
    orders=df['Orders']
))

p2 = figure(
    title='Orders by Day',
    x_range=df['Day'].tolist(),
    x_axis_label='Day',
    y_axis_label='Orders',
    height=350,
    width=650
)

p2.vbar(
    x='day',
    top='orders',
    source=source_bar,
    width=0.7
)

p2.add_tools(
    HoverTool(
        tooltips=[
            ('Day', '@day'),
            ('Orders', '@orders')
        ]
    )
)

show(p2)


# =========================
# 3. SCATTER PLOT
# =========================
# Why:
# To see whether there is a relationship between
# orders and revenue.


source_scatter = ColumnDataSource(data=dict(
    orders=df['Orders'],
    revenue=df['Revenue'],
    day=df['Day']
))

p3 = figure(
    title='Orders vs Revenue',
    x_axis_label='Orders',
    y_axis_label='Revenue ($)',
    height=350,
    width=650
)

p3.scatter(
    x='orders',
    y='revenue',
    source=source_scatter,
    size=12
)

p3.add_tools(
    HoverTool(
        tooltips=[
            ('Day', '@day'),
            ('Orders', '@orders'),
            ('Revenue', '@revenue')
        ]
    )
)

show(p3)


# =========================
# 4. PIE CHART
# =========================
# Why:
# There are only a few product categories,
# so a pie chart clearly shows each category's
# share of total revenue.


total_revenue = sum(cat_revenue)

percentages = [
    revenue / total_revenue * 100
    for revenue in cat_revenue
]


# Convert percentages into angles
angles = [
    percentage / 100 * 2 * 3.14159
    for percentage in percentages
]


source_pie = ColumnDataSource(data=dict(
    category=cat_names,
    revenue=cat_revenue,
    percentage=percentages,
    angle=angles
))


p4 = figure(
    title='Revenue Share by Category',
    height=450,
    width=650,
    toolbar_location=None,
    x_axis_type=None,
    y_axis_type=None
)

p4.wedge(
    x=0,
    y=0,
    radius=0.8,
    start_angle=cumsum('angle'),
    end_angle=cumsum('angle'),
    source=source_pie
)

p4.add_tools(
    HoverTool(
        tooltips=[
            ('Category', '@category'),
            ('Revenue', '@revenue'),
            ('Share', '@percentage{0.0}%')
        ]
    )
)

show(p4)


# =========================
# SO WHAT?
# =========================

print("""
The founder should focus on the strong revenue and order
performance on Friday and Saturday.

Electronics generated the largest share of category revenue,
while higher orders are strongly associated with higher revenue.
""")


