import 'package:flutter/material.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';

class DogScreen extends StatelessWidget {
  const DogScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final args =
        ModalRoute.of(context)?.settings.arguments as Map<String, dynamic>?;
    final bool isCat = args?['isCat'] ?? false;

    return Scaffold(
      appBar: AppBar(
        title: Text('Second Page'),
        centerTitle: true,
        backgroundColor: Colors.green,
        leading: IconButton(
          // FontAweSomeIcons 요거 완전 물건이네!
          icon: Icon(FontAwesomeIcons.dog),
          onPressed: () {
            debugPrint('멍ㅋㅋ멍ㅋㅋㅋ');
          },
        ),
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Center(
            child: ElevatedButton(
                onPressed: () {
                  Navigator.pop(context, {'isCat': true});
                },
                /* 가능은 하지만, 굳이 이렇게 할 필요는 없음
                onPressed: () {
                  Navigator.pushNamed(context, '/cat',
                      arguments: {'isCat': true});
                },
                 */
                child: Text("Back")),
          ),
          SizedBox(height: 20),
          GestureDetector(
            onTap: () {
              debugPrint('isCat: $isCat');
            },
            child: Image.network(
              'https://media.tenor.com/OmRH_WPMgE8AAAAM/laugh-dog.gif',
              width: 360,
              height: 360,
            ),
          ),
        ],
      ),
    );
  }
}
