import os
import pandas as pd
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

# Supabase setup
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Path to your CSV file
csv_file_path = 'data/faqs.csv'

try:
    # Load data from the CSV file
    faqs_df = pd.read_csv(csv_file_path)

    # Convert DataFrame rows to a list of dictionaries for insertion
    data_to_insert = faqs_df.to_dict('records')

    # Insert data into the 'faqs' table
    response = supabase.table("faqs").insert(data_to_insert).execute()

    print("Data inserted successfully!")
    print(response.data)

except FileNotFoundError:
    print(f"Error: The file '{csv_file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")