import pandas as pd

def clean_data(df):
    # Create a copy of the df supplied through our function
    df = df.copy()

    # Standardize the columns
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # Stripping the white space from string values
    for col in df.select_dtypes(include = 'object').columns:
        df[col] = df[col].map(lambda x: x.strip() if isinstance(x, str) else x)

    # Drop duplicate rows
    df.drop_duplicates(inplace = True)

    # Try to convert date similar string to datetime, if not just continue
    for col in df.select_dtypes(include = 'object').columns:
        try:
            df[col] = pd.to_datetime(df[col])
        
        except Exception:
            continue
    
    # Return our final df
    return df