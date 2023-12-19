import 'dart:io';

import 'package:flet/flet.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:path/path.dart' as path;
import 'package:serious_python/serious_python.dart';
import 'package:url_strategy/url_strategy.dart';

const bool isProduction = bool.fromEnvironment('dart.vm.product');

void main() async {
  await setupDesktop();

  if (isProduction) {
    // ignore: avoid_returning_null_for_void
    debugPrint = (String? message, {int? wrapWidth}) => null;
  }

  String pageUrl = "";
  String assetsDir = "";

  if (kIsWeb) {
    // web mode - connect via HTTP
    pageUrl = Uri.base.toString();
    var routeUrlStrategy = getFletRouteUrlStrategy();
    if (routeUrlStrategy == "path") {
      setPathUrlStrategy();
    }
  } else {
    // extract app from asset
    var appDir = await extractAssetZip("app/app.zip");

    // set current directory to app path
    Directory.current = appDir;

    assetsDir = path.join(appDir, "assets");

    var environmentVariables = {
      "FLET_PLATFORM": defaultTargetPlatform.name.toLowerCase()
    };

    if (defaultTargetPlatform == TargetPlatform.windows) {
      // use TCP on Windows
      var port = int.parse("{{ cookiecutter.windows_tcp_port }}");
      pageUrl = "tcp://localhost:$port";
      environmentVariables["FLET_SERVER_PORT"] = port.toString();
    } else {
      // use UDS on other platforms
      pageUrl = "flet.sock";
      environmentVariables["FLET_SERVER_UDS_PATH"] = pageUrl;
    }

    SeriousPython.runProgram(path.join(appDir, "main.pyc"),
        environmentVariables: environmentVariables);
  }

  runApp(FletApp(
    pageUrl: pageUrl,
    assetsDir: assetsDir,
    hideLoadingPage: bool.tryParse(
        "{{ cookiecutter.hide_loading_animation }}".toLowerCase()),
  ));
}
