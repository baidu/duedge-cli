##更新函数代码
**功能概述**
> 更新指定function代码

**请求方式**
> PUT

**请求地址**
> /v2/duedge/functions/{FunctionName}/code?Qualifier={Version}

**其中FunctionName为函数名称，Qualifier为非必传参数(代表版本号version)，如果Qualifier不传的话默认取$LATEST版本**

**返回参数**

|参数名称 | 参数类型 | 参数说明 | 
|---|---|---|
| errors| list | 错误信息 |
| request_uuid | string | 请求uuid |
| result|dict | 资源详情 |
| success| bool | 请求成功与否标志 |

**请求参数**

|参数名称 | 参数类型 | 参数说明 | 
|---|---|---|
| ZipFile| blob | Base64-encoded binary data object |


**示例**

**请求参数**
```
/v2/duedge/functions/fly-hello-001/code?Qualifier=1.1
```
```json
{
    "ZipFile": "UEsDBBQACAAIAAyjX00AAAAAAAAAAAAAAAAIABAAaW5kZXguanNVWAwAsJ/ZW/ie2Vv6Z7qeS60oyC8qKdbLSMxLyUktUrBV0EgtS80r0VFIzs8rSa0AMRJzcpISk7M1FWztFKq5FIAAJqSRV5qTo6Og5JGak5OvUJ5flJOiqKRpzVVrDQBQSwcILzRMjVAAAABYAAAAUEsDBAoAAAAAAHCjX00AAAAAAAAAAAAAAAAJABAAX19NQUNPU1gvVVgMALSf2Vu0n9lb+me6nlBLAwQUAAgACAAMo19NAAAAAAAAAAAAAAAAEwAQAF9fTUFDT1NYLy5faW5kZXguanNVWAwAsJ/ZW/ie2Vv6Z7qeY2AVY2dgYmDwTUxW8A9WiFCAApAYAycQGwFxHRCD+BsYiAKOISFBUCZIxwIgFkBTwogQl0rOz9VLLCjISdXLSSwuKS1OTUlJLElVDggGKXw772Y0iO5J8tAH0QBQSwcIDgnJLFwAAACwAAAAUEsBAhUDFAAIAAgADKNfTS80TI1QAAAAWAAAAAgADAAAAAAAAAAAQKSBAAAAAGluZGV4LmpzVVgIALCf2Vv4ntlbUEsBAhUDCgAAAAAAcKNfTQAAAAAAAAAAAAAAAAkADAAAAAAAAAAAQP1BlgAAAF9fTUFDT1NYL1VYCAC0n9lbtJ/ZW1BLAQIVAxQACAAIAAyjX00OCcksXAAAALAAAAATAAwAAAAAAAAAAECkgc0AAABfX01BQ09TWC8uX2luZGV4LmpzVVgIALCf2Vv4ntlbUEsFBgAAAAADAAMA0gAAAHoBAAAAAA=="
}
```
**返回结果**
```json
{
	"errors": [],
	"request_uuid": null,
	"result": {
		"Description": "test api",
		"FunctionBrn": "brn:bce:cfc:bj:cd64f99c69d7c404b61de0a4f1865834:function:fly-hello-001:3",
		"Region": "bj",
		"Timeout": 5,
		"CodeSha256": "4OFxEke82hUugwILdGb/BxnQdSUTsPAYcSU9PNVdFlU=",
		"FunctionName": "fly-hello-001",
		"Handler": "index.handler",
		"Version": "3",
		"Runtime": "python2",
		"MemorySize": 128,
		"Environment": {
			"Variables": {
				"additionalProp1": "string"
			}
		},
		"CommitId": "dc901628-44b9-4b29-91e2-feaccc3f5099"
	},
	"success": true
}
```