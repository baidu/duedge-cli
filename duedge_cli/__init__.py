# -*- coding: UTF-8 -*-
################################################################################
#
# Copyright (c) 2019 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
init
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import json
import os
import time


# 当前版本号
_VERSION_ = '1.0.9'

# 工作目录
WORK_DIR = ""

# 根目录
HOME_DIR = "duedge_cli/"

# openapi地址
OPENAPI_BASE_URL = "http://apiv5.su.baidu.com/%s"

# 远程获取配置文件url
CONFIG_FILE_URL = "http://duedge.baidu.com/cli/cache"

# 远程获取文档文件url
HELP_FILE_URL = "http://duedge.baidu.com/cli/doc.zip"

# 签名算法
SIGN_METHOD = "HMAC-SHA1"

# 本地函数文件名
LOCAL_FUNCTION_FILE = WORK_DIR + 'index.%s'

# 本地配置文件名
USR_CONFIG_FILE = WORK_DIR + '.usrconfig'

# 本地配置文件名
SYS_CONFIG_FILE = WORK_DIR + '.sysconfig'

# 帮助文件
HELP_OVERVIEW_FILE = WORK_DIR + 'doc/overview.txt'

# 示例代码路径
CODE_EXAMPLE_FILE = 'doc/code-example/%s'

# 配置文件更新时间最大间隔(秒)
CONFIG_UPDATE_INTERVAL = 60 * 60 * 24 * 5