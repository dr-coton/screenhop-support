# apps.dr-coton.com 에 ScreenHop 추가하기

조사 결과(apps-hub 저장소 README·AGENTS.md·`src/lib/{seed,store,admin-actions}.ts` 기준):

- 운영 데이터는 S3 `db/state.json` 하나. 앱 목록은 여기 들어 있고, `seed.ts`의 기본 앱은 **운영 DB에 없을 때 읽을 때마다 자동으로 합쳐진다**(`store.ts normalize`, 있는 앱은 안 건드림).
- 관리 화면 `/admin`(Google 로그인, dr.coton@gmail.com) › 앱 추가로도 만들 수 있다. 다만 기존 화면에는 **내려받기 버튼·"곧 제공" 상태가 없어서** Mac 도우미 안내를 넣으려면 코드 변경이 필요했다.

## 한 일 (로컬, push·배포 안 함)
apps-hub 브랜치 `feat/screenhop-app` (커밋 `4290b51`, 기준 `main` 6c7a625):
- `seed.ts`: `screenhop` 앱(이름·한 줄 소개·아이콘 `public/icons/screenhop.png`·순서 4). App Store 주소는 비워 둠(출시 전)
- `types.ts`·`page.tsx`·`i18n.ts`: 앱에 선택 항목 `download` 추가, `한눈에` 화면에 "Mac 도우미 ScreenHop Host" 카드 표시. 파일 주소가 비면 **"곧 제공됩니다"** + 설치 안내 링크(`https://dr-coton.com/screenhop-support/download.html`)
- `admin-actions.ts`·`AppForm.tsx`: 관리 화면 앱 정보 탭에서 내려받기 주소(https만)·버전·SHA-256(64자리 16진수)·안내 주소를 나중에 코드 없이 입력. (저장 시 `download`가 지워지지 않도록 처리)
- 확인: `npm run check` 통과, `STORE_DRIVER=file` dev 서버에서 `/ko/screenhop`·`/en/screenhop` HTML에 카드·"곧 제공됩니다/Coming soon"·설치 안내·아이콘 확인. **브라우저 시각 확인은 못 함(Aside 미연결)** — 배포 전에 Aside로 한 번 볼 것.

## 게시 단계 (사용자 승인 후)
1. 브랜치 확인: `cd .../apps-hub && git log main..feat/screenhop-app && git diff main...feat/screenhop-app`
2. `main`에 병합 후 push (GitHub `dr-coton/apps-hub`, 비공개): `git switch main && git merge --ff-only feat/screenhop-app && git push`
3. 배포: `source /Users/coton-home/AI-Workspace/99_System/env.sh && npx vercel deploy --prod --yes --scope extra-bold` (프로젝트 `apps-hub`)
4. 확인: https://apps.dr-coton.com/ko/screenhop , `/en/screenhop` 200, "곧 제공됩니다" 카드, 아이콘. 목록 `/ko`에 ScreenHop 표시. (JSON API 5분 캐시)
5. (선택) 운영 DB에 확정 저장: 관리 화면 › ScreenHop › 앱 정보 저장 한 번. 안 해도 seed에서 자동 표시됨.

## DMG가 준비되면 (코드 변경 없음)
`/admin` › ScreenHop › 앱 정보 › 내려받기: 파일 주소(https, DMG 호스팅 위치는 사용자가 결정), 버전(예 1.0.0), SHA-256(`ScreenHop-Host-<버전>.dmg.sha256` 값), 저장 → 버튼으로 바뀜. 출시 후 같은 화면에서 App Store 주소 입력.
그 밖에 앱 소식 탭(`updates`)에 Mac 도우미 릴리스 노트를 올릴 수 있음(공개 문구는 사용자가 정한 내용만).

## 이 페이지가 가리키는 주소 (앱·스토어 문서와 일치 여부)
- 앱·listing: `https://apps.dr-coton.com/ko/screenhop`, `/en/screenhop` ✔ (앱 id `screenhop`)
- 지원: `https://dr-coton.com/screenhop-support/` ✔
- 개인정보: `https://dr-coton.com/screenhop-support/privacy.html` ✔
- ⚠ apps-hub 사이트의 개인정보 처리방침(`/{lang}/privacy`)은 앱 소식 사이트용이라 별개. ScreenHop 앱 처리방침은 위 지원 사이트 것.
