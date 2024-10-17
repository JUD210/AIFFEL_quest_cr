import 'package:flutter/material.dart';
import 'package:intl/date_symbol_data_local.dart';

import 'quest/quest_screen.dart' as quest;
import 'playground/events_example.dart' as playground;
import 'widgets/menu_button.dart' as widgets;

void main() {
  initializeDateFormatting().then((_) => runApp(MaterialApp(home: MyApp())));
}

class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  MyAppState createState() => MyAppState();
}

class MyAppState extends State<MyApp> with SingleTickerProviderStateMixin {
  late TabController _tabController;

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 2, vsync: this);
  }

  @override
  void dispose() {
    _tabController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('플러터 앱 만들기'),
        centerTitle: true, // 타이틀을 가운데 정렬
        backgroundColor: Colors.blue, // 색상을 파란색으로 변경
        leading: widgets.MenuButton(), // 아이콘 추가
      ),
      body: TabBarView(
        controller: _tabController,
        children: [
          quest.QuestScreen(), // 서브 퀘스트 내용
          playground.TableEventsExample(), // 예전에 만든 tmp_calendar 내용
        ],
      ),
      bottomNavigationBar: TabBar(
        controller: _tabController,
        tabs: [
          Tab(icon: Icon(Icons.assignment), text: 'Quest'),
          Tab(icon: Icon(Icons.toys), text: 'Playground'),
        ],
        labelColor: Colors.blue,
        unselectedLabelColor: Colors.grey,
        indicatorSize: TabBarIndicatorSize.tab,
      ),
    );
  }
}
