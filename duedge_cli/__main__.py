# -*- coding: UTF-8 -*-
################################################################################
#
# Copyright (c) 2019 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
DuEdge Cli Main
"""

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import base64
from hashlib import sha1
import hmac
import json
import os
import pkg_resources
import platform
import re
import shutil
import sys
import time
import traceback
import zipfile

from duedge_cli import CONFIG_FILE_URL
from duedge_cli import CODE_EXAMPLE_FILE
from duedge_cli import CONFIG_UPDATE_INTERVAL
from duedge_cli import HELP_FILE_URL
from duedge_cli import HELP_OVERVIEW_FILE
from duedge_cli import LOCAL_FUNCTION_FILE
from duedge_cli import OPENAPI_BASE_URL
from duedge_cli import SIGN_METHOD
from duedge_cli import SYS_CONFIG_FILE
from duedge_cli import USR_CONFIG_FILE
from duedge_cli import WORK_DIR
from duedge_cli import _VERSION_
from duedge_cli import utils
import fire
import requests

PY_VER = 2
if sys.version > '3':
    PY_VER = 3
    
if PY_VER < 3:
    reload(sys) 
    sys.setdefaultencoding('utf8')
    
OS_TYPE = 'Linux'

if platform.platform().startswith('Win'):
    OS_TYPE = 'Windows'

SYS_CONFIG = {}
USR_CONFIG = {}


class BaseCli(object):
    """Cli Base Class"""

    def _check_params(self, params):
        """check parameters。
        Args:
            params: parameters dict
        Returns:
            bool，check result
        Raises:
        """

        return True
    
    def request(self, method='', cmd='', params=None, path='', url=''):
        """Send Http Request To Openapi。
        Args:
            method: http method
            cmd: command
            params: parameters
            path: PATH
            url: URL
        Returns:
        Raises:
        """
        if params is None:
            params = {}
        
        if not self._check_params(params):
            return
        
        if not cmd:
            print_to_term('command must assign')
            return
            
        if not path:
            path = SYS_CONFIG['command_mapping_conf'][cmd]['request_builder']['path']
        
        if not url:
            url = SYS_CONFIG['command_mapping_conf'][cmd]['request_builder']['url']
        
        querystring = {}
        payload = {}
        headers = {}
        
        params = trans_params(cmd, params, {})
        
        if 'GET' == method:
            querystring.update(params)
        else:
            payload.update(params)
        
        headers = get_request_header(path, querystring, payload)
        url = OPENAPI_BASE_URL % url
        
        logit(method, ':', url, os.linesep,
             'Params: ', querystring, os.linesep,
             'Data: ', payload, os.linesep,
             'Headers: ', headers, os.linesep)
        
        resp = send_http_request(method=method, url=url, params=querystring, payload=payload, headers=headers)
        
        resp_proc_func = SYS_CONFIG['command_mapping_conf'][cmd]['response_processor']['func_name']
        
        logit('Openapi Response: ', resp, resp.content)
        
        if resp_proc_func:
            resp_json_text = eval('self.%s' % resp_proc_func)(resp)
        else:
            resp_json_text = json.dumps(json.loads(resp.text), indent=4) \
            .encode('unicode_escape').decode('unicode_escape')
        
        print_to_term(resp_json_text)
        
        
class DuedgeCli(BaseCli):
    """Cli Class"""
    
    def run(self, *cmd, **params):
        """Run Command
        Args:
            cmd: command
            params: parameters
        Returns:
            string, command
        Raises:
        """
        if not cmd or len(cmd) == 0:
            print_to_term('Usage: duedge <command> [parameters]')
            print_to_term()
            print_to_term('To see help text, you can run:')
            print_to_term('    duedge help')
            print_to_term('    duedge <command> help')
            print_to_term('To see version, you can run:')
            print_to_term('    duedge -v')
            print_to_term()
            return
        
        if 'help_overview_less' == cmd[0]:
            self.help_overview_less()
            return
        
        if 'help_less' == cmd[0]:
            self.help_less(cmd[1])
            return
        
        if 'configure' == cmd[0]:
            self.configure(**params)
            return
    
        if 'init-function' == cmd[0]:
            self.init_function(**params)
            return
        
        if 'update' == cmd[0]:
            self.update(**params)
            return
        
        if not load_user_config():
            print_configure_help_info()
            return
        
        to_be_exe_command = cmd[0]
        
        command_all_conf = SYS_CONFIG['command_mapping_conf']
        command_conf = command_all_conf.get(to_be_exe_command, '')
        
        if not command_conf:
            selected_command = guess_command(cmd)
            if not selected_command:
                print_to_term('no such command')
                return ''

            to_be_exe_command = selected_command
            command_conf = command_all_conf[to_be_exe_command]
            
        if 'configure' == to_be_exe_command:
            self.configure(**params)
            return
    
        if 'init-function' == to_be_exe_command:
            self.init_function(**params)
            return
        
        if 'update' == to_be_exe_command:
            self.update(**params)
            return

        req_builder = command_conf['request_builder']
        req_builder_func = req_builder['func_name']
        
        path, url, conv_params = eval('self.%s' % req_builder_func)(to_be_exe_command, params)
    
        method = req_builder['method']
    
        self.request(method=method, cmd=to_be_exe_command, params=conv_params, path=path, url=url)
    
    def help(self, *cmd, **params):
        """Show help doc
        Args:
            cmd: command
            params: parameters
        Returns:
        Raises:
        """
        # export LESSCHARSET=utf-8
        os.environ['LESSCHARSET'] = 'utf-8'
        cmd_len = len(cmd)
        less_cmd = 'less'

        if 'Windows' == OS_TYPE:
            less_cmd = 'more'

        if 1 == cmd_len:
            cmd_str = 'duedge help_overview_less | %s' % less_cmd
        else:
            command_conf = SYS_CONFIG['command_mapping_conf'].get(cmd[0], '')
            if not command_conf:
                selected_command = guess_command(cmd[0:-1])
                if not selected_command:
                    print_to_term('no such command')
                    return
                
                help_command = selected_command
            else:  
                help_command = cmd[0]

            cmd_str = 'duedge help_less %s | %s' % (help_command, less_cmd)
            
        os.system(cmd_str)
    
    def help_overview_less(self):
        """help overview
        Args:
        Returns:
        Raises:
        """
        if not os.path.exists(HELP_OVERVIEW_FILE):
            help_file = pkg_resources.resource_stream(__name__, HELP_OVERVIEW_FILE)
            lines = help_file.readlines()
        else:  
            with open(HELP_OVERVIEW_FILE, 'r') as help_file:
                lines = help_file.readlines()
        
        for line in lines:
            sys.stdout.write(line.decode('utf-8'))
        sys.stdout.write(os.linesep)
        
        command_conf = SYS_CONFIG['command_mapping_conf']
        
        sorted_commands = sorted(command_conf.items(), key=lambda x: x[1]['order'])
        
        command_max_len = 0
        
        for k, v in sorted_commands:
            command_len = len(k)
            if command_len > command_max_len:
                command_max_len = command_len
            
        for k, v in sorted_commands:
            sys.stdout.write('        o %s' % k)
            sys.stdout.write(' ' * (4 + command_max_len - len(k)))
            sys.stdout.write(v['desc'])
            sys.stdout.write(os.linesep)
        
    def help_less(self, cmd):
        """show command help doc
        Args:
            cmd: command
            style: style
        Returns:
        Raises:
        """
        load_user_config()
        cmd_config = SYS_CONFIG['command_mapping_conf'][cmd]
        doc_style = USR_CONFIG.get('doc_style', 'simple')
        if not doc_style:
            doc_style = 'simple'

        help_txt_file_name = '%s%s%s.%s.txt' % (WORK_DIR, cmd_config['doc']['path'], cmd, doc_style)
        
        if not os.path.exists(help_txt_file_name):
            help_file = pkg_resources.resource_stream(__name__, help_txt_file_name)
            lines = help_file.readlines()
        else:
            with open(help_txt_file_name, 'r') as help_file:
                lines = help_file.readlines()
        
        for line in lines:
            sys.stdout.write(line.decode('utf-8'))
                
    def update(self, **params):
        """update cli
        Args:
            params: parameters
        Returns:
        Raises:
        """
        if fetch_config(force=True):
            print_to_term('update succeed')
        else:
            print_to_term('update failed')
    
    def configure(self, **params):
        """configure access_key, secret_key
        Args:
            params: parameters
        Returns:
        Raises:
        """
        try:
            if not os.path.exists(USR_CONFIG_FILE):
                with open(USR_CONFIG_FILE, 'w'):
                    pass
            
            ak = params.get('access_key', '')
            sk = params.get('secret_key', '')
            
            if not (ak and sk):
                print_to_term('missing parameters')
                return
            
            config = {}
            config['access_key'] = ak
            config['secret_key'] = sk
            
            config_json_str = json.dumps(config, indent=4)
            
            with open(USR_CONFIG_FILE, "r+") as f:
                f.seek(0)
                f.truncate()
                
                f.write(config_json_str)
                
            print_to_term('configure succeed')
        except Exception as e:
            print_exc()
            print_to_term('configure failed')
            
    def init_function(self, **params):
        """ init function entrance
        Args:
            params: parameters
        Returns:
        Raises:
        """
        try:
            runtime = params.get('runtime', '')
            if not runtime:
                print_to_term('missing parameters')
                return
            
            if not runtime in ['Python 2', 'Node.js 10', 'Lua']:
                print_to_term('invalid parameters')
                return
            
            if runtime == 'Node.js 10':
                main_file = LOCAL_FUNCTION_FILE % 'js'
            elif runtime == 'Python 2':
                main_file = LOCAL_FUNCTION_FILE % 'py'
            elif runtime == 'Lua':
                main_file = LOCAL_FUNCTION_FILE % 'lua'
                
            func_index_file = pkg_resources.resource_filename(__name__, CODE_EXAMPLE_FILE % main_file)  
            shutil.copyfile(func_index_file, main_file)
                
            print_to_term('init function succeed')
        except Exception as e:
            print_exc()
            print_to_term('init function failed')
            
    def no_conv(self, cmd, params):
        """http builder no conv
        Args:
            cmd: command
            params: parameters
        Returns:
            Tuple: path, url, params
        Raises:
        """
        url = SYS_CONFIG['command_mapping_conf'][cmd]['request_builder']['url']
        path = SYS_CONFIG['command_mapping_conf'][cmd]['request_builder']['path']
            
        return path, url, params
            
    def append_url(self, cmd, params):
        """http builder append url
        Args:
            cmd: command
            params: parameters
        Returns:
            Tuple: path, url, params
        Raises:
        """
        url = SYS_CONFIG['command_mapping_conf'][cmd]['request_builder']['url']
        path = SYS_CONFIG['command_mapping_conf'][cmd]['request_builder']['path']
        if 'function_name' in params.keys():
            path = '%s/%s' % (url, params.get('function_name', ''))
            url = path
            if 'function_name' in params.keys():
                del params['function_name']
        
        if 'version' in params.keys():
            url = '%s?Qualifier=%s' % (url, params.get('version', ''))
            
        return path, url, params
    
    def fill_and_append_url(self, cmd, params):
        """http builder fill parameters and append url
        Args:
            cmd: command
            params: parameters
        Returns:
            Tuple:path, url, params
        Raises:
        """
        url = fill_url_params(cmd, params)
        path = url
        if 'version' in params.keys():
            url = '%s?Qualifier=%s' % (url, params.get('version', ''))
            
        return path, url, params
    
    def fill_url(self, cmd, params):
        """http builder fill url
        Args:
            cmd: command
            params: parameters
        Returns:
            Tuple:path, url, params
        Raises:
        """
        url = fill_url_params(cmd, params)
        path = url
        
        return path, url, params
    
    def update_trigger_order_builder(self, cmd, params):
        """http builder for update_trigger_order
        Args:
            cmd: command
            params: parameters
        Returns:
            Tuple:path, url, params
        Raises:
        """
        url = fill_url_params(cmd, params)
        path = url
        
        if 'Step' in params.keys():
            params['step'] = params['Step']
        
        return path, url, params
    
    def create_function_builder(self, cmd, params):
        """http builder for create_function
        Args:
            cmd: command
            params: parameters
        Returns:
            Tuple:path, url, params
        Raises:
        """
        if not 'zip_file' in params.keys():
            print_to_term('missing parameters')
            sys.exit(1)
            
        if not os.path.exists(params['zip_file']):
            print_to_term('zip file is not exist')
            sys.exit(1)
            
        if not os.path.isfile(params['zip_file']):
            print_to_term('zip file is not file')
            sys.exit(1)
            
        with open(params['zip_file'], 'rb') as f:
            func_code_base64 = base64.b64encode(f.read()).decode()
        
        if 'zip_file' in params.keys():       
            del params['zip_file']
            
        code = {}
        code['ZipFile'] = func_code_base64
        params['Code'] = code
        
        path, url, _ = self.no_conv(cmd, params)
    
        return path, url, params
    
    def update_function_code_builder(self, cmd, params):
        """http builder for update_function_code http
        Args:
            cmd: command
            params: parameters
        Returns:
            Tuple:path, url, params
        Raises:
        """
        if not 'zip_file' in params.keys():
            print_to_term('missing parameters')
            sys.exit(1)
            
        if not os.path.exists(params['zip_file']):
            print_to_term('zip file is not exist')
            sys.exit(1)
            
        if not os.path.isfile(params['zip_file']):
            print_to_term('zip file is not file')
            sys.exit(1)

        with open(params['zip_file'], 'rb') as f:
            func_code_base64 = base64.b64encode(f.read()).decode()
                
        code = {}
        code['ZipFile'] = func_code_base64
        params['Code'] = code
        
        path, url, _ = self.fill_and_append_url(cmd, params)
        
        if 'function_name' in params.keys():
            del params['function_name']
        
        return path, url, params

    def create_trigger_resp_proc(self, resp):
        """http response processor for create trigger。
        Args:
        Returns:
            str
        Raises:
        """
        if resp.status_code in [500]:
            print_to_term('parameters error')
            return ''
        
        return json.dumps(json.loads(resp.text), indent=4).encode('unicode_escape').decode('unicode_escape')
    
    def list_debug_logs_builder(self, cmd, params):
        """http builder for list_debug_logs
        Args:
            cmd: command
            params: parameters
        Returns:
            Tuple:path, url, params
        Raises:
        """
        
        return '', '', {'query': 'zname:%s,create_on__gte:%s,create_on__lt:%s' % 
                           (params.get('domain_name', ''),
                            params.get('start_time', ''),
                            params.get('end_time', ''))}
        
    def list_function_aliases_builder(self, cmd, params):
        """http builder for list_debug_logs
        Args:
            cmd: command
            params: parameters
        Returns:
            Tuple:path, url, params
        Raises:
        """
        result_params = {}
#         result_params['per_page'] = 999
#         result_params['page'] = 1
#         result_params['sortby'] = 'modified_on'
#         result_params['order'] = 'desc'
#         result_params['type'] = 'alias'
        result_params['query'] = 'name:%s' % params.get('name', '')
        
        return '', '', result_params


def get_signature(sec_key, text):
    """signature
    Args:
        sec_key: secret key
        text: waiting for signature string
    Returns:
        string
    Raises:
    """
    hmac_code = hmac.new(sec_key.encode(), text.encode(), sha1).digest()
    return base64.b64encode(hmac_code).decode()


def get_inited_common_params(path):
    """init common parameters。
    Args:
        path: openapi path
    Returns:
        dict: inited parameters
    Raises:
    """
    param_map = {}

    auth_timestamp = str(int(time.time()))
    param_map['X-Auth-Access-Key'] = USR_CONFIG['access_key']
    param_map['X-Auth-Nonce'] = auth_timestamp
    param_map['X-Auth-Path-Info'] = path
    param_map['X-Auth-Signature-Method'] = SIGN_METHOD
    param_map['X-Auth-Timestamp'] = auth_timestamp

    return param_map


def get_parsed_all_params(params):
    """parsed all parameters
    Args:
        params: parameters dict
    Returns:
        string: parsed parameters
    Raises:
    """
    sorted_keys = sorted(params.keys())

    s = ''
    for k in sorted_keys:
        v = params[k]
        if dict == type(v):
            s = '%s&%s=%s' % (s, k, get_parsed_all_params(v))
        elif bool == type(v):
            s = '%s&%s=%s' % (s, k, str(v).lower())
        else:
            s = '%s&%s=%s' % (s, k, v)

    return s.replace('&', '', 1)


def get_request_header(path, query_params, body_params):
    """build http request headers。
    Args:
        path: openapi path
        data_params: http body
    Returns:
        dict, headers
    Raises:
    """
    common_params = get_inited_common_params(path)
    all_params = {}
    headers = {}

    headers.update(common_params)

    all_params.update(common_params)
    all_params.update(query_params)
    all_params.update(body_params)

    all_params_str = get_parsed_all_params(all_params)
    
    logit(all_params_str)

    sign = get_signature(USR_CONFIG['secret_key'], all_params_str)

    headers["X-Auth-Sign"] = sign

    return headers


def send_http_request(method='GET', url='', params=None, payload=None, headers=None):
    """send http request。
    Args:
        method: http method
        url: url
        params: http url args
        payload: http body
        headers: http header
    Returns:
        HttpResponse, HttpResponse
    Raises:
    """
    if params is None:
        params = {}
    if payload is None:
        payload = {}
    if headers is None:
        headers = {}
        
    return requests.request(method, url, params=params, data=json.dumps(payload), headers=headers)


def fill_url_params(cmd, params):
    """fill params in url
    Args:
        cmd: command
        params: parameters
    Returns:
        string: url
    Raises:
    """
    url = SYS_CONFIG['command_mapping_conf'][cmd]['request_builder']['url']
    if not url:
        print_to_term('no such command')
        return ''
    
    url_params = re.findall(r"{(.+?)}", url)
    
    for url_param in url_params:
        url_param_tmp = '{%s}' % url_param
        key = hump_to_connector(url_param, '_')
        to_fill_param = params.get(key, '')
        if not to_fill_param:
            continue

        del params[key]
        
        url = url.replace(url_param_tmp, str(to_fill_param))

    return url


def trans_params(cmd, params, exclude_param_keys):
    """parameters transform。
    Args:
        cmd: command
        params: parameters
        exclude_param_keys: exclude keys
    Returns:
        dict, http body
    Raises:
    """
    cmd_mapping = SYS_CONFIG['command_mapping_conf'].get(cmd, '')

    if not cmd_mapping:
        print_to_term('no such command')
        return ''
    
    cmd_param_mapping = cmd_mapping['param_mapping']
    
    result_params = {}
    
    if 'no_trans' == cmd_param_mapping['type']:
        return params
    
    for k, v in params.items():
        if k in exclude_param_keys:
            continue

        if cmd_param_mapping['type'] in ['hyphen_to_hump', 'under_cross_to_hump']:
            key = connector_to_hump(k, '_')
            result_params[key] = v
        elif 'custom' == cmd_param_mapping['type']:
            param_mapping = cmd_param_mapping['param_mapping']
            
            if not param_mapping.get(k, ''):
                result_params[k] = v
                continue
            
            key = param_mapping[k]
            result_params[key] = v
            
    return result_params

        
def connector_to_hump(str, connector):
    """string connector to hump。eg: do_test to DoTest
    Args:
        str: src string
        connector: connector
    Returns:
        dict类型, http body
    Raises:
    """
    if not connector in str:
        return str.capitalize()
    
    arr = filter(None, str.lower().split(connector))
    res = ''
    for i in arr:
        res = res + i[0].upper() + i[1:]
    return res


def hump_to_connector(str, connector):
    """string hump to connector。eg: DoTest to do_test
    Args:
        str: src string
        connector: connector
    Returns:
        dict类型, http body
    Raises:
    """
    lst = []
    for index, char in enumerate(str):
        if char.isupper() and index != 0:
            lst.append(connector)
        lst.append(char)
 
    return "".join(lst).lower()


def guess_command(cmd):
    """guess user input command
    Args:
        cmd: command
    Returns:
        string, guess command
    Raises:
    """
    command_all_conf = SYS_CONFIG['command_mapping_conf']
    command_arr = []
    
    for k, v in command_all_conf.items():
        command_arr.append(v['command_parts'])
            
    parts = utils.guess_command(cmd, command_arr)
    
    if not parts:
        return ''

    index = 0
    index_arr = []
    print_to_term('Possible commands:')
    for command_parts in parts:
        index += 1
        print_to_term('%d. %s' % (index, '-'.join(command_parts[0])))
        index_arr.append(str(index))
        
    input_func_index = 0
    while input_func_index not in index_arr:
        if 'q' == input_func_index:
            return
        
        input_str = \
        'Please enter the appropriate number + enter to run it.[%s]:' \
         % ', '.join(index_arr)
        
        if PY_VER >= 3:
            input_func_index = input(input_str)
        else:
            input_func_index = raw_input(input_str)

        if input_func_index not in index_arr and 'q' != input_func_index:
            print_to_term('Invalid serial number')

    selected_command = '-'.join(parts[int(input_func_index) - 1][0])
    
    print_to_term('Run:', selected_command)
    
    return selected_command


def load_sys_config():
    """load main system config。
    Args:
    Returns:
    Raises:
    """
    global SYS_CONFIG 
    
    try:
        if not os.path.exists(SYS_CONFIG_FILE):
            cache_temp = pkg_resources.resource_stream(__name__, SYS_CONFIG_FILE)
            SYS_CONFIG = json.load(cache_temp)
            return True
        
        with open(SYS_CONFIG_FILE, 'r') as cache_temp:
            SYS_CONFIG = json.load(cache_temp)
            
            if SYS_CONFIG['version'] <= 0:
                cache_temp = pkg_resources.resource_stream(__name__, SYS_CONFIG_FILE)
                SYS_CONFIG = json.load(cache_temp)
                
            return True
    except Exception as e:
        print_exc()
    
    print_to_term('Load system config failed')
    
    return False
        
    
def load_user_config():
    """load user local config。
    Args:
    Returns:
    Raises:
    """
    global USR_CONFIG
    
    try:
        if not os.path.exists(USR_CONFIG_FILE):
            return False
        
        with open(USR_CONFIG_FILE, 'r') as conf_temp:
            USR_CONFIG = json.load(conf_temp)
            return True
    except:
        pass
    
    return False


def fetch_config(force=False):
    """cli update。
    Args:
    Returns:
    Raises:
        PermissionError
        ConnectionError
        ConnectTimeout
    """
    try:        
        config_file_resp = requests.get(CONFIG_FILE_URL)
        config_file_resp.raise_for_status()
        config_cache_remote = json.loads(config_file_resp.content)
        
        if not force and SYS_CONFIG['version'] >= config_cache_remote['version']:
            return True
        
        doc_zip_file_name = WORK_DIR + 'doc.zip'
        with open(doc_zip_file_name, "wb") as doc_file:
            help_file_resp = requests.get(HELP_FILE_URL)
            help_file_resp.raise_for_status()
            doc_file.write(help_file_resp.content)
            
        zipfile.ZipFile(doc_zip_file_name).extractall('.')
        
        if os.path.exists(doc_zip_file_name):
            os.remove(doc_zip_file_name)
          
        with open(SYS_CONFIG_FILE, "wb") as f:
            f.seek(0)
            f.truncate()
            f.write(config_file_resp.content)
            
        return True
    except Exception as e:
        print_exc()
    
    return False


def print_configure_help_info():
    """
    print configuration tips
    """
    sys.stdout.write('Please run the command first: duedge configure ')
    sys.stdout.write('--access-key=<your access-key> ')
    sys.stdout.write('--secret-key=<your secret-key> ')
    sys.stdout.write('to initialize local user configuration')
    sys.stdout.write(os.linesep)


def logit(*msg):
    """
    out put debug message
    """
    if USR_CONFIG.get('debug_log_enable', ''):
        print(*msg)

    
def print_to_term(*msg):
    """
    output message to user's term
    """
    print(*msg)

    
def print_exc():
    """
    print exc
    """
    if USR_CONFIG.get('debug_log_enable', ''):
        traceback.print_exc()

    
def main():
    """
    main
    """
    try:
        if not load_sys_config():
            return
        
        if '-v' == sys.argv[-1]:
            print_to_term(_VERSION_)
            return
        
        duedgecli = DuedgeCli()
        
        if 'help' == sys.argv[-1]:
            fire.Fire(duedgecli.help)
            return

        fire.Fire(duedgecli.run)
    except Exception as e:
        print_exc()
