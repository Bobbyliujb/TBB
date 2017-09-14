# TBB http://115.29.136.57:6060/
 
## Project for Android and Database courses.

### Register
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

### Sign in
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

### Pictures Util
#### upload avatar
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

#### download avatar
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
#### Upload item pic
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

#### Downlod item pic
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

### Personal information
#### Modify personal info
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

#### Get personal info
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

#### Change password
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

#### Change nickname
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

### Item category, unused!!!
#### Add category
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

#### Get category
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

#### Update category
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

#### Delete category
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

### Sellers Utils
#### Add item
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

#### Get selling item id
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

#### Get selling item info by id
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

#### Delete selling item
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

#### Update selling item info
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

#### Update selling item category
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

#### Get seller of item
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

#### Resell item
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

#### Get all items in sale
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

#### Get my items in sale(including sold ones)
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

#### Get my items in sale(only still in sale)
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


### Customer Utils
#### Purchase item
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
#### Get buyer of item
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


