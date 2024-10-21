import 'package:flutter/material.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';

class CatScreen extends StatelessWidget {
  final bool isCat;

  const CatScreen({super.key, this.isCat = true});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('First Page'),
        centerTitle: true,
        backgroundColor: Colors.blue,
        leading: IconButton(
          // FontAweSomeIcons 요거 완전 물건이네!
          icon: Icon(FontAwesomeIcons.cat),
          onPressed: () {
            debugPrint('냐ㅋㅋ옹ㅋㅋㅋ');
          },
        ),
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Center(
            child: ElevatedButton(
              onPressed: () {
                Navigator.pushNamed(context, '/dog',
                    arguments: {'isCat': false});
              },
              child: Text("Next"),
            ),
          ),
          SizedBox(height: 20),
          GestureDetector(
            onTap: () {
              debugPrint("is_cat: $isCat");
            },
            child: Image.network(
              'https://media.tenor.com/tNfwApVE9RAAAAAM/orange-cat-laughing.gif',
              width: 360,
              height: 360,
            ),
            // 로컬로도 가능하지만, 모든 환경에서의 작동을 보장하기 위해 Image.network를 사용했음.
            /*
            Image.asset(
              'assets/cat.gif',
              width: 360,
              height: 360,
            ),
             */
          ),
        ],
      ),
    );
  }
}
