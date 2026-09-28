# 경쟁사와 자료원 커버리지 인벤토리

기준일: 2026-09-28. 제공된 두 원문과 현재 method-parity 개발 감사에 이름이 나온 대상을 대조하는 독립 범위 마스터다. 제품 채택 완료 보고서, 판매 문구 또는 성능 비교 결과가 아니다. 기준 패키지와 판매 문구는 수정하지 않았다.

## 1. 범위와 집계 원칙

- A: 개발 시 제공된 조사 자료 A, 1–1742줄 전체. 비공개 첨부의 개인 경로는 공개본에서 제외했다. SHA-256 `7F80DFDC44399D8DDE06C252A5DE2459115640E817FD39AFF1D7419ED0CEB2AE`.
- B: 개발 시 제공된 조사 자료 B, 1–374줄 전체. 비공개 첨부의 개인 경로는 공개본에서 제외했다. SHA-256 `A552FC5C9F767C459AAFB53908E79026E4A42484F5CA88DEC829F75814A088D8`.
- A와 B는 서로 다른 원문이다. B와 Desktop의 동명 텍스트(1)끼리 중복이라는 인수 기록을 따른다. 이 둘의 중복을 새로운 경쟁사나 자료원으로 세지 않았다.
- D: [개발 감사](COMPETITIVE_PATTERN_AUDIT_2026-09-28.md), 1–145줄 전체. 조사 플랫폼 목록과 저장소 10개를 모두 포함했다.
- C: [능력 카탈로그](../data/MARKET_RESEARCH_CAPABILITY_CATALOG.md), 기존 대응 위치를 확인한 보조 자료. C에만 있는 Typeform과 Firecrawl은 별도 C ID 및 `supplied=false`로 표시했다.
- 기준 패키지: `work/fieldpilot-method-parity-2e3a46e3/fieldpilot`. 구현 후보 `work/fieldpilot-competitor-coverage-01/fieldpilot`는 이 문서에서 검토하거나 수정하지 않았다.
- 원문의 광고 추적값은 표시 링크에서 제거했다. 링크 대상 본문이 첨부되지 않은 Dola, Manus, Genspark, Sellingbooster, Reportlinker, QuestionPro, 영상 등은 장점을 직접 검증한 것처럼 적지 않았다. 최신 외부 검색이나 저장소 코드를 새로 읽은 검토가 아니다.

| 구분 | ID | 수 | 해석 |
|---|---|---:|---|
| 제공된 비교 대상과 자료원 | E001–E101 | 101 | 경쟁사만 101개라는 뜻이 아님 |
| 카탈로그에만 있는 보조 후보 | C001–C002 | 2 | 사용자 원문에 없는 추가 회사, supplied=false |
| 명명 방법/프레임/분석 기법 | M001–M085 | 85 | 기존 일반 계약과 전용 실행법을 구별 |
| 예시/저자/통합/주변부 링크 | X001–X028 | 28 | 채택해야 할 경쟁사 범위에서 제외 |
| 총 마스터 행 | 모든 ID | 216 | 중복 없는 행 수 |
| 원자 장점/검증 후보 | E/C/M의 하위 ID | 262 | 회사 수 또는 구현 완료 수가 아님 |

E 행의 분류별 수: `provider` 54, `unverified` 12, `method_source` 10, `competitor` 21, `reference` 4. 이름만 나온 제품도 빠짐없이 남기되 `unverified`로 구분했다.

기능 단위 집계: Google Trends, Google Forms, Google Analytics, Google 리뷰는 서로 다른 능력이어서 개별 행이다. SurveyMonkey Audience는 SurveyMonkey에, Statista Consumer Insights는 Statista에, Semrush Market Explorer는 Semrush에 묶고 세부 장점으로 추적한다. 한국갤럽과 글로벌 Gallup은 원문상 별도 조사 자료 단위로 남겼다. i-rose 두 글, Ipsos 반복 행사, 동일 YouTube 링크 두 번은 독립 제공자로 늘리지 않았다. JMP의 잠재계층/SEM 반복은 각각 한 방법으로 합쳤다. 시장규모 SOM과 자기조직화 SOM은 다른 항목이다.

## 2. 상태와 읽는 법

`baseline_paths`는 실제 존재하는 기준 패키지 상대경로다. 대응할 일반 지침/가드가 있다는 뜻이지, 해당 회사 연결이나 고급 통계 구현이 완료됐다는 뜻이 아니다. 이 인벤토리는 행동검증 PASS를 부여하지 않는다. 경쟁사의 원천 데이터/패널/수집 서버/통합 권한을 글로 설명하는 것만으로 취득할 수 없다.

외부조건: P=공개 원문과 허용 접근, U=실제 사용자/기업/참가자 데이터 및 동의, L=라이선스/계정/유료 접근/지출, H=실제 사람/현장/전문가, R=실행도구/계측/외부 런타임. 이는 반드시 모두 유료라는 뜻이 아니라 작업별 확인할 의존성이다.

아래 위치 약칭은 §7의 실제 경로로 해석한다. JSON 파일은 저장하지 않았다. 하네스는 이 Markdown 표의 ID와 위치를 직접 읽는다. A/B/D/C:숫자는 1기준 원문 줄이다. 소스 줄과 URL은 문장/제공자 기원 추적용이며 현행 기능을 검증한 방문 영수증이 아니다.

## 3. 제공자와 자료원 전체 목록

| ID / 분류 / 명칭 | 취할 장점 또는 확인 후보 | 기준 패키지 위치 | 남은 반영/검증 | 원문과 링크 | 외부조건 |
|---|---|---|---|---|---|
| E001<br>provider<br>오픈서베이 / OpenSurvey | E001.a: 조사 설계 교육 자료 재사용<br>E001.b: 주기적 소비자 보고서의 출처별 표본과 추세 비교 | R, B, A, T | 공개 팁과 유료 보고서/패널을 구별하고 실제 이용권 및 최신 방법 확인 | A:1,206; https://blog.opensurvey.co.kr/category/research-tips/ | P,L,H |
| E002<br>unverified<br>Dola | E002.a: 링크만 제공됨: 시장조사 관련 실제 기능을 확인할 후보 | Q, BROKER | 본문 미제공. 시장조사 정확도, 인용, 내보내기를 추정하지 말고 직접 확인 | A:2; https://www.dola.com/chat/ | L,R |
| E003<br>method_source<br>엠핏랩 / Mfitlab | E003.a: 제품 분석 도구의 용도별 비교 관점 확인 후보 | FACT, FUN, SIG | 비교 글 본문 미제공. 판매사 비교와 각 제품 공식 기능을 분리 | A:3; https://www.mfitlab.com/solutions/mixpanel/mixpanel-vs-ga-amplitude | P |
| E004<br>competitor<br>Mixpanel | E004.a: 실제 이벤트 기반 제품 분석을 연결할 후보 | FUN, SIG, A | 퍼널, 코호트, 리텐션, 이벤트 정의 및 추적 구현을 공식 문서와 실제 내보내기로 검증. 원문 URL만으로 해당 기능 채택 완료 아님 | A:3의 URL 경로 mixpanel | U,L,R |
| E005<br>competitor<br>Google Analytics (원문 GA, 버전 미확인) | E005.a: 웹/앱 측정 도구 비교 후보 | FUN, SIG, A | GA와 GA4를 자동 동일시하지 말 것. 이벤트, 세션, 사용자, 동의 설정별 의미 확인 | A:3의 URL 경로 ga | U,L,R |
| E006<br>competitor<br>Amplitude | E006.a: 제품 행동 분석 도구 비교 후보 | FUN, SIG, A | 정확한 제품 기능, 계측, 코호트 정의, 내보내기 검증 필요 | A:3의 URL 경로 amplitude | U,L,R |
| E007<br>method_source<br>퍼블리 / Publy | E007.a: 시장 조사→경쟁사→자사 적합성으로 판단 연결<br>E007.b: 시장 규모, 성장률, 진입 시점, 출처 신뢰성 분리 | SIZ, CASE, R | 기사 예시 연도 및 실제 결론 재검증. 기업 매출 합산을 모든 시장의 정의로 쓰지 않기 | A:4,782–836; https://publy.co/content/6180 | P,L |
| E008<br>unverified<br>Manus | E008.a: 시장조사 실행 및 산출물 기능을 확인할 후보 | Q, BROKER, DEL | 링크만 있음. 자동 조사, 영구 웹 게시, 정확도 또는 비용 우위를 미확인 상태로 유지 | A:5; https://manus.im/ko/playbook/market-research-tool | L,R |
| E009<br>unverified<br>셀링부스터 / Sellingbooster | E009.a: 키워드 추세 및 판매자 자료를 확인할 후보 | T, KR, FACT | 본문 미제공. 지표 분모, 원천, 실판매와 검색량 구별 확인 | A:12; https://sellingbooster.io/trend/keyword | P,L |
| E010<br>provider<br>픽플리 / Pickply | E010.a: 목적→가설→수집→분석→실행→보고 연결<br>E010.b: 기간과 표본 표준화<br>E010.c: 소비자 조사 자료 및 대행 경로 | Q, B, A, REPORT | 기능 이름과 패널 접근을 구별. 누구나 전문가 수준이라는 홍보 문장은 채택하지 않기 | A:18–242; https://pickply.com/blog/market-research-methods-guide | P,L,H |
| E011<br>unverified<br>Genspark | E011.a: 시장조사 도구 및 보고서 기능 확인 후보 | Q, BROKER, DEL | 링크만 있음. 실제 산출물, 인용, 접근 실패와 가격 검증 필요 | A:244; https://www.genspark.ai/ko/tools/market-research-tools | L,R |
| E012<br>provider<br>ChatGPT | E012.a: 허가된 전사본과 설문 답변의 요약/코딩<br>E012.b: 가설 및 초기 산업 개요<br>E012.c: 자료 기반 세그먼트 후보 생성 | A, QL, SIZ, QUAL | 모델/도구/데이터 접근별 실제 수행 검증. 생성 페르소나는 관찰 자료가 아님. 요금 미확인 | A:62,111,197,1638–1641,1670–1673 | U,L,R |
| E013<br>provider<br>Gemini | E013.a: 허가된 데이터 분석 및 응답 요약을 맡길 실행자 후보 | A, QUAL | 현재 도구 접근과 동일 과제 성능 확인. 제품명만으로 분석 정확도 보증 불가 | A:62,108,115,197 | U,L,R |
| E014<br>provider<br>Perplexity | E014.a: 뉴스와 연구자료 발견<br>E014.b: 출처를 따라가는 초기 탐색 | SRC, BROKER, PROV | 검색 결과와 실제 원문 열람 구별. 현재 기능 및 제한 확인 | A:62,108,113,197 | P,L,R |
| E015<br>provider<br>Google Trends / 구글 트렌드 | E015.a: 검색 관심도의 시계열과 지역/키워드 비교<br>E015.b: 계절성과 일시 이슈 분리 | T, FACT, SIZ | 상대 지수와 절대 검색량/고유 인원/유료 수요를 구별. 요청 범위별 추출 증빙 필요 | A:41,120; B:302 | P |
| E016<br>provider<br>NAVER DataLab / 네이버 데이터랩 | E016.a: 국내 검색 및 쇼핑 관심도의 추세 확인 | KR, FACT, T | 상대 지표와 검색광고의 월간 검색량을 구별. 실제 구매량으로 승격 금지 | A:41,122 | P |
| E017<br>unverified<br>카카오 트렌드 (원문 명칭, 실체 미확인) | E017.a: 원문이 주장하는 소셜 트렌드 자료원 확인 후보 | SRC, FACT | 정확한 서비스명/공식 URL/운영 상태 없음. 임의 서비스로 대응시키거나 존재 보장 금지 | A:124 | P,L |
| E018<br>provider<br>KOSIS 국가통계포털 | E018.a: 인구/경제/사회 공식 통계 기반 분모<br>E018.b: 장기 자료와 조사 단위 확인 | SIZ, R, FACT, A | 표 ID, 기준 연도, 개편/정의, 다운로드 실제 검증. 통계청 조직과 기능 단위 별도 집계 | A:129,810,898–902; http://www.kosis.kr/ | P |
| E019<br>provider<br>통계청 (원문 명칭) | E019.a: 공식 통계 원문/조사 방법과 보고서 활용 | R, SRC, SIZ | 기관명은 원문 그대로 보존. 현행 조직 명칭과 링크는 실행 시 확인. KOSIS 중복 통계를 독립 증거로 세지 않기 | A:41,131,810 | P |
| E020<br>provider<br>한국은행 경제통계시스템 / ECOS | E020.a: 거시경제 및 산업 지표로 시장 맥락 점검 | R, SIZ, T | 정확한 계열, 단위, 개정치, 기준시점과 적합성 확인 | A:133 | P |
| E021<br>provider<br>닐슨코리아 / Nielsen Korea | E021.a: 소비자/시장 조사 보고서와 전문 측정 자료 활용 | R, B, CAT | 2015년 소개와 현행 상품 구별. 고유 패널, 측정 데이터와 사용권은 내장되지 않음 | A:138,922–927; http://www.nielsen.com/kr/ | P,L,H |
| E022<br>provider<br>칸타 / Kantar | E022.a: 전문 리서치 보고서와 소비자 증거 활용 후보 | R, B, CAT | 원문에 이름만 있음. 관련 제품, 국가, 표본, 라이선스 확인 | A:138 | P,L,H |
| E023<br>reference<br>트렌드 코리아 (보고서/도서 시리즈) | E023.a: 주제 및 변화 가설을 발굴하는 연례 트렌드 맥락 | T, R | 정확한 연도/저자/판본 미지정. 트렌드 명명을 수요 또는 예측 정확도 증거로 쓰지 않기 | A:140 | P,L |
| E024<br>provider<br>크몽 / Kmong | E024.a: 분석/현장조사 전문가 소싱 경로 | B, BROKER | 특정 판매자의 전문성, 표본과 납품 범위를 검증. 플랫폼이 조사의 품질을 보증하지 않음 | A:204,703–706; kmong.com | L,H |
| E025<br>provider<br>숨고 / Soomgo | E025.a: 인간 조사 전문가 소싱 경로 | B, BROKER | 개별 전문가 자격, 견적, 접근과 실제 업무 범위 확인 | A:204 | L,H |
| E026<br>provider<br>대학내일20대연구소 (원문 명칭) | E026.a: 특정 세대/타깃의 주기적 소비자 보고서 활용 | R, T, CAT | 현행 브랜드/상품, 대상 연령, 모집/가중과 재사용권 확인 | A:206 | P,L,H |
| E027<br>provider<br>썸트렌드 / SomeTrend | E027.a: SNS 언급과 검색 관련 빅데이터 분석 후보 | CAT, T, A | 본문은 서비스명만 제시. 수집 플랫폼/기간/분모와 감정모형 성능 확인 | A:208 | P,L |
| E028<br>provider<br>리스닝마인드 / ListeningMind, 허블 | E028.a: Query Finder로 주제/키워드 확장<br>E028.b: Path Finder로 검색 전후 맥락<br>E028.c: Cluster Finder로 의도 군집<br>E028.d: Journey Finder로 여정 연결 | T, SIZ, A, FACT | 네 기능은 각각 실제 출력 검증 필요. 독자 검색 DB 없음. 검색자=시장 전체 또는 편향 없음이라는 주장 채택 금지 | A:208,1385–1438; https://kr.listeningmind.com/what-is-market-research-guide/ | L,R |
| E029<br>method_source<br>IdeaScale | E029.a: 목적에 맞는 정성/정량 및 혼합방법<br>E029.b: 가격/컨셉/광고/만족도 문제별 조사 설계<br>E029.c: 윤리 및 정기 재검토 | METHOD, B, A, REFRESH, ETH | 소개 기사에서 IdeaScale 제품의 구체 기능을 추정하지 않기 | A:247–317; https://ideascale.com/ko/블로그/시장-조사란-무엇인가요/ | P |
| E030<br>provider<br>아이로즈 / i-rose | E030.a: 타깃별 실제 응답자 모집과 설문 운영<br>E030.b: 설문 기획부터 분석까지 위임<br>E030.c: Excel 원자료/요약 등 반환자료 연결 | B, A, FIELD | 같은 제공자의 두 글은 한 엔터티. 희소집단 모집 가능성과 품질은 개별 견적/자료로 확인. 재구매 보장 표현 채택 금지 | A:318–709 및 1041–1382; i-rose.co.kr | L,H |
| E031<br>method_source<br>Brunch @khushin/97 글 | E031.a: 전문 보고서, 직접 조사, 검색 신호를 조합하는 입문 경로 | R, METHOD, FACT | 검색량=사람 수/시장 규모, 출처 기재만으로 자유 재사용, 고정 FGI 인원 등은 보정 필요 | A:712–778; https://brunch.co.kr/@khushin/97 | P |
| E032<br>reference<br>식품음료신문 / ThinkFood 기사 | E032.a: 국제 진출 사례의 맥락과 원인 후보 발굴 | CASE, R | 비비고 성공 사례 하나로 재현 가능 인과를 확정하지 않기. 현재 자료와 반례 별도 필요 | A:775–776; https://www.thinkfood.co.kr/news/articleView.html?idxno=83215 | P |
| E033<br>method_source<br>QuestionPro 시장조사 가이드 | E033.a: 시장조사 방법론 원문 확인 후보 | METHOD, B | 본문 미제공. 가이드 소개와 QuestionPro 플랫폼 기능을 구별하고 확인 후 채택 | A:777; https://www.questionpro.com/blog/what-is-market-research/ | P,L |
| E034<br>unverified<br>YouTube 영상 7RVkOV5Ly-Y | E034.a: 제공 영상의 시장조사 방법/도구 주장 확인 후보 | SRC, PROV | 제목/채널/전사 미제공, 영상 미열람. 구체 장점을 추정하지 않기 | A:780; https://www.youtube.com/watch?v=7RVkOV5Ly-Y | P,R |
| E035<br>reference<br>KB증권 리서치 보고서 | E035.a: 산업 규모 추정의 기존 보고서/산식 재사용 | R, SIZ, PROV | 2021년 중고시장 추정은 현시점 규모가 아님. 원래 정의와 2022년 보고서 범위 확인 | A:811–812; https://rdata.kbsec.com/pdf_data/20220613143117077K.pdf | P |
| E036<br>provider<br>KISA / 한국인터넷진흥원 | E036.a: 인터넷/디지털 시장 관련 공공 보고서 자료원 후보 | R, SRC, FACT | 정확한 보고서, 날짜와 조사 모집단을 지정해야 사용 가능 | A:810 | P |
| E037<br>provider<br>DART | E037.a: 공시 재무제표 원문으로 기업 수익과 조건 확인 | R, SIZ, PROV | 공시 대상과 회계 연결범위 확인. 기업 총매출 합산을 해당 시장 규모로 자동 전환 금지 | A:814–816 | P |
| E038<br>provider<br>혁신의숲 | E038.a: 비상장 기업 투자/고용/소비자/비교 정보 탐색 | R, CASE, SIZ | 각 지표의 공개/추정 여부와 날짜 확인. 원문의 번개장터 숫자는 예시 과거값 | A:814,817–820 | P,L |
| E039<br>method_source<br>IBK기업은행 블로그 자료원 목록 | E039.a: IT/경제/통계/광고/트렌드 자료원 탐색 경로 | SRC, R | 2015년 목록. 링크 생존, 기관명, 접근권, 기능을 현재 사실로 승격하지 않기 | A:838–997; https://blog.ibk.co.kr/1556 | P |
| E040<br>provider<br>ITFIND / IT지식포털 | E040.a: IT 기술/시장 보고서 발견 | SRC, R, T | 현재 운영기관 및 원문 출처 확인. NIPA와 같은 원자료면 독립 출처 아님 | A:855–858; http://www.itfind.or.kr | P |
| E041<br>provider<br>랭키닷컴 / Rankey | E041.a: 웹 이용/순위 자료로 디지털 관심도 비교 | CAT, FACT | 패널/측정 방식과 커버리지 확인. 방문지표는 매출이나 전체 시장점유율 아님 | A:860–862; http://www.rankey.com | P,L |
| E042<br>provider<br>정보통신산업진흥원 / NIPA 지식마당 | E042.a: ICT 정책 및 산업 조사 자료 활용 | SRC, R, T | 2015년 경로의 현행 위치 확인. ITFIND 중복 원자료 분리 | A:865–869; http://www.nipa.kr/know/trandInformationList.it?menuNo=26&page=1 | P |
| E043<br>provider<br>삼성경제연구소 SERI (원문 명칭) | E043.a: 경제/경영 연구 보고서와 전문가 맥락 | SRC, R | 원문 이름과 역사적 도메인 보존. 현행 기관명/접근/이용권 재확인 | A:874–876; http://www.seri.org | P,L |
| E044<br>provider<br>LG경제연구원 (원문 명칭) | E044.a: 경제/산업/경영 전망의 비교 자료 | SRC, R, T | 현행 기관명, 전망 기준시점과 원문 가정 재확인 | A:879–882; http://www.lgeri.com | P |
| E045<br>provider<br>대외경제정책연구원 / KIEP | E045.a: 국가/통상/대외경제 환경 및 진입 맥락 | SRC, R, REG | 해당 국가/시점의 보고서와 현행 규정 원문 분리 | A:884–887; http://www.kiep.go.kr/ | P |
| E046<br>provider<br>한국개발연구원 / KDI | E046.a: 경제/정책 연구와 전망 맥락 | SRC, R, T | 정책 연구의 범위와 실제 대상 시장 적합성 확인 | A:889–895; http://www.kdi.re.kr | P |
| E047<br>provider<br>IMF | E047.a: 국제 경제지표 비교 자료원 후보 | R, SIZ, T | KOSIS 소개에 등장한 기관명. 정확한 계열/원문과 개정치 확인 | A:902 | P |
| E048<br>provider<br>World Bank / 세계은행 | E048.a: 국가 비교 지표의 공통 정의 활용 후보 | R, SIZ, T | 정확한 지표와 조사 정의를 확인. 여러 포털의 같은 원자료는 중복 | A:902 | P |
| E049<br>provider<br>OECD | E049.a: 국가/정책/산업 비교 통계 활용 후보 | R, SIZ, T | 회원 범위, 단위, 방법 차이와 기준연도 확인 | A:902 | P |
| E050<br>provider<br>Forrester | E050.a: 전문 시장/기술 리서치와 비교 프레임 활용 | R, CAT | 보고서 전문 접근 및 재배포 라이선스, 평가 방법 확인 | A:904–907; http://www.forrester.com/ | P,L |
| E051<br>provider<br>국회도서관 / 전자국회도서관 | E051.a: 논문/보고서의 원문 발견 및 추적 | SRC, R | 현행 원문 접근 조건과 저작권, 실제 열람 범위 확인 | A:909–912; http://www.nanet.go.kr/03_dlib/01_datasearch/datasearch.jsp | P,L |
| E052<br>provider<br>한국갤럽 | E052.a: 국내 여론/소비자 조사 결과와 방법 참조 | R, B, SUR | Gallup 글로벌과 대상/표본 분리. 문항/모집/기간/가중 확인 | A:914–916; http://www.gallup.co.kr/ | P,L,H |
| E053<br>provider<br>Gallup 글로벌 | E053.a: 국제 조사 및 추세 자료 활용 | R, B, SUR | 한국갤럽과 서비스 단위 분리. 국가별 대표성/비교 가능성 및 접근권 확인 | A:917–920; http://www.gallup.com/ | P,L,H |
| E054<br>provider<br>DMC리포트 | E054.a: 디지털 광고/미디어/소비자 동향 보고서 | R, T | 발행시점, 표본과 실제 보고서 원출처 확인 | A:931–934; http://www.dmcreport.co.kr | P,L |
| E055<br>provider<br>한국방송광고진흥공사 / KOBACO | E055.a: 광고 산업과 소비자 조사 자료 활용 | R, T, B | 공개 통계/조사별 단위와 현행 상품 기능 분리 | A:936–939; https://www.kobaco.co.kr/ | P |
| E056<br>provider<br>Ads of the World | E056.a: 광고 크리에이티브 사례의 자극/비교 후보 | CASE, CON, R | 게시 사례는 매출/광고효과 증거 아님. 사용권과 실제 성과 분리 | A:941–943; http://adsoftheworld.com/ | P,L |
| E057<br>provider<br>Creative Ad Awards | E057.a: 광고 아이디어 및 형식 사례 탐색 | CASE, CON, R | 수상/선정 여부와 고객 성과 구별. 현행 사이트와 사용권 확인 | A:944–947; http://www.creativeadawards.com/ | P |
| E058<br>provider<br>trendwatching.com | E058.a: 소비자 변화와 신흥 트렌드 가설 발굴 | T, R | 편집된 사례의 선택 편향, 지역/기간과 유료 접근 확인 | A:949–953; http://trendwatching.com/ | P,L |
| E059<br>reference<br>Mashable | E059.a: 디지털/문화 변화 뉴스 신호 발견 | T, SRC | 뉴스를 원자료와 구별하고 독립 원천으로 역추적 | A:954–958; http://mashable.com/ | P |
| E060<br>unverified<br>risingcat 블로그의 브랜드랭킹 서비스 (제공자 미상) | E060.a: 검색어/사이트 트래픽 기반 순위라는 댓글 속 후보 | SRC, FACT | 2015년 댓글의 운영자/상품명/현재 운영 미확인. NAVER 자체 상품으로 처리 금지 | A:981; blog.naver.com/risingcat | P,L |
| E061<br>unverified<br>myasset.com 증권 리서치 경로 (현행 주체 미확인) | E061.a: 증권사 리서치 자료 발견 후보 | SRC, R | 2015년 댓글 링크. 현재 법인/브랜드를 추정하지 말고 원문과 운영 확인 | A:995; http://www.myasset.com/myasset/mainindex.html | P |
| E062<br>competitor<br>JMP | E062.a: 군집/차원축소/통계검정 및 모델 진단<br>E062.b: 텍스트/척도/구조모형<br>E062.c: 선택/컨조인트/MaxDiff/Uplift | A, SIZ, PRICE, EXP | M043–M072의 기법별 조건과 계산 검증이 필요. 일반 분석 규칙은 JMP 기능 전체 동등성 아님 | A:999–1040 | U,L,R |
| E063<br>unverified<br>Reportlinker | E063.a: 시장 인텔리전스/보고서 탐색 기능 확인 후보 | R, SRC, CAT | 링크만 제공. 데이터 원천, 중복 집계, 라이선스 및 현행 기능 확인 | A:1440; https://www.reportlinker.com/ | P,L |
| E064<br>method_source<br>작성자 미상 영문 시장조사 글 (UK-ONS/Mettelo 경력 표기) | E064.a: 디지털/비디지털 방법의 보완<br>E064.b: 목적→방법→분석→소통<br>E064.c: 지속적 재검토 | METHOD, B, A, REFRESH | 작성자/출판사/원문 식별 필요. 경력 표기를 ONS 공식 지침으로 간주 금지 | A:1442–1456; 원문 URL 미제공 | P |
| E065<br>unverified<br>75개국 Offline Trade Consultant 맞춤형 시장조사 (제공자 미상) | E065.a: 국가별 수출환경과 경쟁/유통 조사<br>E065.b: 실제 현지 바이어 인터뷰와 매장 조사<br>E065.c: 인증/물류/문화 맥락 반영 | B, FIELD, REG, CASE | 제공자 신원과 75개국 네트워크 검증 필요. 현지 인간 접근/구매/방문을 AI만으로 대체 불가 | A:1458–1562; 원문 URL 미제공 | L,H |
| E066<br>method_source<br>Shopify 시장조사 블로그 | E066.a: 분석/소비자 피드백/전략/시간절감의 역할 분리<br>E066.b: 도구별 전문 영역 비교 | A, CAT, BROKER | 도구 기능/요금의 2차 설명. 현재 기능과 효과를 입증하는 벤치마크 아님 | A:1563–1674; https://www.shopify.com/kr/blog/ai-in-market-research | P |
| E067<br>competitor<br>Insight7 | E067.a: 통화/영상/인터뷰에서 고객 문제와 욕구 코드화<br>E067.b: 주제/감정/세그먼트별 분석<br>E067.c: 내부 자료 통합 후보 | A, QL, BROKER | 전사 정확도, 언어/감정 오류, 실제 통합 권한 검증. 정성 빈도를 시장 비율로 승격 금지 | A:1612,1633–1636 | U,L,R |
| E068<br>competitor<br>Quantilope | E068.a: 조사 목적별 재사용 분석/설문 절차<br>E068.b: 컨셉/광고 비교<br>E068.c: 조사 중 모니터링과 차트 산출 | B, A, CON, EXP | 15개 방법의 정확한 목록과 산식은 미제공. 설문 자극 비교를 실매출 무작위 실험으로 등치 금지 | A:1617,1643–1646 | U,L,H,R |
| E069<br>competitor<br>Crayon | E069.a: 경쟁 웹/채용/리뷰/소셜의 변화 탐지<br>E069.b: 가격 변화 추적<br>E069.c: 차별점/반론용 배틀카드 | REFRESH, T, CASE, PROV | 지속 수집/알림 서비스는 내장 아님. 사용자 요청 갱신 규칙과 무인 모니터링을 구별 | A:1607,1648–1651 | P,L,R |
| E070<br>competitor<br>Semrush / Semrush Market Explorer | E070.a: 디지털 경쟁군/트래픽/유입/키워드 비교<br>E070.b: 고객/시장 탐색 가설 | CAT, FACT, T | 시장 탐색 상품과 SEO 플랜을 혼동하지 않기. 추정 디지털 활동과 매출/총시장 구별 | A:1629,1653–1656; D:16 | P,L |
| E071<br>competitor<br>Pecan | E071.a: 수요/규모/캠페인 수익 예측 모델 후보<br>E071.b: 내부 데이터 연결을 통한 분석 | A, SIZ, SCEN | 학습/검증/시점 분할, 누출 방지, 기준모델 비교와 보정 필요. 예측 정확도/ROI 실증 없음 | A:1658–1661 | U,L,R |
| E072<br>unverified<br>groundnews.net 기사 (동명 서비스와 구별) | E072.a: 제공 기사 원문의 주장 확인 후보 | SRC, R | 기사 본문 미제공. ground.news 제품과 동일 서비스로 가정 금지 | A:1676; http://www.groundnews.net/news/articleView.html?idxno=7466 | P |
| E073<br>unverified<br>YouTube 영상 A8-g5GkXkIc | E073.a: 제공 영상의 방법/도구 주장 확인 후보 | SRC, PROV | 두 번 나온 같은 영상은 1개. 제목/채널/전사 미제공, 미열람 | A:1679,1681; https://www.youtube.com/watch?v=A8-g5GkXkIc | P,R |
| E074<br>competitor<br>Ipsos / Ipsos Digital Platform / 입소스 코리아 | E074.a: DIY+전문가 지원 설문<br>E074.b: 클레임/이름/시각자극 선별<br>E074.c: 아이디어→컨셉 평가<br>E074.d: 영상/디지털 광고 평가<br>E074.e: 중복/허위응답 QC<br>E074.f: PPT/Excel/PDF/SPSS 반환 | B, A, CON, FIELD, DEL | 실제 패널/전문가/수집 인프라 필요. 72시간, 43국, 60%절감, 오류 원천차단은 검증 없이 이식 불가 | A:1683–1742; 주제 링크 https://www.ipsos.com/ko-kr/topic/maketing (원 기사 URL 아님) | L,H,R |
| E075<br>provider<br>Google Forms | E075.a: 온라인 설문 작성/회수의 가벼운 실행 경로 | B, SUR | 실제 분기/무작위화/수집/접근성/내보내기 한계를 확인. Forms 보유가 패널 보유 아님 | B:76 | U,R |
| E076<br>provider<br>NAVER 리뷰 | E076.a: 경쟁 제품/서비스의 공개 후기와 불만 후보 탐색 | SRC, A, PROV | 후기 노출/삭제/선택 편향, 작성자/중복, 접근 약관 확인. 모집단 대표성 없음 | B:238 | P |
| E077<br>provider<br>Google 리뷰 | E077.a: 경쟁 서비스의 공개 경험/평판 신호 탐색 | SRC, A, PROV | 별점 및 리뷰 수를 수요/품질 인과로 등치 금지. 대상 장소와 기간/중복 확인 | B:238 | P |
| E078<br>provider<br>Twitter / X | E078.a: 공개 설문/언급/해시태그를 통해 반응 가설 발견 | CAT, ACCESS, A | 원문 Twitter 명칭을 X와 연결하되 현행 API/접근 미검증. 자발 참여는 확률 표본 아님 | A:301; B:301 | P,L,R |
| E079<br>provider<br>Facebook | E079.a: 공개 주제/피드백의 변화 신호 탐색 | CAT, ACCESS, A | 비공개 커뮤니티 접근과 수집 권한 필요. 사용자 집단과 시장 전체 구별 | B:301 | P,L,R |
| E080<br>provider<br>Instagram | E080.a: 공개 해시태그/주제/소비자 반응 신호 | CAT, ACCESS, A | 노출 알고리즘/계정/시기 편향 및 실제 접근 검증 필요 | B:301 | P,L,R |
| E081<br>method_source<br>FasterCapital (제공된 두 방법론 글) | E081.a: 사업개발 목표에 조사 결합<br>E081.b: 정량/정성/경쟁/트렌드의 단계별 조사<br>E081.c: 직접/간접/미래 경쟁자 구분<br>E081.d: BCG/미스터리쇼핑 등 선택지 | Q, METHOD, CASE, T | B 본문은 출처 두 개를 제시하나 각 문장별 대응 미상. 가상 사례와 일반화된 성공 주장을 사실로 채택 금지 | B:352,354; https://fastercapital.com/ko/content/시장-조사를-통한-사업-개발.html ; https://fastercapital.com/ko/content/시장-조사--다단계-마케팅-고객-및-경쟁사를-이해하기-위해-시장-조사를-수행하는-방법.html | P |
| E082<br>competitor<br>SurveyMonkey / SurveyMonkey Audience | E082.a: 설계→모집→수집→정리→검정→추적→보고의 전과정<br>E082.b: 문항 분기/파이핑/무작위화/collector<br>E082.c: Audience 응답자 조달 | B, A, SUR, CAT | 제품 기능별 실제 계정 테스트 필요. Audience는 하위 서비스로 묶되 패널 접근 별도 외부조건 | D:8–10; C:9–10 | U,L,H,R |
| E083<br>competitor<br>Qualtrics | E083.a: 교차표/통계/driver 탐색<br>E083.b: 주제/감정 분석<br>E083.c: 연구 결과 readout | B, A, CAT | driver 연관을 인과로 등치 금지. 세부 통계모형/권한/원자료 실제 결과 검증 | D:11–12; C:9 | U,L,R |
| E084<br>provider<br>Prolific | E084.a: 응답자 접근/스크리닝/모집 통제 | B, FIELD, CAT | 모집단 적합성, 보상/동의, 실제 공급과 부정응답 처리 필요. 패널 내장 아님 | D:13; C:10 | L,H |
| E085<br>provider<br>Pollfish | E085.a: 타깃 응답자 조달 및 패널 관리 | B, FIELD, CAT | 표집 방식/지역/장치별 편향과 QC 확인. 자동 대표성 없음 | D:13; C:10 | L,H |
| E086<br>provider<br>GWI | E086.a: 소비자 속성/행동/미디어 이용 비교 | CAT, R, A | 국가/연령/온라인 모집단, 표본/가중과 라이선스 확인 | D:14; C:11 | P,L,H |
| E087<br>provider<br>SparkToro | E087.a: 오디언스의 관심/매체/도달 경로 후보 | CAT, R, T | 관심 집단의 정의, 추정 방법, 커버리지 검증. 구매자와 관심층을 동일시 금지 | D:14; C:11 | P,L |
| E088<br>provider<br>Statista / Statista Consumer Insights | E088.a: 시장/카테고리/예측 데이터 정리<br>E088.b: 소비자 특성 비교 | CAT, R, SIZ, A | 원출처/추정/설문 결과를 분리. Consumer Insights 하위 서비스와 원천 통계 중복 표시 | D:15; C:11–12 | P,L,H |
| E089<br>provider<br>Similarweb | E089.a: 디지털 경쟁군/추정 트래픽/유입 채널 비교 | CAT, FACT, T | 독점 클릭스트림/모델 데이터는 내장 불가. 추정 트래픽 점유를 전체 시장 매출로 승격 금지 | D:16; C:13 | P,L |
| E090<br>provider<br>Brandwatch | E090.a: 소셜/소비자 대화에서 주제/변화/감정 탐색 | CAT, A, T | firehose/아카이브/과거 수집과 현재 공개웹은 다른 자원. 편향과 모델 오류 검증 | D:17; C:14 | P,L,R |
| E091<br>competitor<br>assafelovic/gpt-researcher | E091.a: 탐색 전 질문 계획<br>E091.b: 과업별 전문 에이전트<br>E091.c: 독립 검색 병렬화<br>E091.d: 출처 추적<br>E091.e: 컨텍스트 필터<br>E091.f: 긴 인용 보고서/내보내기 | Q, QUAL, PROV, DEL | 질문/출처 연결은 문서 반영. 정확한 repo 버전/실행 범위 및 실제 행동 검증 필요. 코드/고정 출처수/필수 병렬 미채택 | D:24–35; https://github.com/assafelovic/gpt-researcher | R |
| E092<br>competitor<br>stanford-oval/storm / STORM, Co-STORM | E092.a: 관점별 질문<br>E092.b: 원문 기반 후속질문<br>E092.c: 집필 전 개요<br>E092.d: 사람 조향과 공유 개념지도 | Q, PROV, REPORT | 질문 커버리지 규칙은 존재. 실제 대화형 공유지도 UI/인간 조향 실행은 미검증. 가상 전문가=증거 금지 | D:37–46; Q:109–118; https://github.com/stanford-oval/storm | R |
| E093<br>provider<br>Panniantong/Agent-Reach | E093.a: 플랫폼별 접근 계층<br>E093.b: 순서 있는 fallback<br>E093.c: 실제 health/doctor 확인 | ACCESS, FREE, BROKER | 지침/레시피와 설치된 실행기를 구별. 플랫폼별 실제 접근 영수증 필요. 새 런타임 의존성 미도입 | D:48–56; https://github.com/Panniantong/Agent-Reach | L,R |
| E094<br>competitor<br>bytedance/deer-flow | E094.a: 하네스와 서브에이전트 역할 분리<br>E094.b: 지속 컨텍스트/기억<br>E094.c: 도구/스킬 확장<br>E094.d: 진단/추적/sandbox | QUAL, CONT, PROV | 외부 상태/호스트에 의존. 전체 super-agent 런타임/자율 영구기억을 스킬이 구현했다는 주장 불가 | D:58–67; https://github.com/bytedance/deer-flow | R |
| E095<br>competitor<br>rageshns/udaplay-market-research-agent / UdaPlay | E095.a: 내부 자료 검색→품질 평가→웹 보완<br>E095.b: 상태를 보존하는 인용 종합 | R, BROKER, PROV, CONT | 실제 내부 검색 연결/원자료 평가와 이어받기 시험 필요. 요약만 재활용해 출처 읽기를 대체하지 않기 | D:69–74; https://github.com/rageshns/udaplay-market-research-agent | U,R |
| E096<br>competitor<br>kevinmhorvath/theboardroom | E096.a: 독립 관점 검토<br>E096.b: 상호 반박/교차검토<br>E096.c: 게이트를 거친 통합 메모 | DEC, QUAL | FieldPilot은 문헌 근거 렌즈로 변환. 한 모델의 역할놀이를 독립 시장 증거/실제 전문가 검토로 세지 않기 | D:76–81; https://github.com/kevinmhorvath/theboardroom | P,R |
| E097<br>competitor<br>666ghj/MiroFish | E097.a: 행위자 지도<br>E097.b: 행위자 상호작용<br>E097.c: 2차 반응 경로<br>E097.d: 시나리오 보고 | SCEN | 규칙상 SYNTHETIC_HYPOTHESIS로 반영. 실제 사람 데이터/수요 예측/정확도 검증 아님. 에이전트 시뮬레이터 자체 이식 미실시 | D:83–87; https://github.com/666ghj/MiroFish | U,R |
| E098<br>competitor<br>shipblueprint/deep-market-research-agent | E098.a: 단일 컨텍스트 책임자와 필요시 도구 호출<br>E098.b: 브랜드/욕구/고통/경쟁/커뮤니티/시장별 조사<br>E098.c: 출처가 있는 실제 고객 인용<br>E098.d: 배치검색/표적 추출/저장 보고서 | Q, QUAL, BROKER, PROV, DEL | 규칙 반영과 실제 배치검색 실행은 별도. 고정 경쟁사/인용 수 미채택. 조건부 분업 손익 검증 | D:91–103; https://github.com/shipblueprint/deep-market-research-agent | P,R |
| E099<br>competitor<br>Hainrixz/maia-skill | E099.a: 무료자료 우선 순차 fallback<br>E099.b: 분리 가능한 전문영역 병렬화<br>E099.c: JSON/수치 계약<br>E099.d: 대화형 보고와 HTML fallback<br>E099.e: 이중언어/접근성/로컬 보관<br>E099.f: 과거 결과 비교 | FREE, QUAL, A, RENDER, REPORT, CONT | 일반 HTML/PDF/연속성 규칙 반영. 실제 대화형 UI, 이중언어 품질, 성과기록 감사 미입증. 투자점수/필수 대시보드 미채택 | D:105–121; https://github.com/Hainrixz/maia-skill | U,R |
| E100<br>competitor<br>ElmatadorZ/MoneyAtlas-ClaudeSkill-Agent | E100.a: 복수 시나리오<br>E100.b: 기각/반전 조건과 모름/판단보류<br>E100.c: 사람의 최종 판단<br>E100.d: 의사결정 게이트 계약시험 | SCEN, DEC, CLAIM, QUAL | 가드 존재와 실제 행동 실패율은 별도. 금융시장 사이클/무보정 확신점수 미채택 | D:123–132; https://github.com/ElmatadorZ/MoneyAtlas-ClaudeSkill-Agent | U,R |
| E101<br>method_source<br>단순함의 기술 (원문 도서명, 판본 미상) | E101.a: 원문이 참고한 시장조사/문제 단순화 방법의 출처 확인 후보 | R, METHOD | 동명 도서 식별 전 특정 저자/내용을 추정하지 말 것 | A:773; 84–91쪽으로 제시, 저자/판본/URL 없음 | P,L |

## 4. 카탈로그에서만 추가한 후보

사용자 원문/개발 감사의 원래 범위와 섞이지 않도록 별도 표시한다. 이 두 회사를 새 사용자 요구사항인 것처럼 확정하지 않는다.

| ID / 이름 | 장점 후보 | 기준 위치 | 남은 확인 | 출처 | 외부조건 |
|---|---|---|---|---|---|
| C001: Typeform<br>supplied=false | 설문 작성/논리/수집 경로 후보 | B, CAT | 사용자 첨부/개발 감사에는 없고 카탈로그에만 있는 추가 후보. 현재 기능과 실제 수집 검증 | C:9 | U,L,R |
| C002: Firecrawl<br>supplied=false | 웹 검색/추출의 대체 실행 경로 후보 | FREE, BROKER, CAT | 사용자 첨부/개발 감사에는 없고 카탈로그에만 있는 추가 후보. 실제 접근/추출/요금 검증 | C:15 | P,L,R |

## 5. 방법론 누락 탐지 목록

통계 기법을 나열한 것은 계산 엔진이나 검증된 분석 레시피를 구현한 것과 다르다. 특히 M043–M072는 JMP 원문에 명시된 이름을 개별로 추적한다. 적용하지 않는 방법도 이유 있는 N/A 또는 안전한 외부 위임으로 마무리할 수 있지만, 이름을 찾았다는 이유로 ADOPTED/PASS 처리하지 않는다.

| ID / 방법 | 취할 장점 | 기존 위치 | 추가 구현/검증 조건 | 원문 줄 | 외부조건 |
|---|---|---|---|---|---|
| M001: 조사 목적, 문제 정의, 의사결정 질문 | 결정에 영향을 주는 질문과 성공/중단 조건을 선명하게 한다 | Q, METHOD | 규칙 존재. 목적→질문→근거→결정 연결이 실제 출력에 남는지 시험 | A:27–35,275–277,1420–1426; B:21–39 | P,U |
| M002: 조사 계획과 단계별 일정/예산/책임 | 수집 전에 방법, 범위, 자원과 보고물을 합의 | Q, B, FIELD | 과업에 없는 기한/목표 수치의 임의 생성 금지. 실행계획 실제 사용성 검증 | A:27–35,262,277; B:35–39 | U,H |
| M003: 데스크 리서치 / 2차 조사 | 기존 자료 재사용으로 불필요한 신규 조사 감소 | R, DESK, SRC | 기존 원문 실제 열람, 적합성/시점/중복을 검증해야 함 | A:269,754–766; B:235–238,298–302 | P,L |
| M004: 정량 조사 | 분포/차이의 규모를 정의된 단위로 분석 | SUR, A | 숫자나 큰 표본만으로 객관성/대표성 보장 불가 | A:264,299–301; B:65–132 | U,H,R |
| M005: 정성 조사 | 맥락, 경험과 의미를 탐색 | QL, A | 연구자 해석/반례/누락 목소리를 기록. 인구 비율로 일반화 금지 | A:263,296–298; B:137–210 | U,H |
| M006: 혼합방법 / 정성-정량 통합 | 수치와 설명의 수렴/보완/충돌을 함께 해석 | A, QL, SUR | COMPILER:91 규칙 존재. 양쪽 불일치를 평균내어 지우지 않는 행동 시험 | A:308,1408; B:210 | U,H,R |
| M007: 설문 / 온라인 피드백 조사 | 목표 구성개념에 맞춘 표준화된 질문과 응답 수집 | B, SUR, A | 도구와 유효설계 구별, 문항/노출/분기/동의/파일럿 실제 검증 | A:99–102,301; B:72–81 | U,H,R |
| M008: 단순 무작위 표집 | 추출 확률이 알려진 모집틀에서 추론 기반 제공 | SUR, FIELD | 확률추출을 실제 구현해야 함. 편의 응답 CSV에 이름만 붙이지 않기 | B:98–103 | U,H,R |
| M009: 층화 표집 | 중요 하위집단의 설계상 커버리지 확보 | SUR, FIELD, A | 층별 추출/가중/설계효과 검증. 단순 quota와 확률층화 구별 | B:98–103 | U,H,R |
| M010: 심층 인터뷰 / IDI / 일대일 인터뷰 | 개인별 동기/상황을 질문하고 후속 탐색 | QL, A | 실제 참가자/동의/훈련된 진행자, 원문 링크와 반례 필요 | A:104,298,755; B:149–155 | U,H,R |
| M011: 포커스 그룹 / FGI | 상호작용 속 공동 언어와 이견 탐색 | QL, A | 6–8명/6–10명 고정 규칙 미채택. 지배/동조와 그룹 단위를 반영 | A:263,298,734,755; B:156–160 | U,H |
| M012: 관찰 / 맥락적 관찰 | 상황 안의 실제 행동/작업흐름 기록 | QL, FIELD | 관찰되지 않은 동기를 단정하지 않기. 현장/영상/접근 및 동의 필요 | A:99,263,1408; B:297 | U,H |
| M013: 참여 관찰 | 참여 맥락과 문화의 세부 행동 탐색 | QL, FIELD | 일반 관찰 가드만 연결됨. 참여자 역할/장기관찰/윤리의 별도 절차 필요 | B:161–165 | U,H |
| M014: 민족지 / Ethnography | 장기간의 문화와 생활 맥락 탐색 | QL, FIELD | 전용 ethnography 카드 미확인. 현지 접근/시간/반성적 기록 및 전문 검토 필요 | B:171–175 | U,H |
| M015: 사례 연구 / Case Study | 실제 맥락에서 과정과 조건을 깊게 비교 | QL, CASE | 서술 사례와 연구설계 구별. 반례 및 전이 조건 검증 | A:298; B:166–170 | P,U,H |
| M016: 미스터리 쇼핑 | 실제 구매/문의 흐름과 고객 경험의 관찰 | DESK, QL, FIELD, ETH | 전용 카드 미확인. 구매/방문 권한, 비용, 녹음/기만/개인정보 검토 필요 | B:233 | U,L,H |
| M017: 주제별 코딩 / Thematic Analysis | 전사/자유응답의 주제와 예외 추출 | A, QL | 원행 ID, 코드북, 애매함/소수 의견, 분석자 검토 재현성 시험 | A:281; B:189 | U,R |
| M018: 내러티브 분석 | 시간 순서/이야기 구조와 의미 관계 분석 | QL, A | 전용 분석 절차 미확인. 요약/주제분류와 구별해 적용 조건/사례 검증 | B:189 | U,R,H |
| M019: 내용 분석 / Content Analysis | 문서/발언의 의미 단위와 규칙 기반 분류 | A, QL | 단위/코딩 규칙/추론 범위 검증. 임의 키워드 빈도를 의미로 확정 금지 | A:281; B:310 | P,U,R |
| M020: 감정 분석 / Sentiment Analysis | 텍스트 반응의 감정 후보를 대량 분류 | A | 언어/풍자/도메인 오분류, 불확실/중립/혼합감정 표기와 검증셋 필요 | A:1027,1610–1612,1634 | U,R |
| M021: A/B 무작위 실험 | 정의된 단위/처치/창에서 효과 추정 | EXP | 무작위화/SRM/군집/간섭/다중비교/효과크기 검증. 설문 비교와 실제 행동 실험 구별 | A:1032,1617; B:82–88 | U,H,R |
| M022: 통제 실험 | 대조 조건과 결과를 비교해 가설 평가 | EXP | 통제군이 있다는 이유만으로 무작위실험 아님. 배정/식별/교란 조건 확인 | B:88–90 | U,H,R |
| M023: SWOT | 내부 강약/외부 기회위협 정리 | Q, CASE | 전용 프레임 계약 미확인. 항목별 근거, 분류 이유와 미확인 칸 필요 | A:6,153,1430; B:242–248 | P,U |
| M024: PEST | 정치/경제/사회/기술의 외부 변화 정리 | Q, T, REG | 관련 영향 경로를 증거로 연결. 모든 칸을 추측으로 채우지 않기 | A:149 | P |
| M025: PESTEL | PEST에 환경/법률 축을 더한 상황 점검 | Q, T, REG | 전용 프레임 계약 미확인. 현행 법률은 해당 관할 원문/전문 검토 필요 | A:6 | P,H |
| M026: Porter 5 Forces / 포터의 5가지 힘 | 신규진입/대체재/경쟁/구매자/공급자 힘 비교 | Q, CASE | 시장 경계/가치사슬과 각 힘의 근거를 명시. 자동 점수화 금지 | A:50,151; B:249–256 | P,U |
| M027: BCG 매트릭스 | 포트폴리오의 성장률과 상대 점유율 비교 | SIZ, CASE | 전용 카드 미확인. 기준 경쟁자 대비 상대 점유율과 성장률의 정의/기간 필요 | B:257–263 | U,P |
| M028: 비즈니스 모델 캔버스 / BMC | 고객/가치/경로/수익/비용 등 사업 가정을 일관되게 연결 | Q, CASE, CONT | 전용 칸별 근거 계약 미확인. 9칸을 모두 검증된 사실로 채우지 않기 | A:6 | P,U |
| M029: 7Ps | 마케팅 실행 요소의 누락 점검 | Q, CASE | 원문 명칭만 있음. 서비스 맥락/각 P의 실행 근거, 측정과 책임을 확인 | A:6 | P,U |
| M030: 3C | 고객/자사/경쟁자 진단을 연결 | Q, CASE, SIZ | 자사 사실과 외부 관찰의 출처 분리. 전용 적용/QA 절차 미확인 | A:1415 | P,U |
| M031: STP | 세분화→표적시장→포지셔닝을 연결 | SIZ, CASE | 세그먼트 발견/도달 가능성과 차별 메시지 검증을 구별. 프레임만으로 수요 입증 불가 | A:1415 | P,U |
| M032: JTBD | 고객이 해결하려는 과업/상황과 대안 비교 | QL, CASE | 인용/관찰 기반으로 작업과 동기를 구별. 생성 이야기만으로 일자리 발견 주장 금지 | A:60 | U,H |
| M033: 페르소나 | 증거에 근거한 고객 차이와 활용 조건 요약 | SIZ, QL | 상상한 인구통계/성격 금지. 가설 페르소나와 관찰 자료 분리 | A:60,155,1639 | U,P |
| M034: 고객/구매 여정 지도 | 단계별 행동/접점/장애 연결 | QL, A, FUN | 실제 고객 로그/계정/시간 흐름 필요. 검색 경로를 전체 구매여정으로 단정 금지 | A:60,155,1436 | U,P |
| M035: TAM / SAM / SOM | 시장 경계와 접근 가능 범위/확보 가정을 분리 | SIZ | 기존 카드 명시. SOM=임의 점유율 금지, 제약/수용능력/채널을 계산으로 연결 | A:1416 | P,U,R |
| M036: CAGR | 동일 정의의 시작/종료값 사이 복리성장 비교 | SIZ, A | 기간/기준연도/통화/음수 또는 0값 조건과 계산 검증. 미래 지속성 보장 아님 | A:836 | P,U,R |
| M037: 시계열 분석 | 추세/계절성/시점 변화 분리 | T, A | 명명 모델별 정상성/구조변화/누출/예측 검증의 전용 절차 미확인 | A:43; B:308 | U,P,R |
| M038: 마케팅/브랜드/광고 테스트 | 인지/선호/이해/회상/감정과 자극 반응 비교 | CON, B, A | 노출/순서/문항/표본/비교기준 검증. 회상/호감은 실제 매출 효과가 아님 | A:66–71,293,1707–1710 | U,H,R |
| M039: 컨셉 테스트 / 아이디어/시제품 평가 | 이해/혜택/구매 의향/개선점의 사전 비교 | CON, B, A | 200–300명/5점중3점은 보편기준 아님. 실제 사용성/구매/유지는 별도 | A:291,1428,1708 | U,H |
| M040: NPS / 순추천지수 | 정의된 질문의 추천응답 구간을 요약 | SUR, A | 전용 산식/스케일/분모/결측/CI fixture 필요. 만족도/성장/수요 자동 대리 금지 | A:301,1620 | U,R |
| M041: CSAT / 고객만족도 | 정의된 경험과 시점에서 만족 반응 집계 | SUR, A | 척도/긍정구간/경험창/대상/분모 명시. 다른 척도와 직접 비교 금지 | A:288,301 | U,R |
| M042: Top2 Box | 지정 척도 상위 두 응답 비율을 일관 계산 | SUR, A | 구간/분모/분기 미노출/가중을 고정. 구매 의향 Top2는 구매 전환률 아님 | A:71 | U,R |
| M043: 군집화 / Clustering | 고객의 데이터상 유사 집단 후보 탐색 | SIZ, A | 기존 SEGMENTATION 계약 존재. 모델/척도/누락/안정성/새 데이터 검증 필요 | A:1007 | U,R |
| M044: 계층적 군집화 | 거리와 결합 방식에 따른 계층 비교 | SIZ, A | 전용 선택/진단 규칙 미확인. 거리/연결법/절단과 민감도 fixture 필요 | A:1008 | U,R |
| M045: K 평균 군집화 / K-means | 연속 변수의 중심 기반 그룹 후보 | SIZ, A | 스케일/거리 가정/초기값/K/seed/이상치/안정성 검증 필요 | A:1009 | U,R |
| M046: 자기 조직화 지도 / SOM | 복잡한 고객 패턴의 지도형 탐색 | SIZ, A | 전용 구현/진단 미확인. 이 SOM은 시장규모 SOM과 다른 방법 | A:1010 | U,R |
| M047: 판별 분석 | 정의된 집단을 구분하는 변수/분류 후보 | A, SIZ | 공분산/분포/표본 조건, 교차검증과 오분류 비용 검증 필요 | A:1011 | U,R |
| M048: 다차원 척도법 / MDS | 유사도/거리 구조의 저차원 시각화 | A, SIZ | 입력 거리, metric/nonmetric, stress 및 축 해석 제한 필요 | A:1012 | U,R |
| M049: t-SNE | 고차원 자료의 국소 구조 탐색 | A, SIZ | seed/perplexity 등 설정과 안정성 검증. 그림상 간격/군집=시장 자연유형 아님 | A:1013 | U,R |
| M050: ANOVA | 정의된 그룹 평균 차이 평가 | A | 모형/독립성/분산/분포/반복측정/사후비교와 효과구간 검증 필요 | A:1014 | U,R |
| M051: 회귀 분석 | 변수 관계/조건부 예측의 정량화 | A | 모형 종류/진단/누출/계층/외부검증 필요. 회귀계수=인과 아님 | A:268,1015; B:107–110 | U,R |
| M052: 잠재 계층 분석 / Latent Class | 응답 패턴의 잠재적 집단 후보 | SIZ, A | 중복 명칭 1개로 통합. 식별/해수/적합도/안정성 및 새 데이터 검증 필요 | A:1016,1025 | U,R |
| M053: 대응 분석 / Correspondence Analysis | 범주 교차표의 연관 구조 탐색 | A | 희소셀/질량/차원/좌표 해석과 재현 계산의 전용 절차 필요 | A:1017 | U,R |
| M054: 승산비 / Odds Ratio | 조건에 따른 odds 비교 | A | 분모/희귀성/표본설계/CI, 보정/비보정 구별. 위험비와 혼용 금지 | A:1018 | U,R |
| M055: 상대 위험도 / Risk Ratio | 정의된 집단의 사건 위험 비율 비교 | A | 위험 추정 가능한 설계인지 확인. odds ratio와 동일시 금지 | A:1019 | U,R |
| M056: 항목 분석 / Item Analysis | 문항 품질/응답 특성/척도 적합성 점검 | B, A | 측정모형/난이도/변별/신뢰도 등 목적별 지표를 명시. 원문은 세부모형 없음 | A:1020 | U,R |
| M057: 범주형 데이터 분석 | 범주 분포/관계 분석 | A | 희소셀/구조적0/표집/가중/반복단위에 맞는 검정/모형 필요 | A:1021 | U,R |
| M058: 텍스트 분석 | 자유응답/문서의 요약/분류/패턴 탐색 | A | 전처리/원문 보존/언어/단위/대표성/동의와 QA fixture 필요 | A:1022,1610 | U,R |
| M059: 요인 분석 | 관측 문항의 잠재적 구성개념 후보 | A | 기존 일반 분석 계약만 확인. EFA/CFA 구별, 척도 유형/식별/적합도 검증 필요 | A:1023 | U,R |
| M060: 구조 방정식 모형 / SEM | 측정모형과 구조관계의 명시적 검토 | A | 중복 1개. 식별/추정/표본/적합도/대안모형 필요. 화살표=인과 아님 | A:1024,1037 | U,R |
| M061: 잠재 의미 분석 / LSA | 문서-용어 구조의 잠재적 의미 차원 탐색 | A | 전처리/가중/차원/검증 및 해석 가능성 확인. 감정분석과 별도 | A:1026 | U,R |
| M062: 용어 선택 / Term Selection | 텍스트 모델의 설명/예측 변수 선택 | A | 선택 기준/훈련셋 내부 수행/중복/누출 방지와 안정성 필요 | A:1028 | U,R |
| M063: 텍스트 회귀 | 텍스트 특징과 결과의 조건부 관계 모델링 | A | 시간/문서/사용자 누출 방지, 과적합/정규화/외부검증 필요 | A:1029 | U,R |
| M064: 연관 규칙 / Association Rules | 동시 발생하는 행동/구매 조합 탐색 | A | support/confidence/lift 분모와 시간순서 검증. 연관규칙=인과 금지 | A:1030 | U,R |
| M065: 친화도 분석 / Affinity Analysis | 함께 나타나는 상품/선호의 관계 탐색 | A | 원문의 정확한 분석 정의 미제공. 연관 규칙과 구현이 같을 수 있으나 명명 항목은 별도 추적 | A:1031 | U,R |
| M066: 선택 / Choice 분석 | 대안 사이 선택 반응으로 trade-off 탐색 | PRICE, A | 원문은 '선택'만 제시. discrete-choice 여부/선택집합/추정모형 확인 | A:1033 | U,H,R |
| M067: 컨조인트 / Conjoint | 속성/가격 사이 진술된 상충관계 추정 | PRICE, A | 기존 카드 명시. 설계 효율/수준/상호작용/모형/holdout 검증. 실구매 입증 아님 | A:1034,289 | U,H,R |
| M068: 최대차이 / MaxDiff | 항목 상대 선호의 최상/최하 선택 추정 | PRICE, A | 전용 설계/추정/점수해석 카드 미확인. 단순 평균 순위와 구별 필요 | A:1035 | U,H,R |
| M069: Uplift | 처치로 달라지는 반응의 이질성 탐색 | EXP, A | 처치/대조 식별, 교차적합/검증 및 정책가치 평가 필요. 단순 반응 예측과 구별 | A:1036 | U,R |
| M070: 탐색적 요인 분석 / EFA | 잠재 구성개념 구조의 탐색 | A | 추출/회전/요인수/서열척도/독립 검증 조건 필요 | A:1038 | U,R |
| M071: 확증적 요인 분석 / CFA | 사전 측정모형의 데이터 적합성 평가 | A | 식별/적합도/수정지수/측정불변성 및 EFA 데이터 재사용 한계 필요 | A:1039 | U,R |
| M072: 경로 다이어그램 | 가정한 변수 관계를 명시적으로 시각화 | A, RENDER | 화살표는 결과나 인과 입증이 아님. 추정값/가정/관측 변수를 구별 | A:1040 | U,R |
| M073: 기술통계 (평균, 중앙값, 표준편차) | 자료의 위치와 변동성을 재현 가능하게 요약 | A | 척도/가중/결측/이상치/단위와 기준표 계산 fixture 필요 | A:1453; B:107–110 | U,R |
| M074: 가설 검정 / 통계적 유의성 | 우연 변동과 효과/불확실성을 분리해 비교 | A, EXP | 사전 가설/다중비교/효과구간/실질적 중요성 및 비확률표본 제한 | A:1453; D:9 | U,R |
| M075: 최선/기준/최악 시나리오 | 복수 가정과 반전 조건에서 결정의 취약점 점검 | SCEN, SIZ | 발생확률/실측 예측으로 포장 금지. 입력 근거/가정/미지수 분리 | B:318–323; D:125–130 | P,U,R |
| M076: 직접/간접/미래 경쟁자와 벤치마킹 | 현재 대안뿐 아니라 다른 해결법과 진입 가능자 비교 | DESK, CASE, Q | 미래 진입은 시나리오. 기능 빈칸=미충족 수요/기회로 자동 결론 금지 | B:222–227; A:1430 | P,U |
| M077: SEO / 검색 키워드 분석 | 검색 의도/언어/노출 경로와 변화 탐색 | T, KR, FACT | 검색건수=사람수, 문서수=경쟁수, 상위노출=수요 입증 금지 | B:42–60; A:736–747,1654 | P,L |
| M078: 문헌/학회/학술지/산업 보고서 조사 | 기존 전문지식과 방법/시장 맥락 재사용 | SRC, R | 원문 열람과 질문 적합성/버전/이해관계/재사용권 확인 | B:42–60,299; A:142 | P,L |
| M079: 가격/지불의향 조사 | 가격 민감도/가치 인식을 조건부로 비교 | PRICE, B, A | 실제 결제와 진술 WTP 분리. 보편적 가격 할인계수/최적가격 주장 금지 | A:289,67 | U,H,R |
| M080: 온라인/전화/대면 혼합 수집 | 디지털만으로 빠지는 사람/상황을 보완 | B, FIELD, A | 모드 차이/중복/질문/기간/접근성을 기록하고 무비판적 합산 금지 | A:1446,1451; B:72–81 | U,H,R |
| M081: 상관관계 분석 | 함께 변하는 요인과 추가 검증 가설 발굴 | A, CLAIM | 상관계수 종류/군집/범위/교란/다중비교 명시. 인과 주장 금지 | A:268,311 | U,R |
| M082: 데이터 마이닝 | 정형/비정형 자료의 탐색적 패턴 발견 | A, SIZ | 포괄명뿐임. 실제 알고리즘/목적/검증을 지정해야 실행 가능 | A:747 | U,R |
| M083: 종단 조사 / 반복 추적 / Tracker | 동일 정의의 시간 변화와 조사 반복 활용 | A, REFRESH, QL | 표본/문항/수집기/가중/정의 변경 시 방법단절 표시, 기준선과 파생 영향 검증 | D:9; A:237; B:331–332 | U,H,R |
| M084: 교차표 / Crosstabs | 하위집단별 응답 분포와 차이 비교 | A | 노출/자격/응답 분모, 가중/비가중, 희소셀, 다중비교와 효과구간 필요 | D:11 | U,R |
| M085: Driver 탐색 | 성과와 관련된 설명 변수의 후보 탐색 | A, CLAIM | 모형/교란/누출/검증을 명시. driver 명칭을 원인으로 번역하지 않기 | D:11 | U,R |

## 6. 별도 분류: 경쟁사로 세지 않은 이름과 주변부

아래 행을 삭제해 이름을 잃는 대신 문맥과 제외 이유를 보존한다. 저자 이름이나 사용사/통합 제품을 새 경쟁사 장점의 증거로 늘리지 않는다.

| ID / 이름 | 분류/문맥 | 원문 줄 | 제외 또는 제한 이유 |
|---|---|---|---|
| X001: CJ / 비비고 | example: 식품 성공사례의 대상 | A:726,775–776 | 실제 경쟁사/조사 제공자가 아님. 사례 원인의 검증은 E032에 연결 |
| X002: W컨셉 / W Concept | example: 시장진입 연습의 가상 화자/회사 | A:794–798 | 비교 도구가 아닌 예시 기업 |
| X003: 당근마켓 / 당근 | example: 중고 명품 시장진입 상황의 예시 | A:796 | 자료 제공자/경쟁 조사 제품으로 세지 않음 |
| X004: 번개장터 | example: 혁신의숲 검색의 예시 기업 | A:818–819 | 과거 매출 숫자만 제시된 사례, E038과 중복 계산 금지 |
| X005: PHYZZ | example: JMP 고객 추천사에 등장한 회사 | A:1005 | 방법론/제품 제공자 아님 |
| X006: John Cunningham | reference: JMP 추천사의 인물 | A:1004–1005 | 사람 이름을 경쟁사로 세지 않음 |
| X007: Nick Jain / 닉 제인 | reference: IdeaScale 글의 저자 | A:247 | 기관 E029와 별도 출처 독립성을 만들어내지 않음 |
| X008: 장윤진 | reference: ListeningMind 글의 저자 | A:1392 | 제공자 E028에 귀속 |
| X009: 쪼렙 서비스 기획자 | reference: Publy 글의 필명 저자 | A:786–787 | 제공자/문헌 E007에 귀속 |
| X010: 하상도 | reference: 비비고 사례 칼럼 저자 | A:775 | 기사 E032에 귀속, 실제 전문가 자문을 받은 것 아님 |
| X011: UK-ONS | reference: 미상 저자의 경력 표기 | A:1442 | 기관 공식 자료를 제공한 것 아님. E064를 ONS 지침으로 격상 금지 |
| X012: Mettelo | reference: 미상 저자의 소속/활동 표기 | A:1442 | 시장조사 제품 기능이 설명되지 않음 |
| X013: Google 앱 (제품 미지정) | reference: Insight7 통합 대상 | A:1634 | Google Trends/Forms/Analytics/리뷰와 별도 경쟁사 수로 더하지 않음 |
| X014: Microsoft 앱 (제품 미지정) | reference: Insight7 통합 대상 | A:1634 | 실제 연결 권한/지원 제품 검증 필요, 조사 제공자로 세지 않음 |
| X015: Salesforce | reference: Pecan의 CRM 통합 대상 | A:1659 | 사용자 내부 데이터/권한 의존성, 독립 시장자료/경쟁사 아님 |
| X016: Amazon S3 | reference: Pecan의 저장소 통합 대상 | A:1659 | 데이터 접근/클라우드 권한 의존성, 조사 방법의 독립 장점 아님 |
| X017: Oracle 기술 제품 (제품 미지정) | reference: Pecan 통합 대상으로 서술 | A:1659 | 구체 제품/드라이버/권한 미상, 제공 기능 추정 금지 |
| X018: SPSS | reference: Ipsos 결과의 분석 파일/출력 형식으로 등장 | A:1724 | SPSS 분석 기능 비교를 제공한 것이 아님. 실제 형식 내보내기는 별도 검증 |
| X019: Excel / 엑셀 | reference: 원자료/결과 반환 형식 및 관련글 | A:696,1365,1724,966 | 스프레드시트 내보내기 지원은 실제 파일로 검사, 별도 경쟁사 아님 |
| X020: PowerPoint / PPT | reference: 보고서 반환/프레젠테이션 형식 | A:970,1724 | 템플릿/관련글은 제품 비교 근거 아님. 실제 출력 검증 별도 |
| X021: Event-us 행사 링크 | reference: [월간BD] 마케팅 전략 행사 홍보 | B:358–359; https://event-us.kr/m/89523/20591 | 연구방법 원문이 아닌 후행 홍보 링크, 자동 탐색 범위에서 제외 |
| X022: Kakao OpenChat 초대 링크 | reference: 사업개발 커뮤니티 초대 | B:362; https://open.kakao.com/o/gZvwBppg | 비공개 집단 가입/수집을 허가한 것이 아님, 카카오 트렌드의 증거 아님 |
| X023: grit-bd.community | reference: 사업개발 커뮤니티 홍보 | B:364; https://www.grit-bd.community | 본문의 조사 도구/방법 제공자로 설명되지 않음 |
| X024: IBK직장인적금 및 블로그 관련글 묶음 | reference: 예금상품, Excel, 이직, PPT, 발상법, IT 커뮤니티, 모바일 자료 목록의 관련 링크 | A:963–976 | 방법론 본문과 별개 웹페이지 주변부. 모든 링크 재귀 추적 범위에 넣지 않음 |
| X025: Google Ads/추적 UTM 파라미터 | reference: 유입 경로 식별 파라미터 | A:2–4,12,1440 | 독립 경쟁사/추천 자료원이 아님. 원문 링크는 보존하되 표시에서는 추적값 제거 |
| X026: 브랜드 없는 스마트스피커/음료/스마트폰/러닝화 예시 | example: 방법을 설명하기 위한 가상 예시 | B:124–132,203–208,334–340; A:1593 | 가상 1,000명 응답/70% 등 숫자를 실제 관측값으로 취급 금지 |
| X027: Michael Porter / 마이클 포터 | reference: 5 Forces 프레임워크의 제안자 | B:250 | 별도 경쟁사가 아닌 방법론 저자, M026에 연결 |
| X028: Ipsos 2018 리서치페어 관련 항목 | reference: 같은 행사의 영어/한국어 중복 소개 | A:1735–1742 | 새 제공자/새 방법론으로 세지 않음 |

## 7. 기준 패키지의 실제 위치 약칭

모든 경로는 기준 패키지 루트에 상대적이다. 이 목록은 일반 지침 연결을 보여줄 뿐, 101개 대상의 실제 통합을 입증하지 않는다.

| 약칭 | 실제 상대경로 |
|---|---|
| Q | `references/modules/RESEARCH_QUESTION_COVERAGE_MAP.md` |
| B | `references/modules/PRIMARY_RESEARCH_PLATFORM_BRIDGE.md` |
| A | `references/modules/RESEARCH_ANALYSIS_COMPILER.md` |
| CAT | `references/data/MARKET_RESEARCH_CAPABILITY_CATALOG.md` |
| R | `references/modules/REFERENCE_FIRST_VALUE.md` |
| SRC | `references/modules/SOURCE_DISCOVERY_AND_SELECTION.md` |
| FREE | `references/modules/ZERO_COST_LIVE_SOURCE_LADDER.md` |
| ACCESS | `references/modules/AGENT_REACH_ACCESS.md` |
| FACT | `references/modules/PLATFORM_FACTS_AND_DATA_ACCESS.md` |
| KR | `references/modules/KOREA_LOCAL_DISTRIBUTION.md` |
| T | `references/modules/LIVE_TREND_AND_FRESHNESS_RADAR.md` |
| REFRESH | `references/modules/RESEARCH_REFRESH_AND_CHANGE_IMPACT.md` |
| PROV | `references/modules/CLIENT_VISIBLE_EVIDENCE_PROVENANCE.md` |
| BROKER | `references/modules/BROKER_RESEARCH_DELIVERY.md` |
| QUAL | `references/modules/QUALIFIED_METHOD_EXECUTION.md` |
| DEC | `references/modules/EVIDENCE_GROUNDED_DECISION_COUNCIL.md` |
| SCEN | `references/modules/SCENARIO_STRESS_TEST.md` |
| CONT | `references/modules/DECISION_CONTINUITY.md` |
| REPORT | `references/modules/PREMIUM_FINAL_REPORT_STANDARD.md` |
| RENDER | `references/modules/RENDERING_CONTRACT.md` |
| DEL | `references/modules/COMMERCIAL_DELIVERABLE_SYSTEM.md` |
| CASE | `references/modules/MARKET_CASE_COMPARISON_AND_GAP.md` |
| REG | `references/modules/REGULATORY_CONTEXT_CHECK.md` |
| FUN | `references/modules/DEMAND_DISTRIBUTION_DIAGNOSTICS.md` |
| SIG | `references/modules/PRODUCT_READINESS_AND_SIGNAL_INTEGRITY.md` |
| SIZ | `references/methods/sizing-and-segmentation.md` |
| PRICE | `references/methods/pricing-and-transactions.md` |
| SUR | `references/methods/surveys.md` |
| QL | `references/methods/qualitative.md` |
| EXP | `references/methods/experiments.md` |
| CON | `references/methods/concept-usability-behavior.md` |
| DESK | `references/methods/secondary-and-competitors.md` |
| FIELD | `references/core/SAMPLE_AND_FIELDWORK.md` |
| CLAIM | `references/core/CLAIM_GRAMMAR.md` |
| METHOD | `references/core/METHOD_ROUTER.md` |
| ETH | `references/modules/RESEARCH_ETHICS_DESIGN_SCAFFOLDING.md` |
| AUDIT | `references/development/COMPETITIVE_PATTERN_AUDIT_2026-09-28.md` |

## 8. 구현 담당자가 우선 닫을 검증 간극

1. **명단 완전성**: 이 표의 E/C/M/X 전체 ID와 장점 하위 ID가 후보 패키지의 채택 매핑에 빠짐없이 대응해야 한다. 상태는 ADOPTED_RULE, IMPLEMENTED_TOOL, BROKERED_EXTERNAL, NOT_APPLICABLE_WITH_REASON, NEEDS_VERIFICATION처럼 구별한다. 무조건 채택/완료로 덮지 않는다.
2. **링크만 있는 후보**: E002–E006, E008–E009, E011, E017, E033–E034, E060–E061, E063, E072–E073, E101은 현재 알려진 내용보다 강하게 기술하지 않는다. 잘못된 상품/기관/동명 서비스 연결이 없는지 확인한다. 외부 읽기가 필요한 경우 그 다음 작업에 실제 원문 범위와 날짜를 기록한다.
3. **기준 데이터가 있는 계산**: 분기 미노출/결측/중복/중첩 응답/가중/희소셀/다중비교가 들어간 자료에서 NPS, CSAT, Top2, 교차표, 회귀/ANOVA 등을 검증한다. 숫자 일치와 해석의 상한을 둘 다 검사한다. 방법 이름 검색 PASS와 계산 PASS를 구별한다.
4. **고급 방법 분기**: 계층군집/K-means/SOM/MDS/t-SNE/LCA/SEM/EFA/CFA/MaxDiff/Uplift를 하나의 '고급통계 지원' 상태로 합치지 않는다. 각 방법별 데이터 요건, 추정/진단 도구, 선택 이유, 실패/보류 조건 및 재현 fixture가 필요하다.
5. **프레임워크 실행**: SWOT/PESTEL/7Ps/BMC/3C/STP/BCG/5 Forces의 이름만 대답하지 않고 실제 해당 칸의 근거, 가정, UNKNOWN, 관련없는 항목의 이유, 결정에 바뀌는 점을 확인한다. 수치가 없으면 점수/매트릭스를 꾸며내지 않는다.
6. **고유 자원 경계**: SurveyMonkey/Qualtrics/Ipsos/Prolific/Pollfish/국내 조사사의 패널, ListeningMind/Similarweb/Brandwatch/GWI의 고유 데이터, Mixpanel/Amplitude/GA의 고객 계측은 외부 연결 또는 실제 자료가 있어야 한다. 사용권/동의 없는 수집이나 유료 발주는 자동 실행하지 않는다.
7. **행동 분석 연결**: E004–E006에 대응하는 이벤트 사전, 중복/시간대/사용자 식별, 코호트 분모와 리텐션 창, 퍼널 노출/순서, 데이터 내보내기/측정 이상을 검증한다. 현행 제품 기능은 원문 URL 하나에서 추론하지 않는다.
8. **멀티에이전트/하네스**: E091–E100의 하위 장점마다 독립 분업 필요조건, 작업별 원문/결과 영수증, 컨텍스트 인계, 실패 회수, 공유 원천 중복, 교차검토 및 최종 합성 책임을 확인한다. 역할 이름을 늘린 결과를 독립 근거로 세지 않는다. 한 모델/한 세션 PASS는 호스트/모델 전체 호환성 증거가 아니다.
9. **추적과 영구 게시**: Crayon식 무인 상시감시는 현재 REFRESH의 사용자 요청 갱신과 다르다. A:6의 공개적/영구적 인터랙티브 웹페이지 요구는 자료 속 요구문이며, 현재 작업에서 게시 권한이나 호스팅 보장을 부여하지 않는다. 로컬 HTML/PDF 생성, 실제 인터랙션, 외부 배포/권한/지속성은 별도 항목이다.
10. **모호한 출처**: E064 작성자 미상 글과 E065 75개국 조사 서비스는 기관명을 새로 지어 붙이지 않는다. E101 도서의 저자/판본도 미상으로 유지한다. B의 두 FasterCapital 링크는 본문 문장별 원출처 대응이 미확정이다.

## 9. 그대로 이식하면 안 되는 원문 주장

- 2015년 IBK 자료원 목록의 도메인/기관명/무료 여부는 현재 상태를 보장하지 않는다.
- A:812의 2021년 시장 규모, A:819의 예시 기업 매출, A:1636–1663의 도구별 요금/환율은 현재값이 아니다. Semrush 제품군/플랜 혼합 여부도 별도 확인한다.
- 검색량을 고유 사람 수/시장 전체 크기로, 문서 수를 실제 경쟁자 수로 바꾸면 안 된다. A:736–747,767 및 1435의 검색 데이터 정확도/무편향 홍보는 원천 방법 검증이 필요하다.
- FGI 6–8명 또는 6–10명, 컨셉 조사 200–300명, 구매의향 평균 3/5는 보편적 연구 기준이 아니다.
- 샘플이 크다거나 수치가 있다는 사실은 대표성/인과/객관성을 보장하지 않는다. 익명/AI 생성/자발응답을 실제 관찰 참가자 데이터로 보충하지 않는다.
- Ipsos의 72시간, 셋업 1시간, 43개국, 60% 비용절감, 부정응답 원천차단은 원문 시점과 조건의 제품 주장이다. FieldPilot의 속도/국가 커버리지/절감률로 복사할 수 없다.
- 리뷰/보고서 출처를 적었다는 이유만으로 전문 복제/공개 재배포 권한이 생기지 않는다. 공개 페이지와 라이선스/개인정보 동의는 별개다.
- 가상 사례의 설문 숫자, 추천사, 한 번의 성공사례, 시뮬레이션 반응은 실제 시장 검증 또는 확정 수익 증거가 아니다.
- 이식 대상은 검증 가능한 방법과 통제 절차다. 독점 데이터/네트워크/인프라 자체, 경쟁사 성과, 모델 자동 전환이나 스스로 영구 진화하는 기능은 이 인벤토리에서 구현됐다고 인정하지 않는다.

## 10. 기계 대조 계약과 저장 상태

각 행의 ID, 이름, 분류, 출처, 장점, 기준 경로, 간극, 외부조건을 독립 범위 마스터로 유지한다. E 행의 하위 장점 ID도 보존하여 후속 채택/시험 결과를 연결한다. 방법 행과 보조 후보 행의 단일 장점 ID는 해당 M/C ID 뒤에 `.a`를 붙인 값이다. 원문 범위에 없는 C 행은 supplied=false이며 X 행은 제외 문맥이다. 후보의 누락이 발견되어도 마스터 항목을 지우거나 이름을 바꾸어 PASS를 만들지 않는다.

동일 구조 JSON 초안은 구성했으나 추가 파일 생성이 최초 MD 전용 편집 범위를 넘는다는 자동 검토 거부로 저장하지 않았다. 이 문서만 저장하며 JSON은 명시적인 사용자 추가 허용 확인 전 보류한다. 문법/ID/경로 검사는 원문 의미의 완전성이나 경쟁사 수준 성능을 자동 증명하지 않는다.

## 11. 별도 전달된 추가 확인 메모

메인 에이전트가 2026-09-28 `https://kmong.com/gig/367992`를 직접 읽고 아이로즈 판매자와 대표 김완진, 온라인/오프라인 조사, 설문/FGI/개별인터뷰/리포트/점검/수정보완의 서비스 광고를 확인했다고 전달했다. 이는 본 에이전트가 새로 독립 열람한 증거가 아니며 E030의 초기 첨부 기반 상태를 바꾸지 않는다. 실제 효과/패널 권한/독립성 검증도 아니다. 또한 메인의 Dola 페이지 접근 시 본문 추출이 없었으며, 별개 heydola 달력 제품과 동일시하지 않는다는 확인을 전달받았다. 이들 후속 확인은 별도 접근 영수증과 함께 검증 상태를 갱신할 때 사용한다.
