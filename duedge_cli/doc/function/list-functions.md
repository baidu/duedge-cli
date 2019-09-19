##函数列表

**功能概述**

> 用户查询自己在DuEdge上自定义函数列表

**请求方式**

> GET

**请求地址**

> /v2/duedge/functions

**请求参数**

|参数名称 |是否必填| 参数类型 | 参数说明 | 
|---|---|---|
|FunctionName|否| string | 函数名称 |
|Qualifier|否| string | 函数版本，仅当FunctionName不为空才会生效 |

**返回参数**

|参数名称 | 参数类型 | 参数说明 | 
|---|---|---|
| errors| list | 错误信息 |
| request_uuid | string | 请求uuid |
| result|dict | 资源详情 |
| success| bool | 请求成功与否标志 |

**请求示例**

```
/v2/duedge/functions
```

**返回结果**

```json
{
	"errors": [],
	"request_uuid": null,
	"result": [{
			"Description": "",
			"FunctionBrn": "brn:bce:cfc:bj:cd64f99c69d7c404b61de0a4f1865834:function:httptrigger-helloworld:$LATEST",
			"Region": "bj",
			"Timeout": 3,
			"CodeSha256": "vIqmTrOvKwuL94XG2HIdGBjqN0LRtZRAird21tOY2u0=",
			"FunctionName": "httptrigger-helloworld",
			"Handler": "index.handler",
			"Version": "$LATEST",
			"Runtime": "nodejs6.11",
			"MemorySize": 128,
			"Environment": {
				"Variables": {
					"a": "b"
				}
			},
			"CommitId": "dcfbd208-796e-4a22-83e7-0c1c0698338d"
		},
		{
			"Description": "",
			"FunctionBrn": "brn:bce:cfc:bj:cd64f99c69d7c404b61de0a4f1865834:function:httptrigger-helloworld:$LATEST",
			"Region": "bj",
			"Timeout": 3,
			"CodeSha256": "vIqmTrOvKwuL94XG2HIdGBjqN0LRtZRAird21tOY2u0=",
			"FunctionName": "httptrigger-helloworld",
			"Handler": "index.handler",
			"Version": "$LATEST",
			"Runtime": "nodejs6.11",
			"MemorySize": 128,
			"Environment": {
				"Variables": {
					"a": "b"
				}
			},
			"CommitId": "dcfbd208-796e-4a22-83e7-0c1c0698338d"
		}
	],
	"result_info": {
		"count": 20,
		"page": 1,
		"per_page": 20,
		"total_count": 38
	},
	"success": true
}
```