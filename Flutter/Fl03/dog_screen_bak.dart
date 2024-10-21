import 'package:flutter/material.dart';

class DogScreen extends StatelessWidget {
  final bool isCat;

  const DogScreen({super.key, this.isCat = true});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Second Page'),
        centerTitle: true,
        backgroundColor: Colors.green,
        leading: IconButton(
          // TODO: Change to dog icon
          icon: Icon(Icons.catching_pokemon),
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
                Navigator.pushNamed(context, '/cat',
                    arguments: {'isCat': true});
              },
              child: Text("Back"),
            ),
          ),
          SizedBox(height: 20),
          GestureDetector(
            onTap: () {
              debugPrint("is_cat: $isCat");
            },
            child: Image.network(
              'https://media.tenor.com/OmRH_WPMgE8AAAAM/laugh-dog.gif',
              width: 360,
              height: 360,
            ),
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
