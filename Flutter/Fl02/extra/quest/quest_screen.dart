import 'package:flutter/material.dart';

class QuestScreen extends StatelessWidget {
  const QuestScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return _buildQuestScreen(context);
  }
}

Widget _buildQuestScreen(BuildContext context) {
  return Column(
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
