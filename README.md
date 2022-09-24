# Python Terminal UI Library

A library for terminal UI components in Python

---

## Progress Bar

The progress bar is initialized with a `max_val`, and it will be updated every time the `update` method is called. If you don't provide a parameter for the `update` method, the default value will be `1`.

Sample usage:

```python
pb = ProgressBar(100)
pb.start()
for i in range(100):
    # do something
    pb.update()
```

Output:

```
Progress |█████████---------------------| [33.0%] in 6.7s
```
```
Progress |██████████████████████████████| [100.0%] in 20.3s ✅
```
