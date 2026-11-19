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

## 채널 에셋 (`play-developer-profile/`)
`build-profile-assets.py` 한 벌이 **네 장**을 그린다 — Play 개발자 프로필용 아이콘(512)·헤더(4096×2304, 16:9), 유튜브 채널(`UCDicnirkQDhzq6Tlc77qODw`)용 아바타(800)·배너(2560×1440). 2026-10-22에 Play 두 장으로 시작해 2026-10-30 커밋(`167569b`/`04fb45b`), 2026-11-18에 유튜브 두 장을 더했다.
- 앱 페이지들과 같은 어휘 — Big Shoulders의 KM 모노그램 + 이중 괘선, Space Mono 워드마크, 앱마다 하나씩인 스팟 컬러 레지스터 바.
- **앱이 늘면 `SPOTS`에 한 줄만 추가**하면 된다. 바 개수가 리스트 길이를 따라간다. **그림 안에 앱 개수를 글자로 적지 않는다** — 원래 헤더에 "EIGHT TITLES INSIDE"가 박혀 있다가 8일간 낡은 숫자로 방치됐었고, 지금은 "APPS AND GAMES ON GOOGLE PLAY"로 바꿔 숫자 자체를 없앴다.
- **유튜브는 자르기 규칙이 까다롭다.** 아바타는 **원형으로 잘리므로** `build_icon(..., circle=True)`가 괘선을 원형으로 바꾸고 안쪽을 당겨 넣는다. 배너는 **휴대폰에서 가운데 1546×423만 보여서** 글자는 전부 그 띠 안에, 폴리오는 데스크톱에서만 보이는 양옆 날개에 뒀다. 둘 다 넘치면 빌드가 `assert`로 멈춘다 — 문구를 늘릴 때 이 가드를 믿고 고치면 된다.
- **폰트는 저장소에 없다** (OFL 5종, 2.4MB, `.gitignore` 처리). 재생성 절차와 받는 명령은 `play-developer-profile/README.md`에 있다. `out/`도 ignore(미리보기 5장 포함) — 업로드하는 4장만 폴더 루트에 커밋한다.

## 유튜브 플레이 영상 (2026-11-19, 연화사)
연화사 영상은 **에뮬레이터가 아니라 웹 빌드를 헤드리스 크롬으로 녹화**해서 뽑는다 (`C:\src\yunhwasa` 의 `scripts/make-video.mjs`, `d72de22`). 릴리스 APK가 낡아 최신 연출이 안 들어 있었고, 크롬은 GPU로 79fps 가 나와 에뮬레이터보다 깨끗하다.
- `npm run dev` 를 띄워 두고 `node scripts/make-video.mjs` → `docs/영상/연화사-플레이.mp4` (1080×1920, 59.9초, 16MB). 출력은 `.gitignore` — 스크립트만 커밋한다.
- **함정**: `Page.screencastFrame` 은 `setDeviceMetricsOverride` 의 배율을 무시하고 CSS 픽셀로 보낸다. 처음에 360×640 짜리가 나왔다. 크롬에 `--force-device-scale-factor=3` 을 줘야 1080×1920 이 온다 — 스크립트가 첫 장면 폭을 확인해 작으면 멈춘다.
- **소리는 앱 음원을 얹는다. 염불은 CC BY 4.0 이라 영상 설명에 출처를 적을 의무가 있다**: `염불 「염불소리1」 김용배, 공유마당, CC BY 4.0 — 앞뒤 무음을 잘라 사용`. 법당 배경음은 직접 만든 것이라 표시 의무 없음.
- 다른 앱도 같은 방식으로 뽑을 수 있지만 `__sceneStore` 로 연출을 기다리는 부분은 연화사 전용이다.

## 디자인 시스템 (2026-10-13 전면 개편)
허브 + 9개 앱 페이지 전부가 동일한 "인쇄 매거진" 비주얼 시스템을 공유한다.
- 타이포: Big Shoulders Display(마스트헤드/헤드라인), Source Serif 4(본문, 드롭캡), Space Mono(폴리오·팩트박스·스펙)
- 공통 요소: 세로 러닝헤드, §번호 킥커, 드롭캡 본문, 팩트박스(Platform/Status/Genre), FIG. 캡션이 붙은 스크린샷 플레이트, 콜로폰 푸터
- 각 앱 고유 스팟 컬러: PomPom Ville `#a855c9` · 어디뒀지? `#c1694f` · 불씨 `#ff7a3d` · 동행 `#2e7d9a` · Dear Star `#d9ac52` · Orbit Hop `#e8502f` · Top of Gravity `#9b6bff` · Bubble Rumble `#2f7cf6` · 연화사 `#2a7d5f`
- 앱 페이지들의 스크린샷은 각 앱의 로컬 프로젝트 폴더(Play 스토어용 에셋) 또는 Play 스토어 리스팅에서 직접 가져온 실제 이미지 — placeholder 금지.
- 다른 앱 페이지를 수정/추가할 때는 이 톤(§번호, 드롭캡, 팩트박스, 러닝헤드)을 그대로 따를 것.
- **주의**: Artifact 미리보기용으로 쓴 HTML 조각(fragment, `<!DOCTYPE>`/`<html>`/`<head>`/`<body>` 없음)을 실제 사이트 파일에 그대로 복사하면 깨진다 — 실제 배포 파일은 항상 완전한 문서 구조(doctype, head, charset, viewport, body, 닫는 태그)를 갖춰야 함. 2026-10-13에 이 실수로 6개 사이트가 전부 깨졌다가 수정됨.

## 현재 앱 목록 (허브 목차와 동일하게 유지)
1. **PomPom Ville** (§01) — 버블 팝 매치 퍼즐 게임. Google Play 출시 완료. 저장소: `pompomville`
2. **어디뒀지?** (§02) — 박스 정리 앱. 저장소: `box-find-web`
3. **불씨 (Bulssi)** (§03) — 계정 없는 습관 트래커. 저장소: `bulssi-homepage`
4. **동행** (§04) — 교대근무 캘린더 앱. 저장소: `shift-calendar` (Pages 루트는 `docs/`)
5. **Dear Star, My Wish** (§05) — 저널링 앱. 저장소: `dear-star-my-wish`. 개인정보방침은 `privacy.html` (자기 경로 하위, 루트 아님).
6. **Orbit Hop** (§06) — 원터치 궤도 아케이드. Google Play 출시 완료 (`com.kakimind.orbithop`, 2026-11-07). 저장소: `orbit-hop-site`. 100단계 티어·위성 100종·20개 언어·오프라인 기본 플레이. 배포 주소도 `/orbit-hop-site/`로, 다른 앱과 달리 `-site` 접미사가 붙음에 주의.
7. **Top of Gravity** (§07) — 중력 전환 매치-3 퍼즐. Google Play 출시 완료 (`com.kakimind.topgravity`). 저장소: `tower-of-gravity`, **Pages 루트는 `docs/`**. 한국어 스토어 이름은 '중력의 탑'. 1000 스테이지·100개 층·특수 재료 4종·안내자 5명·22개 언어. 배포 주소는 `/tower-of-gravity/`로 저장소명을 그대로 씀.
8. **Bubble Rumble** (§08) — 버블 격자 파티 아케이드 (Flutter). Google Play **출시 완료** (`com.kakimind.bubble_rumble`, 2026-11-16). 사이트 저장소: `bubble-rumble-site`, 앱 저장소는 비공개(로컬 `C:\src\Bubble Rumble`). 버디 8종·스킨 72종·맵 4종·모드 2종(배틀로얄 4인 / 클래식 2vs2), 온라인은 WebRTC P2P.
9. **연화사** (§09) — 함께 절하고 명상하는 3D 온라인 사찰 (Next.js 정적 빌드 + Capacitor). Google Play **출시 완료** (`com.kakimind.yunhwasa`, 2026-11-17). 앱 저장소는 비공개(`kakimind/yunhwasa`, 로컬 `C:\src\yunhwasa`)라 **사이트 저장소가 따로 없고, 허브 저장소 안의 `yeonhwasa/` 폴더에서 서빙된다** (`https://kakimind.github.io/yeonhwasa/`, `/privacy.html`). 삼배·108배·염주 108알·명상 3/5/10분·향·연등·오늘의 법문 365개, 실시간 함께 참배는 Cloudflare Workers + Durable Objects.
10. **LUNARCANA** (§10) — 직접 그린 78장 타로 덱으로 한 장씩 대화하며 읽는 AI 타로 앱 (Flutter). Google Play **비공개 테스트 중** (`com.kakimind.lunarcana`). 로컬 `C:\src\LUNARCANA`. 리딩은 Gemini API(기본) + Groq(대체)로 생성 — 온디바이스 아님. 언어는 18개(2026-11-17에 사이트 표기를 22 → 18로 내림). 스팟 컬러 가넷 `#8a2846`. 사이트는 **공개 저장소 `lunarcana`의 `docs/`** 에서 `https://kakimind.github.io/lunarcana/`로 서빙 (`/privacy.html` 포함).

### ⚠️ LUNARCANA는 원격이 둘이다 (푸시 주의)
- 로컬 `C:\src\LUNARCANA`에서 `origin`은 **공개 사이트 저장소 `lunarcana`** (`docs/`만 있는 트리, Pages 루트 `docs/`), `app`은 **비공개 앱 저장소 `lunarcana-app`**.
- 로컬 `main`은 `app/main`과 같고 `origin/main`보다 앞서 있으며 그 차이가 **Flutter 앱 전체**다. `git push origin main`을 하면 앱 소스가 공개 저장소로 넘어간다 — 하지 말 것.
- 사이트를 고칠 때는 `origin/main`에서 브랜치를 따서 `docs/`만 담은 커밋을 만들어 `HEAD:main`으로 푸시한다 (2026-11-12에 `site-main` 브랜치로 그렇게 했다).


**연화사만 예외**: 위 1~8과 10은 각자 저장소에서 배포되지만 연화사는 허브 저장소의 하위 폴더다. 고칠 때 `kakimind.github.io` 저장소에서 `yeonhwasa/`를 수정하면 된다.

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
- Bubble Rumble: `C:\src\Bubble Rumble` (Flutter). 스토어용 스크린샷 9장은 `store/screenshots/한국어/`에 있고(2026-10-30 캡처), **앱 아이콘은 아직 없음** (`ic_launcher.png`가 Flutter 템플릿 기본값). 아이콘 대신 쓸 수 있는 이미지는 `assets/images/skins/<캐릭터>/`의 캐릭터 아트 72장(512×512 PNG)뿐이며, 사이트 사본은 `bubble-rumble-site/assets/`에 webp로 있음.
- Orbit Hop: `C:\src\Orbit_Hop` — **스크린샷 있음** (2026-10-22 생성). `store/screenshots/<언어>/`에 **20개 언어 × 6장**(`01-플레이` `02-로비` `03-격납고` `04-결과` `05-설정` `06-미션`, 각 1080×1920). 한국어는 `02-한국어-ko-KR`. 테스트 광고 배너·에러 다이얼로그 없이 깨끗함. `store/feature-graphic/`에 언어별 피처 그래픽도 있음.
  - 랜딩 페이지용 웹 사본(720×1280)은 `Design/orbit_hop_1/shots/`에 영문명(`lobby/play/result/hangar/missions/settings.png`)으로 두고 `build-site.mjs`가 `assets/shots/`로 복사함. 스토어 원본은 건드리지 말 것.
  - **주의**: `.report_assets/device/`의 기기 캡쳐 73장은 여전히 QA용이라 사용 불가 ("Test Ad" 배너, 에러 다이얼로그, 영어·이탈리아어 혼재). 혼동하지 말 것.
  - 콘셉트 아트는 `Design/modern_minimalist_.../screen.png`(→ 배포 시 `assets/orbit-art.png`), 랜딩 페이지의 FIG. 01로 계속 사용 중.
- LUNARCANA: `C:\src\LUNARCANA` (Flutter). 덱 원화는 `assets/tarot/images/`(78장, 720×1290), 스토어 아이콘 `store/icon/icon.png`, 스크린샷 `store/screenshots/`(4장, 900×1600 — **기기 프레임 + 마케팅 헤드라인이 박힌 홍보 이미지이고 실제 화면은 뽑기·켈틱크로스 두 종류뿐**), 등록정보 원본 `store/LISTING.md`. 랜딩용 웹 사본은 `docs/shots/*.webp`(640×1137). **덱은 직접 그린 한국풍 78장이고 RWS 스캔이 아니다** — 출처를 적는 문구는 `assets/tarot/ART_LICENSE.txt`를 근거로 쓸 것.

## 방문자 카운터 (2026-11-16)
- 허브(`kakimind.github.io` `192debb`)에만 **GoatCounter** 무료 계정(`kakimind.goatcounter.com`)을 붙였다. 집계는 `//gc.zgo.at/count.js` 한 줄, 표시는 커버 킥커(데이트라인) 줄 오른쪽 끝에 "오늘/이번 달/전체" (`135428c`에서 콜로폰 → 상단으로 이동, 킥커 규칙을 `display:flex`+`space-between`으로 바꿔 같은 줄 양끝에 놓음) + 인라인 스크립트에서 `https://kakimind.goatcounter.com/counter/TOTAL.json`을 `?start=` 유무로 세 번 호출. 새 CSS 없음(기존 Space Mono `.meta` 재사용), 실패하면 `—` 유지.
- **대시보드의 "Allow adding visitor counts on your website" 설정을 켜야 한다** — 꺼져 있으면 카운터 API가 403(`Need to enable the 'allow using the visitor counter' setting`). 숫자가 `—`로만 보이면 여기부터 확인. 2026-11-16에 켜고 실제 표시 확인 완료.
- 무가입 대안은 다 죽어 있었다 — `api.counterapi.dev/v1`은 410 폐기(v2는 워크스페이스 필요), `abacus.jasoncameron.dev`는 500. 그래서 가입이 필요한 GoatCounter를 썼다.
- "오늘" 경계는 브라우저 로컬 시간 기준이라 GoatCounter 사이트 타임존과 다르면 자정 전후로 어긋난다. 앱 10개 페이지에는 넣지 않았다.

## 애드센스 — 보류 (2026-11-19)
붙일 수 있는지 따져만 보고 **미뤘다.** 심사용 스니펫과 `ads.txt`를 허브에 넣었다가(`264fd01`) 같은 날 되돌렸다(`bafd2d9`) — 광고도 없는데 구글 광고 스크립트만 모든 방문자에게 실릴 이유가 없어서.
- **퍼블리셔 ID는 앱의 애드몹과 같은 `pub-7834868288333512`다.** 계정이 하나라 **사이트 쪽 정책 위반이 앱 광고 수익까지 번진다** — 이게 미룬 가장 큰 이유다. 다시 꺼낼 때도 자동 광고는 쓰지 말고 **콜로폰 위 작은 한 칸만**.
- **승인 걸림돌로 예상되는 것**: ① 본문 분량이 적다(허브 약 3,500자, 앱 페이지 각 2,300자 내외 — "가치가 낮은 콘텐츠") ② `github.io`는 공용 호스트라 도메인 소유 증명이 안 된다 ③ **허브에는 사이트용 개인정보처리방침이 없다**(앱별 방침만 있음) — 애드센스는 쿠키·제3자 광고 고지를 요구한다.
- 다시 할 때 순서: 헤드 스니펫 + 루트 `ads.txt`(내용은 `app-ads.txt`와 동일) → 온보딩에서 사이트 심사 요청 → 승인되면 디스플레이 단위 하나 만들어 슬롯 ID를 받아 콜로폰 위에 삽입.

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
- 2026-11-07: **Orbit Hop 정식 출시 반영.** 랜딩 페이지와 허브에서 "출시 준비 중" 표기를 전부 걷어내고 Play 다운로드 링크를 붙였다. 랜딩은 소스(`orbit-hop` `a71f812`)를 고쳐 `build-site.mjs`로 재빌드 후 배포(`orbit-hop-site` `dceafe6`), 허브는 `31a4574`. 광고 섹션의 "테스트 광고 모드" 문구도 같이 제거(`dcbd80d`/`ac7240d`) — release 빌드는 `testMode: false`로 실제 단위를 쓴다. 배포본 작업은 `C:\src\Orbit_Hop\.site-worktree`에서 — `C:\src\orbit-hop-site` 클론은 `a3c9760`에 멈춰 있어 낡았다.
- 2026-11-16: **Bubble Rumble 프로덕션 출시 반영.** 랜딩·개인정보처리방침·허브에서 비공개 테스트 표기를 걷어내고 Play 다운로드 링크를 붙였다 (사이트 `5a22512`, 허브 `dfc6a1e`).
- 2026-11-12: **LUNARCANA 비공개 테스트 진입 반영.** 허브 §10 추가(`496cb4a`), 랜딩/개인정보처리방침을 실제 앱 기준으로 교정(사이트 `fd1def4`, 앱 저장소 `92c3501`). 랜딩이 덱을 "라이더-웨이트 원화 스캔"이라 설명하고 방침 1항이 "온디바이스 처리, 서버 미전송"이라 단언하던 것을 둘 다 고쳤다 — 후자는 Play Console에 올라가는 문서라 데이터 안전성 양식과 어긋나면 심사 문제가 된다.

- 2026-11-17: **LUNARCANA 랜딩 스크린샷 교체.** 앱에서 새로 뽑은 한국어 스토어 이미지 5장(`store/screenshots/korean/screen1~5.jpeg`)을 640×1138 webp로 줄여 `docs/shots/`를 갈아끼우고 갤러리를 4칸 → 5칸으로(1040px·760px 중간 브레이크포인트 추가). 사이트 `origin/main 4d47d29`, 앱 저장소 쪽 동일 커밋 `f15a7e6`(현재 브랜치 `i18n-18-languages`, 미푸시).
- 2026-11-17: **연화사 정식 출시 반영 + 실제 화면 5장 추가.** 킥커·팩트박스 Status `Released`, pending 배지 → Play 링크, 개인정보처리방침의 테스트 광고 문단 삭제·시행일 갱신, 허브 §09 "앱 · 출시됨" (허브 `00c5722`, 이미지 경로 보정 `ffcba47`). 스크린샷 원본은 앱 저장소 `docs/스토어-그림/`, 웹 사본은 `yeonhwasa/shots/*.webp`(720×1280).
- 2026-11-17: **LUNARCANA 언어 표기 22 → 18.** 랜딩 다섯 군데 + 언어 칩에서 아랍어·힌디어·태국어·그리스어 삭제, 허브 §10도 같이 (사이트 `f572d3a`, 허브 `00c5722`).
- 2026-11-18: **유튜브 채널 에셋 추가.** `build-profile-assets.py`가 Play 두 장에 더해 유튜브 아바타(원형 괘선)·배너(휴대폰 안전 영역 1546×423)까지 그린다. 같은 커밋에서 헤더의 "TEN TITLES INSIDE" 문구를 없앴다 — 앱이 늘 때마다 낡는 숫자라 "APPS AND GAMES ON GOOGLE PLAY"로 바꿨다.
- 2026-11-19: **연화사 랜딩 스크린샷 갱신.** 앱 저장소 `docs/스토어-그림/`의 새 렌더(금빛 불상·연등)를 720×1280 webp로 줄여 `yeonhwasa/shots/`에 반영, `together.webp` → `lantern.webp`(연등 달기)로 교체하고 FIG. 04 캡션·alt를 고쳐 씀. 명상 화면은 원본이 안 바뀌어 그대로 (허브 `dff72b7`).
- 2026-11-17: 허브에 우측 하단 고정 `↑ TOP` 버튼(`ac15af4`), LUNARCANA 랜딩에 고정 우상단 `← Back to Issue Index` 추가(`59fa034`)하면서 내비의 "비공개 테스트 중" 알약 제거(`c56c5ec`).

## 미해결 / TODO
- ~~Orbit Hop 페이지에 스크린샷이 1장뿐이다~~ → **2026-10-22 해결.** 실제 한국어 플레이 화면 6장으로 Gallery 섹션 추가, 배포 완료.
- Orbit Hop 페이지가 자체 완결형(인라인 `<style>` + Google Fonts)이 되면서 `site.css`와 로컬 woff2 5종이 `index.html`에서 더 이상 참조되지 않음. `privacy.html`도 원래 독립이라 사실상 미사용 — 정리 여부 미결정. 정리하려면 `tools/build-site.mjs`의 복사 목록도 같이 수정해야 함.
- ~~Orbit Hop 출시 후 할 일~~ → **2026-11-07 해결.** 팩트박스·킥커 Status `Released`, pending 배지 → 실제 `.playbadge` 링크, 허브 §06 킥커 "게임 · 출시됨"까지 반영 (소스 `a71f812` / 배포 `dceafe6` / 허브 `31a4574`).
- ~~`bubble-rumble-site` 저장소가 없어 배포가 막혀 있음~~ → **2026-10-30 해결.** Chrome 자동화로 GitHub 웹에서 저장소 생성(Public, 초기화 항목 없음) → `git push -u origin main`(`d09d897`) → Settings → Pages → `main` / `(root)` 저장. `https://kakimind.github.io/bubble-rumble-site/`와 `/privacy.html` 둘 다 정상 서빙 확인. 허브 §08 링크의 404도 같이 해소됨.
  - 이전 세션에서 막혔던 원인은 Chrome 확장이 계정에 연결돼 있지 않았던 것(`list_connected_browsers` → `[]`). 이번엔 연결돼 있어서 바로 처리됨. 비슷한 GitHub 웹 작업이 필요하면 `gh` CLI나 토큰 대신 Chrome 자동화를 쓸 것.
- **남은 일: Play Console 프로덕션의 개인정보처리방침 URL로 `https://kakimind.github.io/bubble-rumble-site/privacy.html` 등록 확인** (사용자 작업).

- **Bubble Rumble: 앱 아이콘이 없다.** `ic_launcher.png`가 Flutter 템플릿 기본값이라, 허브 §08 플레이트와 사이트 파비콘을 캐릭터 아트로 대신 쓰고 있음(캡션에 "캐릭터 아트"라고 명시). 아이콘이 생기면 `kakimind-hub/assets/bubblerumble.png`와 `bubble-rumble-site/icon.png`를 교체하고 허브 캡션도 "아이콘"으로 되돌릴 것.
- ~~Bubble Rumble: 실제 플레이 스크린샷이 없다~~ → **2026-10-30 해결.** Pixel 6 에뮬레이터에 release APK를 올려 한국어로 직접 플레이하며 캡처. 랜딩 페이지에 `From the Arena — 실제 플레이 화면` Gallery를 FIG. 02~07로 추가하고 버디 로스터는 FIG. 08~15로 밀었다 (`bubble-rumble-site` `5741bcc`).
  - **이 게임은 가로 모드다** (2400×1080). 다른 앱들의 1080×1920 세로 스크린샷과 달라서 Gallery는 3열이 아니라 2열(`repeat(2, 1fr)`), 웹 사본은 1280×576 webp(6장 248KB)로 만들었다.
  - 스토어 원본 9장은 `C:\src\Bubble Rumble\store\screenshots\한국어\`에 보존 (로비·방만들기·아레나·플레이·상점·스킨옷장·대기방·가방·결과). **Play 스토어 등록 때 이걸 쓰면 된다 — 지금까지 없던 자산이다.**
  - 재캡처 방법: 에뮬레이터 부팅 → `flutter build apk --release` 산출물 설치 → `adb exec-out screencap -p` + `adb shell input tap`. 봇은 방을 만들고 `준비 완료`를 누르면 자동으로 들어찬다 (빈 자리를 탭해서 넣는 게 아니다 — `_EmptySeat`의 주석은 오래된 것).
  - 결과 화면(`07-result`)은 캐릭터 아트가 화면을 거의 다 채워서 Gallery에 넣지 않았다.
- ~~Bubble Rumble 출시 후 할 일~~ → **2026-11-16 해결.** 킥커·팩트박스 Status `Released`, 점선 배지 → 실제 Play 링크, 허브 §08 킥커 "게임 · 출시됨", 개인정보처리방침의 테스트 광고 단위 문단 삭제 (사이트 `5a22512` / 허브 `dfc6a1e`). release 빌드는 `kReleaseMode`로 실제 Android 단위(`ca-app-pub-7834868288333512/6156308171`)를 쓴다.

- **LUNARCANA 남은 일**: ① **Play Console 비공개 테스트의 개인정보처리방침 URL에 `https://kakimind.github.io/lunarcana/privacy.html` 등록**(사용자 작업). 같이, 방침이 "리딩 내용을 Google·Groq로 전송"으로 바뀌었으니 **데이터 안전성 양식도 '앱 활동/기타 사용자 콘텐츠 → 제3자 전송'으로 맞춰야 한다.** ② Play 개발자 프로필에 10개 기준으로 다시 뽑은 아이콘 512 / 헤더 4096×2304 업로드(사용자 작업). ③ 랜딩의 화면 5장(2026-11-17에 새 한국어 스토어 이미지로 교체: 1장 모드·3장 질문·첫 장 리딩·마무리·78덱 도감)은 여전히 스토어 홍보 이미지라 마케팅 밴드가 박혀 있다 — 지난 리딩·설정 화면을 깨끗하게 찍으면 교체. 원본은 `store/screenshots/<언어>/screen1~5.jpeg`(19개 언어), 웹 사본은 `docs/shots/*.webp`(640×1138). ④ 출시되면 킥커·팩트박스 Status를 `Released`로, CTA를 Play 배지로, 허브 §10 킥커를 "앱 · 출시됨"으로. ~~⑤ 개발자 프로필 에셋 재생성~~ → 2026-11-12 완료. ~~⑥ 언어 수를 22 → 18로~~ → **2026-11-17 완료** (사이트 `f572d3a`, 허브 `00c5722`). 원래 메모: **언어 수를 22 → 18로 내려야 한다** (앱 브랜치 `i18n-18-languages`의 실제 로케일이 18개: `cs de en es fr id it ja ko nl pl pt ru sv tr uk vi zh` — 빠진 4개는 아랍어·힌디어·태국어·그리스어). 고칠 곳은 `docs/index.html`의 meta description, 히어로 본문, 히어로 메타 `<b>22</b>대화 언어`, 기능 카드 제목 "22개 언어로 루나와", `#languages` 섹션 `<h2>`, 그리고 `.lang-strip`의 `lang-pill` 22개 중 ar·hi·th·el 4개 삭제. 허브 §10 설명문("22개 언어")과 이 CLAUDE.md의 §10 줄도 같이. 앱 출시 전엔 건드리지 않음 (사용자 요청: 나중에).

## 메모
- 앱 상태(출시/심사중 등) 태그는 각 페이지의 §킥커("앱 · 출시됨" 등)로 표시 — 상태 변경 시 커밋 메시지와 CHANGELOG.md에 함께 기록.
- 허브를 고칠 때는 이 저장소(`apps`)와 `kakimind.github.io` 저장소 둘 다 고쳐야 함 (위 "도메인 구조" 참고).
