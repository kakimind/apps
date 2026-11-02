# Changelog

이 저장소(kakimind-apps 허브 페이지)의 변경 기록. 최신 항목이 위에 오도록 추가.

## 2026-11-01
- **연화사(온라인 사찰 앱) 소개 페이지 + 개인정보처리방침 신설.** 다른 앱들과 달리 **별도 사이트 저장소를 만들지 않고 허브 저장소(`kakimind.github.io`) 안의 `yeonhwasa/` 하위 폴더에 두었다** — 앱 저장소 `yunhwasa`가 비공개라 거기서 Pages를 켤 수 없고, 저장소 하나 + Pages 설정을 새로 만드는 대신 이미 서빙 중인 호스트에 폴더만 더하면 끝나기 때문. 주소는 다른 앱과 같은 모양(`/yeonhwasa/`, `/yeonhwasa/privacy.html`)이다.
- 허브에 §09로 추가. 스팟 컬러는 단청 녹색 `#2a7d5f`(아이콘의 짙은 녹색 바탕에서 가져옴), `#f09`의 `grid-column` 쌍도 같이 넣었다. 목차·사이트맵·`9 FEATURES INSIDE`·메타 설명의 "8종"까지 전부 맞췄다 (`6 FEATURES INSIDE`로 한참 틀려 있던 것도 같이 고침).
- **스크린샷이 아직 없다.** placeholder 금지 규칙에 따라 FIG. 01은 실제 앱 아이콘(금빛 연꽃, `yunhwasa/assets/icon-only.png` → 512/256으로 축소)만 쓰고, 나머지는 수치 블록(염주 108 · 법문 365 · 방석 100 · 등급 6)과 참배 등급 사다리로 채웠다.
- 개인정보처리방침은 앱 저장소의 `docs/데이터-보안-양식.md`(코드에서 확인된 사실만 적힌 문서)를 그대로 근거로 썼다. 핵심 두 가지를 명시 — **서버가 아무것도 보관하지 않는다**(연등이 WebSocket 세션에 매달려 있어 접속이 끊기면 사라짐), **연등은 기본이 비공개이고 공개로 고른 것만 서버로 나간다**. 현재 빌드가 구글 테스트 광고 단위를 쓴다는 것도 적어 뒀다.
- **개발자 프로필 에셋을 9개 기준으로 다시 뽑았다.** `SPOTS`에 `("09", (42,125,95))` 한 줄을 더하고 스크립트를 돌린 것이 전부다 — 레지스터 바가 아홉 개가 되고 헤더 문구도 "NINE TITLES INSIDE"로 알아서 바뀌었다. 10-30에 개수를 리스트에서 끌어오게 고쳐 둔 것이 의도대로 작동했다.
- 앱 저장소(`yunhwasa`)의 `docs/할일.md`·`docs/작업기록.md`에도 주소와 "허브 저장소 하위 폴더"라는 사실을 적어 뒀다 (`b262205`). 그 저장소에서 사이트 파일을 찾다 헤매지 않도록.
- `app-ads.txt`는 손대지 않았다. 호스트 루트(`kakimind.github.io/app-ads.txt`)에 실제 게시자 ID가 이미 올라가 있어, Play 등록정보의 웹사이트를 `https://kakimind.github.io/`로 적으면 연화사도 그대로 인증된다 (앱 저장소 `docs/app-ads/app-ads.txt`는 게시자 ID가 `0000...`인 안내용 사본이라 올릴 필요 없음).

## 2026-10-30
- **커밋 안 된 채 남아 있던 두 가지 정리.** `.idea/`는 `.gitignore`로 제외하고 (`413252c`), `play-developer-profile/`은 커밋했다 (`167569b`). 후자는 Play 개발자 프로필용 아이콘 512 + 헤더 4096×2304와 그걸 그리는 스크립트로, 2026-10-22에 만든 뒤 8일간 untracked 상태였다. 무슨 폴더인지 알 수 없던 것이라 CLAUDE.md에 설명을 붙였다.
- **개발자 프로필 에셋을 8개 앱 기준으로 다시 뽑았다** (`04fb45b`). 레지스터 바가 여섯 개뿐이었다 — Top of Gravity와 Bubble Rumble이 스크립트를 쓴 뒤에 들어와서, 아이콘과 헤더가 정작 대표하는 허브보다 두 개 적었다.
- 같은 일이 또 생기지 않게 개수를 두 군데 적지 않도록 고쳤다. `SPOTS`에 두 줄을 더하고, 헤더의 "EIGHT TITLES INSIDE" 숫자는 리스트 길이에서 끌어오게 했다 — 다음 앱은 한 줄 수정으로 끝난다.
- 폰트 5종(Big Shoulders Display, Source Serif 4 Roman/Italic, Space Mono Regular/Bold)이 이 머신에 아예 없어서 Google Fonts에서 받았다. OFL이고 합계 2.4MB라 저장소에는 넣지 않고 `.gitignore` 처리했으며, 받는 명령과 재생성 절차를 `play-developer-profile/README.md`에 적어 뒀다. **스크립트가 없는 `fonts/`에서 조용히 죽는 게 이 에셋이 8일간 낡은 줄도 모르고 방치된 이유였다.**
- **Bubble Rumble 랜딩 페이지에 실제 플레이 스크린샷 Gallery 추가** (`bubble-rumble-site` `5741bcc`). 아침까지 FIG.가 전부 캐릭터 아트였던 건, 돌아가는 게임을 찍은 이미지가 아예 없었기 때문이다. Pixel 6 에뮬레이터에 release APK를 올리고 한국어로 직접 한 판 플레이하며 9장을 캡처해 해소했다.
- 고른 6장: 로비 / 방 만들기(모드·맵 선택) / 아레나 4인 교전 / 갇힘·버프가 떠 있는 플레이 순간 / 버블 상점 / 클로이 스킨 옷장. FIG. 02~07로 넣고 버디 로스터는 FIG. 08~15로 밀었다.
- **이 게임은 가로 모드(2400×1080)라** 세로 스크린샷을 쓰는 다른 앱 페이지와 그리드가 달라야 했다 — Gallery를 3열이 아닌 2열로 두고, 웹 사본은 1280×576 webp(6장 합계 248KB)로 만들었다.
- 스토어 원본 9장은 `C:\src\Bubble Rumble\store\screenshots\한국어\`에 보존. Play 스토어 리스팅에 필요한 스크린샷이 그동안 없었는데 이걸로 채울 수 있다.
- 캡처 중 확인한 것: 봇은 빈 자리를 탭해서 넣는 게 아니라 방을 만들고 `준비 완료`를 누르면 알아서 들어찬다 (`_EmptySeat`의 "host can tap it to drop an AI bot" 주석은 더 이상 맞지 않는다). 리워드 광고는 버튼으로만 뜨므로 Orbit Hop 때처럼 "Test Ad" 배너가 캡처에 끼는 문제는 없었다.
- **`bubble-rumble-site` 배포 완료 — 전날 남아 있던 유일한 블로커 해소.** 원격 저장소가 없어 푸시하지 못했던 건을, Chrome 자동화로 github.com/new에서 Public 저장소(초기화 항목 전부 해제)를 만들어 해결. 로컬 `d09d897`을 `git push -u origin main`으로 올리고, Settings → Pages → Deploy from a branch → `main` / `(root)` 저장.
- 배포 확인: `https://kakimind.github.io/bubble-rumble-site/`(랜딩)와 `/privacy.html`(개인정보처리방침) 둘 다 정상 렌더링. 허브 §08의 `계속 읽기 →`가 가리키던 404도 같이 해소됐다.
- 이전 세션에서 막혔던 원인은 `gh` CLI 미설치/토큰 차단이 아니라 **Chrome 확장이 계정에 연결돼 있지 않았던 것**(`list_connected_browsers` → `[]`). 연결된 상태에서는 GitHub 웹 작업을 브라우저로 그대로 처리할 수 있다.
- 남은 일: Play Console 비공개 테스트의 개인정보처리방침 URL에 `https://kakimind.github.io/bubble-rumble-site/privacy.html` 등록(사용자 작업).
- **Top of Gravity(중력의 탑) 출시 반영.** 허브 §07 항목 자체는 `14a3d9e`로 이미 들어가 있었으나, 여덟 항목 중 **유일하게 소개 페이지 링크가 없고**(Play 스토어로 바로 가는 링크뿐) 사이트맵에도 빠져 있었다. `계속 읽기 →`를 `kakimind.github.io/tower-of-gravity/`로 맞추고 사이트맵에 추가.
- TOG 랜딩 페이지(`tower-of-gravity` 저장소, **Pages 루트는 `docs/`**)를 매거진 에디토리얼 시스템으로 재작성 (`f65ddac`). 원래는 Cinzel Decorative + 보라/금색 자체 판타지 디자인이라 나머지 일곱과 톤이 달랐음. 스팟 컬러는 허브 목차와 같은 `#9b6bff`.
- "◷ 출시 준비 중" 표시를 실제 Google Play 배지로 교체. 한국어 플레이 스크린샷 5장(`store/스크린샷/한국어/`)을 720×1280 webp로 줄여 FIG. 02~06 Gallery로, 피처 그래픽을 FIG. 01 플레이트로 사용 (5장 합계 218KB). 스토어 원본은 그대로 보존.
- TOG `privacy.html`은 자체 디자인을 유지하고 **사실이 어긋난 문장만** 갱신 — "출시 준비 단계" 콜아웃, AdMob을 미래형으로 쓴 두 문장, 시행일.
- **Bubble Rumble 사이트 신설** (`bubble-rumble-site`, 첫 커밋 `d09d897`). 비공개 테스트에 Play Console이 요구하는 개인정보처리방침 URL과 소개 페이지가 필요해서 만듦. 랜딩은 매거진 시스템 §08, 스팟 컬러 `#2f7cf6`.
- Bubble Rumble은 **실제 스크린샷도 앱 아이콘도 아직 없다.** placeholder 금지 규칙에 따라 FIG.는 전부 게임의 실제 캐릭터 아트(`assets/images/skins/`)로 채우고, 캡션에 "캐릭터 아트"라고 명시했다. 버디 8종은 각자의 역할·스킬 설명을 앱의 `app_ko.arb`에서 그대로 가져와 붙였다.
- Bubble Rumble `privacy.html`은 코드에서 확인한 실제 데이터 흐름대로 작성. 빠뜨리기 쉬운 두 가지를 명시했다 — **방 목록의 방 제목이 플레이어 닉네임**이라 같은 지역 로비를 보는 사람에게 노출된다는 점, 그리고 **P2P 연결 특성상 상대에게 IP 주소가 노출될 수 있다**는 점. 현재 빌드가 구글 공개 테스트 광고 단위를 쓴다는 것도 적어 뒀다.
- 허브에 Bubble Rumble을 §08로 추가 (`kakimind.github.io` `e99764c`). `#f08`의 `grid-column` 쌍을 같이 추가 — 빠뜨리면 figure/article이 auto 배치로 떨어져 레이아웃이 깨진다 (2026-10-13에 실제로 겪은 버그).
- **미완**: `bubble-rumble-site` 원격 저장소가 아직 없어 푸시하지 못했다. 로컬 커밋 `d09d897`로 내용은 완성. 허브 §08 링크가 이미 그 주소를 가리키므로 저장소가 생기기 전까지는 404다. 재개 절차는 CLAUDE.md의 "지금 막혀 있는 일" 참고.

## 2026-10-22 (2)
- Orbit Hop 랜딩 페이지에 **실제 플레이 스크린샷 6장**으로 Gallery 섹션(`From the Cockpit — 실제 플레이 화면`) 추가. 이로써 전날 남겨뒀던 "이미지가 콘셉트 아트 1장뿐" 문제 해소.
- 출처는 `C:\src\Orbit_Hop\store\screenshots\02-한국어-ko-KR\` (20개 언어 × 6장이 생성돼 있었음). 로비·비행 중·비행 종료·격납고·일일 미션·설정 순서로 FIG. 02~07 캡션 부여. 웹용으로 1080×1920 → 720×1280 축소·최적화해 6장 합계 879KB.
- 웹용 사본은 소스 저장소의 `Design/orbit_hop_1/shots/`에 두고, `tools/build-site.mjs`가 `assets/shots/`로 복사하도록 빌드 스크립트 수정 (스토어 원본은 그대로 보존).
- 기존 CLAUDE.md 메모("Orbit Hop은 쓸만한 스크린샷이 없음, `.report_assets/device/`는 Test Ad 배너 때문에 사용 불가")는 **더 이상 유효하지 않음**. `store/screenshots/`의 새 캡쳐는 테스트 광고 배너·에러 다이얼로그가 없고 로케일도 한국어로 통일돼 있음.
- 두 저장소 커밋·푸시 (`orbit-hop` `10d84c3` / `orbit-hop-site` `a3c9760`). 배포 반영 확인 완료.
- 배포 중 발견: `.site-worktree` 로컬 클론이 원격 `6177b3c`와 내용은 같고 해시만 다른 상태여서 푸시가 거부됨. `index.html`이 산출물인 점을 이용해 원격으로 초기화 후 재빌드하는 방식으로 해결(삭제 0줄, 추가 39줄). 같은 상황이 재발하면 수동 병합하지 말고 재빌드할 것.

## 2026-10-22
- Orbit Hop 랜딩 페이지(`kakimind.github.io/orbit-hop-site/`)를 나머지 페이지들과 동일한 "KAKIMIND Issue No. 01" 매거진 에디토리얼 시스템으로 재작성. 기존엔 자체 디자인(로컬 woff2 폰트 + 외부 `site.css` + 히어로/카드 레이아웃)이라 허브 및 다른 5개 앱 페이지와 톤이 전혀 달랐음.
- 적용한 공통 요소: 세로 러닝헤드, `§06 — Orbital Arcade — Coming Soon` 킥커, Big Shoulders 마스트헤드, 드롭캡 본문, Platform/Status/Genre 팩트박스, FIG. 캡션 플레이트, 콜로폰 푸터. 타이포는 Big Shoulders Display / Source Serif 4 / Space Mono, 스팟 컬러는 허브 목차와 동일한 `#e8502f`.
- 기존 콘텐츠(핵심 플레이, 수치, 플레이 방법, 오프라인·기록, 광고 정책)는 전부 §번호 피처 리스트 idiom으로 재배치해 보존.
- 미출시 상태라 Play 다운로드 배지 대신 점선 "◷ Google Play 출시 준비 중" 표시 사용.
- **주의**: 이 페이지는 `orbit-hop-site`의 `index.html`이 산출물이고 진짜 소스는 비공개 `orbit-hop` 저장소의 `Design/orbit_hop_1/code.html`이다. 두 저장소 모두 커밋·푸시함 (`b4f7538` / `6177b3c`). 소스를 빠뜨리면 다음 `build-site.mjs` 실행 때 원복됨.
- 남은 문제: 쓸 수 있는 실제 스크린샷이 없어 이미지가 콘셉트 아트 1장뿐 (다른 앱 페이지는 5장, PomPom Ville은 15장). Gallery 섹션 미작성 — CLAUDE.md의 "미해결 / TODO" 참고.

## 2026-10-21
- 실제 허브(`kakimind.github.io`)에 Orbit Hop을 여섯 번째 항목으로 추가. 앱 아이콘·출시 준비 상태·소개 페이지 링크·목차·사이트맵 반영 (허브 저장소 `260d848`). 이 저장소는 기존 리다이렉트를 유지하며 설명 메타데이터를 6종으로 갱신.

## 2026-10-13
- kakimind-apps 허브 + 5개 앱 페이지(pompomville, box-find-web, bulssi-homepage, shift-calendar, dear-star-my-wish) 전부를 "KAKIMIND Issue No. 01" 매거진 에디토리얼 시스템으로 통일 재디자인. 각 앱 페이지에는 Play 스토어/프로젝트 폴더에서 가져온 실제 스크린샷 반영. 6개 저장소 모두 커밋·푸시 완료.
- 배포 직후 발견된 버그 수정: 모든 페이지에 `<!DOCTYPE>`/`<html>`/`<head>`/`<body>` 등 문서 뼈대가 빠져있던 것(Artifact 미리보기용 fragment를 그대로 복사했던 게 원인), 허브의 `.spread:nth-of-type(N)` 선택자가 `.cover`도 `<section>`이라 인덱스가 밀려서 전혀 매치 안 되던 레이아웃 버그, 앱 페이지들에 잘못 박혀있던 허브 URL(`/kakimind-apps/` → `/apps/`).
- SEO 등록 완료: 메타 title/description, sitemap.xml, robots.txt 추가. 네이버 서치어드바이저가 호스트 단위로만 등록을 받는다는 제약 때문에, 허브를 `kakimind.github.io` 루트로 옮기고 원래 루트에 있던 Dear Star 개인정보처리방침은 `kakimind.github.io/dear-star-my-wish/privacy.html`로 이전. 네이버 호스트 소유확인 + 구글 서치콘솔(URL 접두어) 소유확인 모두 완료, 사이트맵 제출. Google Play Console의 개인정보처리방침 URL도 새 주소로 갱신 완료.
- 허브를 옮기는 과정에서 `kakimind.github.io` 저장소에 아이콘 에셋(`assets/*.png`) 복사를 빠뜨려 아이콘이 깨졌던 것 수정.
- md 기반 기록 체계 도입 (CLAUDE.md, CHANGELOG.md 생성)

## 2026-10-10
- PomPom Ville 상태 태그를 "출시" 상태로 업데이트 (Google Play 정식 출시)

## 2026-10-09
- 허브 페이지에 자기소개(about-me) 섹션 추가
- 실제 앱 아이콘과 앱별 강조 색상(accent color)으로 허브 리디자인
- PomPom Ville 상태를 "심사중"으로 업데이트

## 2026-09-19
- 앱 허브 페이지 최초 추가
