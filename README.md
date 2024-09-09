LA Crime Data Analysis Project
This repository contains a project aimed at analysing crime data in Los Angeles from 2020 to the present, focusing on exploring patterns, trends, and insights derived from the dataset. The analysis uses various Python libraries to clean, process, and visualise the data.

Project Overview
The objective of this project is to understand crime patterns in Los Angeles by analysing the crime dataset. This includes identifying trends over time, age distributions of victims, and the most frequent types of crimes. Additionally, the project explores the time it takes to report crimes after they occur and highlights the crimes with the highest average victim age.

Key Steps:
Data Loading & Cleaning:

The dataset is loaded from a CSV file containing information about various crimes reported in LA.
Columns that are irrelevant to the analysis (e.g., modus operandi, weapon descriptions) are removed.
Data types are converted appropriately, particularly dates for date_reported and date_occurred.
Feature Engineering:

Extracted key time-based features such as year and month from the date_occurred column.
Calculated the time difference between when a crime occurred and when it was reported.
Grouped data to count the occurrences of specific crime types over time.
Data Visualisation:

Trends over time: Line plots are used to visualise the occurrence of crimes per month and year.
Age distribution: A histogram presents the distribution of crime victims' ages.
Top 20 crimes: A bar plot shows the most frequent crime types and their average daily occurrences.
Additional Insights:

Computed the average time it takes to report crimes.
Identified the top 3 crimes with the highest average victim age.
Project Structure
Crime_Data_from_2020_to_Present.csv: The raw dataset containing LA crime reports.
LA Crime Project (1).py: The main Python script used to analyse and visualise the data.
README.md: Project documentation.
