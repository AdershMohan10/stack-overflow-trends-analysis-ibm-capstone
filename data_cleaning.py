import pandas as pd

# Load your CSV file
df = pd.read_csv('survey_data_updated.csv')

# Function to split answers like "Python;C++;JavaScript"
def split_multiselect(column):
    return column.dropna().apply(lambda x: [item.strip() for item in x.split(';')]).explode()

# Split tech answers
langs_now = split_multiselect(df['LanguageHaveWorkedWith'])
langs_future = split_multiselect(df['LanguageWantToWorkWith'])

dbs_now = split_multiselect(df['DatabaseHaveWorkedWith'])
dbs_future = split_multiselect(df['DatabaseWantToWorkWith'])

platforms_now = split_multiselect(df['PlatformHaveWorkedWith'])
platforms_future = split_multiselect(df['PlatformWantToWorkWith'])

# Get top 10 counts
def top_10(series):
    return series.value_counts().nlargest(10)

# Save top 10s to CSV files
top_10(langs_now).to_csv('top10_languages_now.csv')
top_10(langs_future).to_csv('top10_languages_future.csv')

top_10(dbs_now).to_csv('top10_databases_now.csv')
top_10(dbs_future).to_csv('top10_databases_future.csv')

top_10(platforms_now).to_csv('top10_platforms_now.csv')
top_10(platforms_future).to_csv('top10_platforms_future.csv')

# Demographics (age, country, education)
demo = df[['Age', 'Country', 'EdLevel']].dropna()

demo['Age'].value_counts().to_csv('age_counts.csv')
demo['Country'].value_counts().to_csv('country_counts.csv')
demo['EdLevel'].value_counts().to_csv('education_counts.csv')

# Age + Education stacked chart
age_edu = demo.groupby(['Age', 'EdLevel']).size().unstack(fill_value=0)
age_edu.to_csv('age_education_stacked.csv')

print("✅ Done! Check the new CSV files in your folder.")
