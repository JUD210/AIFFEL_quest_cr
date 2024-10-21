import 'package:flutter/material.dart';
import 'cat_screen.dart';
import 'dog_screen.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      initialRoute: '/cat',
      routes: {
        '/cat': (context) => CatScreen(),
        '/dog': (context) => DogScreen(),
      },
    );
  }
}
