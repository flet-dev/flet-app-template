This is the development version of a directory to store application's temporary data such as logs, cache, etc.

You can get the full path to "temp" directory from `FLET_APP_TEMP` environment variable:

```py
temp_dir = os.getenv("FLET_APP_TEMP")
```

When Flet app is built and deployed to a user device `FLET_APP_TEMP` variable will contain
a real platform-specific and application-unique path.

In development mode the contents of this directory is removed on application start.