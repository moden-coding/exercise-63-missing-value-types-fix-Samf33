#!/usr/bin/env python3

import pandas as pd
import numpy as np

def missing_value_types():
    states = ["United Kingdom", "Finland", "USA","Sweden", "Germany", "Russia"]
    year = [np.nan, 1917, 1776, 1523, np.nan, 1992]
    presidents = [None, "Niinistö", "Trump", None, "Steinmeier", "Putin"]
    df=pd.DataFrame(index=states, data={"Year of independence":year, "President":presidents})
    df.index.name = "State"
    return df
    pass
               
def main():
    print(missing_value_types())

if __name__ == "__main__":
    main()
