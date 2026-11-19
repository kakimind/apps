# Play 개발자 프로필 에셋

Google Play 개발자 프로필에 올라가는 두 장. 허브와 앱 페이지들이 쓰는 매거진
시스템과 같은 어휘로 그린다 — Big Shoulders의 KM 모노그램, Space Mono
워드마크, 앱마다 하나씩인 스팟 컬러 레지스터 바.

- `kakimind-developer-icon-512.png` — 512×512
- `kakimind-developer-header-4096x2304.png` — 4096×2304 (16:9)

유튜브 채널(`UCDicnirkQDhzq6Tlc77qODw`)용 두 장도 같은 스크립트가 그린다.

- `kakimind-youtube-avatar-800.png` — 800×800. 유튜브는 **원형으로 자르기**
  때문에 Play 아이콘의 사각 이중 괘선을 그대로 쓸 수 없다. `build_icon(...,
  circle=True)`가 원형 괘선으로 바꾸고 안쪽 내용을 당겨 넣는다.
- `kakimind-youtube-banner-2560x1440.png` — 2560×1440. **휴대폰에서는 가운데
  1546×423만 보인다.** 글자는 전부 그 띠 안에 있고, 양옆 날개(데스크톱에서만
  보임)에 폴리오를 뒀다. 띠 밖으로 넘치면 빌드가 assert로 멈춘다.

## 다시 뽑기

폰트는 저장소에 넣지 않는다 (OFL, 합계 2.4MB). 먼저 받아야 한다:

```sh
cd play-developer-profile && mkdir -p fonts && cd fonts
B=https://github.com/google/fonts/raw/main/ofl
curl -sSL -o BigShouldersDisplay.ttf  "$B/bigshouldersdisplay/BigShouldersDisplay%5Bwght%5D.ttf"
curl -sSL -o SourceSerif4.ttf         "$B/sourceserif4/SourceSerif4%5Bopsz,wght%5D.ttf"
curl -sSL -o SourceSerif4-Italic.ttf  "$B/sourceserif4/SourceSerif4-Italic%5Bopsz,wght%5D.ttf"
curl -sSL -o SpaceMono-Regular.ttf    "$B/spacemono/SpaceMono-Regular.ttf"
curl -sSL -o SpaceMono-Bold.ttf       "$B/spacemono/SpaceMono-Bold.ttf"
```

그다음:

```sh
python build-profile-assets.py        # out/ 에 생성
cp out/kakimind-*.png .               # 업로드하는 4장은 루트에 둔다
```

`out/`에는 눈으로 확인하라고 축소본도 같이 나온다 (`preview-header.png`,
48px로 줄였다 키운 `preview-icon-48.png`, 휴대폰이 실제로 보는 배너 영역
`preview-banner-phone-safe.png`, TV용 전체 `preview-banner-tv.png`, 원형으로
자른 48px 아바타 `preview-avatar-48-circle.png`).

## 앱이 늘면

`build-profile-assets.py`의 `SPOTS` 리스트에 `("<번호>", (R, G, B))` 한 줄만
더하면 된다. 아이콘·헤더의 바 개수와 헤더의 "EIGHT TITLES INSIDE" 문구가
리스트 길이를 따라간다. 스팟 컬러는 루트 CLAUDE.md의 디자인 시스템 절에
앱별로 적혀 있다.

> 한 번 어긋난 적이 있다. 개수가 코드에 박혀 있어서, Top of Gravity와
> Bubble Rumble이 추가된 뒤에도 에셋은 8일 동안 여섯 개짜리였다.
