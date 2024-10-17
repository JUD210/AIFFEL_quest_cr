import 'package:flutter/material.dart';

void main() {
  runApp(MaterialApp(home: MyApp()));
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('플러터 앱 만들기'),
        centerTitle: true, // 타이틀을 가운데 정렬
        backgroundColor: Colors.blue, // 색상을 파란색으로 변경
        leading: MenuButton(), // 아이콘 추가
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Center(
            child: ElevatedButton(
              child: Text('Text'),
              onPressed: () {
                debugPrint('버튼이 눌렸습니다.');
                _showPopupMessage(context);
              },
            ),
          ),
          SizedBox(height: 80), // 버튼과 컨테이너들 간의 간격
          Stack(
            alignment: Alignment.topLeft,
            children: [
              for (int i = 0; i < 5; i++)
                Container(
                  width: 300 - (i * 60),
                  height: 300 - (i * 60),
                  decoration: BoxDecoration(
                    color: Colors.grey[300 + i * 100],
                    border: Border.all(
                      color: Colors.black,
                      width: 3,
                    ),
                  ),
                ),
            ],
          ),
        ],
      ),
    );
  }

  void _showPopupMessage(BuildContext context) {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: Text("팝업 메시지"),
          content: Text("버튼이 눌렸습니다."),
          actions: [
            TextButton(
              child: Text("확인"),
              onPressed: () {
                Navigator.of(context).pop(); // 팝업 닫기
              },
            ),
          ],
        );
      },
    );
  }
}

class MenuButton extends StatelessWidget {
  const MenuButton({super.key});

  @override
  Widget build(BuildContext context) {
    return IconButton(
      icon: Icon(Icons.menu),
      onPressed: () {
        showDialog(
          context: context,
          builder: (BuildContext context) {
            return AlertDialog(
              title: Text('메뉴 샘플'),
              content: Text('좌상단 메뉴 버튼이 눌렸습니다.'),
              actions: [
                TextButton(
                  child: Text('확인'),
                  onPressed: () {
                    Navigator.of(context).pop();
                  },
                ),
              ],
            );
          },
        );
      },
    );
  }
}
