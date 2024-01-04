```python
# python 中新的条件判断语句
match name:
    case "A" | "B" | "C":
        pass
    case "D":
        pass
    case _: # 没有选项时候 进入这里
        pass
```


