import pandas as pd
import geojson
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash
from dash import dcc #dcc to embed graphs in the dashboard
import dash_bootstrap_components as dbc
from dash import html # html to set up the layout
from dash.dependencies import Input, Output


# Read CSV files into Pandas data frames
victims = pd.read_csv("../data/victims.csv")
incidents = pd.read_csv("../data/incidents.csv")
offenders = pd.read_csv("../data/offenders.csv")
offenses = pd.read_csv("../data/offenses.csv")
comparison = pd.read_csv("../data/comparison.csv")
comparison2 = pd.read_csv("../data/comparison2.csv")
disability = pd.read_csv("../data//disability.csv", dtype={'VICTIM_COUNT': 'int', 'STATE_ABBR': 'str'})
physical = pd.read_csv("../data/physical.csv", dtype={'VICTIM_COUNT': 'int', 'STATE_ABBR': 'str'})
mental = pd.read_csv("../data/mental.csv", dtype={'VICTIM_COUNT': 'int', 'STATE_ABBR': 'str'})
sex = pd.read_csv("../data/sex.csv")
race = pd.read_csv("../data/race.csv")
age = pd.read_csv("../data/age.csv")
disability_type = pd.read_csv("../data/disability_type.csv")
victimization_rate = pd.read_csv("../data/victimization_rate.csv")
crime_type = pd.read_csv("../data/crime_type.csv")
victimization_sex = pd.read_csv("../data/victimization_sex.csv")
victimization_race = pd.read_csv("../data/victimization_race.csv")

with open("../data/us-state-boundaries.geojson") as f:
    us_map = geojson.load(f)


# hate_crime['VICTIM_COUNT'] = hate_crime['VICTIM_COUNT'].astype(int)
# disability.VICTIM_COUNT.dtype # Check that it's a string
# disability.STATE_ABBR.dtype

# Aggregate sums of total victims by state
disability_vcounts = disability.groupby(['STATE_ABBR', 'STATE_NAME'])['VICTIM_COUNT'].agg('count').reset_index()
physical = physical.groupby(['STATE_ABBR', 'STATE_NAME'])['VICTIM_COUNT'].agg('count').reset_index()
mental = mental.groupby(['STATE_ABBR', 'STATE_NAME'])['VICTIM_COUNT'].agg('count').reset_index()

# Check total counts
disability['VICTIM_COUNT'].sum()
physical['VICTIM_COUNT'].sum()
mental['VICTIM_COUNT'].sum()

# Aggregate victim counts by type of offense
offense_type = disability.groupby(['OFFENSE_NAME'])['VICTIM_COUNT'].agg('count').reset_index()

# Aggregate victim counts by type of location
location = disability.groupby(['LOCATION_NAME'])['VICTIM_COUNT'].agg('count').reset_index()

# Aggregate victim counts by type of victims
victim_types = disability.groupby(['VICTIM_TYPES'])['VICTIM_COUNT'].agg('count').reset_index()

# Create charts

# (1) Victims
chart1 = px.line(victims, x="Year", y= victims.columns, markers=True,
                title = "Number of Disabled Victims, <br>by Disability Bias (2004-2019)", height=600,)
chart1.update_layout(xaxis = dict(
        tickmode = 'linear',))
chart1.update_traces(marker_size=8)
chart1.update_layout(
    plot_bgcolor='rgba(0, 0, 0, 0)',
                     paper_bgcolor='rgba(0, 0, 0, 0)',
                     yaxis_title="Number of Victims")
chart1.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')
chart1.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')
chart1.update_layout(title_x=0.5, legend_title_text='Disability Bias')
chart1.update_traces(marker=dict(size=10),
                               hovertemplate= '<b>%{x}</b><br><br>' +
                                              "Number of victims: %{y:,.0f}<br>")



# (2) Incidents
chart2 = px.line(incidents, x="Year", y= incidents.columns, markers=True,
                title = "Number of Incidents, <br>by Disability Bias (2004-2019)", height=600,)
chart2.update_layout(xaxis = dict(
        tickmode = 'linear',))
chart2.update_traces(marker_size=8)
chart2.update_layout(
    plot_bgcolor='rgba(0, 0, 0, 0)',
                     paper_bgcolor='rgba(0, 0, 0, 0)',
                     yaxis_title="Number of Incidents")
chart2.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')
chart2.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')
chart2.update_layout(title_x=0.5, legend_title_text='Disability Bias')
chart2.update_traces(marker=dict(size=10),
                               hovertemplate= '<b>%{x}</b><br><br>' +
                                              "Number of Incidents: %{y:,.0f}<br>")

# (3) Offenders

chart3 = px.line(offenders, x="Year", y= offenders.columns, markers=True,
                title = "Number of Offenders, <br>by Disability Bias (2004-2019)", height=600,)
chart3.update_layout(xaxis = dict(
        tickmode = 'linear',))
chart3.update_traces(marker_size=8)
chart3.update_layout(
    plot_bgcolor='rgba(0, 0, 0, 0)',
                     paper_bgcolor='rgba(0, 0, 0, 0)',
                     yaxis_title="Number of Offenders")
chart3.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')
chart3.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')
chart3.update_layout(title_x=0.5, legend_title_text='Disability Bias')
chart3.update_traces(marker=dict(size=10),
                               hovertemplate= '<b>%{x}</b><br><br>' +
                                              "Number of Offenders: %{y:,.0f}<br>")

# (4) Offenses

chart4 = px.line(offenses, x="Year", y= offenses.columns, markers=True,
                title = "Number of Offenses, <br>by Disability Bias (2004-2019)", height=600,)
chart4.update_layout(xaxis = dict(
        tickmode = 'linear',))
chart4.update_traces(marker_size=8)
chart4.update_layout(
    plot_bgcolor='rgba(0, 0, 0, 0)',
                     paper_bgcolor='rgba(0, 0, 0, 0)',
                     yaxis_title="Number of Offenses")
chart4.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')
chart4.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')
chart4.update_layout(title_x=0.5, legend_title_text='Disability Bias')
chart4.update_traces(marker=dict(size=10),
                               hovertemplate= '<b>%{x}</b><br><br>' +
                                              "Number of Offenses: %{y:,.0f}<br>")


# (5) Comparison

chart5 = px.line(comparison, x="Year", y= comparison.columns, markers=True,
                title = "Number of Victims, <br>by Bias (2004-2019)", height=600,)
chart5.update_layout(xaxis = dict(
        tickmode = 'linear',))
chart5.update_traces(marker_size=8)
chart5.update_layout(
    plot_bgcolor='rgba(0, 0, 0, 0)',
                     paper_bgcolor='rgba(0, 0, 0, 0)',
                     yaxis_title="Number of Offenses")
chart5.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')
chart5.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')
chart5.update_layout(title_x=0.5, legend_title_text='Bias')
chart5.update_traces(marker=dict(size=10),
                               hovertemplate= '<b>%{x}</b><br><br>' +
                                              "Number of Victims: %{y:,.0f}<br>")


# (6) US MAP by Victim Count, Disability Bias
chart6 = px.choropleth_mapbox(disability_vcounts , geojson=us_map, locations='STATE_ABBR', color='VICTIM_COUNT',
                           featureidkey="properties.stusab",
                           hover_name = 'STATE_NAME', 
                           hover_data={'VICTIM_COUNT': True, 'STATE_NAME': False, 'STATE_ABBR': False},
                           color_continuous_scale=px.colors.sequential.deep,
                           mapbox_style="carto-positron",
                           zoom=3, center = {"lat": 37.09024, "lon": -95.712891},
                           opacity=0.8,
                           )
chart6.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# (7) US MAP by Victim Count, Anti-Physical Bias
chart7 = px.choropleth_mapbox(physical, geojson=us_map, locations='STATE_ABBR', color='VICTIM_COUNT',
                           featureidkey="properties.stusab",
                           hover_name = 'STATE_NAME', 
                           hover_data={'VICTIM_COUNT': True, 'STATE_NAME': False, 'STATE_ABBR': False},
                           color_continuous_scale=px.colors.sequential.BuPu,
                           mapbox_style="carto-positron",
                           zoom=3, center = {"lat": 37.09024, "lon": -95.712891},
                           opacity=0.8,
                           )
chart7.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# (8) US MAP by Victim Count, Anti-Mental Bias
chart8 = px.choropleth_mapbox(mental, geojson=us_map, locations='STATE_ABBR', color='VICTIM_COUNT',
                           featureidkey="properties.stusab",
                           hover_name = 'STATE_NAME', 
                           hover_data={'VICTIM_COUNT': True, 'STATE_NAME': False, 'STATE_ABBR': False},
                           color_continuous_scale=px.colors.sequential.Reds,
                           mapbox_style="carto-positron",
                           zoom=3, center = {"lat": 37.09024, "lon": -95.712891},
                           opacity=0.8,
                           )
chart8.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


# TYPES OF OFFENSES
# Sort column by victim count
sorted_off = offense_type.sort_values('VICTIM_COUNT', ascending=False)
# Top 15 offenses by victim count
top15_off = sorted_off.iloc[0:10,]

chart9 = px.bar(top15_off, x=top15_off['VICTIM_COUNT'], y=top15_off['OFFENSE_NAME'],
                title = "Disability Bias Victim Count, by Top 15 Types of Offenses",
                height=600)
chart9.update(layout=dict(title=dict(x=0.5)))
chart9.update_traces(hovertemplate= '<b>%{y}</b><br><br>' +
                                    "No. of Victims: %{x:,.0f}<br>")
chart9.update_layout(yaxis=dict(showgrid=False, showline=False, showticklabels=True))
chart9.update_layout(yaxis={'categoryorder':'total ascending'})
chart9.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)',paper_bgcolor='rgba(0, 0, 0, 0)',
                    xaxis_title="Number of Victims", yaxis_title="Type of Offense")


# LOCATIONS
# Sort column by victim count
sorted_loc = location.sort_values('VICTIM_COUNT', ascending=False)
# Top 15 offenses by victim count
top15_loc = sorted_loc.iloc[0:10,]

chart10 = px.bar(top15_loc, x=top15_loc['VICTIM_COUNT'], y=top15_loc['LOCATION_NAME'],
                title = "Disability Bias Victim Count, by Top 15 Locations",
                height=600)
chart10.update(layout=dict(title=dict(x=0.5)))
chart10.update_traces(hovertemplate= '<b>%{y}</b><br><br>' +
                                    "No. of Victims: %{x:,.0f}<br>")
chart10.update_layout(yaxis=dict(showgrid=False, showline=False, showticklabels=True))
chart10.update_layout(yaxis={'categoryorder':'total ascending'})
chart10.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)',paper_bgcolor='rgba(0, 0, 0, 0)',
                    xaxis_title="Number of Victims", yaxis_title="Location")


# VICTIM TYPES
chart11 = px.pie(victim_types, values = "VICTIM_COUNT", names ="VICTIM_TYPES",
               title="Disability Bias Victim Count, by Victim Type",
                height = 600,)
chart11.update(layout=dict(title=dict(x=0.5)))
chart11.update_traces(textposition='inside', textinfo='percent')
chart11.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)',paper_bgcolor='rgba(0, 0, 0, 0)')
chart11.update_traces(textposition='inside',
                      textinfo='percent',
                      hovertemplate= '<b>%{label}</b><br><br>' +
                                    "No. Victims: %{value:,.0f}<br>")


# DISABILITY POPULATION: OVERVIEW
# Pie chart by sex
chart12 = px.pie(sex, values = "Count", names ="Sex",
               title="Disability Population, by Sex (2017-2019)",
                height = 600,
                color_discrete_sequence=px.colors.qualitative.Set2)
chart12.update(layout=dict(title=dict(x=0.5)))
chart12.update_traces(textposition='inside', textinfo='percent')
chart12.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)',paper_bgcolor='rgba(0, 0, 0, 0)')
chart12.update_traces(textposition='inside',
                      textinfo='percent',
                      hovertemplate= '<b>%{label}</b><br><br>' +
                                    "№ People: %{value:,.0f}<br>")

# Race Treemap
chart13 = px.treemap(race, path=['Race'], values = 'Counts', height = 500,
                     title = "Disability Population, Disaggregated by Race (2017-2019)",
                     color_discrete_sequence=px.colors.qualitative.Pastel)
chart13.update_layout(margin = dict(t=50, l=25, r=25, b=25))
chart13.update_traces(hovertemplate='<b>%{label} </b> <br> № People: %{value}<br>')

# Age Treemap
chart14 = px.treemap(age, path=['Age'], values = 'Counts', height = 500,
                     title = "Disability Population, Disaggregated by Age (2017-2019)",
                     color_discrete_sequence=px.colors.qualitative.Pastel)
chart14.update_layout(margin = dict(t=50, l=25, r=25, b=25))
chart14.update_traces(hovertemplate='<b>%{label} </b> <br> № People: %{value}<br>')

# Disability Type Treemap
chart15 = px.treemap(disability_type, path=['Disability'], values = 'Counts', height = 500,
                     title = "Disability Population, by Type of Disability (2017-2019)",
                     color_discrete_sequence=px.colors.qualitative.Pastel)
chart15.update_layout(margin = dict(t=50, l=25, r=25, b=25))
chart15.update_traces(hovertemplate='<b>%{label} </b> <br> № People: %{value}<br>')


# Line Chart - Victimization Rate comparison
chart16 = px.line(victimization_rate, x="Year", y= victimization_rate.columns, markers=True,
                title = "Victimization Rates Comparison, <br>Persons with and without Disabilities (2009-2019)", height=600,
                color_discrete_sequence=px.colors.qualitative.Pastel)
chart16.update_layout(xaxis = dict(
        tickmode = 'linear',))
chart16.update_traces(marker_size=8)
chart16.update_layout(
    plot_bgcolor='rgba(0, 0, 0, 0)',
                     paper_bgcolor='rgba(0, 0, 0, 0)',
                     yaxis_title="Victimization Rate")
chart16.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')
chart16.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')
chart16.update_layout(title_x=0.5, legend_title_text='Disability Bias')
chart16.update_traces(marker=dict(size=10),
                               hovertemplate= '<b>%{x}</b><br><br>' +
                                              "Number: %{y:,.0f}<br>")

# Bar Chart - Victimization Rates by Crime Type
chart17 = px.bar(crime_type, x=crime_type['Type of crime'], y=crime_type.columns,
                title = "Victimization Rates Comparison by Crime Type <br> Persons with and without Disabilities (2017-2019)",
                height=600, color_discrete_sequence=px.colors.qualitative.Pastel,)
chart17.update(layout=dict(title=dict(x=0.5)))
chart17.update_traces(hovertemplate= "Rate: %{y}<br>")
chart17.update_layout(yaxis=dict(showgrid=False, showline=False, showticklabels=True))
chart17.update_layout(yaxis={'categoryorder':'total descending'})
chart17.update_layout(title_x=0.5, legend_title_text='Category')
chart17.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)',paper_bgcolor='rgba(0, 0, 0, 0)',
                    xaxis_title="Type of Crime", yaxis_title="Victimization Rate")


# Bar Chart - Victimization Rates by Sex
chart18 = px.bar(victimization_sex, x=victimization_sex['Sex'], y=victimization_sex['Rate'],
                title = "Disability Victimization Rates <br> by Sex (2017-2019)",
                height=600, 
                color='Sex',
                color_discrete_sequence=px.colors.qualitative.Set2,)
chart18.update(layout=dict(title=dict(x=0.5)))
chart18.update_traces(hovertemplate= "Rate: %{y}<br>")
chart18.update_layout(yaxis=dict(showgrid=False, showline=False, showticklabels=True))
chart18.update_layout(yaxis={'categoryorder':'total descending'})
chart18.update_layout(title_x=0.5, legend_title_text='Category')
chart18.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)',paper_bgcolor='rgba(0, 0, 0, 0)',
                    xaxis_title="Sex", yaxis_title="Victimization Rate")

# Bar Chart - Victimization Rates by Race
chart19 = px.bar(victimization_race, x=victimization_race['Race'], y=victimization_race['Rate'],
                title = "Disability Victimization Rates <br> by Race (2017-2019)",
                height=600, 
                color='Race',
                color_discrete_sequence=px.colors.qualitative.Set2,)
chart19.update(layout=dict(title=dict(x=0.5)))
chart19.update_traces(hovertemplate= "Rate: %{y}<br>")
chart19.update_layout(yaxis=dict(showgrid=False, showline=False, showticklabels=True))
chart19.update_layout(yaxis={'categoryorder':'total descending'})
chart19.update_layout(title_x=0.5, legend_title_text='Category')
chart19.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)',paper_bgcolor='rgba(0, 0, 0, 0)',
                    xaxis_title="Race", yaxis_title="Victimization Rate")


# Start the app
app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.LUX])

app.layout = html.Div(children=[

                html.Br(), 
                html.Br(), 

                html.Div(children=[
                html.H2(children="Disability Population in the US: An Overview", 
                className="overview"), ],),

                html.Div(children = dcc.Graph(
                    id = 'sex_pop',
                    figure = chart12),
                    style={'width': '50%', 'display': 'inline-block', 'font-family': 'Montserrat', 'padding-top': '1%', 
                    'padding-bottom': '1%'}),

                html.Div(children = dcc.Graph(
                    id = 'race_pop',
                    figure = chart13),
                    style={'width': '50%', 'display': 'inline-block', 'font-family': 'Montserrat', 'padding-top': '1%', 
                    'padding-bottom': '1%'}),

                html.Div(dcc.Textarea(
                value = "Source: Bureau of Justice Statistics, Crime Against Persons with Disabilities, 2009-2019 - Statistical Tables NCJ 301367. Appendix table 1.",
                style={'fontSize': "14px", 'float': 'left','margin': 'auto','display': 'flex', 'flex-direction': 'column',
                    'font-family': 'Montserrat','width': '46%','color':'#4d4d4d','padding-left' : '2%'} ,
                readOnly = True)),


                html.Div(dcc.Textarea(
                value = "Source: Bureau of Justice Statistics, Crime Against Persons with Disabilities, 2009-2019 - Statistical Tables NCJ 301367. Appendix table 1.",
                style={'fontSize': "14px", 'float': 'right','display': 'flex', 'flex-direction': 'column',
                    'font-family': 'Montserrat', 'width': '50%', 'color':'#4d4d4d'},
                readOnly = True)),

                html.Br(), 
                html.Br(), 

                html.Div(children = dcc.Graph(
                    id = 'age_pop',
                    figure = chart14),
                    style={'width': '50%', 'display': 'inline-block', 'font-family': 'Montserrat', 'padding-top': '1%', 
                    'padding-bottom': '1%'}),

                html.Div(children = dcc.Graph(
                    id = 'dis_type_pop',
                    figure = chart15),
                    style={'width': '50%', 'display': 'inline-block', 'font-family': 'Montserrat', 'padding-top': '1%', 
                    'padding-bottom': '1%'}),
                
                html.Div(dcc.Textarea(
                value = "Source: Bureau of Justice Statistics, Crime Against Persons with Disabilities, 2009-2019 - Statistical Tables NCJ 301367. Appendix table 1.",
                style={'fontSize': "14px", 'float': 'left','margin': 'auto','display': 'flex', 'flex-direction': 'column',
                    'font-family': 'Montserrat','width': '46%','color':'#4d4d4d','padding-left' : '2%'} ,
                readOnly = True)),


                html.Div(dcc.Textarea(
                value = "Source: Bureau of Justice Statistics, Crime Against Persons with Disabilities, 2009-2019 - Statistical Tables NCJ 301367. Appendix table 1.",
                style={'fontSize': "14px", 'float': 'right','display': 'flex', 'flex-direction': 'column',
                    'font-family': 'Montserrat', 'width': '50%', 'color':'#4d4d4d'},
                readOnly = True)),

                html.Br(), 
                html.Br(), 
                html.Br(), 
                html.Br(), 

                html.Div(children=[
                html.H2(children="Victimization Rates for Persons with Disability are Alarmingly High", 
                className="header"), ],),

                html.Div(children = dcc.Graph(
                    id = 'victimization_rate',
                    figure = chart16),
                    style={'width': '60%', 'display': 'inline-block', 'font-family': 'Montserrat', 'padding-top': '1%', 
                    'padding-bottom': '1%'}),

                html.Div(children = dcc.Graph(
                    id = 'crime_type',
                    figure = chart17),
                    style={'width': '40%', 'display': 'inline-block', 'font-family': 'Montserrat', 'padding-top': '1%', 
                    'padding-bottom': '1%'}),

                html.Div(dcc.Textarea(
                value = "Note: Comparison group with rates calculated with population data from the American Community Survey (ACS) for persons with disabilities are compared to age-adjusted rates for persons without disabilities.",
                style={'fontSize': "15px", 'float': 'left', 'display': 'flex', 'flex-direction': 'column',
                    'font-family': 'Montserrat', 'font-style': 'italic', 'font-weight': 'bold', 'width': '46%', 'height': '100px',
                    'color':'#4d4d4d', 'padding-left' : '2%'},
                readOnly = True)),


                html.Div(dcc.Textarea(
                value = "",
                style={'fontSize': "15px", 'float': 'left', 'display': 'flex', 'flex-direction': 'column',
                    'font-family': 'Montserrat', 'font-style': 'italic', 'font-weight': 'bold', 'width': '50%',
                    'color':'#4d4d4d'},
                readOnly = True)),

                html.Br(), 
                html.Br(), 
                html.Br(), 
                html.Br(), 
                html.Br(), 

                html.Div(dcc.Textarea(
                value = 'Source: Bureau of Justice Statistics, Crime Against Persons with Disabilities, 2009-2019 - Statistical Tables NCJ 301367. Appendix table 2.',
                style={'fontSize': "14px", 'float': 'left','margin': 'auto','display': 'flex', 'flex-direction': 'column',
                    'font-family': 'Montserrat','width': '46%','color':'#4d4d4d','padding-left' : '2%'} ,
                readOnly = True)),

                html.Div(dcc.Textarea(
                value = "Source: Bureau of Justice Statistics, Crime Against Persons with Disabilities, 2009-2019 - Statistical Tables NCJ 301367. Appendix table 3.",
                style={'fontSize': "14px", 'float': 'right','display': 'flex', 'flex-direction': 'column',
                    'font-family': 'Montserrat', 'width': '50%', 'color':'#4d4d4d'},
                readOnly = True)),


                html.Br(), 
                html.Br(), 

                html.Div(children = dcc.Graph(
                    id = 'vic_rate_sex',
                    figure = chart18),
                    style={'width': '50%', 'display': 'inline-block', 'font-family': 'Montserrat', 'padding-top': '1%', 
                    'padding-bottom': '1%'}),

                
                html.Div(children = dcc.Graph(
                    id = 'vic_rate_race',
                    figure = chart19),
                    style={'width': '50%', 'display': 'inline-block', 'font-family': 'Montserrat', 'padding-top': '1%', 
                    'padding-bottom': '1%'}),

                
                html.Div(dcc.Textarea(
                value = 'Source: Bureau of Justice Statistics, Crime Against Persons with Disabilities, 2009-2019 - Statistical Tables NCJ 301367. Appendix table 5.',
                style={'fontSize': "14px", 'float': 'left','margin': 'auto','display': 'flex', 'flex-direction': 'column',
                    'font-family': 'Montserrat','width': '46%','color':'#4d4d4d','padding-left' : '2%'} ,
                readOnly = True)),

                html.Div(dcc.Textarea(
                value = "Source: Bureau of Justice Statistics, Crime Against Persons with Disabilities, 2009-2019 - Statistical Tables NCJ 301367. Appendix table 5.",
                style={'fontSize': "14px", 'float': 'right','display': 'flex', 'flex-direction': 'column',
                    'font-family': 'Montserrat', 'width': '50%', 'color':'#4d4d4d'},
                readOnly = True)),



                html.Div(children = dcc.Graph(
                    id = 'incidents',
                    figure = chart2),
                    style={'width': '50%', 'display': 'inline-block', 'font-family': 'Montserrat', 'padding-top': '1%', 
                    'padding-bottom': '1%'}),

                html.Div(children = dcc.Graph(
                    id = 'offenders',
                    figure = chart3),
                    style={'width': '50%', 'display': 'inline-block', 'font-family': 'Montserrat', 'padding-top': '1%', 
                    'padding-bottom': '1%'}),

                html.Div(children = dcc.Graph(
                    id = 'offenses',
                    figure = chart4),
                    style={'width': '50%', 'display': 'inline-block', 'font-family': 'Montserrat', 'padding-top': '1%', 
                    'padding-bottom': '1%'}),
                

                html.Div(children = dcc.Graph(
                    id = 'comparison',
                    figure = chart5),
                    style={'width': '50%', 'display': 'inline-block', 'font-family': 'Montserrat', 'padding-top': '1%', 
                    'padding-bottom': '1%'}),

                html.Div(children = dcc.Graph(
                    id = 'counts_by_offense',
                    figure = chart9),
                    style={'width': '50%', 'display': 'inline-block', 'font-family': 'Montserrat', 'padding-top': '1%', 
                    'padding-bottom': '1%'}),
                
                html.Div(children = dcc.Graph(
                    id = 'counts_by_location',
                    figure = chart10),
                    style={'width': '50%', 'display': 'inline-block', 'font-family': 'Montserrat', 'padding-top': '1%', 
                    'padding-bottom': '1%'}),

                html.Div(children = dcc.Graph(
                    id = 'victim_types',
                    figure = chart11),
                    style={'width': '50%', 'display': 'inline-block', 'font-family': 'Montserrat', 'padding-top': '1%', 
                    'padding-bottom': '1%'}),

                html.Div(children=[
                html.H2(children="Victim Count by Disability Bias (1997-2020)", 
                className="header"), ],),
                
                html.Div(children = dcc.Graph(
                    id = 'map',
                    figure = chart6),
                    style={'width': '100%', 'display': 'inline-block', 'font-family': 'Montserrat', 'padding-top': '1%', 
                    'padding-bottom': '1%'}),

                html.Div(dcc.Textarea(
                value = "Source: FBI Hate Crime Database (1997-2020) ",
                style={'fontSize': "14px",'width': '80%', 'display': 'inline-block', 'font-family': 'Montserrat', 'margin-left': '50px', 
                'margin-right': '50px', 'color':'#4d4d4d'},
                readOnly = True)),

                html.Div(children=[
                html.H2(children="Victim Count by Anti-Physical Disability Bias (1997-2020)", 
                className="header"), ],),

                html.Div(children = dcc.Graph(
                    id = 'physical',
                    figure = chart7),
                    style={'width': '100%', 'display': 'inline-block', 'font-family': 'Montserrat', 'padding-top': '1%', 
                    'padding-bottom': '1%'}),
                
                html.Div(dcc.Textarea(
                value = "Source: FBI Hate Crime Database (1997-2020) ",
                style={'fontSize': "14px",'width': '80%', 'display': 'inline-block', 'font-family': 'Montserrat', 'margin-left': '50px', 
                'margin-right': '50px', 'color':'#4d4d4d'},
                readOnly = True)),

                html.Div(children=[
                html.H2(children="Victim Count by Anti-Mental Disability Bias (1997-2020)", 
                className="header"), ],),
                
                html.Div(children = dcc.Graph(
                    id = 'mental',
                    figure = chart8),
                    style={'width': '100%', 'display': 'inline-block', 'font-family': 'Montserrat', 'padding-top': '1%', 
                    'padding-bottom': '1%'}),

                html.Div(dcc.Textarea(
                value = "Source: FBI Hate Crime Database (1997-2020) ",
                style={'fontSize': "14px",'width': '80%', 'display': 'inline-block', 'font-family': 'Montserrat', 'margin-left': '50px', 
                'margin-right': '50px', 'color':'#4d4d4d'},
                readOnly = True)),

                
                ])


if __name__ == "__main__":
    app.run_server(debug=True)