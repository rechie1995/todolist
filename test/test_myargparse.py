import unittest
import myargparse


class TestMyargparse(unittest.TestCase):

    def setUp(self):
        self.args_string = "list app --version"
        self.args_list = ['list', 'app', '--version']

    def test__get_args(self):
        args = myargparse.Myargparser()._get_args()
        self.assertListEqual(args, self.args_list)
