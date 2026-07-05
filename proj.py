import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\63947\OneDrive\Documents\codes\.vscode\Project 1\gold-silver.csv")


df["date"] = pd.to_datetime(df["date"])

df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month

print(df.head())
print(df.dtypes)

def basic_stats(df):
    highest = df['gold'].max()
    lowest = df['gold'].min()
    average_price = df['gold'].mean()
    lowest_date = df[df["gold"] == lowest]["date"].dt.strftime("%Y-%m-%d").values[0]
    highest_date = df[df["gold"] == highest]["date"].dt.strftime("%Y-%m-%d").values[0]
    
    print(f"Highest Gold price: ${highest:.2f} on {highest_date}")  # indented
    print(f"Lowest Gold price: ${lowest:.2f} on {lowest_date}")     # indented
    print(f"Average Gold price: ${average_price:.2f}")              # indented




def yearly_performance (df):
    grouped_by_year = df.groupby('year') ['gold'].mean()
    
    for year in grouped_by_year:
        print(f"{year}: ${grouped_by_year[year]: .2f}")



def gold_silver_correlation (df):
    correlation = df ['gold'].corr(df ['silver'])
    print(f"Correlation: {correlation}")
    if correlation > 0.8:
        print("Positive correlation")
    elif correlation < 0.5:
        print("Weak correlation")
    elif correlation >= 0.5 and correlation <= 0.8:
        print("Moderate positive correlaltion")
    else:
        print("Negative correlation")
        



def best_worst_months (df):
    month_names = {1: "January", 2: "February", 3: "March", 4: "April", 
               5: "May", 6: "June", 7: "July", 8: "August", 
               9: "September", 10: "October", 11: "November", 12: "December"}
               
    grouped_by_month = df.groupby('month') ['gold'].mean()
    best_month = grouped_by_month.idxmax()
    worst_month = grouped_by_month.idxmin()
    print(f"Best month: {month_names[best_month]} - ${grouped_by_month[best_month]:.2f}")
    print(f"Worst month: {month_names[worst_month]} - ${grouped_by_month[worst_month]:.2f}")
    

  
def plot_all(df):
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 8))
    
    # Chart 1
    axes[0].plot(df["date"], df["gold"], label="Gold")
    axes[0].plot(df["date"], df["silver"], label="Silver")
    axes[0].legend()
    axes[0].set_title("Gold vs Silver Price Over Time")
    axes[0].set_xlabel("Date")
    axes[0].set_ylabel("Price (USD)")
    
    # Chart 2
    grouped_by_year = df.groupby("year")["gold"].mean()
    axes[1].bar(grouped_by_year.index, grouped_by_year.values)
    axes[1].set_title("Yearly Average Gold Price")
    axes[1].set_xlabel("Year")
    axes[1].set_ylabel("Average Price (USD)")
    
    plt.tight_layout()

    
def save_summary(df):
        highest = df['gold'].max()
        lowest = df['gold'].min()
        average = df['gold'].mean()
        correlation = df ['gold'].corr(df ['silver'])
        
        grouped_by_month = df.groupby('month') ['gold'].mean()
        best_month = grouped_by_month.idxmax()
        worst_month = grouped_by_month.idxmin()
        
        month_names = {1: "January", 2: "February", 3: "March", 4: "April", 
               5: "May", 6: "June", 7: "July", 8: "August", 
               9: "September", 10: "October", 11: "November", 12: "December"}
    
        with open("gold_summary.txt", "w") as file:
            file.write("=== Gold vs Silver Analysis ===\n\n")
            file.write(f"Highest Gold Price: ${highest:.2f}\n")
            file.write(f"Lowest Gold Price: ${lowest:.2f}\n")
            file.write(f"Average Gold Price: ${average:.2f}\n")
            file.write(f"Correlation: {correlation:.2f}\n")
            file.write(f"Best Month: {month_names[best_month]}\n")
            file.write(f"Worst Month: {month_names[worst_month]}\n")
            
save_summary(df)   
plot_all(df)
plt.show()