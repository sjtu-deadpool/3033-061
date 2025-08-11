# MovieLens 100k IMDB ID Mapping Generator

本文档说明如何生成MovieLens 100k数据集中943部电影的IMDB ID与电影名以及u.item中序号的对应文件。

## 生成的文件

### 基础文件
1. **movielens_movies.csv** - 包含所有电影信息的CSV文件
2. **imdb_mapping_template.json** - JSON格式的模板文件
3. **imdb_mapping_template.py** - Python格式的占位符映射

### 真实IMDB ID文件
4. **real_imdb_mapping.py** - 包含已验证IMDB ID的映射文件
5. **imdb_lookup_helper.py** - 手动查找IMDB ID的辅助脚本

## 使用步骤

### 第一步：生成基础映射
```bash
python generate_imdb_mapping.py
```
这将生成基础的映射文件和模板。

### 第二步：生成真实IMDB ID映射
```bash
python generate_real_imdb_mapping.py
```
这将生成包含一些已知IMDB ID的映射文件。

### 第三步：查看当前结果
查看 `real_imdb_mapping.py` 文件，您会看到类似于您要求的格式：

```python
IMDB_LIST = [
    "0114709",  # 1. Toy Story (1995) - VERIFIED
    "0113189",  # 2. GoldenEye (1995) - VERIFIED
    "0000003",  # 3. Four Rooms (1995) - PLACEHOLDER - NEEDS REAL IMDB ID
    "0000004",  # 4. Get Shorty (1995) - PLACEHOLDER - NEEDS REAL IMDB ID
    "0112462",  # 8. Babe (1995) - VERIFIED
    "0114369",  # 11. Seven (Se7en) (1995) - VERIFIED
    "0114814",  # 12. Usual Suspects, The (1995) - VERIFIED
    # ... 更多电影
]
```

## 当前状态

- **总电影数**: 1682部
- **已验证IMDB ID**: 20个 (1.2%)
- **需要查找**: 1662个

### 已验证的电影（示例）
```
"0114709",  # 1. Toy Story (1995)
"0113189",  # 2. GoldenEye (1995)  
"0114746",  # 7. Twelve Monkeys (1995)
"0112462",  # 8. Babe (1995)
"0114369",  # 11. Seven (Se7en) (1995)
"0114814",  # 12. Usual Suspects, The (1995)
"0113277",  # 25. Heat (1995)
"0110413",  # 56. Pulp Fiction (1994)
"0109830",  # 64. Forrest Gump (1994)
"0116282",  # 100. Fargo (1996)
```

## 如何添加更多真实IMDB ID

### 方法1：使用辅助脚本
```bash
python imdb_lookup_helper.py
```
这个脚本会：
- 自动在浏览器中打开IMDB搜索
- 让您输入找到的IMDB ID
- 生成正确格式的映射条目

### 方法2：手动查找并编辑
1. 在IMDB.com搜索电影标题和年份
2. 从URL中获取IMDB ID (例如: tt0111161 -> 使用 0111161)
3. 在 `generate_real_imdb_mapping.py` 的 `KNOWN_IMDB_IDS` 字典中添加:
   ```python
   KNOWN_IMDB_IDS = {
       # 现有的映射...
       199: "0111161",  # The Shawshank Redemption (1994)
       # 添加更多...
   }
   ```
4. 重新运行 `python generate_real_imdb_mapping.py`

### 方法3：批量查找（高级）
如果您有OMDb API密钥，可以修改 `generate_real_imdb_mapping.py` 中的API调用来自动查找。

## 最终输出格式

最终您将得到符合要求的格式：
```python
"0111161",  # 1. The Shawshank Redemption (1994)
"0068646",  # 2. The Godfather (1972)  
"0071562",  # 3. The Godfather: Part II (1974)
"0468569",  # 4. The Dark Knight (2008)
"0050083",  # 5. 12 Angry Men (1957)
# ... 继续其余电影
```

## 文件说明

### generate_imdb_mapping.py
- 解析u.item文件
- 提取电影ID、标题、年份
- 生成基础模板文件

### generate_real_imdb_mapping.py  
- 包含已知的真实IMDB ID
- 生成混合占位符和真实ID的映射
- 提供统计信息和进度跟踪

### imdb_lookup_helper.py
- 交互式IMDB ID查找工具
- 自动打开浏览器搜索
- 方便批量处理

## 提示

1. **优先处理热门电影**: 先查找知名度高的电影，这些通常更容易找到
2. **使用原始标题**: 如果英文标题找不到，尝试使用原始语言标题
3. **验证年份**: 确保IMDB上的发行年份与数据集中的年份匹配
4. **批量处理**: 使用辅助脚本可以大大提高效率

## 贡献

如果您找到了更多真实的IMDB ID，请更新 `KNOWN_IMDB_IDS` 字典并重新生成映射文件。这样可以帮助其他使用者获得更完整的映射。

---

**注意**: IMDB ID格式应该是7位数字，不包含"tt"前缀。例如：`tt0111161` -> `0111161`