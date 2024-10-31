This is the development version of a directory to store application's persistent data such as databases, settings, etc.

You can get the full path to "data" directory from `FLET_APP_DATA` environment variable:

```py
data_dir = os.getenv("FLET_APP_DATA")
```

When Flet app is built and deployed to a user device `FLET_APP_DATA` variable will contain
a real platform-specific and application-unique path.

The contents of this directory is guaranteed to stay intact between application updates.