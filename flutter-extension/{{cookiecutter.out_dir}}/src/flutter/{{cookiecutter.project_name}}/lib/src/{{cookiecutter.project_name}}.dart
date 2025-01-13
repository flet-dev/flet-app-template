import 'package:flet/flet.dart';
import 'package:flutter/material.dart';

class {{cookiecutter.project_name.replace('-','_').split('_')|map('capitalize')|join}}Control extends StatelessWidget {
  final Control? parent;
  final Control control;

  const {{cookiecutter.project_name.replace('-','_').split('_')|map('capitalize')|join}}Control({
    super.key,
    required this.parent,
    required this.control,
  });

  @override
  Widget build(BuildContext context) {
    var color = control.attrColor("color", context);
    var value = control.attrString("value");
    Widget myControl = Text(value, style: TextStyle(color: color),);


    return constrainedControl(context, myControl, parent, control);
  }
}
