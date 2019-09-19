##函数调试
**功能概述**
> 调试函数功能

**请求方式**
> POST

**请求地址**
> /v2/duedge/functions/{FunctionName}/invocations


**请求参数**

|参数名称 |是否必填| 参数类型 | 参数说明 | 
|---|---|---|
| InvocationType |否| string | 调用类型，Event:异步调用;RequestResponse:同步返回;DryRun:测试函数。此字段应设置为RequestResponse，其它的为保留类型，非必须 |
| LogType  |否| string | 日志类型，None：无；：日志附在返回应答的最后，此字段应设置为Tail，其它的为保留类型，非必须 |
| Paraments  |否| string | 函数调用的参数 |

**返回参数**

|参数名称 |参数类型 | 参数说明 | 
|---|---|---|
| errors| list | 错误信息 |
| request_uuid | string | 请求uuid |
| result|dict | 资源详情 |
| log_info|string | 执行的日志信息 |
| output|string | 执行的结果和输出信息 |
| status|int | 调用cfc测试接口http状态码|
| success| bool | 请求成功与否标志 |

**请求示例**
>/v2/duedge/functions/testHelloworld/invocations

**请求参数**
```json
{
    "InvocationType": "RequestResponse",
    "LogType": "Tail",
    "paraments": "{\"key1\":\"val1\"}"
}
```

**返回结果**
```json
{
     "errors": [],
    "request_uuid": "977b238d-5e34-4704-8c7e-349b8fd408af",
    "result": {
        "error_info": "Unhandled",
        "log_info": "START RequestId: c631ac84-bc30-48d8-8019-ed0d641be8dc Version: $LATEST\n\n\nEND RequestId: c631ac84-bc30-48d8-8019-ed0d641be8dc\nREPORT RequestId: c631ac84-bc30-48d8-8019-ed0d641be8dc\tDuration: 10ms\tBilled Duration: 100ms\tMax Memory Used: 884K\n",
        "output": "{\"errorMessage\":\"Cannot find module '/var/task/index'\",\"errorType\":\"Error\",\"stackTrace\":[\"at Function.Module._resolveFilename (module.js:469:15)\",\"at Function.Module._load (module.js:417:25)\",\"at Module.require (module.js:497:17)\",\"at require (internal/module.js:20:19)\",\"at resolveHandler (/var/runtime/lib/node_modules/@baidu/nodejs6-runtime/runtime.js:260:26)\",\"at CfcRuntime._handleMessage (/var/runtime/lib/node_modules/@baidu/nodejs6-runtime/runtime.js:133:36)\",\"at emitOne (events.js:96:13)\",\"at WebSocket.emit (events.js:188:7)\",\"at Receiver._receiver.onmessage (/var/runtime/lib/node_modules/@baidu/nodejs6-runtime/node_modules/ws/lib/WebSocket.js:141:47)\",\"at Receiver.dataMessage (/var/runtime/lib/node_modules/@baidu/nodejs6-runtime/node_modules/ws/lib/Receiver.js:389:14)\"]}",
        "status": 200
    },
    "success": true
}
```