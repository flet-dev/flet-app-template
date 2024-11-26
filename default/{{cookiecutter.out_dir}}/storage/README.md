This is the development version of a directory to store application's data.

`data` sub-directory contains persistent data such as databases, settings, etc.

You can get the full path to "data" directory from `FLET_APP_STORAGE_DATA` environment variable:

```py
data_dir = os.getenv("FLET_APP_STORAGE_DATA")
```

When Flet app is built and deployed to a user device `FLET_APP_STORAGE_DATA` variable will contain
a real platform-specific and application-unique path.

The contents of this directory is guaranteed to stay intact between application updates.

`temp` sub-directory contains temporary data such as logs, cache, etc.

You can get the full path to "temp" directory from `FLET_APP_STORAGE_TEMP` environment variable:

```py
temp_dir = os.getenv("FLET_APP_STORAGE_TEMP")
```

When Flet app is built and deployed to a user device `FLET_APP_STORAGE_TEMP` variable will contain
a real platform-specific and application-unique path.

In development mode the contents of this directory is removed on application start.