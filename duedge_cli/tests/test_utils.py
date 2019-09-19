# -*- coding: UTF-8 -*-
################################################################################
#
# Copyright (c) 2019 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
DuEdge Cli UT
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import unittest

from duedge_cli import utils
from mock import MagicMock
from mock import Mock
from mock import patch


class TestUtils(unittest.TestCase):
    """
    test utils
    """
     
    def test_find_match_characters(self):
        """
        test find match characters
        """
        
        self.assertEqual(utils.find_match_characters('abc', 'a'), [('a', 0)])
        
    def test_find_most_match_pattern(self):
        """
        test find most match pattern
        """
        self.assertEqual(utils.find_most_match_pattern('abc', 'ab'), ('ab ', -3))
            
    def test_guess_command(self):
        """
        test guess command
        """
        self.assertEqual(utils.guess_command('g', [['get', 'function']]), [(['get', u'function'], ['g  '])])
        
if __name__ == '__main__':
    unittest.main()
