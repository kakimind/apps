# kakimind-apps

kakimind의 앱/게임 모음을 소개하는 허브 페이지 저장소. 단일 파일 `index.html` (인라인 CSS)로 구성된 정적 사이트, GitHub Pages로 배포.

## 구조
- `index.html` — 허브 페이지 전체. "KAKIMIND Issue No. 01" 매거진 에디토리얼 레이아웃(표지 + 목차 + 앱별 지면).
- `assets/` — 각 앱 아이콘 이미지

## 디자인 시스템 (2026-10-13 전면 개편)
허브 + 5개 앱 페이지 전부가 동일한 "인쇄 매거진" 비주얼 시스템을 공유한다.
- 타이포: Big Shoulders Display(마스트헤드/헤드라인), Source Serif 4(본문, 드롭캡), Space Mono(폴리오·팩트박스·스펙)
- 공통 요소: 세로 러닝헤드, §번호 킥커, 드롭캡 본문, 팩트박스(Platform/Status/Genre), FIG. 캡션이 붙은 스크린샷 플레이트, 콜로폰 푸터
- 각 앱 고유 스팟 컬러: PomPom Ville `#a855c9` · 어디뒀지? `#c1694f` · 불씨 `#ff7a3d` · 동행 `#2e7d9a` · Dear Star `#d9ac52`
- 앱 페이지들의 스크린샷은 각 앱의 로컬 프로젝트 폴더(Play 스토어용 에셋) 또는 Play 스토어 리스팅에서 직접 가져온 실제 이미지 — placeholder 금지.
- 다른 앱 페이지를 수정/추가할 때는 이 톤(§번호, 드롭캡, 팩트박스, 러닝헤드)을 그대로 따를 것.

## 현재 앱 목록 (허브 목차와 동일하게 유지)
1. **PomPom Ville** (§01) — 버블 팝 매치 퍼즐 게임. Google Play 출시 완료. 저장소: `pompomville`
2. **어디뒀지?** (§02) — 박스 정리 앱. 저장소: `box-find-web`
3. **불씨 (Bulssi)** (§03) — 계정 없는 습관 트래커. 저장소: `bulssi-homepage`
4. **동행** (§04) — 교대근무 캘린더 앱. 저장소: `shift-calendar` (Pages 루트는 `docs/`)
5. **Dear Star, My Wish** (§05) — 저널링 앱. 저장소: `dear-star-my-wish`

각 앱은 별도 저장소/페이지(`kakimind.github.io/<app>/`)로 운영되며, 이 저장소는 그 목록을 소개하는 허브 역할만 한다. `kakimind.github.io`(메인 도메인)는 Dear Star의 개인정보처리방침 전용이라 건드리면 안 됨 — 주소 고정 필요.

## 결정 사항 / 진행 상황
- 2026-10-13: md 기반 기록 체계 시작 (CLAUDE.md: 맥락/결정사항, CHANGELOG.md: 변경 로그).
- 2026-10-13: 허브+5개 앱 페이지를 매거진 에디토리얼 시스템으로 통일 재디자인, 6개 저장소 모두 커밋·푸시 완료.

## 메모
- 앱 상태(출시/심사중 등) 태그는 각 페이지의 §킥커("앱 · 출시됨" 등)로 표시 — 상태 변경 시 커밋 메시지와 CHANGELOG.md에 함께 기록.
