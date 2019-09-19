##删除函数

**功能概述**
> 删除函数

**请求方式**
> DELETE

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
/v2/duedge/functions/testHelloWorld?Qualifier=1.1
```

**返回结果**

```json
{
	"errors": [],
	"request_uuid": "",
	"result": true
}
```