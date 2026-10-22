# Changelog

이 저장소(kakimind-apps 허브 페이지)의 변경 기록. 최신 항목이 위에 오도록 추가.

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
