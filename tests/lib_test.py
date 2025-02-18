# -*- coding: UTF-8 -*-

# Import from standard library
import os
import WorkforceSentimentMonitoring
import pandas as pd
# Import from our lib
from WorkforceSentimentMonitoring.lib import get_df, merge
import pytest


# def test_clean_data():
#     datapath = os.path.dirname(os.path.abspath(WorkforceSentimentMonitoring.__file__)) + '/data'
#     df = pd.read_csv('{}/data.csv.gz'.format(datapath))
#     first_cols = ['id', 'civility', 'birthdate', 'city', 'postal_code', 'vote_1']
#     assert list(df.columns)[:6] == first_cols
#     assert df.shape == (999, 142)
#     out = clean_data(df)
#     assert out.shape == (985, 119)

def test_get_df():
    datapath = os.path.dirname(os.path.abspath(WorkforceSentimentMonitoring.__file__)) + '/raw_data'
    submission = pd.read_csv('{}/sample_submission.csv'.format(datapath))
    train = pd.read_csv('{}/train.csv'.format(datapath))
    test = pd.read_csv('{}/test.csv'.format(datapath))
    df = merge(submission, train, test)
    first_cols = ['summary', 'positives', 'negatives', 'advice_to_mgmt', 'work-balance', 'culture-values']
    assert list(df.columns)[:6] == first_cols
    assert df.shape == (52815, 11)
