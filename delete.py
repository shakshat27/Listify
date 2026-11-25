import os
import google.generativeai as genai


API_KEY = os.getenv("GOOGLE_API_KEY")  # export GOOGLE_API_KEY=...

def main():
    try:
        # Initialize the Generative AI client
        genai.configure(api_key=API_KEY)

        # List files
        print("Fetching files...")
        files = genai.list_files()  # Fetch the list of files
        if not files:
            print("No files found.")
            return

        # Delete each file
        for file in files:
            try:
                print(f"Deleting: {file.name}")
                file.delete()  # Delete the file
            except Exception as e:
                print(f"Error deleting {file.name}: {e}")

        print("All files have been deleted.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
