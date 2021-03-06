##查询函数配置
**功能概述**
> 用户获取自己在DuEdge上创建的具体的某个函数

**请求方式**
> GET

**请求地址**
> /v2/duedge/functions/{FunctionName}/configuration?Qualifier={version}

**其中FunctionName为函数名称，Qualifier为非必传参数(代表版本号version)，如果Qualifier不传的话默认取$LATEST版本**


**返回参数**

|参数名称 | 参数类型 | 参数说明 | 
|---|---|---|
| errors| list | 错误信息 |
| request_uuid | string | 请求uuid |
| result|dict | 资源详情 |
| success| bool | 请求成功与否标志 |



**请求示例**


**返回结果**
```json
{
	"errors": [],
	"request_uuid": null,
	"result": {
		"Description": "",
		"FunctionBrn": "brn:bce:cfc:bj:cd64f99c69d7c404b61de0a4f1865834:function:testHelloWorld:$LATEST",
		"Region": "bj",
		"Timeout": 3,
		"UpdatedAt": "2019-03-14T14:23:51+08:00",
		"LastModified": "2019-03-14T14:23:51+08:00",
		"CodeSha256": "Zpf3bcfyy2h7roMY9BmbmVEIqlyapn3Er7LUmDp+qck=",
		"FunctionName": "testHelloWorld",
		"Handler": "index.handler",
		"Version": "$LATEST",
		"Runtime": "nodejs6.11",
		"MemorySize": 128,
		"Environment": {},
		"CommitId": "d5cfc35b-a109-44f6-a6c7-7b82e6fca830"
	},
	"success": true
}
```