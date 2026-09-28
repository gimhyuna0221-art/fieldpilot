# 사용 후기와 문제 제보

실제로 사용한 질문과 결과에서 무엇이 도움 됐고 무엇이 부족했는지 알려주세요. “더 좋게 해주세요”보다 틀린 출처 하나나 이해하기 어려운 문장 하나가 수정에 도움이 됩니다.

## Issue에 적어주실 내용

1. 사용하는 AI와 가능하면 모델, FieldPilot 버전
2. 문제를 재현할 수 있는 질문. 개인정보와 고객 자료는 지워주세요.
3. 기대한 결과와 실제 결과의 차이
4. 근거가 잘못됐다면 해당 주장과 공개 출처

비밀번호, API 키, 개인 연락처, 고객의 비공개 자료는 올리지 마세요. 공개 저장소의 Issue와 첨부파일은 누구나 볼 수 있습니다.

## 코드를 바꾸는 경우

한 가지 문제를 다루는 작은 수정부터 제안해 주세요. 원래 질문 범위를 바꾸거나 모든 조사에 새 절차를 강제하는 수정은 실제 사례와 함께 설명해 주세요.

로컬 검사:

```sh
cd skills/fieldpilot
python -X utf8 -B -m unittest discover -s tests -p "test_*.py"
python tools/competitor_coverage_check.py --inventory references/development/COMPETITOR_SOURCE_INVENTORY.md --manifest references/development/COMPETITOR_ADOPTION_CHECKLIST.md
```

Windows에서는 심볼릭 링크 권한 때문에 일부 검사가 실행되지 않을 수 있습니다. 권한을 낮추거나 미실행 검사를 성공으로 처리하지 말고 오류를 함께 남겨주세요. 테스트 통과는 실제 시장조사 품질이나 고객 효과를 보장하지 않습니다.
