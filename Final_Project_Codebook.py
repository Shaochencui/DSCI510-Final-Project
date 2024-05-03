
import streamlit as st
import pandas as pd
#from mpl_toolkits.mplot3d import Axes3D
import plotly.express as px
st.markdown("<link rel='stylesheet' type='text/css' href='styles.css'>", unsafe_allow_html=True)
merged_df = pd.read_csv("merged_lebron_james_stats1.csv")
st.set_option('deprecation.showPyplotGlobalUse', False)

def main():
    st.title("Final Project for DSCI510 : LeBron James' Basketball Career Analysis")
    st.write("Shaochen Cui (Student ID: 1797162168)")
    st.write("Email: cuishaoc@usc.edu")
    
    # Sidebar navigation
    page = st.sidebar.selectbox("Navigate", ["About", "Web App Usage", "Instructions", "Conclusion", "Gotchas", "Contact Information","Problem Answer Page","Dataset description"])

    if page == "About":
        about_page()
    elif page == "Web App Usage":
        web_app_usage_page()
    elif page == "Instructions":
        instructions_page()
    elif page == "Conclusion":
        conclusion_page()
    elif page == "Gotchas":
        gotchas_page()
    elif page == "Contact Information":
        contact_info_page()
    elif page == "Problem Answer Page":
        problem_answer_page()
    elif page == "Dataset description":
        dataset_description()

def about_page():
    st.header("About the Project")
    st.write("In this project, we analyze the performance and career trajectory of LeBron James, one of the greatest basketball players of all time. We explore different metrics such as points scored, rebounds, assists, three-pointers made, and more, to gain insights into his playing style, impact on the game, and overall success. Additionally I will explore how lebron James' salary makes a impact on the season performance.I will mainly use the WS as the standard to analyze LeBron James' performance since WS is an important golden standard to measure how a player impact the game")

def web_app_usage_page():
    st.header("Web App Usage")
    st.write("This web app provides interactive visualizations and analysis tools to explore LeBron James' career data. You can select different metrics, compare them, and visualize trends over time. You can use the side bar to select different part you want to explore about the project")

def instructions_page():
    st.header("Instructions")
    st.write("1. Use the sidebar to select the page you want to explore.")
    st.write("2. Make selections or input parameters as needed.")
    st.write("3. View the results and insights generated by the app.")

def conclusion_page():
    st.header("Conclusion")
    st.write("After I finished the project, I found out that if Lebron James increase more personal attack towards the rim then he might could contribute more to the team which is not surprising since Lebron is always known for unselfishness")
    st.write("For the salary analysis it is kind of surprising to find out that when lebron is not earning huge amount of money, he performs the best on court and when he earn a huge amount on salary, his performance decreaes which is kind of surprising. ")
    st.write("Through this project, we aim to gain a deeper understanding of LeBron James' career, his impact on the sport of basketball, and the factors contributing to his success. We hope you find the insights and analysis provided by this web app informative and engaging.")

def gotchas_page():
    st.header("Gotchas")
    st.write("1. Some visualizations may take a few moments to load, especially for larger datasets.")
    st.write("2. Make sure to select relevant metrics and parameters to get meaningful insights.")
    st.write("3. The variety of the database might also be a little bit small that other databases such as the data of performance of team that Lebron has stayed could better help to analyze how Lebron helped his team")
    st.write("4. Some charts I create might be a little bit hard to read due to its complexity")
    st.write("5. Still, Data fetching is the hardest part for me in this project")

def contact_info_page():
    st.header("Contact Information")
    st.write("If you have any questions, feedback, or suggestions, feel free to reach out to me at cuishaoc@usc.edu. I value your input and are always looking for ways to improve my analysis and user experience.")
def problem_answer_page():
    st.header("Problems Answer")
    st.subheader("Problem 1:.What did you set out to study?  (i.e. what was the point of your project?  This should be close to your Milestone 1 assignment, but if you switched gears or changed things, note it here.)")
    st.write("In this project, I set out to study and analyze the basketball career of LeBron James, one of the most iconic and influential players in the history of the NBA. As a huge fan of LeBron James, I wanted to delve deep into his performance metrics, playing style, impact on the game, and overall success throughout his illustrious career. My goal was to gain insights into various aspects of his career, such as points scored, rebounds, assists, three-pointers made, salary trends, and Player Efficiency Rating (PER), among others. Further, I will mainly use the WS data as a standard to analyze LeBron's statistic since it is a representative data in how LeBron contributing the winning of the team ")
    st.subheader("Problem2:.What did you Discover/what were your conclusions (i.e. what were your findings?  Were your original assumptions confirmed, etc.?)")
    st.write("My original assumption is that when if lebron james passes more ball to his teammate then he could better help his team ")
    st.write("But after i finished the analysis I found out that if Lebron increases his personal attack, he could better helped his team to win. I am also kind of surpised how lebron evolved over 20 years of career that his three point shooting is better and better every year he gets older. ")
    st.write("By conducting a thorough analysis of LeBron James' career, I aimed to uncover patterns, trends, and correlations within his performance data. Additionally, I wanted to provide interactive visualizations and insights to help basketball enthusiasts, researchers, and fans gain a deeper understanding of LeBron James' impact on the sport and his journey to becoming one of the greatest basketball players of all time.")
    st.subheader("Problem 3:What difficulties did you have in completing the project?  ")
    st.write("I think the main gotcha is the data fetching process including merging three datasets because learing to use api is kind of hard for me and web scraping data also sometime fetch the wrong target table when i am trying to merge them I found out that datasets from different sources often have different size so it is kind of hard to merge them")
    st.subheader("problem4:What skills did you wish you had while you were doing the project?")
    st.write("Improving my knowledge of database management systems (DBMS) and SQL would have been beneficial for efficiently storing, querying, and managing large datasets. Understanding concepts like indexing, normalization, and database optimization could have improved the performance of data retrieval and manipulation.")
    st.subheader("Problem5:What would you do “next” to expand or augment the project?")
    st.write("Gather additional player statistics beyond the basic performance metrics currently included in the database. This could include advanced metrics like usage rate, true shooting percentage, defensive rating, and box plus-minus, among others. Collecting data from multiple sources and seasons would provide a more comprehensive understanding of player performance.Incorporate Team and Opponent Statistics: Include team-level statistics such as win-loss records, team offensive and defensive ratings, pace of play, and opponent strength. This would allow for a deeper analysis of player performance in different team contexts and against varying levels of competition.")
def dataset_description():
    st.write("Dataset Description:The dataset contains detailed statistics representing various aspects of LeBron James' performance over his career in the NBA. Each row corresponds to a single season, and the dataset includes metrics such as player age, team, league, position, games played, minutes played, player efficiency rating (PER), true shooting percentage (TS%), three-point attempt rate (3PAr), free throw attempt rate (FTr), offensive rebound percentage (ORB%), defensive rebound percentage (DRB%), total rebound percentage (TRB%), assist percentage (AST%), steal percentage (STL%), block percentage (BLK%), turnover percentage (TOV%), usage percentage (USG%), offensive win shares (OWS), defensive win shares (DWS), win shares (WS), win shares per 48 minutes (WS/48), offensive box plus/minus (OBPM), defensive box plus/minus (DBPM), player ID, season ID, league ID, team ID, team abbreviation, games played, games started, minutes played, field goals made (FGM), field goals attempted (FGA), field goal percentage (FG%), three-point field goals made (FG3M), three-point field goals attempted (FG3A), three-point field goal percentage (FG3%), free throws made (FTM), free throws attempted (FTA), free throw percentage (FT%), offensive rebounds (OREB), defensive rebounds (DREB), total rebounds (REB), assists (AST), steals (STL), blocks (BLK), turnovers (TOV), personal fouls (PF), points scored (PTS), and salary.")
    st.header("Head of the dataset")
    st.dataframe(merged_df.head())
# Run the app
if __name__ == "__main__":
    main()

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the merged dataset
merged_df = pd.read_csv("merged_lebron_james_stats1.csv")

# Define the Streamlit app
def main():
    st.sidebar.title("Analysis Part")
    selected_page = st.sidebar.radio("Go to", ["Home", "LeBron James' Basketball Career Analysis", "LeBron James' Three-Pointers vs Total Points Analysis","Lebron James'Salary and win share analysis","LeBron James' Defensive effort influencing Game","LeBron James'passing makes a team better","How Lebron James' personal attack inlfuence the game"])

    if selected_page == "Home":
        home_page()
    elif selected_page == "LeBron James' Basketball Career Analysis":
        lebron_career_analysis()
    elif selected_page == "LeBron James' Three-Pointers vs Total Points Analysis":
        three_point_analysis()
    elif selected_page == "Lebron James'Salary and win share analysis":
        salary_per_analysis()
    elif selected_page == "LeBron James' Defensive effort influencing Game":
        defensive_effort_analysis()
    elif selected_page == "LeBron James'passing makes a team better":
        lebron_can_pass()
    elif selected_page == "How Lebron James' personal attack inlfuence the game":
        personal_attack()
    


def home_page():
    st.title("Welcome to LeBron James' Analysis App")
    st.write("Select an option from the sidebar to analyze LeBron James' basketball career.")
    

def lebron_career_analysis():
    st.title("LeBron James' Basketball Career Analysis")
    st.write("Tips: Please do not select any selection end with ID, For example PLAYER_ID and TEAM_ABBREVIATION")
    st.write("I will start with an heatmap to let you have a overall look on the lebron career's statistic and how they related to each other")
    st.write("This app allows you to analyze the relationship between any two metrics of LeBron James' basketball career.")
    st.write("You can select any two lebron james' career data to show on the heatmap to represent the correlational relationship ")

    # Allow users to select metrics for analysis
    selected_metrics = st.multiselect(
        "Select metrics to analyze:", 
        [col for col in merged_df.columns if col not in ["Tm", "Lg", "Pos", "PLAYER_AGE"]]
    )
    
    if not selected_metrics:
        st.warning("Please select at least one metric.")
        return
    
    # Calculate the correlation matrix
    correlation_matrix = merged_df[selected_metrics].corr()
    
    # Visualize correlation matrix using heatmap
    st.subheader("Correlation Heatmap")
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
    st.pyplot()
    
    # Show correlation values as a table
    st.subheader("Correlation Values")
    st.dataframe(correlation_matrix)
    
    # Additional analysis or visualizations can be added here based on user selection
   

def three_point_analysis():
    st.title("LeBron James' Three-Pointers vs Total Points Analysis")
    st.write("This app analyzes the relationship between the total three-pointers LeBron James made and the total points he scored each season.")
    
    # Scatter plot
    st.subheader("Scatter Plot")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=merged_df, x='3PAr', y='PTS', hue='SEASON_ID', palette='viridis')
    plt.xlabel("3 point shooting percentage")
    plt.ylabel("Total Points")
    plt.title("LeBron James' 3-pointer shooting vs Total Points Each Season")
    st.pyplot()
    st.write("We can see from the plot that the if Lebron James attempted to shoot around 23 percent of three-pointer out of his total shooting, he will score the most points in the season ")
    st.write("From the plot, it becomes evident that when LeBron James attempts to shoot around 23 percent of his total shots from the three-point line, he tends to score the most points in the season. This observation underscores the strategic importance of three-point shooting in maximizing scoring output for LeBron.")
    st.write("Additionally, it's worth noting that while three-point shooting may not directly correlate with Win Shares (WS), analyzing this aspect of LeBron's game provides valuable insights into his offensive efficiency and adaptability to modern basketball trends. In today's fast-paced NBA, where teams increasingly emphasize three-point shooting as a primary offensive strategy, understanding LeBron's performance from beyond the arc helps contextualize his overall impact on the court.")
    st.write("By integrating three-pointer analysis alongside traditional metrics like Win Shares, we gain a more comprehensive understanding of LeBron's versatility and effectiveness in today's evolving basketball landscape. This approach allows us to appreciate how LeBron's ability to adapt to contemporary playing styles contributes to his continued success and leadership within the league.")
def salary_per_analysis():
    st.title("LeBron James' Salary vs Player Efficiency Rating Analysis")
    st.write("This app analyzes the relationship between LeBron James' salary and his Player Efficiency Rating (PER) each season.This could also be influeced by the age and the team he stayed in.")
    # Scatter plot
    st.subheader("Scatter Plot")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=merged_df, x='SALARY', y='PER', hue='SEASON_ID', palette='viridis')
    plt.xlabel("LeBron James' Salary")
    plt.ylabel("Player Efficiency Rating (PER)")
    plt.title("LeBron James' Salary vs Player Efficiency Rating (PER)")
    plt.legend(title="Season")
    st.pyplot()

    # Analysis
    st.subheader("Analysis")
    st.write("""
    - The x-axis represents LeBron James' salary for each season, while the y-axis represents his Player Efficiency Rating (PER).
    - Each point on the scatter plot corresponds to a specific season in LeBron James' career.
    - The color of each point indicates the season, providing a visual reference for the data points.
    """)
    
    st.write("The scatter plot suggests that when LeBron James earns $15,000,000 (or $15 million), he tends to have the highest Player Efficiency Rating (PER). Several factors could contribute to this observation:")
    st.write("Motivation and Performance Incentives: Higher earnings may serve as a motivating factor for LeBron James to perform at his peak level. Athletes often strive to justify their salaries through exceptional performance on the court.")
    st.write("Health and Fitness: With higher earnings, LeBron may have access to better training facilities, medical resources, and support staff to maintain optimal health and fitness. Improved physical conditioning can enhance his performance and efficiency on the court.")
    st.write("Overall, the correlation between LeBron's earnings and his PER suggests a complex interplay of various factors, including motivation, experience, team dynamics, leadership, off-court opportunities, and overall well-being.")
def defensive_effort_analysis():
    st.title("LeBron James' Defensive Impact Analysis")
    st.write("Explore how blocks (BLK) and steals (STL) influence LeBron James' Win Shares (WS).")

    # Allow users to select metrics for analysis
    selected_metrics = st.multiselect(
        "Select metrics to analyze:", 
        ["BLK", "STL", "WS"]
    )

    if not selected_metrics:
        st.warning("Please select at least one metric.")
        return

    # Create 3D scatter plot
    fig = px.scatter_3d(
        merged_df, 
        x='BLK', 
        y='STL', 
        z='WS', 
        color="SEASON_ID",
        labels={'BLK': 'Blocks (BLK)', 'STL': 'Steals (STL)', 'WS': 'Win Shares (WS)'},
        title="LeBron James' Impact Analysis",
        width=800, 
        height=600
    )

    fig.update_layout(scene=dict(
        xaxis_title='Blocks (BLK)',
        yaxis_title='Steals (STL)',
        zaxis_title='Win Shares (WS)'
    ))

    st.plotly_chart(fig)

    st.write("In this graph, we can see how different combinations of blocks (BLK) and steals (STL) influence LeBron James' Win Shares (WS).")
    st.write("In this graph, we can observe how different combinations of blocks (BLK) and steals (STL) contribute to LeBron James' Win Shares (WS), providing insights into his defensive impact on the team's success. A higher number of blocks and steals by LeBron correlates with an increase in Win Shares, suggesting that his defensive efforts play a crucial role in the team's overall performance.The data visualized here showcases that as LeBron accumulates more blocks and steals, his Win Shares tend to rise proportionally. This indicates that his defensive actions, such as blocking shots and stealing the ball, directly translate into positive outcomes for the team, as reflected by the Win Shares metric. Essentially, the more active LeBron is in disrupting opponent plays through blocks and steals, the more he contributes to the team's success and overall defensive effectiveness.")
    st.write("Therefore, this graph highlights the importance of LeBron's defensive efforts in shaping the team's performance and underscores his value beyond scoring points. It emphasizes how his defensive prowess significantly impacts the team's ability to secure victories and achieve success on the court.")
    st.write("The chart illustrates that LeBron James achieves the highest Win Shares (WS) when he records around 550 to 600 assists and maintains an assists rate (AST%) in the range of 35 percent to 40 percent. This suggests that LeBron's effectiveness in facilitating scoring opportunities for his teammates significantly contributes to his overall impact on the team's success.

When LeBron accumulates a moderate number of assists (550 to 600), it indicates his active involvement in setting up scoring plays for his teammates. This level of distribution suggests a balance between scoring and facilitating, where LeBron optimally utilizes his passing skills to create scoring opportunities while also contributing to team cohesion and offensive fluidity.

Furthermore, the observed range of assists rates (35 percent to 40 percent) implies that LeBron is not only distributing the ball frequently but also doing so efficiently. A high assists rate within this range suggests that LeBron is making effective decisions with the ball, consistently finding open teammates, and generating high-quality scoring chances.

Overall, the combination of moderate assist volume and efficient passing reflects LeBron's ability to orchestrate the offense and elevate his team's performance. By striking a balance between scoring and playmaking, LeBron maximizes his impact on the court, leading to higher Win Shares and ultimately contributing to his team's success.")
def lebron_can_pass():
    st.title("LeBron James' Passing Analysis")
    st.write("This analysis explores how LeBron James' passing affects his Win Shares (WS).")
    

    # Add a selectbox for choosing the chart
    chart_choice = st.selectbox("Select Chart", ["AST% vs WS", "AST vs WS"])

    # Plot line chart based on selection
    if chart_choice == "AST% vs WS":
        ast_percentage_ws_chart()
    elif chart_choice == "AST vs WS":
        ast_ws_chart()

def ast_percentage_ws_chart():
    st.subheader("AST% vs Win Shares (WS)")
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=merged_df, x='AST%', y='WS', color='blue')
    sns.scatterplot(data=merged_df, x='AST%', y='WS', color='red', marker='o', s=50)
    plt.xlabel("AST%")
    plt.ylabel("Win Shares (WS)")
    plt.title("LeBron James' AST% vs Win Shares (WS)")
    st.pyplot()
    st.write(" We can see from the chart that when lebron has around 550 to 600 assists he has the best WS win-share while when his assists rates are around 35 percent to 40 percent He has the highest winshare value. It could mean that when Lebron has middle portion of passing the ball then he will mostly helps his team")

def ast_ws_chart():
    st.subheader("AST vs Win Shares (WS)")
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=merged_df, x='AST', y='WS', color='green')
    sns.scatterplot(data=merged_df, x='AST', y='WS', color='red', marker='o', s=50)
    plt.xlabel("AST")
    plt.ylabel("Win Shares (WS)")
    plt.title("LeBron James' AST vs Win Shares (WS)")
    st.pyplot()

    st.write(" We can see from the chart that when lebron has around 550 to 600 assists he has the best WS win-share while when his assists rates are around 35 percent to 40 percent He has the highest winshare value. It could mean that when Lebron has middle portion of passing the ball then he will mostly helps his team")
    st.write("The chart illustrates that LeBron James achieves the highest Win Shares (WS) when he records around 550 to 600 assists and maintains an assists rate (AST%) in the range of 35 percent to 40 percent. This suggests that LeBron's effectiveness in facilitating scoring opportunities for his teammates significantly contributes to his overall impact on the team's success.")
    st.write("When LeBron accumulates a moderate number of assists (550 to 600), it indicates his active involvement in setting up scoring plays for his teammates. This level of distribution suggests a balance between scoring and facilitating, where LeBron optimally utilizes his passing skills to create scoring opportunities while also contributing to team cohesion and offensive fluidity.")
    st.write("Furthermore, the observed range of assists rates (35 percent to 40 percent) implies that LeBron is not only distributing the ball frequently but also doing so efficiently. A high assists rate within this range suggests that LeBron is making effective decisions with the ball, consistently finding open teammates, and generating high-quality scoring chances.")
    st.write("Overall, the combination of moderate assist volume and efficient passing reflects LeBron's ability to orchestrate the offense and elevate his team's performance. By striking a balance between scoring and playmaking, LeBron maximizes his impact on the court, leading to higher Win Shares and ultimately contributing to his team's success.")
def personal_attack():
    st.title("LeBron James' Performance Analysis")
    st.write("Explore how points scored, field goals made, free throws made, and usage rate influence win shares.")

    # Select variables for analysis
    selected_variables = st.multiselect("Select variables:", ["PTS", "FGM", "FTM", "USG%", "WS"])

    # Filter dataframe based on selected variables
    filtered_df = merged_df[selected_variables]

    # Display selected variables dataframe
    st.write(filtered_df)

    # Check if there are selected variables
    if len(selected_variables) > 1:
        # Pairplot for selected variables
        st.subheader("Pairplot")
        sns.pairplot(filtered_df, diag_kind='kde')
        st.pyplot()
    st.write("1.Selection of Variables: Use the multiselect widget to choose the variables you want to analyze. You can select from the following options: points scored (PTS), field goals made (FGM), free throws made (FTM), usage rate (USG%), and win shares (WS). Selecting multiple variables will provide a comprehensive view of their relationships.")
    st.write("2.Display of Dataframe: Below the variable selection widget, you'll see a dataframe displaying the selected variables. This dataframe provides a tabular representation of the data, showing the values of each variable for each observation (e.g., each season or game).")
    st.write("3.Pairplot: If you select more than one variable, a pairplot will be generated below the dataframe. The pairplot consists of multiple scatterplots arranged in a grid format. Each scatterplot shows the relationship between two selected variables")
    st.write("4.Interpreting Scatterplots: In the pairplot, each scatterplot represents the relationship between two variables. The points on the scatterplot indicate the values of the selected variables for each observation. The position of the points relative to the axes shows how the variables are related.")
    st.subheader("Analysis")
    st.write("Interpretation: When LeBron aggressively attacks the basket, drawing fouls and earning free throw opportunities, it indicates a proactive offensive strategy. This aggressive playstyle not only results in personal scoring opportunities but also benefits the team by putting pressure on the opposing defense and creating scoring opportunities for teammates.")
    st.write("This inference underscores the strategic importance of LeBron's offensive versatility and ability to draw fouls. It highlights how his aggressive playstyle not only benefits his individual performance but also serves as a key factor in his team's overall success.")

# Run the app
if __name__ == "__main__":
    main()

