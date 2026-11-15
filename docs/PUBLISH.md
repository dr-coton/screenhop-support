# 게시 절차 (사용자 승인 후에만)

## 먼저 정할 것
1. 지원 이메일 → `site.json`의 `contactEmail`
2. 시행일(출시일) → `effectiveDate` (ko/en)
3. 게시 승인 (GitHub 저장소 공개, Pages 켜기)

## 값 반영·점검
```sh
cd /Users/coton-home/AI-Workspace/10_Projects/05_GitHub/dr-coton/screenhop-support
# site.json 수정 후
python3 -I tools/build.py
python3 -I tools/check_links.py
grep -rn "확정 필요\|To be confirmed" --include=*.html .   # 아무것도 나오면 안 됨
git add -A && git commit -m "Set contact email and effective date"
```

## 게시 (다른 지원 사이트와 같은 방식: GitHub Pages, 주소 dr-coton.com/<저장소>/)
`gh` CLI는 이 Mac에 없음 → GitHub 웹에서 만들거나 gh를 설치해 쓴다.
1. GitHub에서 `dr-coton/screenhop-support` 빈 저장소 만들기(공개, README 추가 안 함)
2. ```sh
   git remote add origin https://github.com/dr-coton/screenhop-support.git
   git push -u origin main
   ```
3. 저장소 Settings › Pages › Source: `main` / `(root)` 저장. `dr-coton.github.io` 저장소의 `CNAME`이 dr-coton.com이라 주소는 자동으로 `https://dr-coton.com/screenhop-support/`
4. 1~2분 뒤 확인(200이어야 함): `/`, `/privacy.html`, `/download.html`, `/en/`, `/en/privacy.html`, `/en/download.html`
   ```sh
   for p in "" privacy.html download.html en/ en/privacy.html en/download.html; do curl -s -o /dev/null -w "%{http_code} $p\n" https://dr-coton.com/screenhop-support/$p; done
   ```
5. App Store Connect의 개인정보 처리방침·지원 URL이 위 주소와 같은지 확인

## 나중에 (DMG 준비 후)
`site.json`의 `host`(`dmgUrl`, `version`, `dmgSha256`, `size`, `date`) 채우기 → build → 커밋·push. DMG 파일 자체를 둘 위치(GitHub Release 또는 apps-hub)는 사용자가 결정.
