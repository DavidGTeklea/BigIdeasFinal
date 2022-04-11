import pandas as pd
import numpy as np

se = pd.read_csv("feeder_enrollment.csv")
se.plot(kind='bar')
