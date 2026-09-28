# 설치 안내

FieldPilot은 AI 모델이 아닙니다. 사용하는 AI에 조사 지침과 참고 자료, 보조 도구를 추가하는 스킬입니다. AI 구독이나 웹 검색 서비스를 포함하지 않습니다.

## 가장 간단한 방법

1. 저장소에서 Code → Download ZIP으로 내려받아 압축을 풉니다.
2. `skills/fieldpilot` 폴더 전체를 복사합니다.
3. 아래 위치 중 사용하는 AI에 맞는 곳에 넣고 새 세션을 엽니다.

| 환경 | 한 프로젝트에서 사용 | 모든 프로젝트에서 사용 |
|---|---|---|
| Claude Code | 프로젝트의 `.claude/skills/fieldpilot/` | 사용자 폴더의 `.claude/skills/fieldpilot/` |
| Codex | 프로젝트의 `.agents/skills/fieldpilot/` | 사용자 폴더의 `.agents/skills/fieldpilot/` |

사용자 폴더는 Windows의 `C:\Users\사용자이름`, macOS/Linux의 `~`입니다. 이미 같은 이름의 스킬이 있으면 먼저 다른 곳에 백업하세요. 기존 버전 위에 일부 파일만 덮어쓰지 마세요.

Claude Code에서는 `/fieldpilot`, Codex CLI/IDE에서는 `$fieldpilot`으로 호출합니다. Codex 인터페이스에 따라 스킬 선택 메뉴로 고를 수도 있습니다. 이 저장소에서는 실제 새 호스트의 로그인부터 보고서 납품까지 모든 조합을 검증하지는 않았습니다.

## Git으로 받아 프로젝트에 복사

Git이 설치되어 있다면 원하는 프로젝트 위치에서 실행하세요. 아래 명령은 기존 설치가 있으면 덮어쓰지 않고 멈추도록 구성했습니다.

### Windows PowerShell, Claude Code

```powershell
git clone https://github.com/gimhyuna0221-art/fieldpilot.git fieldpilot-source
if ($LASTEXITCODE -ne 0) { throw '다운로드에 실패했습니다.' }
if (Test-Path -LiteralPath '.claude/skills/fieldpilot') { throw '기존 FieldPilot을 먼저 백업해 주세요.' }
New-Item -ItemType Directory -Force -Path '.claude/skills' | Out-Null
Copy-Item -LiteralPath 'fieldpilot-source/skills/fieldpilot' -Destination '.claude/skills/fieldpilot' -Recurse
```

### macOS/Linux, Claude Code

```sh
git clone https://github.com/gimhyuna0221-art/fieldpilot.git fieldpilot-source && \
test ! -e .claude/skills/fieldpilot && \
mkdir -p .claude/skills && \
cp -R fieldpilot-source/skills/fieldpilot .claude/skills/fieldpilot
```

Codex는 위 명령의 `.claude/skills`를 `.agents/skills`로 바꿉니다. 내려받은 저장소 폴더 이름인 `fieldpilot-source`가 이미 있다면 먼저 다른 이름을 정하세요.

## 어떤 도구가 필요한가

- 최신 외부 자료 조사: AI 호스트의 웹 검색과 페이지 읽기 기능
- 사용자가 준 문서 분석: 해당 파일을 읽을 수 있는 호스트 기능과 권한
- 포함된 계산 및 보고서 도구: Python 3.10 이상 구문 지원
- PDF: 호스트에서 실행 가능한 Chromium 계열 로컬 브라우저. 선택적으로 `pypdf`를 이용한 추가 검사

Python 보조 도구는 표준 라이브러리로 실행합니다. 별도 유료 데이터 계정이나 API 키가 자동으로 생기지는 않습니다. 도구 실행에 필요한 권한은 사용하는 AI의 승인 절차를 따릅니다.

## HTML 보고서 출력

이미 생성된 Markdown 보고서는 다음처럼 HTML로 변환할 수 있습니다. 이 명령이 시장조사 내용을 새로 생성하거나 사실을 검증하는 것은 아닙니다.

```sh
python .claude/skills/fieldpilot/tools/render_report.py --help
python .claude/skills/fieldpilot/tools/render_report.py --input REPORT.md --outdir report-output --no-pdf
```

실제 지원 인수는 `--help`를 기준으로 확인하세요. PDF가 필요한 경우 로컬 브라우저와 납품 파일을 별도로 확인해야 합니다. 브라우저 보안 기능을 끄는 방식으로 실행하지 마세요.

## 공식 설치 문서

- [Claude Code 스킬](https://code.claude.com/docs/en/skills)
- [Codex 스킬](https://learn.chatgpt.com/docs/build-skills)
