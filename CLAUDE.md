# kakimind-apps (저장소명: `apps`)

kakimind의 앱/게임 모음을 소개하는 허브 페이지 **원본 소스** 저장소. 단, 2026-10-13부터 **실제 서빙 주소는 이 저장소가 아니라 `kakimind.github.io` 저장소**다 — 아래 "도메인 구조" 참고.

## ⚠️ 도메인 구조 (중요, 헷갈리기 쉬움)
- **`https://kakimind.github.io/`** (저장소: `kakimind.github.io`) — **진짜 허브 페이지**. 이 저장소(`apps`)의 `index.html`을 그대로 복사해서 배포한 것.
- **`https://kakimind.github.io/apps/`** (이 저장소 `apps`가 배포되는 주소) — **리다이렉트 전용 페이지**. 사람이 들어오면 즉시 `https://kakimind.github.io/`로 튕겨짐. 실제 콘텐츠 없음.
- **`https://kakimind.github.io/dear-star-my-wish/privacy.html`** — Dear Star, My Wish의 개인정보처리방침 (예전엔 `kakimind.github.io` 루트였는데 이리로 옮김).
- 이렇게 된 이유: 네이버 서치어드바이저가 `kakimind.github.io/apps/` 같은 하위 경로 단위 등록을 지원하지 않고 **호스트 전체(`kakimind.github.io`) 단위로만** 사이트 등록을 받음. 원래 루트에 Dear Star 개인정보방침이 있었는데, 허브를 검색 등록하려면 호스트 루트에 허브가 있어야 해서 서로 자리를 바꿈.
- **이 저장소(`apps`)의 `index.html`은 더 이상 허브가 아니라 순수 리다이렉트 스텁이다** (`https://kakimind.github.io/`로 즉시 이동). 허브 콘텐츠의 실제 소스는 **`kakimind.github.io` 저장소 하나뿐** — 이 저장소를 고쳐도 허브에는 아무 영향 없음.
- Google Play Console의 Dear Star 개인정보처리방침 URL은 `https://kakimind.github.io/dear-star-my-wish/privacy.html`로 갱신 완료 (2026-10-13).

## 구조 (이 저장소 `apps`)
- `index.html` — 리다이렉트 전용 스텁 (`https://kakimind.github.io/`로 즉시 이동, 콘텐츠 없음).
- `assets/` — 과거 허브용 아이콘이 남아있지만 현재 실사용 안 함 (실제 허브 에셋은 `kakimind.github.io` 저장소에 따로 있음).
- **허브를 수정할 땐 이 저장소가 아니라 `kakimind.github.io` 저장소(스크래치 클론 또는 재클론)에서 작업할 것.**

## Play 개발자 프로필 에셋 (`play-developer-profile/`)
Google Play 개발자 프로필에 올라가는 아이콘(512)과 헤더(4096×2304, 16:9). 2026-10-22에 만들어 뒀다가 2026-10-30에 커밋(`167569b`)하고 **8개 앱 기준으로 다시 뽑았다**(`04fb45b`).
- `build-profile-assets.py`가 둘 다 그린다. 앱 페이지들과 같은 어휘 — Big Shoulders의 KM 모노그램 + 이중 괘선, Space Mono 워드마크, 앱마다 하나씩인 스팟 컬러 레지스터 바.
- **앱이 늘면 `SPOTS`에 한 줄만 추가**하면 된다. 바 개수와 헤더의 "EIGHT TITLES INSIDE" 문구가 리스트 길이를 따라가게 고쳐 뒀다 (원래는 개수가 코드에 박혀 있어서 8일간 6개짜리로 방치됐었다).
- **폰트는 저장소에 없다** (OFL 5종, 2.4MB, `.gitignore` 처리). 재생성 절차와 받는 명령은 `play-developer-profile/README.md`에 있다. `out/`도 ignore — 업로드하는 2장만 폴더 루트에 커밋한다.

## 디자인 시스템 (2026-10-13 전면 개편)
허브 + 8개 앱 페이지 전부가 동일한 "인쇄 매거진" 비주얼 시스템을 공유한다.
- 타이포: Big Shoulders Display(마스트헤드/헤드라인), Source Serif 4(본문, 드롭캡), Space Mono(폴리오·팩트박스·스펙)
- 공통 요소: 세로 러닝헤드, §번호 킥커, 드롭캡 본문, 팩트박스(Platform/Status/Genre), FIG. 캡션이 붙은 스크린샷 플레이트, 콜로폰 푸터
- 각 앱 고유 스팟 컬러: PomPom Ville `#a855c9` · 어디뒀지? `#c1694f` · 불씨 `#ff7a3d` · 동행 `#2e7d9a` · Dear Star `#d9ac52` · Orbit Hop `#e8502f` · Top of Gravity `#9b6bff` · Bubble Rumble `#2f7cf6`
- 앱 페이지들의 스크린샷은 각 앱의 로컬 프로젝트 폴더(Play 스토어용 에셋) 또는 Play 스토어 리스팅에서 직접 가져온 실제 이미지 — placeholder 금지.
- 다른 앱 페이지를 수정/추가할 때는 이 톤(§번호, 드롭캡, 팩트박스, 러닝헤드)을 그대로 따를 것.
- **주의**: Artifact 미리보기용으로 쓴 HTML 조각(fragment, `<!DOCTYPE>`/`<html>`/`<head>`/`<body>` 없음)을 실제 사이트 파일에 그대로 복사하면 깨진다 — 실제 배포 파일은 항상 완전한 문서 구조(doctype, head, charset, viewport, body, 닫는 태그)를 갖춰야 함. 2026-10-13에 이 실수로 6개 사이트가 전부 깨졌다가 수정됨.

## 현재 앱 목록 (허브 목차와 동일하게 유지)
1. **PomPom Ville** (§01) — 버블 팝 매치 퍼즐 게임. Google Play 출시 완료. 저장소: `pompomville`
2. **어디뒀지?** (§02) — 박스 정리 앱. 저장소: `box-find-web`
3. **불씨 (Bulssi)** (§03) — 계정 없는 습관 트래커. 저장소: `bulssi-homepage`
4. **동행** (§04) — 교대근무 캘린더 앱. 저장소: `shift-calendar` (Pages 루트는 `docs/`)
5. **Dear Star, My Wish** (§05) — 저널링 앱. 저장소: `dear-star-my-wish`. 개인정보방침은 `privacy.html` (자기 경로 하위, 루트 아님).
6. **Orbit Hop** (§06) — 원터치 궤도 아케이드. Android 출시 준비 중. 저장소: `orbit-hop-site`. 100단계 티어·위성 100종·20개 언어·오프라인 기본 플레이. 배포 주소도 `/orbit-hop-site/`로, 다른 앱과 달리 `-site` 접미사가 붙음에 주의.
7. **Top of Gravity** (§07) — 중력 전환 매치-3 퍼즐. Google Play 출시 완료 (`com.kakimind.topgravity`). 저장소: `tower-of-gravity`, **Pages 루트는 `docs/`**. 한국어 스토어 이름은 '중력의 탑'. 1000 스테이지·100개 층·특수 재료 4종·안내자 5명·22개 언어. 배포 주소는 `/tower-of-gravity/`로 저장소명을 그대로 씀.
8. **Bubble Rumble** (§08) — 물풍선 격자 파티 아케이드 (Flutter). Google Play **비공개 테스트 준비 중** (`com.kakimind.bubble_rumble`). 사이트 저장소: `bubble-rumble-site`, 앱 저장소는 비공개(로컬 `C:\src\Bubble Rumble`). 버디 8종·스킨 72종·맵 4종·모드 2종(배틀로얄 4인 / 클래식 2vs2), 온라인은 WebRTC P2P.

각 앱 페이지는 자기 저장소에서 `kakimind.github.io/<app>/`으로 배포된다 (이건 전처럼 유지됨, 안 바뀜).

### ⚠️ Orbit Hop만 빌드 파이프라인이 다름 (중요)
- `orbit-hop-site/index.html`은 **직접 수정하면 안 되는 산출물**이다. 진짜 소스는 비공개 앱 저장소 `orbit-hop`(로컬 `C:\src\Orbit_Hop`)의 `Design/orbit_hop_1/code.html`이고, `node tools/build-site.mjs`가 이걸 `.site-worktree`로 export한다.
- 따라서 이 페이지를 고칠 땐 **두 저장소를 같이 커밋해야 한다**. 소스를 안 고치면 다음 빌드 때 원복됨.
- 빌드 스크립트는 `privacy.html`은 건드리지 않고 보존한다 (`privacy.html`은 매거진 톤이 아니라 앱별 독자 디자인 — 다른 앱들도 동일).

## 로컬 프로젝트 소스 위치 (스크린샷/에셋 재사용 시 참고)
- PomPom Ville: `C:\src\pompomville` (assets/backgrounds에 챕터별 배경아트, ad_recording에 Play 스토어용 스크린샷)
- 어디뒀지?: `C:\src\BOX_FIND` (website/assets에 스크린샷)
- 불씨: `C:\src\RoutineBox` (store-assets/screenshots/ko-raw에 한국어 스크린샷)
- 동행: `C:\src\Shift Calendar` (store_screenshots/한국어)
- Dear Star: `C:\src\Dear Star_ My Wish\flutter_application_1` (store_assets/screenshots) — 주의: 비슷한 이름의 `Dear Star, My Wish` 폴더(쉼표)는 빈 스텁이고, 진짜는 언더스코어 버전.
- Top of Gravity: `C:\src\Top of gravity` (Capacitor+Phaser). `store/스크린샷/<언어>/`에 **22개 언어 × 5장**(`01-로비` `02-상점` `03-이야기` `04-플레이` `05-스테이지클리어`, 1080×1920), `store/그래픽이미지/`에 언어별 피처 그래픽. 사이트용 사본은 `docs/assets/shots/*.webp`(720×1280)로 축소해 둠 — 스토어 원본은 건드리지 말 것.
- Bubble Rumble: `C:\src\Bubble Rumble` (Flutter). **스토어용 스크린샷과 앱 아이콘이 아직 없음** (`ic_launcher.png`가 Flutter 템플릿 기본값). 쓸 수 있는 이미지는 `assets/images/skins/<캐릭터>/`의 캐릭터 아트 72장(512×512 PNG)뿐이며, 사이트 사본은 `bubble-rumble-site/assets/`에 webp로 있음.
- Orbit Hop: `C:\src\Orbit_Hop` — **스크린샷 있음** (2026-10-22 생성). `store/screenshots/<언어>/`에 **20개 언어 × 6장**(`01-플레이` `02-로비` `03-격납고` `04-결과` `05-설정` `06-미션`, 각 1080×1920). 한국어는 `02-한국어-ko-KR`. 테스트 광고 배너·에러 다이얼로그 없이 깨끗함. `store/feature-graphic/`에 언어별 피처 그래픽도 있음.
  - 랜딩 페이지용 웹 사본(720×1280)은 `Design/orbit_hop_1/shots/`에 영문명(`lobby/play/result/hangar/missions/settings.png`)으로 두고 `build-site.mjs`가 `assets/shots/`로 복사함. 스토어 원본은 건드리지 말 것.
  - **주의**: `.report_assets/device/`의 기기 캡쳐 73장은 여전히 QA용이라 사용 불가 ("Test Ad" 배너, 에러 다이얼로그, 영어·이탈리아어 혼재). 혼동하지 말 것.
  - 콘셉트 아트는 `Design/modern_minimalist_.../screen.png`(→ 배포 시 `assets/orbit-art.png`), 랜딩 페이지의 FIG. 01로 계속 사용 중.

## SEO / 검색 등록 상태 (2026-10-13)
- `kakimind.github.io` 호스트 전체가 네이버 서치어드바이저에 등록되고 소유확인 완료 (`naver-site-verification` 메타태그는 허브 index.html에 있음).
- sitemap.xml, robots.txt는 `kakimind.github.io` 저장소 루트에 있음 (이 저장소 `apps`에는 없음 — 리다이렉트 스텁이라 불필요해서 제거함).
- 구글 서치콘솔 등록 완료: `google-site-verification` 메타태그를 허브(`kakimind.github.io` 저장소) index.html에 추가함 (URL 접두어 방식, `https://kakimind.github.io/`).
- 네이버 사이트맵도 제출 완료. 남은 선택 단계: 웹 페이지 수집 요청(선택사항). 색인 반영까지 1~4주 소요 예상.

## 결정 사항 / 진행 상황
- 2026-10-13: md 기반 기록 체계 시작 (CLAUDE.md: 맥락/결정사항, CHANGELOG.md: 변경 로그).
- 2026-10-13: 허브+5개 앱 페이지를 매거진 에디토리얼 시스템으로 통일 재디자인, 6개 저장소 모두 커밋·푸시.
- 2026-10-13: 배포 직후 발견된 구조적 버그(문서 뼈대 누락, 허브 그리드 레이아웃 깨짐, 잘못된 허브 URL) 전부 수정.
- 2026-10-13: 네이버 SEO 등록 과정에서 호스트 단위 제약 발견 → 허브를 `kakimind.github.io` 루트로, Dear Star 개인정보방침을 `dear-star-my-wish/privacy.html`로 맞교환. Play Console 개인정보방침 URL도 사용자가 새 주소로 갱신 완료.
- 2026-10-13: 네이버 호스트 소유확인 + 구글 서치콘솔(URL 접두어) 소유확인 완료, 양쪽 다 사이트맵 제출까지 완료.
- 2026-10-21: Orbit Hop을 허브에 §06으로 추가 (허브 저장소 커밋 `260d848`, 사이트맵에도 반영).
- 2026-10-22: Orbit Hop 랜딩 페이지에 실제 플레이 스크린샷 6장(FIG. 02~07) Gallery 추가. 소스(`orbit-hop` `10d84c3`)와 배포본(`orbit-hop-site` `a3c9760`) 양쪽 커밋·푸시. Orbit Hop은 현재 **비공개 테스트 중이며 출시 예정**.
- 2026-10-22: Orbit Hop 랜딩 페이지를 매거진 에디토리얼 시스템으로 재작성. 원래는 자체 디자인(로컬 woff2 폰트 + `site.css` + 카드/히어로 레이아웃)이라 나머지 5개와 완전히 달랐음. 소스(`orbit-hop` 저장소 `b4f7538`)와 배포본(`orbit-hop-site` 저장소 `6177b3c`) 양쪽 커밋·푸시 완료.
- 2026-10-30: **Top of Gravity 출시 반영 + Bubble Rumble 신규 추가.** TOG는 허브 §07에 이미 들어가 있었지만(`14a3d9e`) 소개 페이지 링크가 없고 사이트맵에도 빠져 있었음 — 둘 다 보강. TOG 랜딩 페이지(`tower-of-gravity` `f65ddac`)를 자체 판타지 디자인에서 매거진 시스템으로 재작성하고 "출시 준비 중"을 실제 Play 배지로 교체, 한국어 스크린샷 5장을 FIG. 02~06으로 추가. privacy.html은 디자인 유지한 채 출시 전 기준으로 쓰인 문장만 갱신.
- 2026-10-30: **Bubble Rumble 사이트 신설** (`bubble-rumble-site`, 로컬 `C:\src\bubble-rumble-site`, 첫 커밋 `d09d897`). 비공개 테스트에 필요한 랜딩 + 개인정보처리방침. 허브에 §08로 추가 (`kakimind.github.io` `e99764c`).
- 2026-10-30: **`bubble-rumble-site` 원격 저장소 생성 + 배포 완료.** Chrome 자동화(claude-in-chrome)로 github.com/new에서 Public 저장소를 만들고 `d09d897` 푸시, Pages를 `main` / `(root)`로 설정. 허브 §08 링크 404 해소.
- 2026-10-30: **Bubble Rumble 실제 플레이 스크린샷 확보 + Gallery 추가.** 에뮬레이터에서 직접 플레이해 9장 캡처, 6장을 랜딩 페이지 FIG. 02~07로 (`bubble-rumble-site` `5741bcc`). 원본은 앱 저장소 `store/screenshots/한국어/`에 보존.

## 미해결 / TODO
- ~~Orbit Hop 페이지에 스크린샷이 1장뿐이다~~ → **2026-10-22 해결.** 실제 한국어 플레이 화면 6장으로 Gallery 섹션 추가, 배포 완료.
- Orbit Hop 페이지가 자체 완결형(인라인 `<style>` + Google Fonts)이 되면서 `site.css`와 로컬 woff2 5종이 `index.html`에서 더 이상 참조되지 않음. `privacy.html`도 원래 독립이라 사실상 미사용 — 정리 여부 미결정. 정리하려면 `tools/build-site.mjs`의 복사 목록도 같이 수정해야 함.
- Orbit Hop 출시 후 할 일: 팩트박스 Status를 `Released`로, 점선 "◷ Google Play 출시 준비 중" 배지를 Dear Star처럼 실제 `.playbadge` 다운로드 링크로 교체, 허브 §06 킥커도 "게임 · 출시됨"으로 변경.
- ~~`bubble-rumble-site` 저장소가 없어 배포가 막혀 있음~~ → **2026-10-30 해결.** Chrome 자동화로 GitHub 웹에서 저장소 생성(Public, 초기화 항목 없음) → `git push -u origin main`(`d09d897`) → Settings → Pages → `main` / `(root)` 저장. `https://kakimind.github.io/bubble-rumble-site/`와 `/privacy.html` 둘 다 정상 서빙 확인. 허브 §08 링크의 404도 같이 해소됨.
  - 이전 세션에서 막혔던 원인은 Chrome 확장이 계정에 연결돼 있지 않았던 것(`list_connected_browsers` → `[]`). 이번엔 연결돼 있어서 바로 처리됨. 비슷한 GitHub 웹 작업이 필요하면 `gh` CLI나 토큰 대신 Chrome 자동화를 쓸 것.
- **남은 일: Play Console 비공개 테스트의 개인정보처리방침 URL로 `https://kakimind.github.io/bubble-rumble-site/privacy.html` 등록** (사용자 작업).

- **Bubble Rumble: 앱 아이콘이 없다.** `ic_launcher.png`가 Flutter 템플릿 기본값이라, 허브 §08 플레이트와 사이트 파비콘을 캐릭터 아트로 대신 쓰고 있음(캡션에 "캐릭터 아트"라고 명시). 아이콘이 생기면 `kakimind-hub/assets/bubblerumble.png`와 `bubble-rumble-site/icon.png`를 교체하고 허브 캡션도 "아이콘"으로 되돌릴 것.
- ~~Bubble Rumble: 실제 플레이 스크린샷이 없다~~ → **2026-10-30 해결.** Pixel 6 에뮬레이터에 release APK를 올려 한국어로 직접 플레이하며 캡처. 랜딩 페이지에 `From the Arena — 실제 플레이 화면` Gallery를 FIG. 02~07로 추가하고 버디 로스터는 FIG. 08~15로 밀었다 (`bubble-rumble-site` `5741bcc`).
  - **이 게임은 가로 모드다** (2400×1080). 다른 앱들의 1080×1920 세로 스크린샷과 달라서 Gallery는 3열이 아니라 2열(`repeat(2, 1fr)`), 웹 사본은 1280×576 webp(6장 248KB)로 만들었다.
  - 스토어 원본 9장은 `C:\src\Bubble Rumble\store\screenshots\한국어\`에 보존 (로비·방만들기·아레나·플레이·상점·스킨옷장·대기방·가방·결과). **Play 스토어 등록 때 이걸 쓰면 된다 — 지금까지 없던 자산이다.**
  - 재캡처 방법: 에뮬레이터 부팅 → `flutter build apk --release` 산출물 설치 → `adb exec-out screencap -p` + `adb shell input tap`. 봇은 방을 만들고 `준비 완료`를 누르면 자동으로 들어찬다 (빈 자리를 탭해서 넣는 게 아니다 — `_EmptySeat`의 주석은 오래된 것).
  - 결과 화면(`07-result`)은 캐릭터 아트가 화면을 거의 다 채워서 Gallery에 넣지 않았다.
- **Bubble Rumble 출시 후 할 일**: 팩트박스 Status를 `Released`로, 점선 "◷ Google Play 비공개 테스트 중" 배지를 실제 `.playbadge` 다운로드 링크로, 허브 §08 킥커를 "게임 · 출시됨"으로 변경. 개인정보처리방침 4항의 "테스트 광고 단위" 문단도 실제 광고 단위 전환에 맞춰 갱신해야 함.

## 메모
- 앱 상태(출시/심사중 등) 태그는 각 페이지의 §킥커("앱 · 출시됨" 등)로 표시 — 상태 변경 시 커밋 메시지와 CHANGELOG.md에 함께 기록.
- 허브를 고칠 때는 이 저장소(`apps`)와 `kakimind.github.io` 저장소 둘 다 고쳐야 함 (위 "도메인 구조" 참고).
