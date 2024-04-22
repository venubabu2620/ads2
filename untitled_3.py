# -*- coding: utf-8 -*-
"""untitled 3

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mm2UKOF0AeRrfSR7obdNBO2Fz4-tjlZl
"""

# Loading neccessary packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Loading the dataset
df = pd.read_csv("/content/Data.csv")
# Viewing the top 5 rows
df.head(5)

df.shape

number_of_countries= df['Country'].value_counts()
print(number_of_countries)

number_of_years= df['Year'].value_counts()
print(number_of_years)

number_of_countries= df['Club'].value_counts()
print(number_of_countries)

number_of_Leagues= df['League'].value_counts()
print(number_of_Leagues)

total_goals_by_player = df.groupby("Player Names")["Goals"].sum().sort_values(ascending=False)
total_goals_by_player.head()

def plot_top_10_players_goals(data):
    """
    Plot a bar graph showing the total goals scored by the top 10 players across all years.

    Parameters:
    - data: pandas DataFrame containing football player data with columns 'Player Names', 'Goals', and 'Year'.
    """
    # Extract unique years from the DataFrame
    years = data['Year'].unique()

    # Initialize an empty list to store top 10 players across all years
    top_10_all_years = []

    # Loop through each year
    for year in years:
        # Filter the DataFrame for the current year
        df_year = data[data['Year'] == year]

        # Grouping by player name and summing up the goals for the current year
        total_goals_by_player = df_year.groupby('Player Names')['Goals'].sum().reset_index()

        # Sorting the DataFrame by total goals in descending order
        total_goals_sorted = total_goals_by_player.sort_values(by='Goals', ascending=False)

        # Selecting the top 10 players for the current year
        top_10_players_year = total_goals_sorted.head(10)

        # Append the top 10 players for the current year to the list
        top_10_all_years.append(top_10_players_year)

    # Concatenate the DataFrames in the list into a single DataFrame
    top_10_all_years = pd.concat(top_10_all_years, ignore_index=True)

    # Grouping by player name and summing up the goals across all years
    total_goals_all_years = top_10_all_years.groupby('Player Names')['Goals'].sum().reset_index()

    # Sorting the DataFrame by total goals in descending order
    total_goals_sorted_all_years = total_goals_all_years.sort_values(by='Goals', ascending=False)

    # Selecting the top 10 players across all years
    top_10_players_all_years = total_goals_sorted_all_years.head(10)

    # Plotting the bar graph
    plt.figure(figsize=(10, 6))
    bars = plt.bar(top_10_players_all_years['Player Names'], top_10_players_all_years['Goals'], color='skyblue')
    plt.xlabel('Players', fontsize=16)
    plt.ylabel('Total Goals', fontsize=16)
    plt.title('Total Goals Scored by Top 10 Players Across All Years', fontsize=14)
    plt.xticks(rotation=90, ha='right', fontsize=16,)
    plt.yticks(fontsize=10)
    plt.tight_layout()

    # Annotate the bars with the total goals
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height)}', ha='center', va='bottom', fontsize=14)

    plt.show()

# Call the function with the DataFrame containing football player data.
plot_top_10_players_goals(df)

def plot_total_games_played_by_country(df):
    """
    Plot a pie chart showing the distribution of total games played by country across all years.

    Parameters:
        df: The path to the CSV file containing the data.
    """
    # Group by country and calculate the total games played
    total_games_by_country = df.groupby("Country")["Matches_Played"].sum().sort_values(ascending=False)

    # Plotting the pie chart
    plt.figure(figsize=(8, 8))  # Adjust figure size for better readability
    plt.pie(total_games_by_country, labels=total_games_by_country.index,
            autopct='%1.1f%%', startangle=140)  # Simplified autopct format for percentage display
    plt.title('Total Games Played by Country Across All Years', fontsize=16)  # Increased font size for title
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    plt.show()

# Example usage
plot_total_games_played_by_country(df)

def plot_goals_vs_minutes(df):
    """
    Plot a scatter plot of goals versus minutes played.

    Parameters:
        dataframe (DataFrame): The DataFrame containing the 'Mins' and 'Goals' columns.

    Returns:
        None
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Mins'], df['Goals'], color='blue')
    plt.title("Scatter Plot: Goals vs Minutes", fontsize=14)
    plt.xlabel('Minutes', fontsize=14)
    plt.ylabel('Goals', fontsize=14)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

plot_goals_vs_minutes(df)

# Get descriptive statistics for numerical columns and round the values
describe_table = df.iloc[:, :-1].describe().round(2)  # Round to 2 decimal places
describe_table

# Calculating the correlation matrix for the dataframe confusion_matrix_1
confusion_matrix_1 = df.corr(numeric_only=True)
print(confusion_matrix_1)

def plot_heatmap(confusion_matrix_1, title='Heatmap of Correlation matrix'):
    """
    Plotting a heatmap of the correlation matrix.

    Parameters:
        correlation_matrix (DataFrame): Correlation matrix data.
        title (str, optional): Title of the plot. Defaults to 'Heatmap of Correlation matrix'.
    """
    plt.figure(figsize=(8, 6))
    # plot the correlation matrtix
    sns.heatmap(confusion_matrix_1, annot=True, cmap='summer', linewidths=0.5, fmt='.2f', linecolor='white')
    plt.title(title, fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.show()

# Calling the function
plot_heatmap(confusion_matrix_1, title='Heatmap of Correlation Matrix')

def line_fitting(x, y):
    """
    Perform linear fitting and visualize the fitted line with confidence interval.

    Parameters:
        x : Independent variable (x-axis).
        y : Dependent variable (y-axis).

    Returns:
        tuple: Tuple containing slope, intercept, and confidence interval of the fitted line.
    """
    # Fitting a degree 1 using polyfit function.
    coefficients = np.polyfit(x, y, 1)

    # getting slope and y-intercept from the coefficients
    m, b = coefficients

    # Generate predicted y-values based on the line equation.
    y_pred = m * x + b

    # Calculating residuals
    residuals = y - y_pred

    # calculating the variance for the residuals
    variance = np.sum(residuals ** 2) / (len(x) - 2)

    # Calculating the standard error of the estimate
    std_error = np.sqrt(variance)

    # Calculate the t-value for a 95% confidence interval.
    t_value = 1.96

    # Calculating the confidence interval.
    confidence_interval = t_value * std_error

    # Plot the figure with size 10 X 6.
    plt.figure(figsize=(10, 6))
    # plotting the data points on the axis using scatter plot.
    plt.scatter(x, y, color='blue', label='Data points')
    # Fitting the best fit line on the data points.
    plt.plot(x, y_pred, color='red', label='Fitted line')

    # Plot error bars for the confidence interval
    plt.fill_between(x, y_pred - confidence_interval, y_pred + confidence_interval, color='gray', alpha=0.2)

    #  Adding the X and Y labels for the plot.
    plt.xlabel('Shots', fontsize=14)
    plt.ylabel('Goals', fontsize=14)
    # add the titles for the plot.
    plt.title('Linear Fitting with Confidence Interval (Shots vs. Goals)', fontsize=14)
    plt.legend()
    # Adding the grid.
    plt.grid(True)
    plt.show()

    return m, b, confidence_interval

# Example data (replace with your actual data)
shots = df['Shots']
goals = df['Goals']

# fitting the best fit line along with confidence interval 95%.
slope, intercept, confidence_interval = line_fitting(shots, goals)
# printing the slope.
print("Slope:", slope)
# printing the intercept.
print("Intercept:", intercept)
# printing the value at the confidence interval 95%.
print("Confidence Interval (95%):", confidence_interval)

print(df.columns)

scaler = StandardScaler()
def preprocess_data(data):
    """
    Standardizing the 'Matches_Played' and 'Substitution' columns.

    Parameters:
        data: DataFrame containing 'Year' and 'Substitution' columns.

    Returns:
        ndarray: Standardized data.
    """
    return scaler.fit_transform(data[['Matches_Played', 'Shots Per Avg Match']])

def perform_elbow_method(data_scaled):
    """
    calculating the optimal value using elbow method for clusters.

    Parameters:
        data_scaled: Standardized data.

    Returns:
        integer: Optimal number of clusters.
    """
    wcss = []
    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, random_state=0)
        kmeans.fit(data_scaled)
        wcss.append(kmeans.inertia_)
    # Plot the elbow curve
    plt.plot(range(1, 11), wcss, marker='o')
    plt.xlabel('Number of Clusters')
    plt.ylabel('WCSS')
    plt.title('Elbow Method')
    plt.grid(True)
    plt.show()
    # Find the elbow point
    diff = np.diff(wcss)
    diff_r = diff[1:] / diff[:-1]
    return np.argmin(diff_r) + 2  # Adding 2 to consider the shift in indices

def visualize_clusters(data_scaled, optimal_num_clusters):
    """
    Visualizing the clusters.

    Parameters:
        data_scaled (ndarray): Standardized data.
        optimal_num_clusters (int): Optimal number of clusters.
    """
    kmeans = KMeans(n_clusters=optimal_num_clusters, random_state=0)
    cluster_labels = kmeans.fit_predict(data_scaled)

    plt.figure(figsize=(8, 6))
    for cluster_label in range(optimal_num_clusters):
        plt.scatter(data_scaled[cluster_labels == cluster_label, 0],
                    data_scaled[cluster_labels == cluster_label, 1],
                    label=f'Cluster {cluster_label + 1}')

    plt.xlabel('Standardized Year')
    plt.ylabel('Standardized Substitution')
    plt.title('KMeans Clustering')
    plt.legend()
    plt.grid(True)
    plt.show()

# preprocessing the data
data_scaled = preprocess_data(df[['Matches_Played', 'Shots Per Avg Match']])

# calulating the optimal value for determing the clusters using elbow method.
optimal_num_clusters = perform_elbow_method(data_scaled)

# Performing KMeans clustering with the optimal number of clusters
kmeans = KMeans(n_clusters=optimal_num_clusters, random_state=0)
cluster_labels = kmeans.fit_predict(data_scaled)

# Visualizing the clusters
visualize_clusters(data_scaled, optimal_num_clusters)

# Sample data for prediction
X_new = np.array([[30, 50000], [40, 600], [50, 7000000], [90, 100000]])

# Predict cluster labels for the sample data points
predicted_labels = kmeans.predict(scaler.transform(X_new))

# Generate colors randomly based on the number of clusters
colors = plt.cm.viridis(np.linspace(0, 1, optimal_num_clusters))

# Plot the sample data points with colors corresponding to their predicted clusters
for i, label in enumerate(predicted_labels):
    plt.scatter(X_new[i, 0], X_new[i, 1], color=colors[label], label=f'Predicted Cluster {label}')

plt.xlabel('Matches Played', fontsize=14)
plt.ylabel('Shots Per Avg Match', fontsize=14)
plt.title('KMeans Clustering', fontsize=14)
plt.legend()
plt.grid(True)
plt.show()

print("Predicted labels for the sample data points:", predicted_labels)

mean_df = df.select_dtypes(include=['int64', 'float64'])
# Calculating the mean for each numeric column
means = mean_df.mean()

print("Mean values for each numeric column:", means,sep='\n')

median_df = df.select_dtypes(include=['int64', 'float64'])
# Calculating the meadian for each numeric column
medians = median_df.median()

print("Median values for each numeric column:", medians,sep='\n')

standard_deviation_df = df.select_dtypes(include=['int64', 'float64'])
# Calculating the standard deviation for each numeric column
standard_deviation = standard_deviation_df.std()

print("Standarad deviation values for each numeric column:", standard_deviation,sep='\n')

skew_df = df.select_dtypes(include=['int64', 'float64'])
# Calculating the skew for each numeric column
skewness = standard_deviation_df.skew()

print("skewness values for each numeric column:", skewness,sep='\n')

df_kurtosis_df = df.select_dtypes(include=['int64', 'float64'])
# Calculating the standard deviation for each numeric column
df_kurtosis = standard_deviation_df.kurtosis()

print("kurtosis values for each numeric column:", df_kurtosis,sep='\n')