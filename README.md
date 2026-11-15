# ScreenHop 지원·개인정보·Mac 도우미 안내 (정적 사이트)

ScreenHop(iPad용 Mac 원격 화면 + SSH) v1.0의 공개 페이지. GitHub Pages로 `https://dr-coton.com/screenhop-support/` 에 게시한다 (다른 앱 지원 사이트와 같은 방식).

| 페이지 | 한국어 | English |
| --- | --- | --- |
| 지원·FAQ | `index.html` | `en/index.html` |
| Mac 도우미 받기·설치 안내 | `download.html` | `en/download.html` |
| 개인정보 처리방침 | `privacy.html` | `en/privacy.html` |

**상태: 로컬 완성, 게시 안 됨(원격 없음).** 문의 이메일·시행일은 자리표시(`[확정 필요 …]`).

## 고치는 법
- 이메일·시행일·DMG 주소·App Store 주소·버전·SHA-256: `site.json` 한 곳. 바꾼 뒤 `python3 -I tools/build.py`
- 문구: `tools/build.py`의 한/영 본문. 만든 HTML을 직접 고치지 않는다(다시 만들면 사라짐)
- 스타일: `style.css`
- 링크 검사: `python3 -I tools/check_links.py` (깨진 링크·없는 앵커)
- 로컬 보기: `python3 -I -m http.server 8765 --bind 127.0.0.1` → http://127.0.0.1:8765/

## 내용의 출처
개인정보 처리방침: ScreenHop 저장소 `docs/store/privacy-policy.md` v1.0판(수집 없음)을 그대로 옮기고 영어로 옮김. Mac 도우미 안내: `docs/DISTRIBUTION.md` 4절. 앱·Mac 화면 문구는 실제 String Catalog의 한국어를 따름. 방침을 바꿀 때는 앱 저장소 쪽 원문과 같이 고친다.

## 게시 (사용자 승인 후)
`docs/PUBLISH.md`, apps.dr-coton.com 반영은 `docs/APPS_HUB.md`.
