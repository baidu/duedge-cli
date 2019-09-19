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

from duedge_cli import __main__ as duedge_cli
from mock import MagicMock
from mock import Mock
from mock import patch


class TestMain(unittest.TestCase):
    """
    test main
    """
     
    def test_get_signature(self):
        """
        test get signature
        """
        
        self.assertEqual(duedge_cli.get_signature('key', 'text'), 'Np4pWetJRQM4shJ0j3fY3tdIR7s=')
        
    def test_get_inited_common_params(self):
        """
        test get common params
        """
        with patch('duedge_cli.__main__.USR_CONFIG', {'access_key': 'ak'}), \
             patch('duedge_cli.__main__.SIGN_METHOD', 'HMAC-SHA1'):
            common_params = duedge_cli.get_inited_common_params('user/', '1')
            self.assertEqual(common_params['X-Auth-Nonce'], common_params['X-Auth-Timestamp'])
            
    def test_get_parsed_all_params(self):
        """
        test get parsed params
        """
        params = {}
        params['a'] = 'a'
        params['b'] = 1
        params['c'] = {'subkey': 'subvalue'}
        
        self.assertEqual(duedge_cli.get_parsed_all_params(params), 'a=a&b=1&c=subkey=subvalue')
        
if __name__ == '__main__':
    unittest.main()