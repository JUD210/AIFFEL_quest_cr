import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

void main() {
  runApp(MyApp()); // 앱 실행 진입점
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: JellyfishClassifierPage(), // 메인 페이지 설정
    );
  }
}

class JellyfishClassifierPage extends StatefulWidget {
  const JellyfishClassifierPage({super.key});

  @override
  JellyfishClassifierPageState createState() =>
      JellyfishClassifierPageState(); // StatefulWidget의 State 생성
}

class JellyfishClassifierPageState extends State<JellyfishClassifierPage> {
  String result = ""; // 예측 결과 저장 변수
  TextEditingController urlController = TextEditingController(
      text: "https://b7a1-59-6-226-10.ngrok-free.app/"); // URL 입력 컨트롤러, 기본값 설정

  // 고정된 이미지 및 아이콘 경로
  final String imagePath = 'assets/images/jellyfish.jpg'; // 해파리 이미지 경로
  final String iconPath = 'assets/icons/icon.png'; // 해파리 아이콘 경로

  // 예측 결과를 가져오는 함수
  Future<void> fetchPrediction(String endpoint) async {
    try {
      final enteredUrl = urlController.text; // 입력된 URL 가져오기
      final response = await http.get(
        Uri.parse("$enteredUrl$endpoint"), // 입력된 URL 사용하여 엔드포인트 호출
        headers: {
          'Content-Type': 'application/json',
          'ngrok-skip-browser-warning': '69420', // ngrok 브라우저 경고 무시 헤더
        },
      );
      if (response.statusCode == 200) {
        final data = jsonDecode(response.body); // 서버에서 받은 JSON 응답 디코딩
        setState(() {
          if (endpoint == 'predict_class') {
            result =
                "Predicted Label: ${data['predicted_label']}"; // 예측된 클래스 결과 저장
          } else if (endpoint == 'predict_probability') {
            result =
                "Prediction Score: ${data['prediction_score']}"; // 예측 확률 결과 저장
          }
        });
      } else {
        setState(() {
          result =
              "Failed to fetch data. Status Code: ${response.statusCode}"; // 오류 상태 코드 출력
        });
      }
    } catch (e) {
      setState(() {
        result = "Error: $e"; // 예외 처리 시 오류 메시지 저장
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Jellyfish Classifier"), // 앱바 제목 설정
        leading: IconButton(
          icon: Image.asset(
            iconPath,
            width: 48,
            height: 48,
          ), // 해파리 아이콘 이미지
          onPressed: () {},
        ),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Image.asset(
              imagePath,
              width: 300,
              height: 300,
            ), // 상단에 고정된 해파리 이미지 표시
            SizedBox(height: 20),
            TextField(
              controller: urlController, // URL 입력을 위한 TextField
              decoration: InputDecoration(labelText: "URL 입력"), // 입력 필드의 라벨
            ),
            SizedBox(height: 20),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                ElevatedButton(
                  onPressed: () =>
                      fetchPrediction('predict_class'), // 해파리 클래스 예측 버튼
                  child: Text("해파리 클래스 예측"),
                ),
                SizedBox(width: 20),
                ElevatedButton(
                  onPressed: () =>
                      fetchPrediction('predict_probability'), // 예측 확률 출력 버튼
                  child: Text("예측 확률 출력"),
                ),
              ],
            ),
            SizedBox(height: 40),
            Text(
              result, // 예측 결과 표시
              style: TextStyle(fontSize: 18, color: Colors.black),
              textAlign: TextAlign.center,
            ),
          ],
        ),
      ),
    );
  }
}
