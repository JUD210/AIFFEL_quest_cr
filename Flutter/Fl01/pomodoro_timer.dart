import 'dart:async';

void main() {
  PomodoroTimer timer = PomodoroTimer();
  timer.startPomodoro();
}

class PomodoroTimer {
  // 일반 타이머
  // int workDuration = 25 * 60;
  // int shortBreakDuration = 5 * 60;
  // int longBreakDuration = 15 * 60;

  // 시연용 타이머
  int workDuration = 3;
  int shortBreakDuration = 1;
  int longBreakDuration = 2;

  int cycleCount = 0;
  Timer? _timer;
  int _timeLeft = 0;

  // 첫 번째 사이클을 시작하여 Pomodoro 타이머를 시작함
  void startPomodoro() {
    print("Pomodoro Timer 시작!");
    _nextCycle();
  }

  // 다음 사이클(작업 또는 휴식)을 결정함
  // 화살표 함수 대신 콜백 함수 사용
  void _nextCycle() {
    if (cycleCount == 3) {
      _startTimer(workDuration, '작업', () {
        print("작업 시간이 종료되었습니다. 긴 휴식 시간을 시작합니다.");
        _startTimer(longBreakDuration, '긴 휴식', _resetCycle);
      });
    } else {
      _startTimer(workDuration, '작업', () {
        print("작업 시간이 종료되었습니다. 짧은 휴식 시간을 시작합니다.");
        _startTimer(shortBreakDuration, '짧은 휴식', () {
          cycleCount++;
          _nextCycle();
        });
      });
    }
  }

  // 주어진 지속 시간과 단계(작업 또는 휴식)에 대한 카운트다운 타이머를 시작함
  // 타이머가 0에 도달하면 콜백 함수가 실행됨
  void _startTimer(int duration, String phase, Function callback) {
    _timeLeft = duration;
    _timer = Timer.periodic(Duration(seconds: 1), (Timer t) {
      // 1초마다 호출되어 남은 시간을 업데이트해줌.
      if (_timeLeft > 0) {
        _timeLeft--;
        String timeString = _formatTime(_timeLeft);
        print('[${cycleCount + 1}회차 사이클 ($phase)] $timeString');
      } else {
        t.cancel();
        _timer = null; // 타이머를 취소하고 null로 설정하여 더 이상 활성 상태가 아님을 표시함
        print('$phase 완료!');
        callback();
      }
    });
  }

  // 남은 시간을 MM:SS 형식으로 포맷하여 가독성을 높임
  String _formatTime(int timeInSeconds) {
    int minutes = timeInSeconds ~/ 60; // 정수 나눗셈
    int seconds = timeInSeconds % 60;
    String minutesStr = minutes.toString().padLeft(2, '0');
    String secondsStr = seconds.toString().padLeft(2, '0');
    return '$minutesStr:$secondsStr';
  }

  // 4번의 작업 사이클과 긴 휴식을 완료한 후 사이클 카운트를 리셋함
  void _resetCycle() {
    cycleCount = 0;
    print('4회차 완료, 사이클 리셋!');
    _nextCycle();
  }
}
