import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Updated dataset with more players
players = [
    ('Rohit Sharma', 265, 10866, 49.17, 92.44, 31, 57, 264, 2),
    ('Virat Kohli', 295, 13906, 58.18, 93.54, 50, 72, 183, 4),
    ('Kane Williamson', 165, 6811, 48.3, 81.39, 13, 45, 148, 31),
    ('Steven Smith', 163, 5583, 43.62, 87.23, 12, 34, 164, 19),
    ('Joe Root', 171, 6522, 47.61, 86.77, 16, 39, 133, 46),
    ('Babar Azam', 117, 5409, 58.4, 89.02, 19, 28, 125, 1),
    ('David Warner', 161, 6932, 45.1, 95.13, 18, 32, 179, 6),
    ('Shikhar Dhawan', 167, 6793, 44.11, 91.35, 17, 39, 143, 28),
    ('Faf du Plessis', 143, 5507, 47.47, 88.96, 12, 35, 135, 25),
    ('Quinton de Kock', 140, 6176, 44.81, 94.67, 17, 29, 178, 22),
    ('MS Dhoni', 350, 10773, 50.57, 87.56, 10, 73, 183, 36),
    ('KL Rahul', 72, 2887, 47.2, 88.5, 5, 21, 112, 20),
    ('Ben Stokes', 105, 3159, 41.0, 93.87, 4, 15, 102, 37),
    ('Shreyas Iyer', 67, 2650, 44.91, 87.0, 3, 17, 113, 9),
    ('Rishabh Pant', 73, 2242, 35.45, 91.2, 1, 15, 128, 41),
]

columns = ['Player', 'Matches', 'Runs', 'Average', 'Strike Rate', '100s', '50s', 'Highest score', 'ICC Ranking']
df = pd.DataFrame(players, columns=columns)

# Streamlit app title and header
st.title("Cricket Player Statistics")
st.header("Cricket Player Stats Overview")
st.dataframe(df)

# Sidebar for player selection
st.sidebar.header("Select Player for Analysis")
selected_player = st.sidebar.selectbox("Choose a player:", df['Player'])

# Show selected player's data
st.subheader(f"Statistics of {selected_player}")
player_data = df[df['Player'] == selected_player]
st.write(player_data)

# Top 5 Players by Runs
st.header("Top 5 Players by Runs")
top_5_runs = df.nlargest(5, 'Runs')
st.dataframe(top_5_runs)

# Player Performance Over Time (Assuming random years for demonstration)
df['Year'] = [2010 + (i % 10) for i in range(len(df))]
st.header("Player Performance Over Time")
fig, ax = plt.subplots()
for player in df['Player']:
    player_data = df[df['Player'] == player]
    ax.plot(player_data['Year'], player_data['Runs'], label=player)
ax.set_xlabel('Year')
ax.set_ylabel('Runs')
ax.set_title('Player Performance Over Time')
ax.legend()
st.pyplot(fig)

# Strike Rate vs Runs Scatter Plot
st.header("Strike Rate vs Runs")
fig, ax = plt.subplots()
ax.scatter(df['Runs'], df['Strike Rate'], color='blue')
ax.set_xlabel('Runs')
ax.set_ylabel('Strike Rate')
ax.set_title('Strike Rate vs Runs')
st.pyplot(fig)

# Compare Multiple Metrics for Selected Players
st.header("Compare Multiple Metrics for Selected Players")
players_comparison = st.multiselect('Select Players:', df['Player'], default=[df['Player'][0], df['Player'][1]])

metrics = ['Runs', 'Average', 'Strike Rate']
fig, ax = plt.subplots()

for player in players_comparison:
    player_data = df[df['Player'] == player]
    ax.plot(metrics, player_data[metrics].values[0], label=player)

ax.set_xlabel('Metrics')
ax.set_ylabel('Values')
ax.set_title('Comparison of Multiple Metrics')
ax.legend()
st.pyplot(fig)

# Pie Chart for Player's 100s and 50s
st.header(f"Centuries and Fifties of {selected_player}")
player_data = df[df['Player'] == selected_player].iloc[0]
centuries = player_data['100s']
fifties = player_data['50s']

fig, ax = plt.subplots()
ax.pie([centuries, fifties], labels=['Centuries', 'Fifties'], autopct='%1.1f%%', startangle=90, colors=['red', 'blue'])
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig)

# Player's Strike Rate vs Runs (Top Performers Only)
st.header("Top Players Comparison Based on Runs and Strike Rate")
top_performers = df.nlargest(5, 'Runs')
top_performers_fig, top_performers_ax = plt.subplots()

top_performers_ax.scatter(top_performers['Runs'], top_performers['Strike Rate'], color='green')
top_performers_ax.set_xlabel('Runs')
top_performers_ax.set_ylabel('Strike Rate')
top_performers_ax.set_title('Top Players Strike Rate vs Runs')
st.pyplot(top_performers_fig)

# Player's Performance Summary
st.header(f"Performance Summary of {selected_player}")
st.write(f"**Total Runs:** {player_data['Runs']}")
st.write(f"**Batting Average:** {player_data['Average']}")
st.write(f"**Strike Rate:** {player_data['Strike Rate']}")
st.write(f"**Centuries (100s):** {player_data['100s']}")
st.write(f"**Fifties (50s):** {player_data['50s']}")

# Comparison of Players Based on Runs
st.header("Comparison of Players Based on Runs")
fig, ax = plt.subplots()
ax.bar(df['Player'], df['Runs'], color='skyblue')
ax.set_xlabel('Players')
ax.set_ylabel('Runs')
ax.set_title('Total Runs Scored by Players')
plt.xticks(rotation=90)
st.pyplot(fig)

player1 = st.selectbox('Select Player 1:', df['Player'])
player2 = st.selectbox('Select Player 2:', df['Player'], index=1)

player1_data = df[df['Player'] == player1].iloc[0]
player2_data = df[df['Player'] == player2].iloc[0]

st.write(f"### {player1} vs {player2}")
st.write(f"{player1}: {player1_data['Runs']} runs, {player1_data['Strike Rate']} strike rate")
st.write(f"{player2}: {player2_data['Runs']} runs, {player2_data['Strike Rate']} strike rate")

comparison_fig, comparison_ax = plt.subplots()
comparison_ax.bar([player1, player2], [player1_data['Runs'], player2_data['Runs']], color=['blue', 'green'])
comparison_ax.set_ylabel('Runs')
comparison_ax.set_title(f'Comparison of Runs: {player1} vs {player2}')
st.pyplot(comparison_fig)

comparison_fig, comparison_ax = plt.subplots()
comparison_ax.bar([player1, player2], [player1_data['100s'], player2_data['100s']], color=['blue', 'red'])
comparison_ax.set_ylabel('100s')
comparison_ax.set_title(f'Comparison of 100s: {player1} vs {player2}')
st.pyplot(comparison_fig)

comparison_fig, comparison_ax = plt.subplots()
comparison_ax.bar([player1, player2], [player1_data['Average'], player2_data['Average']], color=['orange', 'red'])
comparison_ax.set_ylabel('Average')
comparison_ax.set_title(f'Comparison of Averages: {player1} vs {player2}')
st.pyplot(comparison_fig)
