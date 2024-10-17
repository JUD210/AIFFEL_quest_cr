import 'dart:collection';
import 'dart:math';

import 'package:table_calendar/table_calendar.dart';

class Event {
  final String title;
  final bool isRating;

  const Event(this.title, {this.isRating = false});

  @override
  String toString() => title;
}

final kToday = DateTime.now();
final kFirstDay = DateTime(kToday.year, kToday.month - 3, kToday.day);
final kLastDay = DateTime(kToday.year, kToday.month + 3, kToday.day);
final Random random = Random();

// 이벤트를 생성하는 함수
List<Event> createRandomEvents() {
  return [
    Event('오늘의 평점 ${random.nextInt(5) + 1}/5', isRating: true),
    Event('섭취 칼로리: ${random.nextInt(1400) + 200}/1600kcal'),
    Event('운동 시간: ${random.nextInt(120) + 1}분'),
  ];
}

final _kEventSource = {
  for (var item in List<DateTime>.generate(
      kToday.difference(kFirstDay).inDays + 1, // 오늘까지의 일수만 생성
      (index) =>
          DateTime.utc(kFirstDay.year, kFirstDay.month, kFirstDay.day + index)))
    item: createRandomEvents()
};

final kEvents = LinkedHashMap<DateTime, List<Event>>(
  equals: isSameDay,
  hashCode: getHashCode,
)..addAll(_kEventSource);

int getHashCode(DateTime key) {
  return key.day * 1000000 + key.month * 10000 + key.year;
}

/// Returns a list of [DateTime] objects from [first] to [last], inclusive.
List<DateTime> daysInRange(DateTime first, DateTime last) {
  final dayCount = last.difference(first).inDays + 1;
  return List.generate(
    dayCount,
    (index) => DateTime.utc(first.year, first.month, first.day + index),
  );
}
