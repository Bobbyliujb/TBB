# TBB http:/115.29.96.197:6060/
 
## Project for Android and Database courses.

### 用户注册
- Url: /sign_up
- Method: GET/POST
- Para:
```python
{
    "username": String,
    "password": String,
    "nickname": String
}
```
- Return: rescode
```python
{
    "rescode": String
}
```

### 用户登录
- Url: /sign_in
- Method: POST
- Para:
```python
{
    "username": String,
    "password": String
}
```
- Return: rescode
```python
{
    "rescode": String
}
```

### 图片操作
#### 上传头像
- Url: /pict
- Method: POST
- Para:
```python
{
    "username": String,
    "head": String(utf-8)
    "request": "uploadHead"
}
```
- Return: rescode
```python
{
    "rescode": String
}
```

#### 下载头像
- Url: /pict
- Method: POST
- Para: 
```python
{
    "username": String,
    "request": "downloadHead"
}
```
- Return: rescode
```python
{
    "rescode": String
    "head": String(utf-8)
}
```
#### 上传商品图片
- Url: /pict
- Method: POST
- Para:
```python
{
    "username": String,
    "item_id": int,
    "image": String(utf-8)
    "request": "uploadItem"
}
```
- Return: rescode
```python
{
    "rescode": String
}
```

#### 下载商品图片
- Url: /pict
- Method: POST
- Para: 
```python
{
    "username": String,
    "item_id": int, 
    "request": "downloadItem"
}
```
- Return: rescode
```python
{
    "rescode": String
    "image": String(utf-8)
}
```

### 个人信息
#### 修改个人资料
- Url: /personal_msg
- Method: POST
- Para: 
```python
{
    "username": String,
    "request": "updateMessage",
    "college": String,
    "qq": String,
    "grade", String,
    "phone": String
}
```
- Return: rescode
```python
{
    "rescode": String
}
```

#### 获取个人资料
- Url: /personal_msg
- Method: POST
- Para: 
```python
{
    "username": String,
    "request": "getMessage"
}
```
- Return: rescode
```python
{
    "rescode": String,
    "college": String,
    "qq": String,
    "grade", String,
    "phone": String
}
```

#### 修改密码
- Url: /personal_msg
- Method: POST
- Para: 
```python
{
    "username": String,
    "oldpassword": String,
    "newpassword": String,
    "request": "updatePassword"
}
```
- Return: rescode
```python
{
    "rescode": String
}
```

#### 修改昵称
- Url: /personal_msg
- Method: POST
- Para: 
```python
{
    "username": String,
    "request": "updateNickname",
    "nickname": String
}
```
- Return: rescode
```python
{
    "rescode": String
}
```

### 商品类型
#### 添加类型
- Url: /item_type
- Method: POST
- Para: 
```python
{
    "typename": String,
    "typetext": String(default ""),
    "request": "addType"
}
```
- Return: rescode
```python
{
    "rescode": String
}
```

#### 获取类型信息
- Url: /item_type
- Method: POST
- Para: 
```python
{
    "typename": String,
    "request": "getType"
}
```
- Return: rescode
```python
{
    "rescode": String
}
```

#### 更新类型信息
- Url: /item_type
- Method: POST
- Para: 
```python
{
    "typename": String,
    "typetext": String,
    "request": "getType"
}
```
- Return: rescode
```python
{
    "rescode": String
}
```

#### 删除类型
- Url: /item_type
- Method: POST
- Para: 
```python
{
    "typename": String,
    "request": "getType"
}
```
- Return: rescode
```python
{
    "rescode": String
}
```

### 商品卖家
#### 添加商品
- Url: /seller
- Method: POST
- Para: 
```python
{
    "username": String,
    "request": "addItem",
    "item_name": String,
    "item_text": String,
    "item_time": String (milisecond),
    "item_price": String,
    "typename": String
}
```
- Return: rescode
```python
{
    "rescode": String,
    "item_id": int (if success)
}
```

#### 获取商品ID（处理异常）
- Url: /seller
- Method: POST
- Para: 
```python
{
    "username": String,
    "request": "getItemId",
    "item_name": String,
    "item_text": String,
    "item_time": String,
    "item_price": String,
}
```
- Return: rescode
```python
{
    "rescode": String,
    "item_id": int (if success)
}
```

#### 获取商品信息
- Url: /seller
- Method: POST
- Para: 
```python
{
    "username": String,
    "request": "getItem",
    "item_id": String,
}
```
- Return: rescode
```python
{
    "rescode": String,
    "item_name": String,
    "item_text": String,
    "item_time": String,
    "item_price": String, 
    "typename": String,
    "buy_flag": bool,
    "username": String
}
```

#### 删除商品
- Url: /seller
- Method: POST
- Para: 
```python
{
    "username": String,
    "request": "delItem"
    "item_id": int
}
```
- Return: rescode
```python
{
    "rescode": String
}
```

#### 更新商品
- Url: /seller
- Method: POST
- Para: 
```python
{
    "username": String,
    "request": "updateItem",
    "item_id": int, 
    "item_name": String,
    "item_text": String,
    "item_time": String (milisecond),
    "item_price": String,
}
```
- Return: rescode
```python
{
    "rescode": String,
}
```

#### 更新商品类型
- Url: /seller
- Method: POST
- Para: 
```python
{
    "username": String,
    "request": "updateItemType",
    "item_id": int, 
    "typename": String
}
```
- Return: rescode
```python
{
    "rescode": String,
}
```

#### 获取商品卖家
- Url: /seller
- Method: POST
- Para: 
```python
{
    "username": String,
    "request": "getSeller"
    "item_id": int
}
```
- Return: rescode
```python
{
    "rescode": String,
    "username": String,
}
```

#### 重新放出商品
- Url: /seller
- Method: POST
- Para: 
```python
{
    "username": String,
    "request": "resellItem",
    "item_id": int
}
```
- Return: rescode
```python
{
    "rescode": String,
    "username": String,
}
```

#### 获取售卖中商品
- Url: /seller
- Method: POST
- Para: 
```python
{
    "username": String,
    "request": "getSellingItems"
}
```
- Return: rescode
```python
{
    "rescode": String,
    "item_num": int,
    "item_list": String,
}
```

#### 获取自己的商品
- Url: /seller
- Method: POST
- Para: 
```python
{
    "username": String,
    "request": "getOwnItems"
}
```
- Return: rescode
```python
{
    "rescode": String,
    "item_num": int,
    "item_list": String,
}
```

#### 获取用户的商品（售卖中）
- Url: /seller
- Method: POST
- Para: 
```python
{
    "username": String,
    "request": "getOwnItems",
    "other": String(the username of user)
}
```
- Return: rescode
```python
{
    "rescode": String,
    "item_num": int,
    "item_list": String,
}
```


### 买家操作
#### 购买商品
- Url: /buyer
- Method: POST
- Para: 
```python
{
    "username": String,
    "request": "buyItem",
    "item_id": int
}
```
- Return: rescode
```python
{
    "rescode": String
}
```
#### 获取商品买家
- Url: /buyer
- Method: POST
- Para: 
```python
{
    "username": String,
    "request": "getBuyer",
    "item_id": int,
}
```
- Return: rescode
```python
{
    "rescode": String,
    "username": String
}
```


