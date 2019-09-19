##函数创建 

**功能概述**

> DuEdge上创建用户自定义函数

**请求方式**

> POST

**请求地址**

> /v2/duedge/functions

**请求参数**

|参数名称 |是否必填| 参数类型 | 参数说明 | 
|---|---|---|
| Code|是| string | 函数内容|
| FunctionName|是| string | 函数名称|
| Runtime|是| string | 运行时环境 Node.js10、Python2、Node.js8.5|
| Handler|是| string | 函数调用的入口，格式为"文件名.方法名"，如填写 "index.handler"，调用 index.js（runtime为nodejs的情况下）中的exports.handler|
| MemorySize|否| int | 内存的大小，以MB为单位，DuEdge使用此内存大小来推断分配给您的函数的CPU和内存数量。|
| Description|否| string | 函数说明|
| Environment|否| dict | 函数代码运行时的用户自定义环境变量 |
| Region|否| string | 函数代码所在百度云区域（目前只有bj,su,gz），默认为bj，不传或者传入空值时会被修正为bj |
| Timeout|否| int | 超时时间 1-300 最大300 |

**返回参数**

|参数名称 | 参数类型 | 参数说明 | 
|---|---|---|
| errors| list | 错误信息 |
| request_uuid | string | 请求uuid |
| result|dict | 资源详情 |
| id|int | 唯一标识符|
| Description|string| 一个简短的说明，0-256字符。 |
| FunctionBrn|string | 函数的唯一性资源标志符，1-170字符。|
| Region|string | 区域，现有 bj（北京）、su（苏州）、gz（广州）。|
| Timeout|int | 超时时间 1-300，最大300。|
| CodeSha256| string | 函数代码包的SHA256散列。|
| FunctionName| string | 函数的名称，由数字、字母、-或_组成。则长度限制为64个字符。|
| Handler| string | 入口函数 |
| Version| string | 版本。LATEST表示最新，否则由数字组成。1-32字符。|
| alias| string | 函数某一版本的别名|
| Runtime| string | 运行时环境|
| MemorySize| int | 内存的大小，以MB为单位，目前只支持128MB |
| Environment| string | 环境变量|
| CommitId| string | 单次提交的唯一标志|
| success| bool | 请求成功与否标志 |

**请求示例**

```json
{
    "Code": {
        "ZipFile": "UEsDBBQACAAIAAyjX00AAAAAAAAAAAAAAAAIABAAaW5kZXguanNVWAwAsJ/ZW/ie2Vv6Z7qeS60oyC8qKdbLSMxLyUktUrBV0EgtS80r0VFIzs8rSa0AMRJzcpISk7M1FWztFKq5FIAAJqSRV5qTo6Og5JGak5OvUJ5flJOiqKRpzVVrDQBQSwcILzRMjVAAAABYAAAAUEsDBAoAAAAAAHCjX00AAAAAAAAAAAAAAAAJABAAX19NQUNPU1gvVVgMALSf2Vu0n9lb+me6nlBLAwQUAAgACAAMo19NAAAAAAAAAAAAAAAAEwAQAF9fTUFDT1NYLy5faW5kZXguanNVWAwAsJ/ZW/ie2Vv6Z7qeY2AVY2dgYmDwTUxW8A9WiFCAApAYAycQGwFxHRCD+BsYiAKOISFBUCZIxwIgFkBTwogQl0rOz9VLLCjISdXLSSwuKS1OTUlJLElVDggGKXw772Y0iO5J8tAH0QBQSwcIDgnJLFwAAACwAAAAUEsBAhUDFAAIAAgADKNfTS80TI1QAAAAWAAAAAgADAAAAAAAAAAAQKSBAAAAAGluZGV4LmpzVVgIALCf2Vv4ntlbUEsBAhUDCgAAAAAAcKNfTQAAAAAAAAAAAAAAAAkADAAAAAAAAAAAQP1BlgAAAF9fTUFDT1NYL1VYCAC0n9lbtJ/ZW1BLAQIVAxQACAAIAAyjX00OCcksXAAAALAAAAATAAwAAAAAAAAAAECkgc0AAABfX01BQ09TWC8uX2luZGV4LmpzVVgIALCf2Vv4ntlbUEsFBgAAAAADAAMA0gAAAHoBAAAAAA=="
    },
    "Description": "test api",
    "Environment": {
        "Variables": {
            "additionalProp1": "string"
        }
    },
    "FunctionName": "fly-hello-001",
    "Handler": "index.handler",
    "MemorySize": 128,
    "Runtime": "python2",
    "Timeout": 5
}
```

**返回结果**

```json
{
	"errors": [],
	"request_uuid": "820a56305227b35",
	"result": {
		"Description": "test api",
		"FunctionBrn": "brn:bce:cfc:bj:cd64f99c69d7c404b61de0a4f1865834:function:fly-hello-001:1",
		"Region": "bj",
		"Timeout": 5,
		"CodeSha256": "4OFxEke82hUugwILdGb/BxnQdSUTsPAYcSU9PNVdFlU=",
		"FunctionName": "fly-hello-001",
		"Handler": "index.handler",
		"Version": "1",
		"Runtime": "python2",
		"MemorySize": 128,
		"Environment": {
			"Variables": {
				"additionalProp1": "string"
			}
		},
		"CommitId": "0feb0174-4288-4669-bfb6-a8c8c80df112"
	}
}
```
