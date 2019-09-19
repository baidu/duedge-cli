##删除触发器 
**功能概述**
> 删除某条具体的触发器 

**请求方式**
> DELETE

**请求地址**
> /duedge/v2/trigger/{id}


**返回参数**

|参数名称 | 参数类型 | 参数说明 | 
|---|---|---|
| errors| list | 错误信息 |
| request_uuid | string | 请求uuid |
| result|dict | 资源详情 |
| success| bool | 请求成功与否标志 |

**示例**
> /duedge/v2/trigger/112233334


**返回结果**
```html
{
	"errors": [],
	"result": true,
	"success": true
}
```