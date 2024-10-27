import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
columns = ['sex', 'length', 'diameter', 'height', 'whole_weight', 'shucked_weight', 'viscera_weight',
               'shell_weight', 'rings']
quantitative_columns = ['length', 'diameter', 'height', 'whole_weight', 'shucked_weight', 'viscera_weight', 'shell_weight', 'rings']

def create_tab1(df):
    counts = df['sex'].value_counts()
    percent = df['sex'].value_counts(normalize=True) * 100
    table = pd.DataFrame({'count': counts, '%': percent.round(2)})
    print(table)
def create_tab2():
    summary_table = numeric_cols.describe().T
    print(summary_table[['mean', 'std', 'min', '25%', '50%', '75%', 'max']])
def generate_all_plots(df):
    plt.figure(figsize=(8, 6))
    df['sex'].value_counts().plot(kind='bar', color='skyblue')
    plt.title('Liczba wystąpień dla każdej kategorii płci')
    plt.xlabel('Płeć')
    plt.ylabel('Liczba wystąpień')
    plt.show()

    fig, axes = plt.subplots(nrows=4, ncols=2, figsize=(12, 16))
    for ax, col in zip(axes.flatten(), quantitative_columns):
        df[col].plot(kind='hist', ax=ax, bins=20, title=col, color='lightcoral')
        ax.set_xlabel(col)
    plt.tight_layout()
    plt.show()

    sns.pairplot(df[quantitative_columns])
    plt.show()

    correlation_matrix = df[quantitative_columns].corr()
    print("Macierz korelacji:\n", correlation_matrix)

    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Heatmapa macierzy korelacji zmiennych ilościowych')
    plt.show()

    sns.lmplot(x='length', y='whole_weight', data=df, height=6, aspect=1.5, scatter_kws={'alpha':0.5})
    plt.title('Regresja liniowa: Length vs Whole Weight')
    plt.show()


if __name__ == '__main__':
    df = pd.read_csv('data.csv', header=None, names=columns)
    numeric_cols = df.select_dtypes(include=['float64', 'int64'])
    df.head()
    create_tab1(df)
    create_tab2()
    generate_all_plots(df)