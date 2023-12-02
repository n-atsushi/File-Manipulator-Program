# File-Manipulator-Program
Recurion BackendProject2 File-Manipulator-Program


1. ファイルの内容を逆順にする（reverse）
2. ファイルをコピーする（copy）
3. ファイルの内容を指定した回数だけ複製する（duplicate_contents）
4. ファイル内の指定した文字列を別の文字列に置換する（replace_string）
## 使用方法

コマンドラインから以下のように使用します。

``` bash
python3 file_manipulator.py <command> <arguments>
```

## コマンドの種類

### reverse

ファイルの内容を逆順にします。

```bash
python3 file_manipulator.py reverse <input_file> <output_path>
```
### copy

ファイルをコピーします。

```bash
python3 file_manipulator.py copy <input_file> <output_path>
```

### duplicate_contents

ファイルの内容を指定した回数だけ複製します。
```bash
python3 file_manipulator.py duplicate_contents <input_file> <n>
```

### replace_string

ファイル内の指定した文字列を別の文字列に置換します。
```bash
python3 file_manipulator.py replace_string <input_file> <before_word> <after_word>

```

# 注意事項

- このスクリプトはPython 3で動作します。
- ファイルパスは絶対パスまたはスクリプトからの相対パスで指定します。