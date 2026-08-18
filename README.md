# og-preview-test

게임 슬러그마다 **링크 공유 미리보기(Open Graph 메타태그)** 를 다르게 보여줄 수 있는지 검증하는 PoC.
빌드·서버·프레임워크 없이 순수 정적 HTML + GitHub Pages.

## 공개 URL

| 페이지 | URL |
|---|---|
| 목록 | https://songseyoung.github.io/og-preview-test/ |
| 코스믹 드리프트 | https://songseyoung.github.io/og-preview-test/game1.html |
| 던전 오브 엠버 | https://songseyoung.github.io/og-preview-test/game2.html |
| 픽셀 팜 스토리 | https://songseyoung.github.io/og-preview-test/game3.html |

## 왜 정적 파일로 충분한가

소셜 미리보기 크롤러(Slack, 카카오톡, X 등)는 **JS를 실행하지 않고, 최초 응답 HTML의 `<head>` 메타태그만** 읽는다.
따라서 게임별로 OG 태그가 다른 정적 HTML을 각각의 URL로 두면 그대로 검증된다.

## 구조

```
index.html          목록
game1.html          코스믹 드리프트   (og:* 하드코딩)
game2.html          던전 오브 엠버     (og:* 하드코딩)
game3.html          픽셀 팜 스토리     (og:* 하드코딩)
images/game1~3.png  1200x630 썸네일
```

각 페이지에 들어간 태그: `og:type`, `og:site_name`, `og:locale`, `og:url`, `og:title`,
`og:description`, `og:image`(+`width`/`height`/`alt`), `twitter:card`, `twitter:title`,
`twitter:description`, `twitter:image`, `description`.

`og:image` / `og:url` 은 **https 절대경로**여야 한다. 상대경로는 크롤러가 못 읽는 경우가 많다.

## 검증 순서

1. **태그 확인** — https://www.opengraph.xyz 또는 https://metatags.io 에 위 URL을 넣어 게임별로 다르게 나오는지 확인.
2. **슬랙 확인** — 3개 URL을 슬랙 채널(또는 본인 DM)에 붙여넣고 카드 3개가 서로 다른지 확인.
3. **재확인** — 슬랙은 URL 단위로 미리보기를 캐시한다. 태그를 수정한 뒤 다시 볼 때는
   `...?v=2`, `...?v=3` 처럼 쿼리를 붙여 **새 URL**로 테스트한다.

## 커맨드라인으로 바로 확인

```bash
curl -s https://songseyoung.github.io/og-preview-test/game2.html | grep 'og:'
```

## 썸네일 재생성 (macOS, 별도 툴 불필요)

SVG를 만들고 `qlmanage`(QuickLook)로 1200x1200 PNG를 뽑은 뒤 `sips`로 1200x630 중앙 크롭.
자세한 값은 `images/` 안의 결과물 참고. 실제 게임 이미지가 준비되면 같은 파일명으로 덮어쓰면 된다.
