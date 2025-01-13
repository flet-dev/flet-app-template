import 'package:flet/flet.dart';
import 'package:flutter/material.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';

class SpinkitControl extends StatelessWidget {
  final Control? parent;
  final Control control;

  const SpinkitControl({
    super.key,
    required this.parent,
    required this.control,
  });

  @override
  Widget build(BuildContext context) {
    var color = control.attrColor("color", context);
    var size = control.attrDouble("size");
    var spinkitType = control.attrString("spinkittype");
    late Widget spinkitControl;

    switch (spinkitType) {
      case "rotatingcircle":
        spinkitControl = SpinKitRotatingCircle(
          color: color,
          size: size ?? 50,
        );
        break;
      case "foldingcube":
        spinkitControl = SpinKitFoldingCube(
          color: color,
          size: size ?? 50,
        );
        break;
      default:
        spinkitControl = SpinKitPumpingHeart(
          color: color,
          size: size ?? 50,
        );
    }

    return constrainedControl(context, spinkitControl, parent, control);
  }
}
