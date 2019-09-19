##修改触发器
**功能概述**
> 修改某条具体的触发器

**请求方式**
> PATCH

**请求地址**
> /duedge/v2/trigger/{id}

**请求参数**

|参数名称 |是否必填| 参数类型 | 参数说明 | 
|---|---|---|
| Regular|是| string | 节点调用函数计算时正则匹配条件|
| Description|否| string | 规则的描述信息 |
| FunctionBrn|否| string | 规则的描述信息 |
| FunctionName|否| string | 函数名 |
| Version|否| string | 函数版本(FunctionBrn或者FunctionName+Version 必须至少有一个不为空) |
| ClientRequest|否| bool | client_request触发器是否绑定函数 |
| ClientResponse|否| bool | client_response触发器是否绑定函数 |
| OriginRequest|否| bool | origin_request触发器是否绑定函数 |
| OriginResponse|否| bool | origin_response触发器是否绑定函数|
| ClientRespBody|否| bool | client_resp_body触发器是否绑定函数 |
| ClientReqBody|否| bool | client_req_body触发器是否绑定函数|
| OriginRreqBody|否| bool | origin_req_body触发器是否绑定函数 |
| OriginRespBody|否| bool | origin_resp_body触发器是否绑定函数|
**注:ClientRequest，ClientResponse，OriginRequest，OriginResponse至少有一个不为空**

**返回参数**

|参数名称 | 参数类型 | 参数说明 | 
|---|---|---|
| errors| list | 错误信息 |
| request_uuid | string | 请求uuid |
| result|dict | 资源详情 |
| success| bool | 请求成功与否标志 |

**示例**

> /duedge/v2/trigger/112233334

**请求参数**
```json
{
    "ClientRequest": true,
    "Regular":"index*.baidu.com",
    "Description":"test"
}
```


**返回结果**
```json
{
	"errors": [],
	"result": {
			"Id": 112233334,
			"DomainName": "www.test.com",
			"Regular": "*test.com",
			"FunctionBrn": "brn:bce:cfc:bj:e3e68d83bba03f911f5fd01ea4a042b5:function:helloworld:34",
			"FunctionName": "helloworld",
			"Version": "34",
			"Description": "test",
			"ClientRequest": true,
			"ClientResponse": true,
			"OriginRequest": false,
			"OriginResponse": false,
			"ClientReqBody": false,
			"ClientRespBody": false,
			"OriginReqBody": false,
			"OriginRespBody": false
		},
	"success": true
}
```