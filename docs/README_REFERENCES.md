# README 구조 레퍼런스 — 2026-09-29

FieldPilot의 README는 기능을 전부 나열하는 내부 매뉴얼이 아니라, 처음 방문한 사용자가 **무엇인지 → 왜 써야 하는지 → 어떻게 시작하는지 → 무엇을 받는지 → 어디까지 믿어야 하는지** 빠르게 이해하도록 재구성했습니다.

아래는 구조를 결정할 때 확인한 공개 저장소입니다. 스타 수는 2026-09-29 확인 시점의 참고값이며 품질 순위가 아닙니다.

## 1. oh-my-claudecode

- Repository: https://github.com/Yeachan-Heo/oh-my-claudecode
- 확인 시점 stars: 약 39.4K

가져온 구조 원칙:
- 첫 화면에서 제품을 한 문장으로 정의
- "Zero learning curve"처럼 사용자의 부담을 먼저 줄임
- Quick Start를 README 앞부분에 배치
- 복잡한 내부 기능은 뒤쪽 문서로 확장

FieldPilot 적용:
- “시장조사 용어를 몰라도 된다”를 유지
- 설치/첫 질문을 상단으로 올림
- 내부 모듈 설명은 FEATURE_GUIDE로 분리

## 2. OmO / oh-my-openagent

- Repository: https://github.com/code-yeongyu/oh-my-openagent
- 확인 시점 stars: 약 69.6K

가져온 구조 원칙:
- 설치 명령을 매우 짧게 노출
- `Why ...` 섹션에서 기능 목록보다 차별화 이유를 설명
- “사용자가 실제로 얻는 결과” 중심으로 기능을 표현

FieldPilot 적용:
- “왜 FieldPilot인가”를 README의 핵심 섹션으로 이동
- 내부 모듈명이 아니라 발견력/근거통제/결정 연결을 설명

## 3. GPT Researcher

- Repository: https://github.com/assafelovic/gpt-researcher

가져온 구조 원칙:
- 어떤 결과물을 만드는지 구체적으로 설명
- 설치/사용법과 보고서 output을 분리
- 고급 기능은 문서로 연결
- 성능 수치를 주장할 경우 benchmark 방법과 비교 조건을 함께 제시

FieldPilot 적용:
- 결과물과 보고서 형식을 명시
- 구조 테스트 수치와 시장조사 성능을 명확히 구분
- 최신 버전의 일반 AI 대비 우월성은 입증되지 않았다고 명시

## 4. STORM / Co-STORM

- Repository: https://github.com/stanford-oval/storm
- 확인 시점 stars: 약 31.5K

가져온 구조 원칙:
- Overview → How it works로 개념을 먼저 이해시킴
- 연구 프로세스를 단계로 설명
- 연구 프리뷰와 논문/근거를 연결
- publication-ready가 아니라는 한계를 README에서 직접 밝힘

FieldPilot 적용:
- 조사 흐름을 짧은 다이어그램으로 공개
- Quality Max와 전문 보고서가 무엇을 하고 무엇을 보장하지 않는지 같이 설명

## 5. MAIA Skill

- Repository: https://github.com/Hainrixz/maia-skill
- 확인 시점 stars: 약 144

가져온 구조 원칙:
- 결과 화면/산출물, 요구사항, 설치, 사용법을 명확히 분리
- fallback과 limitations를 구체적으로 표기
- 실제 데이터와 AI 분석의 한계를 구분

FieldPilot 적용:
- 요구사항과 현재 한계를 독립 섹션으로 유지
- 전문 데이터베이스/설문 인프라가 내장된 것이 아니라는 경계를 명시

## 6. deep-market-research-agent

- Repository: https://github.com/shipblueprint/deep-market-research-agent
- 확인 시점 stars: 0

스타 수와 무관하게 참고한 부분:
- README 초반에서 “What you get”을 구체적으로 보여줌
- 조사 단계를 사용자에게 이해 가능한 언어로 설명
- single-agent + tools를 선택한 이유를 명시

채택하지 않은 부분:
- “항상 경쟁사 10–15개”, “항상 20+ 페이지”, “항상 Reddit 50+ quotes” 같은 고정 수량을 FieldPilot 품질 기준으로 사용하지 않음.
- FieldPilot은 의사결정에 필요한 coverage와 semantic saturation을 기준으로 멈춤.

## FieldPilot README의 최종 설계 원칙

```text
1. 한 줄 가치
2. 왜 다른가
3. 실제 파일럿에서 나온 신호
4. Quick Start
5. 무엇을 받는가
6. 어떻게 작동하는가
7. 언제 쓰는가
8. Quality Max 정책
9. 고급 기능은 별도 가이드
10. 요구사항 / 한계 / 검증
11. 라이선스 / 피드백
```

README에서 일부러 뺀 것:
- 모든 내부 모듈의 장문 설명
- 개발 히스토리 전체
- 사용자가 처음부터 알 필요 없는 규칙 ID
- 독립 검증되지 않은 “최고”, “1등”, “일반 AI보다 우수” 표현
- 사용량 절감 자체를 핵심 USP로 내세우는 표현

이 문서는 README 구조 결정의 개발 참고자료이며 각 저장소의 품질·시장성 순위를 주장하지 않습니다.
