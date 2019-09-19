##触发器优先级排序
**功能概述**
> 调整触发器优先级顺序 

**请求方式**
> PATCH

**请求地址**
> /duedge/v2/trigger/reorder/{id}

**请求参数**

|参数名称 |是否必填| 参数类型 | 参数说明 | 
|---|---|---|
| step|是| int | 调整这个绑定规则的优先级顺序，step > 0，这条规则优先级降低3位次（如果在这条规则优先级之后有3条规则，调整后优先级排在这3条规则后）； step < 0，这条规则的优先级提高三个位次|



**返回参数**

|参数名称 | 参数类型 | 参数说明 | 
|---|---|---|
| errors| list | 错误信息 |
| request_uuid | string | 请求uuid |
| result|dict | 资源详情 |
| success| bool | 请求成功与否标志 |

**示例**
> /duedge/v2/trigger/reorder/1234

```json
{
	"step": 1
}
```


**返回结果**
```json
{
	"errors": [],
	"result": true,
	"success": true
}
```
