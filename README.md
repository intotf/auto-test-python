# 自动化测试 Python版

#### 2018.02.26
1. 基本html框架完成
2. 完成分组列表读取，以及分组新建、删除

#### 2018.02.27
1. 优化了分组数据添加的提示信息，包括成功、失败；执行新建分组后及时关闭新建对话框。
2. 分组编辑功能完成。
3. 完成了Vue.js表单验证。（非常重要）
4. 优化了消息提示，使得添加信息成功或失败都有消息提示。

- 剩下查看接口信息没有完成。

#### 2018.02.28
1. 接口列表增加api_id。
2. 解决modal窗口无法渲染vue指令的问题。（有content.js干扰导致modal窗口在vue实例的容器外）
3. 完成分页及分组的数据渲染。


#### 2018.03.01
1. 增加了点击分组，给出当前分组高亮的显示。
2. 接口信息页完成了数据库列表获取、构造器保存。

- 接口信息页： 数据库列表获取、构造器保存、发送测试、文档组装、返回结果显示、返回值结果属性

#### 2018.03.02
1. 接口信息页去掉了原构造器下拉框显示的jQuery监听事件，保持程序的整体性。
2. 修改了构造器保存发送数据结构。
3. 增加了数据库配置列表。（未加编辑、删除功能）

#### 2018.03.05
1. 添加了返回列表按钮，方便操作。
2. 列表接口名也加了链接，提高便捷性。
3. 测试结果页返回JSON字符串加了JsonViewer插件格式化。
4. 接口信息页增加了一个发送按钮，方便操作。

#### 2018.03.06
1. 用Vue插件实现拖动创建任务流。

#### 2018.03.07
1. 大概搭上添加任务的框架，定好任务管理的基本字段和基本流程。

#### 2018.03.08
1. 完成了任务列表的显示，任务添加。

#### 2018.03.09
1. 完成了任务编辑的入参配置，还差入参配置的raw显示。



## API
### 任务管理
#### 任务列表
地址：/task/tasklist  
请求方式：传参POST，不传参GET

返回值
```json
{
  "code": 200,
  "msg": "success",
  "data": [{
    "task_id": "taskid",
    "title": "任务描述",
    "caselists": [{
      "case_id": "api_id",
      "case_title": "案例描述"
    },{
      "case_id": "api_id",
      "case_title": "案例描述"
    }]
  },{
    "task_id": "taskid",
    "title": "任务描述",
    "caselists": [{
      "case_id": "api_id",
      "case_title": "案例描述"
    }]
  }]
}
```

#### 任务创建
地址：/task/createtask  
请求方式：POST  

发送值
```json
{
  "title": "任务描述"
}
```
返回值
```json
{
  "code": 200,
  "msg": "success",
  "data": {
    "task_id": "taskid",
    "title": "任务描述"
  }
}
```

#### 任务明细（任务编辑）
地址：/task/getdata  
请求方式：POST

发送值
```json
{
  "task_id": "task_id"
}
```
返回值
```json
{
  "code": 200,
  "msg": "success",
  "data": {
    "task_id": "taskid",
    "title": "任务描述",
    "task_flow": [
      {
        "api_id": "API-201802280003",
        "title": "接口测试标题",
        "restful": [
          ["key", "value", {
              "assign_type": "upload",
              "upload_id": 777,
              "field": "name1"
            }
          ],
          ["key", "value", {
              "assign_type": "database",
              "database_field": "",
              "sql": "SQL语句",
              "database_type": "mysql",
              "database": 301144446
            }
          ],
          ["key", "value", {
              "assign_type": "normal",
              "const_no": "chinese_name"
            }
          ],
          ["key", "value", {
              "assign_type": "normal",
              "const_no": "chinese_name"
            }
          ]
        ],
        "result": {
          "judge_type": "complete",
          "prev_data": "返回结果"
        } 
      },{
        "api_id": "API-201802280003",
        "title": "接口测试标题",
        "restful": [],
        "result": {
          "judge_type": "expect_match",
          "match_field": "匹配字段",
          "prev_data": "返回结果"
        }
      },{
        "api_id": "API-201802280003",
        "title": "接口测试标题",
        "restful": [],
        "result": {
          "judge_type": "database_match",
          "database_field": "数据库字段",
          "sql": "SQL语句",
          "database_type": "数据库类型",
          "database": "数据库配置",
          "return_key": "返回结果KEY",
          "prev_data": "返回结果"
        } 
      },{
        "api_id": "API-201802280003",
        "title": "接口测试标题",
        "restful": [],
        "result": {
          "judge_type": "execute_match",
          "execute_before":  [ "key", "value" ],
          "execute_after":  [ "key", "value" ],
          "prev_data": "返回结果"
        } 
      }
    ]
  }
}
```

#### 任务明细 > 点击入参配置获取接口restful属性
地址：/data/getparams  
请求方式：POST

发送值
```json
{
  "api_id": "api_id"
}
```
返回值
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "api_id": "api_id",
    "raw": "",
    "restful": [
      ["key1", "value1"],
      ["key2", "value2"],
      ["key3", "value3"]
    ]
  }
}
```


#### 添加入参



#### 任务保存
地址：/task/savetask  
请求方式：POS

发送值
```json
{
  "task_id": "taskid",
  "title": "任务描述",
  "task_flow": [
    {
      "api_id": "API-201802280003",
      "title": "接口测试标题",
      "restful": [
        ["key", "value", {
            "assign_type": "upload",
            "upload_id": 777,
            "field": "name1"
          }
        ],
        ["key", "value", {
            "assign_type": "database",
            "database_field": "",
            "sql": "SQL语句",
            "database_type": "mysql",
            "database": 301144446
          }
        ],
        ["key", "value", {
            "assign_type": "normal",
            "const_no": "chinese_name"
          }
        ]
      ],
      "result": {
        
      }
    }
  ]
}
```

返回值
```json
{
  "code": 200,
  "msg": "success"
}
```


#### 任务删除
地址：/task/deltask  
请求方式：POST

发送值
```json
{
  "task_id": "task_id"
}
```

返回值
```json
{
  "code": 200,
  "msg": "success"
}
```

#### 接口用例返回值设定

| 名称 | 使用字段 |
| ----- | ----- |
| 返回结果 | result |
| 判断类型 | judge_type |
|  | 完全匹配 'complete' |
|  | 预期结果与返回结果匹配 'expect_match' |
|  | 与数据库字段匹配 'database_match' |
|  | 执行前后数据比对 'execute_match' |
| 匹配字段 | match_field |
| 数据库字段 | database_field |
| SQL语句 | sql |
| 数据库类型 | database_type |
| 数据库配置 | database |
| 返回结果KEY | return_key |
| 执行前数据 | execute_before: [ key, value ] |
| 执行后预期结果 | execute_after: [ key, value ] |

## 存在问题
- [ ] 分页没有限定显示页数
- [ ] 删除没有提示
- [ ] 接口列表没有做编辑