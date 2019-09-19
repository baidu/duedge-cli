##函数信息

**功能概述**

> 查询用户单个函数

**请求方式**

> GET

**请求地址**

> /v2/duedge/functions/{FunctionName}?Qualifier={Version}

**其中FunctionName为函数名称，Qualifier为非必传参数(代表版本号version)，如果Qualifier不传的话默认取$LATEST版本**

**返回参数**

|参数名称 | 参数类型 | 参数说明 | 
|---|---|---|
| errors| list | 错误信息 |
| request_uuid | string | 请求uuid |
| result|dict | 资源详情 |
| success| bool | 请求成功与否标志 |

**请求示例**

```
/v2/duedge/functions/testHelloWorld
```

**返回结果**
```json
{
	"errors": [],
	"request_uuid": "",
	"result": {
		"Code": {
			"Location": "https://cfcbj.bj.bcebos.com/42f6fbc2cd374bfcb80d9967370fd8ff/sltest_3ec6ae9a1aa36374b2efac5d03d8fe499270d578c5053e7352ad2b21451952bc.zip?authorization=bce-auth-v1%2F4746faeb37854542b225fef7cc87fc36%2F2018-01-23T07%3A17%3A03Z%2F600%2Fhost%2Ffdea74e91c35c3dede418b8f9cf71b5269c42cce5c9d464af3d9e015ac8f4609"
		},
		"Configuration": {
			"Description": "测试",
			"FunctionBrn": "brn:bce:cfc:bj:1a2cbf55b97ac8a7c760c4177db4e17d:function:sltest:1",
			"Region": "bj",
			"Timeout": 3,
			"CodeSha256": "PsaumhqjY3Sy76xdA9j+SZJw1XjFBT5zUq0rIUUZUrw=",
			"FunctionName": "sltest",
			"Handler": "index.handler",
			"Version": "1",
			"Runtime": "python2",
			"MemorySize": 128,
			"Environment": {
				"Variables": {
					"": ""
				}
			},
			"CommitId": "349dd8a4-db7d-4fc3-a4cd-8c8b482e00c3"
		}
	}
}
```