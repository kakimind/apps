# Play 개발자 프로필 에셋

Google Play 개발자 프로필에 올라가는 두 장. 허브와 앱 페이지들이 쓰는 매거진
시스템과 같은 어휘로 그린다 — Big Shoulders의 KM 모노그램, Space Mono
워드마크, 앱마다 하나씩인 스팟 컬러 레지스터 바.

- `kakimind-developer-icon-512.png` — 512×512
- `kakimind-developer-header-4096x2304.png` — 4096×2304 (16:9)

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
cp out/kakimind-developer-*.png .     # 업로드하는 2장은 루트에 둔다
```

`out/`에는 눈으로 확인하라고 축소본도 같이 나온다 (`preview-header.png`,
48px로 줄였다 키운 `preview-icon-48.png`).

## 앱이 늘면

`build-profile-assets.py`의 `SPOTS` 리스트에 `("<번호>", (R, G, B))` 한 줄만
더하면 된다. 아이콘·헤더의 바 개수와 헤더의 "EIGHT TITLES INSIDE" 문구가
리스트 길이를 따라간다. 스팟 컬러는 루트 CLAUDE.md의 디자인 시스템 절에
앱별로 적혀 있다.

> 한 번 어긋난 적이 있다. 개수가 코드에 박혀 있어서, Top of Gravity와
> Bubble Rumble이 추가된 뒤에도 에셋은 8일 동안 여섯 개짜리였다.
