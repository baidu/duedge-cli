##发布版本
**功能概述**
> 发布函数版本

**请求方式**
> POST

**请求地址**
> /v2/duedge/functions/{FunctionName}/versions

**请求参数**

|参数名称 |是否必填| 参数类型 | 参数说明 | 
|---|---|---|
| Description|否| string | 版本描述 |



**返回参数**

|参数名称 | 参数类型 | 参数说明 | 
|---|---|---|
| errors| list | 错误信息 |
| request_uuid | string | 请求uuid |
| result|dict | 资源详情 |
| success| bool | 请求成功与否标志 |

**请求示例**
**请求参数**
 /v2/duedge/functions/fly-hello-001/versions
```json
{
    "Description": "xxxxxxx"
}
```


**返回结果**
```json
{
	"errors": [],
	"result": {
		"Uid": "df391b08c64c426a81645468c75163a5",
		"Description": "",
		"FunctionBrn": "brn:bce:cfc:bj:cd64f99c69d7c404b61de0a4f1865834:function:testHelloWorld:2",
		"Region": "bj",
		"Timeout": 3,
		"CodeSha256": "Zpf3bcfyy2h7roMY9BmbmVEIqlyapn3Er7LUmDp+qck=",
		"FunctionName": "testHelloWorld",
		"Handler": "index.handler",
		"Version": "2",
		"Runtime": "nodejs6.11",
		"MemorySize": 128,
		"Environment": {
			"Variables": {}
		},
		"CommitId": "d5cfc35b-a109-44f6-a6c7-7b82e6fca830"
	},
	"success": true
}
```