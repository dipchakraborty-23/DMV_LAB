import re
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

# Read the CSV file
df = pd.read_csv('D:\Dip_DMV_LAB\company_dataset.csv')

# Clean the data
df['name'] = df['name'].str.strip()
df['ratings'] = pd.to_numeric(df['ratings'], errors='coerce')
df['review_count'] = df['review_count'].str.replace('(', '').str.replace(')', '').str.replace('k Reviews', '').str.strip()
df['review_count'] = pd.to_numeric(df['review_count'], errors='coerce')
df['years'] = df['years'].str.replace(' years old', '').str.strip()
df['years'] = pd.to_numeric(df['years'], errors='coerce')

# Extract main headquarters (first location)
df['main_hq'] = df['hq'].str.split('+').str[0].str.strip()

print("="*80)
print("TASK 1: HEADQUARTER NAMES OF TOP 10 COMPANIES")
print("="*80)
top_10_hq = df.head(10)[['name', 'main_hq']]
for idx, row in top_10_hq.iterrows():
    print(f"{idx+1}. {row['name']}: {row['main_hq']}")

# TASK 2: Bar Chart - Company Rating wise (Top 10)
print("\n" + "="*80)
print("TASK 2: BAR CHART - TOP 10 COMPANIES BY RATING")
print("="*80)

plt.figure(figsize=(12, 6))
top_10 = df.head(10)
plt.bar(range(len(top_10)), top_10['ratings'], color='steelblue', edgecolor='black')
plt.xlabel('Companies', fontsize=12, fontweight='bold')
plt.ylabel('Ratings', fontsize=12, fontweight='bold')
plt.title('Top 10 Companies by Rating', fontsize=14, fontweight='bold')
plt.xticks(range(len(top_10)), top_10['name'], rotation=45, ha='right')
plt.ylim(0, 5)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('task2_bar_chart_ratings.png', dpi=300, bbox_inches='tight')
plt.show()
print("✓ Bar chart saved as 'task2_bar_chart_ratings.png'")

# TASK 3: Funnel Chart - Companies Review wise (Top 10)
print("\n" + "="*80)
print("TASK 3: FUNNEL CHART - TOP 10 COMPANIES BY REVIEW COUNT")
print("="*80)

top_10_reviews = df.nlargest(10, 'review_count')[['name', 'review_count']].sort_values('review_count', ascending=False)

fig = go.Figure(go.Funnel(
    y=top_10_reviews['name'],
    x=top_10_reviews['review_count'],
    textposition="inside",
    textinfo="value+percent initial",
    marker=dict(color=px.colors.sequential.Blues_r),
    connector={"line": {"color": "royalblue"}}
))

fig.update_layout(
    title="Top 10 Companies by Review Count (Funnel Chart)",
    title_font_size=16,
    height=600,
    width=900
)

fig.write_html('task3_funnel_chart_reviews.html')
fig.show()
print("✓ Funnel chart saved as 'task3_funnel_chart_reviews.html'")

# TASK 4: Line Chart - Company Count wise (Top 10)
print("\n" + "="*80)
print("TASK 4: LINE CHART - TOP 10 COMPANIES BY COUNT/INDEX")
print("="*80)

plt.figure(figsize=(12, 6))
top_10 = df.head(10)
plt.plot(range(1, 11), top_10['ratings'], marker='o', linewidth=2, 
         markersize=8, color='darkgreen', markerfacecolor='lightgreen', 
         markeredgewidth=2, markeredgecolor='darkgreen')
plt.xlabel('Company Rank', fontsize=12, fontweight='bold')
plt.ylabel('Rating', fontsize=12, fontweight='bold')
plt.title('Rating Trend of Top 10 Companies', fontsize=14, fontweight='bold')
plt.xticks(range(1, 11), top_10['name'], rotation=45, ha='right')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('task4_line_chart_count.png', dpi=300, bbox_inches='tight')
plt.show()
print("✓ Line chart saved as 'task4_line_chart_count.png'")

# TASK 5: Pie Chart - Top 5 Companies by Years
print("\n" + "="*80)
print("TASK 5: PIE CHART - TOP 5 COMPANIES BY AGE (YEARS)")
print("="*80)

top_5_years = df.nlargest(5, 'years')[['name', 'years']]

plt.figure(figsize=(10, 8))
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc']
explode = (0.05, 0.05, 0.05, 0.05, 0.05)

plt.pie(top_5_years['years'], labels=top_5_years['name'], autopct='%1.1f%%',
        startangle=90, colors=colors, explode=explode, shadow=True,
        textprops={'fontsize': 11, 'fontweight': 'bold'})
plt.title('Top 5 Oldest Companies by Age (Years)', fontsize=14, fontweight='bold', pad=20)
plt.axis('equal')
plt.tight_layout()
plt.savefig('task5_pie_chart_years.png', dpi=300, bbox_inches='tight')
plt.show()
print("✓ Pie chart saved as 'task5_pie_chart_years.png'")

# Display summary statistics
print("\n" + "="*80)
print("SUMMARY STATISTICS")
print("="*80)
print(f"Total Companies: {len(df)}")
print(f"Average Rating: {df['ratings'].mean():.2f}")
print(f"Average Reviews: {df['review_count'].mean():.1f}k")
print(f"Average Age: {df['years'].mean():.1f} years")
print("="*80)