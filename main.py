import pandas as pd
import numpy as np
from helpers import Explorator


def main():
    df = pd.read_csv('data/TelcoCustomerChurn.csv')
    expl = Explorator(df)
    expl.totals()


if __name__ == '__main__':
    main()
