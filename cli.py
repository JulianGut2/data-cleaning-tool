import pandas as pd
import argparse
from cleaner.core import clean_data

def main():
    parser = argparse.ArgumentParser(description = "Clean messy CSV files")
    parser.add_argument("--input", required = True, help = "Path to input CSV")
    parser.add_argument("--output", default = "cleaned_output.csv", help = "Output CSV name")

    args = parser.parse_args()

    df = pd.read_csv(args.input)
    cleaned = clean_data(df)
    cleaned.to_csv(args.output, index = False)
    print(f"Cleaned file saved to {args.output}")

if __name__  == "__main__":
    main()