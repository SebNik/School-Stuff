def read_questions():
    import pandas as pd
    df = pd.read_csv('/home/niklas/Desktop/School-Stuff/Geschichtsquiz/data.csv', sep=';', encoding="utf-16")
    print(df.sample())


if __name__ == "__main__":
    read_questions()