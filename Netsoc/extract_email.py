import pandas as pd


def extract_email(path):
    df = pd.read_csv(path)
    emails = df['Email Address']
    emails.to_csv('netsoc_emails.csv', index=False)


if __name__ == "__main__":
    extract_email("netsoc.csv")
