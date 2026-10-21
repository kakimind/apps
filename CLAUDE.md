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

## 디자인 시스템 (2026-10-13 전면 개편)
허브 + 5개 앱 페이지 전부가 동일한 "인쇄 매거진" 비주얼 시스템을 공유한다.
- 타이포: Big Shoulders Display(마스트헤드/헤드라인), Source Serif 4(본문, 드롭캡), Space Mono(폴리오·팩트박스·스펙)
- 공통 요소: 세로 러닝헤드, §번호 킥커, 드롭캡 본문, 팩트박스(Platform/Status/Genre), FIG. 캡션이 붙은 스크린샷 플레이트, 콜로폰 푸터
- 각 앱 고유 스팟 컬러: PomPom Ville `#a855c9` · 어디뒀지? `#c1694f` · 불씨 `#ff7a3d` · 동행 `#2e7d9a` · Dear Star `#d9ac52`
- 앱 페이지들의 스크린샷은 각 앱의 로컬 프로젝트 폴더(Play 스토어용 에셋) 또는 Play 스토어 리스팅에서 직접 가져온 실제 이미지 — placeholder 금지.
- 다른 앱 페이지를 수정/추가할 때는 이 톤(§번호, 드롭캡, 팩트박스, 러닝헤드)을 그대로 따를 것.
- **주의**: Artifact 미리보기용으로 쓴 HTML 조각(fragment, `<!DOCTYPE>`/`<html>`/`<head>`/`<body>` 없음)을 실제 사이트 파일에 그대로 복사하면 깨진다 — 실제 배포 파일은 항상 완전한 문서 구조(doctype, head, charset, viewport, body, 닫는 태그)를 갖춰야 함. 2026-10-13에 이 실수로 6개 사이트가 전부 깨졌다가 수정됨.

## 현재 앱 목록 (허브 목차와 동일하게 유지)
1. **PomPom Ville** (§01) — 버블 팝 매치 퍼즐 게임. Google Play 출시 완료. 저장소: `pompomville`
2. **어디뒀지?** (§02) — 박스 정리 앱. 저장소: `box-find-web`
3. **불씨 (Bulssi)** (§03) — 계정 없는 습관 트래커. 저장소: `bulssi-homepage`
4. **동행** (§04) — 교대근무 캘린더 앱. 저장소: `shift-calendar` (Pages 루트는 `docs/`)
5. **Dear Star, My Wish** (§05) — 저널링 앱. 저장소: `dear-star-my-wish`. 개인정보방침은 `privacy.html` (자기 경로 하위, 루트 아님).

6. **Orbit Hop** (§06) — 원터치 궤도 아케이드. Android 출시 준비 중. 저장소: `orbit-hop-site`. 100단계 티어·위성 100종·20개 언어·오프라인 기본 플레이.

각 앱 페이지는 자기 저장소에서 `kakimind.github.io/<app>/`으로 배포된다 (이건 전처럼 유지됨, 안 바뀜).

## 로컬 프로젝트 소스 위치 (스크린샷/에셋 재사용 시 참고)
- PomPom Ville: `C:\src\pompomville` (assets/backgrounds에 챕터별 배경아트, ad_recording에 Play 스토어용 스크린샷)
- 어디뒀지?: `C:\src\BOX_FIND` (website/assets에 스크린샷)
- 불씨: `C:\src\RoutineBox` (store-assets/screenshots/ko-raw에 한국어 스크린샷)
- 동행: `C:\src\Shift Calendar` (store_screenshots/한국어)
- Dear Star: `C:\src\Dear Star_ My Wish\flutter_application_1` (store_assets/screenshots) — 주의: 비슷한 이름의 `Dear Star, My Wish` 폴더(쉼표)는 빈 스텁이고, 진짜는 언더스코어 버전.

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

## 메모
- 앱 상태(출시/심사중 등) 태그는 각 페이지의 §킥커("앱 · 출시됨" 등)로 표시 — 상태 변경 시 커밋 메시지와 CHANGELOG.md에 함께 기록.
- 허브를 고칠 때는 이 저장소(`apps`)와 `kakimind.github.io` 저장소 둘 다 고쳐야 함 (위 "도메인 구조" 참고).
