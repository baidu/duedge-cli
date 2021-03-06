##查询触发器

**功能概述**
> 查询用户创建的所有触发器

**请求方式**
> GET

**请求地址**
> /duedge/v2/trigger



**返回参数**

|参数名称 | 参数类型 | 参数说明 | 
|---|---|---|
| errors| list | 错误信息 |
| request_uuid | string | 请求uuid |
| result|dict | 资源详情 |
| success| bool | 请求成功与否标志 |

**示例**

**请求参数**

```
/duedge/v2/trigger
```

**返回结果**
```json
{
	"errors": [],
	"result": [{
			"Id": 112233333,
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
		{
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
		}
	],
	"success": true
}
```