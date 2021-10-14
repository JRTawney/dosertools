import numpy as np
import pandas as pd
import pandas._testing
import os
import json

from scipy.optimize import curve_fit
from scipy.optimize import fsolve
from scipy import stats

import data_processing.array as array
import data_processing.csv as process
import data_processing.fitting as fitting


def test_find_EC_slope():
    test_dataset = pd.read_csv(os.path.join("tests","fixtures","example_DOS_data.csv"))
    slope, intercept, r_value = fitting.find_EC_slope(test_dataset, 0.1, 0.045)
    assert np.isclose(slope, -347.7499821602085)
    assert np.isclose(intercept, 0.2809024757035168)
    assert np.isclose(r_value,-0.9996926885633579)
    
def test_annotate_lambdaE_df():
    fitting_results_list = [["test sample", -347, 0.28, -0.999, 1]]
    target_lambdaE_df = pd.io.json.read_json(os.path.join("tests","fixtures","target_lambdaE_df.json"))
    lambdaE_df = fitting.annotate_lambdaE_df(fitting_results_list, _)
    pd.testing.assert_frame_equal(lambdaE_df, target_lambdaE_df, check_dtype=False) 
    pass

def test_find_lambdaE():
    
    
    pass
