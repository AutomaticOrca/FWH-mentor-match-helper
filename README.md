# Mentorship Matching Data Description

## 使用指南

1. **Clone** 本仓库：
   ```bash
   git clone <repo_url>
   ```

2. **准备数据文件**：
   - 在本地仓库文件夹内，根据以下**文件命名**和**格式**，将 Google Sheets 中的数据粘贴成 CSV 文件。
   - **文件命名要求**：
     - 导师信息文件：`origin_mentor.csv`
     - 导师-mentee 匹配关系文件：`origin_miniapp.csv`

3. **运行程序**：
   - 打开 Terminal，执行以下命令生成 `result.csv`：
     ```bash
     python3 main.py
     ```

4. **导入结果到 Google Sheets**：
   - 打开 Google Sheets，创建一个新的空表。
   - 点击 **File** → **Import** → 将生成的 `result.csv` 拖入即可。

---

## 1. `origin_mentor.csv`

该文件存储了所有导师的信息，每列的含义如下：
**注意**：
- 第一列是导师 ID，第二列是导师姓名。
- **最后一列**是导师可接受的 mentee 名额。
- 中间可以包含其他数据（如志愿者信息或微信号），无需删除。

| 列名               | 含义                                     |
|------------------|----------------------------------------|
| **mentor_id**    | 导师的唯一标识符（ID），可能包含前导零。        |
| **mentor_name**  | 导师的姓名。                              |
| **max_capacity** | 导师最多可接受的 mentee 数量。               |

### 示例数据
```
01	Alice	3
02	Bob	2
```

## 2. `origin_miniapp.csv`

该文件记录了 mentee 与导师的匹配关系，每列的含义如下：

| 列名               | 含义                                   |
|------------------|--------------------------------------|
| **mentor_id**    | 被 mentee 选择的导师 ID（对应 `origin_mentor.csv` 的 `mentor_id`）。 |
| **mentee_name**  | mentee 的姓名或标识符。                    |

### 示例数据
```
01	Charlie
02	David
02	Eve
```

## 3. `result.csv`

这是程序生成的结果文件，整合了导师和 mentee 的匹配信息。

| 列名               | 含义                                      |
|------------------|-----------------------------------------|
| **mentor_id**    | 导师 ID。                                   |
| **mentor_name**  | 导师姓名。                                   |
| **mentee1**      | 第 1 位 mentee（如果有）。                       |
| **mentee2**      | 第 2 位 mentee（如果有）。                       |
| **mentee3**      | 第 3 位 mentee（如果有）。                       |
| **mentee4**      | 第 4 位 mentee（如果有）。                       |
| **remaining_slots** | 导师还可以接受的 mentee 名额（最大容量 - 已分配人数）。 |
| **unselected**   | 导师是否未被任何 mentee 选择（Yes/No）。         |

### 示例数据
```
mentor_id,mentor_name,mentee1,mentee2,mentee3,mentee4,remaining_slots,unselected
01,Alice,Charlie,,,,2,No
02,Bob,David,Eve,,,0,No
03,Carol,,,,,3,Yes
```

---

💗 如在使用过程中遇到问题或需要新增功能，请联系**人事组 Joyce**，或发送邮件至：**liangjiaying1013@outlook.com**。💗

