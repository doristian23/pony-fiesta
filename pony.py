import unittest

from ..verbosity import verbosity
from ..mentions import mentions
from ..follow_on import follow_on
from ..non_dict_words import non_dict_words
import os.path as osp
import pandas as pd

class PonyTestCase(unittest.TestCase):

    
    def test_v_tw(self):
        script_dir = osp.dirname(__file__)
        test_file = osp.join(script_dir, 'test_dialog1.csv')
        df = pd.read_csv(test_file)

        df2, values = verbosity(df)
        self.assertEqual(values['twilight'], 0.14)

    def test_m_aj(self):
        script_dir = osp.dirname(__file__)
        test_file = osp.join(script_dir, 'test_dialog1.csv')
        df = pd.read_csv(test_file)
        df2, values = verbosity(df)
        values_m = mentions(df2)

        self.assertEqual(values_m['applejack']['rarity'], 0.0)

    def test_m_ra(self): 
        script_dir = osp.dirname(__file__)
        test_file = osp.join(script_dir, 'test_dialog1.csv')
        df = pd.read_csv(test_file)

        df2, values = verbosity(df)
        values_m = mentions(df2)
        self.assertEqual(values_m['rarity']['twilight'], 0.5)

    def test_m_tw(self):
        script_dir = osp.dirname(__file__)
        test_file = osp.join(script_dir, 'test_dialog1.csv')
        df = pd.read_csv(test_file)

        df2, values = verbosity(df)
        values_m = mentions(df2)
        self.assertEqual(values_m['twilight']['pinkie'], 0.67)

    def test_f_tw(self):
        script_dir = osp.dirname(__file__)
        test_file = osp.join(script_dir, 'test_dialog1.csv')
        df = pd.read_csv(test_file)

        df2, values = verbosity(df)
        values_f = follow_on(df2)
        self.assertEqual(values_f['twilight']['other'], 1)

    def test_f_rd(self):
        script_dir = osp.dirname(__file__)
        test_file = osp.join(script_dir, 'test_dialog1.csv')
        df = pd.read_csv(test_file)

        df2, values = verbosity(df)
        values_f = follow_on(df2)
        self.assertEqual(values_f['rainbow']['applejack'], 1)

    def test_n_rd(self):
        script_dir = osp.dirname(__file__)
        test_file = osp.join(script_dir, 'test_dialog1.csv')
        df = pd.read_csv(test_file)

        df2, values = verbosity(df)
        values_n = non_dict_words(df2)
        self.assertEqual(values_n['rainbow'], ['wheeeee'])

    def test_n_aj(self):
        script_dir = osp.dirname(__file__)
        test_file = osp.join(script_dir, 'test_dialog1.csv')
        df = pd.read_csv(test_file)

        df2, values = verbosity(df)
        values_n = non_dict_words(df2)
        self.assertEqual(values_n['applejack'], ['yall', 'doin'])

    def test_f_pp(self):
        script_dir = osp.dirname(__file__)
        test_file = osp.join(script_dir, 'test_dialog1.csv')
        df = pd.read_csv(test_file)

        df2, values = verbosity(df)
        values_f = follow_on(df2)
        self.assertEqual(values_f['pinkie']['rarity'], 1)

    def test_n_tw(self):
        script_dir = osp.dirname(__file__)
        test_file = osp.join(script_dir, 'test_dialog1.csv')
        df = pd.read_csv(test_file)

        df2, values = verbosity(df)
        values_n = non_dict_words(df2)
        self.assertEqual(values_n['twilight'], [])
