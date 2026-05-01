import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def StackedBarChart(sheet,colors,chart_title):
    #Stacked Bar Chart Function
    
    # If the input is a string (file path), read it into a DataFrame; 
    # otherwise, assume it is already a pandas DataFrame.
    if isinstance(sheet, str):
        df = pd.read_excel(sheet)
    else:
        df = sheet
        
    # Remove 'Total' column if it exists so it doesn't become part of the stack
    total_cols = [col for col in df.columns if str(col).lower() == 'total']
    if total_cols:
        df = df.drop(columns=total_cols)
        
    # Assume the first column contains the labels for the y-axis (e.g., Team or Individual name)
    y_col = df.columns[0]
    
    # Calculate the total score for each row to sort the bars (largest at the top)
    totals = df.set_index(y_col).sum(axis=1, numeric_only=True).sort_values(ascending=True)
    
    # Create a new figure using graph_objects for more explicit control
    fig = go.Figure()
    
    # Get the categories (columns) and the y-axis labels (teams) in sorted order
    categories = [col for col in df.columns if col != y_col]
    teams_ordered = totals.index.tolist()

    # Add a separate Bar trace for each category
    for i, category in enumerate(categories):
        # Get the values for the current category, ordered by the total scores
        x_values = [df.loc[df[y_col] == team, category].iloc[0] for team in teams_ordered]
        
        # Build the list of colors for the bars in this trace
        marker_colors = []
        for team in teams_ordered:
            team_colors = colors.get(team, [])
            # Map the corresponding shade, cycling through colors if there are more categories than colors.
            color = team_colors[i % len(team_colors)] if team_colors else 'gray'
            marker_colors.append(color)

        fig.add_trace(go.Bar(
            y=teams_ordered,
            x=x_values,
            name=category,
            orientation='h',
            marker=dict(color=marker_colors)
        ))
    
    # Set the layout to stack the bars and ensure the y-axis order is correct
    fig.update_layout(barmode='stack', title=chart_title, xaxis=dict(title='Points'), yaxis=dict(categoryorder='array', categoryarray=teams_ordered), showlegend=False)
    
    return fig
    