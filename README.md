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


## API
### 任务管理
#### 任务创建
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

#### 任务编辑
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
          ]
        ]
      }
    ]
  }
}
```

#### 入参保存
发送值
```json
{
  "task_id": "task_id",
  "api_id": "API-201802280003",
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
  ]
}
```

返回值
> 如果麻烦，可以不返回data字段
```json
{
  "code": 200,
  "msg": "success",
  "data": {
    "api_id": "API-201802280003",
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
    ]
  }
}
```

#### 任务保存
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
      ]
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

## 存在问题
- [ ] 分页没有限定显示页数
- [ ] 删除没有提示
- [ ] 接口列表没有做编辑