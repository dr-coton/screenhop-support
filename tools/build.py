#!/usr/bin/env python3
"""site.json + 이 파일의 문구로 정적 페이지(ko: 루트, en: en/)를 만든다.

사용: cd screenhop-support && python3 -I tools/build.py
문구를 고칠 때는 이 파일(PAGES)을, 이메일·시행일·DMG 주소는 site.json을 고친다.
"""
import html
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
CFG = json.loads((ROOT / "site.json").read_text(encoding="utf-8"))
BASE = "https://dr-coton.com/screenhop-support/"
HUB = {"ko": "https://apps.dr-coton.com/ko/screenhop", "en": "https://apps.dr-coton.com/en/screenhop"}


def esc(s):
    return html.escape(s, quote=True)


def mail(lang):
    e = CFG["contactEmail"]
    return f'<a href="mailto:{esc(e)}">{esc(e)}</a>' if "@" in e and not e.startswith("[") else f'<span class="todo">{esc(e)}</span>'


def effective(lang):
    d = CFG["effectiveDate"][lang]
    return f'<span class="todo">{esc(d)}</span>' if d.startswith("[") else esc(d)


# ───────────────────────── 한국어 ─────────────────────────
KO = {
    "lang": "ko",
    "nav": {"support": "지원", "download": "Mac 도우미 받기", "privacy": "개인정보 처리방침", "switch": "English"},
    "title": {
        "index": "ScreenHop 지원 · 자주 묻는 질문",
        "download": "ScreenHop Host for Mac 다운로드",
        "privacy": "ScreenHop 개인정보 처리방침",
    },
    "desc": {
        "index": "ScreenHop(iPad용 Mac 원격 화면·SSH 터미널) 설치, 권한, 연결, 문제 해결 안내.",
        "download": "iPad에서 내 Mac을 쓰기 위한 무료 도우미 ScreenHop Host. 요구 사항, 설치 방법, 삭제 방법.",
        "privacy": "ScreenHop은 개인정보를 수집하지 않습니다.",
    },
}

KO["index"] = f"""
<h1>ScreenHop 지원</h1>
<p class="lead">iPad에서 <strong>내 Mac</strong>을 매끄럽게 쓰는 원격 화면 앱, 그리고 같은 앱 안의 SSH 터미널. 무료이며 광고가 없습니다.</p>
<div class="card"><p><strong>문의</strong><br>Code Black Inc.<br>{mail("ko")}</p>
<p class="muted">문의할 때 비밀번호나 화면 속 개인 정보는 보내지 마세요. 어떤 기기·버전에서 무슨 일이 있었는지 적어 주시면 빨리 도와드릴 수 있어요.</p></div>
<nav class="toc" aria-label="이 페이지의 항목"><ul>
<li><a href="#start">처음 시작하기</a></li><li><a href="#permissions">권한 3가지</a></li><li><a href="#pairing">처음 연결할 때</a></li>
<li><a href="#wifi">같은 Wi-Fi</a></li><li><a href="#outside">밖에서 쓰기 (Tailscale 등)</a></li><li><a href="#lock">Mac 화면이 잠겼을 때</a></li>
<li><a href="#trouble">문제 해결</a></li><li><a href="#data">내 화면 정보는 어디로 가나요?</a></li><li><a href="#uninstall">지우는 방법</a></li></ul></nav>

<h2 id="start">처음 시작하기</h2>
<p>두 가지가 필요합니다. <strong>iPad의 ScreenHop 앱</strong>과 <strong>Mac의 무료 도우미 ScreenHop Host</strong>입니다. Mac 쪽 도우미가 화면을 iPad로 보내 주고 iPad의 입력을 받아 줍니다.</p>
<ol>
<li>Mac에 ScreenHop Host를 설치합니다. → <a href="download.html">Mac 도우미 받기·설치 안내</a> (macOS 14 이상)</li>
<li>iPad와 Mac을 <strong>같은 Wi-Fi</strong>에 둡니다.</li>
<li>iPad에서 ScreenHop을 열고 목록의 내 Mac을 누릅니다. 양쪽 화면에 같은 6자리 코드가 보이면 Mac에서 [허용]을 누릅니다.</li>
</ol>
<p>Mac이 없어도 연결 목록의 <strong>데모로 둘러보기</strong>(Mac 없이 둘러보기)로 화면 구성을 미리 볼 수 있습니다.</p>

<h2 id="permissions">권한 3가지</h2>
<p>Mac에서 2개, iPad에서 1개를 허용해야 합니다. 모두 언제든 시스템 설정에서 바꿀 수 있습니다.</p>
<table><thead><tr><th>어디서</th><th>권한</th><th>왜 필요한가요</th></tr></thead><tbody>
<tr><td>Mac</td><td>화면 기록</td><td>iPad가 이 Mac의 화면을 볼 수 있게 합니다. 허용한 뒤 macOS가 ScreenHop Host를 다시 열라고 할 수 있습니다.</td></tr>
<tr><td>Mac</td><td>손쉬운 사용</td><td>iPad로 이 Mac의 포인터 이동·클릭·입력을 할 수 있게 합니다.</td></tr>
<tr><td>iPad</td><td>로컬 네트워크</td><td>같은 Wi-Fi에 있는 내 Mac(과 SSH 기기)을 찾는 데 씁니다.</td></tr></tbody></table>
<p>Mac: 시스템 설정 › 개인정보 보호 및 보안 › <strong>화면 기록</strong> / <strong>손쉬운 사용</strong>에서 ScreenHop Host를 켭니다. ScreenHop Host를 처음 열면 안내 창이 이 설정을 열어 줍니다.<br>iPad: 설정 › ScreenHop › <strong>로컬 네트워크</strong>를 켭니다.</p>

<h2 id="pairing">처음 연결할 때</h2>
<ol>
<li>iPad에서 목록의 Mac을 누릅니다.</li>
<li>iPad와 Mac 양쪽에 <strong>같은 6자리 코드</strong>가 보이는지 확인합니다. 다르면 [거부]하세요.</li>
<li>Mac 메뉴 막대의 ScreenHop Host 창에서 <strong>[허용]</strong>을 누릅니다.</li>
</ol>
<p>한 번 짝지으면 다음부터는 자동으로 연결됩니다. 짝짓기를 지우려면 Mac의 ScreenHop Host 메뉴 › 짝지은 iPad에서 [해제]하고, iPad에서는 앱 설정의 ‘페어링한 Mac’에서 잊기를 하세요. 해제하면 그 iPad는 다시 짝지어야 합니다.</p>

<h2 id="wifi">같은 Wi-Fi</h2>
<p>ScreenHop은 <strong>같은 Wi-Fi(같은 로컬 네트워크)</strong>의 iPad와 Mac을 직접 이어 줍니다. 인터넷을 거치는 중계 서버나 계정은 없습니다. 목록에 Mac이 보이지 않으면 아래 <a href="#trouble">문제 해결</a>을 확인하세요.</p>
<p class="muted">USB 케이블 연결은 지금 지원하지 않습니다.</p>

<h2 id="outside">밖에서 쓰기 (Tailscale 등 VPN)</h2>
<p>집 밖에서는 <strong>Tailscale</strong> 같은 VPN을 직접 설정해 쓸 수 있습니다. 목록에 자동으로 나타나지 않으므로 Mac의 주소(Tailscale IP, 예: 100.x.x.x)를 iPad에서 <strong>직접 입력</strong>해 추가하세요.</p>
<ol>
<li>Mac과 iPad 모두에 Tailscale 등 VPN을 켭니다(같은 계정·같은 네트워크).</li>
<li>iPad ScreenHop의 연결 목록에서 <strong>주소로 Mac 추가</strong>를 열고 Mac의 VPN 주소(IP 또는 호스트 이름)를 넣습니다.</li>
<li>이후 짝짓기·연결은 같은 Wi-Fi일 때와 똑같습니다.</li>
</ol>
<p class="muted">VPN은 이용자가 직접 설정해야 하며, ScreenHop은 VPN이나 인터넷 중계를 제공하지 않습니다. 내가 소유하거나 사용 권한이 있는 Mac에만 연결하세요.</p>

<h2 id="lock">Mac 화면이 잠겼을 때</h2>
<p>ScreenHop은 <strong>Mac에 사용자가 로그인해 있는 상태</strong>에서 동작합니다. Mac이 잠기거나 로그인 화면이면 iPad에서 풀 수 없고, <strong>Mac에서 직접 잠금을 풀어야</strong> 합니다. 이는 보안을 위한 macOS의 제한입니다. 잠금이 풀리면 연결이 이어집니다.</p>
<p>자리를 비우기 전에 Mac이 잠자기·잠금으로 들어가는 것이 걱정되면 Mac 메뉴 막대의 ScreenHop Host 메뉴에서 ‘연결 중 Mac 잠자기 방지’를 켜 두세요.</p>

<h2 id="trouble">문제 해결</h2>
<h3>목록에 내 Mac이 보이지 않아요</h3>
<ul>
<li>Mac에서 ScreenHop Host가 실행 중인지 확인하세요. 메뉴 막대에 아이콘이 있어야 하고, 메뉴에 ‘같은 Wi-Fi의 iPad를 기다리는 중’이 보입니다.</li>
<li>iPad와 Mac이 <strong>같은 Wi-Fi</strong>인지 확인하세요. 게스트 Wi-Fi나 공유기의 ‘기기 간 격리(AP 격리)’가 켜져 있으면 서로 보이지 않을 수 있습니다.</li>
<li>iPad 설정 › ScreenHop › <strong>로컬 네트워크</strong>가 켜져 있는지 확인하세요.</li>
<li>VPN(Tailscale 등)을 쓰는 중이면 목록에 나오지 않습니다. Mac 주소를 직접 입력해 추가하세요(주소로 Mac 추가).</li>
<li>그래도 안 되면 Mac의 ScreenHop Host를 종료했다가 다시 열고, iPad 앱도 다시 열어 보세요.</li>
</ul>
<h3>연결은 됐는데 화면이 검게 보이거나 안 보여요</h3>
<p>Mac의 시스템 설정 › 개인정보 보호 및 보안 › <strong>화면 기록</strong>에서 ScreenHop Host가 켜져 있는지 확인하세요. 방금 켰다면 ScreenHop Host를 다시 열어야 적용될 수 있습니다. Mac이 잠겨 있지는 않은지도 확인하세요.</p>
<h3>화면은 보이는데 클릭·입력이 안 돼요</h3>
<p>시스템 설정 › 개인정보 보호 및 보안 › <strong>손쉬운 사용</strong>에서 ScreenHop Host를 켜세요. 비밀번호 입력란처럼 macOS가 ‘보안 입력’으로 보호하는 곳에서는 일부 입력이 막힐 수 있습니다.</p>
<h3>“Mac 도우미를 업데이트하세요”라고 떠요</h3>
<p>iPad 앱과 Mac 도우미의 연결 규격(프로토콜) 버전이 달라서입니다. <a href="download.html">Mac 도우미 페이지</a>에서 최신 ScreenHop Host를 받아 설치하세요. 반대로 도우미가 더 새로우면 iPad 앱을 업데이트하세요.</p>
<h3>연결이 느리거나 자주 끊겨요</h3>
<ul>
<li>iPad와 Mac(또는 공유기) 사이의 Wi-Fi 신호를 확인하세요. 가능하면 같은 5GHz Wi-Fi에 두세요.</li>
<li>Mac이 잠자기에 들어가지 않았는지 확인하세요.</li>
<li>Mac 메뉴 막대의 ScreenHop Host 메뉴에서 화질·프레임 설정(지연·균형·데이터 절약 등)을 바꿔 볼 수 있습니다.</li>
</ul>
<h3>한/영 전환은 어떻게 하나요?</h3>
<p>입력 소스 전환은 Mac의 입력기가 처리합니다. Mac에서 쓰는 전환 키(예: Caps Lock, Control+Space)를 그대로 쓰세요.</p>
<h3>그래도 해결되지 않아요</h3>
<p>iPad 모델·iPadOS 버전, Mac 모델·macOS 버전, 같은 Wi-Fi인지 여부, 어느 단계에서 멈추는지를 적어 <a href="#contact">문의</a>해 주세요.</p>

<h2 id="data">내 화면 정보는 어디로 가나요?</h2>
<p>회사 서버로 가지 않습니다. 화면·키 입력·클립보드·터미널 내용은 <strong>내 iPad와 내 Mac(또는 내가 지정한 SSH 서버) 사이에서만 암호화되어</strong> 오갑니다. 계정이 없고, 광고·분석·추적 SDK도 없습니다. 자세한 내용은 <a href="privacy.html">개인정보 처리방침</a>을 보세요.</p>

<h2 id="uninstall">지우는 방법</h2>
<ul>
<li><strong>iPad 앱</strong>: 홈 화면에서 ScreenHop을 길게 눌러 앱 삭제. 짝지은 Mac의 신뢰 키·SSH 정보까지 지우려면 삭제하기 전에 앱 설정의 ‘페어링한 Mac’, SSH 호스트·키 관리에서 먼저 지우세요.</li>
<li><strong>Mac 도우미</strong>: <a href="download.html#uninstall">Mac 도우미 삭제 방법</a>을 보세요.</li>
</ul>

<h2 id="contact">문의</h2>
<p>Code Black Inc. · {mail("ko")}</p>
"""

KO["download"] = f"""
<h1>ScreenHop Host for Mac</h1>
<p class="lead">iPad의 ScreenHop 앱으로 이 Mac을 쓰기 위한 <strong>무료 도우미</strong>입니다. 메뉴 막대에서 실행되며 개인정보를 수집하지 않습니다.</p>
@@DLBOX@@
<h2>요구 사항</h2>
<ul>
<li>macOS 14 이상 (Apple Silicon·Intel 모두 지원), 사용자가 로그인한 상태</li>
<li>iPad에 <strong>ScreenHop</strong> 앱 설치 @@APPSTORE@@</li>
<li><strong>같은 Wi-Fi</strong>. 밖에서는 Tailscale 같은 VPN을 직접 설정하고 iPad에서 Mac 주소를 직접 입력할 수 있습니다. USB 케이블 연결은 지원하지 않습니다.</li>
</ul>
<h2>설치 3단계</h2>
<ol>
<li>내려받은 <strong>ScreenHop-Host-<em>버전</em>.dmg</strong>를 엽니다.</li>
<li><strong>ScreenHop Host</strong>를 <strong>응용 프로그램</strong> 폴더로 끌어다 놓습니다.</li>
<li>응용 프로그램에서 ScreenHop Host를 실행하고, 안내에 따라 <strong>화면 기록</strong>과 <strong>손쉬운 사용</strong>을 허용합니다. 허용한 뒤 macOS가 앱을 다시 열라고 할 수 있습니다.</li>
</ol>
<p class="muted">ScreenHop Host는 메뉴 막대에서 실행됩니다(Dock에 창이 뜨지 않을 수 있어요). 메뉴에서 ‘로그인 시 열기’를 켜 두면 Mac을 켤 때마다 자동으로 준비됩니다.</p>
<h2>권한 2개</h2>
<table><thead><tr><th>권한</th><th>용도</th></tr></thead><tbody>
<tr><td>화면 기록</td><td>이 Mac의 화면을 iPad에 보여 주기 위해 필요합니다.</td></tr>
<tr><td>손쉬운 사용</td><td>iPad에서 마우스와 키보드를 조작하기 위해 필요합니다.</td></tr></tbody></table>
<p>시스템 설정 › 개인정보 보호 및 보안에서 언제든 켜고 끌 수 있습니다.</p>
<h2>처음 연결</h2>
<ol>
<li>같은 Wi-Fi에서 iPad의 ScreenHop을 열고 목록의 Mac을 누릅니다.</li>
<li>iPad와 Mac 양쪽에 같은 6자리 코드가 보이는지 확인합니다.</li>
<li>Mac 메뉴 막대에서 <strong>[허용]</strong>을 누릅니다. 이후에는 자동으로 연결됩니다.</li>
</ol>
<p>Mac이 잠겨 있으면 Mac에서 직접 잠금을 풀어야 합니다. 안 풀리거나 연결이 안 되면 <a href="index.html#trouble">문제 해결</a>을 보세요.</p>
<h2>개인정보</h2>
<p>화면·키 입력·클립보드는 암호화되어 로컬 네트워크로, 짝지은 iPad에만 전송됩니다. 개발사 서버로 보내는 것이 없고, 분석·광고 SDK도 없습니다. <a href="privacy.html">개인정보 처리방침</a></p>
<h2 id="uninstall">지우는 방법</h2>
<ol>
<li>삭제 전에 메뉴 막대의 ScreenHop Host 메뉴 › <strong>짝지은 iPad</strong>에서 iPad를 [해제]합니다(짝짓기 키가 지워지며, 그 iPad는 다시 짝지어야 합니다).</li>
<li>메뉴 막대에서 <strong>ScreenHop Host 종료</strong>를 누릅니다.</li>
<li>응용 프로그램 폴더에서 ScreenHop Host를 휴지통으로 옮깁니다.</li>
<li>시스템 설정 › 개인정보 보호 및 보안 › <strong>화면 기록</strong>, <strong>손쉬운 사용</strong>에서 ScreenHop Host 항목을 끄거나 제거합니다.</li>
</ol>
<h2>업데이트</h2>
<p>지금은 자동 업데이트가 없습니다. 새 버전은 이 페이지에서 다시 받아 응용 프로그램 폴더의 앱을 덮어 설치하세요. iPad 앱과 연결 규격이 바뀌는 업데이트는 같은 날 함께 배포하고, 필요하면 이 페이지에 “iPad 앱 x.y 이상 필요”를 적습니다.</p>
<p>도움이 필요하면 <a href="index.html">지원 페이지</a>를 보세요.</p>
"""

KO["privacy"] = f"""
<h1>ScreenHop 개인정보 처리방침</h1>
<p class="muted">시행일: {effective("ko")} · 버전 1.0</p>
<p>Code Black Inc.(이하 “회사”)는 iPad 앱 ScreenHop과 Mac 도우미 ScreenHop Host(이하 “앱”)에서 이용자의 개인정보를 다음과 같이 처리합니다.</p>

<h2>1. 수집하는 개인정보: 없음</h2>
<ul>
<li>앱은 개인정보를 수집하지 않으며, 회사 서버로 어떤 정보도 보내지 않습니다. 계정·회원가입이 없고, 회사가 운영하는 중계 서버도 없습니다.</li>
<li>광고, 분석, 추적 SDK를 쓰지 않습니다. 앱 추적 투명성(ATT) 요청도 하지 않습니다.</li>
<li><strong>Mac 화면 내용, 키보드·마우스·터치 입력, 클립보드, 소리, SSH 터미널 내용</strong>은 이용자의 iPad와 이용자의 Mac(또는 이용자가 지정한 SSH 서버) 사이에서만 암호화되어 오갑니다. 회사 서버로 수집하지 않으며, 세션 내용을 파일 등으로 영구 기록하지 않습니다(화면 표시를 위한 기기 메모리, 이용자가 직접 복사·붙여넣기한 내용은 예외).</li>
</ul>

<h2>2. 기기 안에만 저장되는 정보</h2>
<table><thead><tr><th>항목</th><th>목적</th><th>위치</th></tr></thead><tbody>
<tr><td>페어링한 Mac 이름·식별자, 직접 추가한 주소</td><td>연결 목록 표시, 자동 재연결</td><td>iPad 앱 데이터</td></tr>
<tr><td>기기 신원 키, 페어링한 Mac의 공개 키</td><td>암호화 연결, 다른 컴퓨터의 위장 방지</td><td>iPad Keychain(이 기기에만, iCloud 동기화 안 함)</td></tr>
<tr><td>SSH 호스트 정보(이름·주소·포트·사용자)</td><td>터미널 연결</td><td>iPad 앱 데이터</td></tr>
<tr><td>SSH 비밀번호·개인 키</td><td>SSH 인증</td><td>iPad Keychain(이 기기에만)</td></tr>
<tr><td>Mac 도우미: Mac의 신원 키, 페어링한 iPad의 이름·공개 키, 설정</td><td>페어링한 iPad만 연결 허용, 암호화 연결</td><td>Mac Keychain(이 Mac에만)·Mac 앱 설정. 메뉴 막대 › 페어링한 iPad에서 해제하면 지워짐</td></tr>
<tr><td>설정</td><td>앱 기능</td><td>iPad 앱 데이터</td></tr></tbody></table>
<p>이 정보는 회사로 전송되지 않습니다. 앱을 삭제하면 앱 데이터가 지워집니다(Keychain 항목은 iPadOS 정책에 따라 남을 수 있으며, 페어링한 Mac의 신뢰 키는 설정 › 페어링한 Mac에서 잊기로, SSH 비밀번호는 호스트 삭제로, SSH 개인 키는 터미널 › 키 관리에서 삭제로 지울 수 있습니다).</p>

<h2>3. 로컬 네트워크</h2>
<p>같은 Wi-Fi의 Mac(및 SSH 기기)을 찾기 위해 iPadOS 로컬 네트워크 권한을 요청합니다. 찾은 기기 정보는 기기 안에서 목록 표시에만 씁니다.</p>

<h2>4. 아동</h2>
<p>앱은 아동을 대상으로 하지 않으며 아동의 정보를 수집하지 않습니다.</p>

<h2>5. 문의</h2>
<p>회사는 이용자를 식별할 수 있는 정보를 보관하지 않으므로 열람·삭제 요청 대상 정보가 회사에 없습니다.</p>
<p>문의: {mail("ko")} · 지원: <a href="index.html">{BASE}</a></p>

<h2>6. 변경</h2>
<p>향후 광고 등 수집이 생기는 기능을 추가하면 앱 업데이트 전에 이 방침을 고치고 앱 안에서 알립니다.</p>
"""

# ───────────────────────── English ─────────────────────────
EN = {
    "lang": "en",
    "nav": {"support": "Support", "download": "Get the Mac helper", "privacy": "Privacy policy", "switch": "한국어"},
    "title": {
        "index": "ScreenHop Support · FAQ",
        "download": "Download ScreenHop Host for Mac",
        "privacy": "ScreenHop Privacy Policy",
    },
    "desc": {
        "index": "Setup, permissions, connecting and troubleshooting for ScreenHop (Mac remote screen and SSH terminal for iPad).",
        "download": "ScreenHop Host, the free helper that lets your iPad use your Mac. Requirements, install steps and how to remove it.",
        "privacy": "ScreenHop collects no personal information.",
    },
}

EN["index"] = f"""
<h1>ScreenHop Support</h1>
<p class="lead">A remote-screen app that lets you use <strong>your own Mac</strong> smoothly from your iPad, with an SSH terminal in the same app. Free, no ads.</p>
<div class="card"><p><strong>Contact</strong><br>Code Black Inc.<br>{mail("en")}</p>
<p class="muted">Please don’t send passwords or personal information shown on your screen. Tell us your device, versions and what happened so we can help quickly.</p></div>
<nav class="toc" aria-label="On this page"><ul>
<li><a href="#start">Getting started</a></li><li><a href="#permissions">The 3 permissions</a></li><li><a href="#pairing">Connecting the first time</a></li>
<li><a href="#wifi">Same Wi-Fi</a></li><li><a href="#outside">Away from home (Tailscale, VPN)</a></li><li><a href="#lock">When the Mac is locked</a></li>
<li><a href="#trouble">Troubleshooting</a></li><li><a href="#data">Where does my screen data go?</a></li><li><a href="#uninstall">Removing ScreenHop</a></li></ul></nav>

<h2 id="start">Getting started</h2>
<p>You need two things: the <strong>ScreenHop app on your iPad</strong> and the free <strong>ScreenHop Host helper on your Mac</strong>. The helper sends the Mac’s screen to the iPad and receives your input.</p>
<ol>
<li>Install ScreenHop Host on your Mac. → <a href="download.html">Get the Mac helper · install guide</a> (macOS 14 or later)</li>
<li>Put the iPad and the Mac on the <strong>same Wi-Fi</strong>.</li>
<li>Open ScreenHop on the iPad and tap your Mac in the list. When both screens show the same 6-digit code, click Allow on the Mac.</li>
</ol>
<p>No Mac at hand? Use <strong>Explore the demo</strong> (Explore Without a Mac) on the connection list to preview the screens.</p>

<h2 id="permissions">The 3 permissions</h2>
<p>You allow two on the Mac and one on the iPad. You can change any of them later in System Settings.</p>
<table><thead><tr><th>Where</th><th>Permission</th><th>Why it is needed</th></tr></thead><tbody>
<tr><td>Mac</td><td>Screen Recording</td><td>Lets the iPad see this Mac’s screens. After allowing, macOS may ask you to reopen ScreenHop Host.</td></tr>
<tr><td>Mac</td><td>Accessibility</td><td>Lets the iPad move the pointer, click and type on this Mac.</td></tr>
<tr><td>iPad</td><td>Local Network</td><td>Used to find your Mac (and SSH machines) on the same Wi-Fi.</td></tr></tbody></table>
<p>Mac: turn on ScreenHop Host under System Settings › Privacy &amp; Security › <strong>Screen Recording</strong> and <strong>Accessibility</strong>. The setup window that appears the first time you open ScreenHop Host takes you there.<br>iPad: Settings › ScreenHop › turn on <strong>Local Network</strong>.</p>

<h2 id="pairing">Connecting the first time</h2>
<ol>
<li>Tap your Mac in the iPad’s list.</li>
<li>Check that the iPad and the Mac show the <strong>same 6-digit code</strong>. If they differ, choose Deny.</li>
<li>In the ScreenHop Host window from the Mac’s menu bar, click <strong>Allow</strong>.</li>
</ol>
<p>After you pair once, the iPad connects automatically next time. To undo pairing, choose Remove under Paired iPads in the ScreenHop Host menu on the Mac, and forget the Mac under “Paired Macs” in the iPad app’s settings. A removed iPad has to pair again.</p>

<h2 id="wifi">Same Wi-Fi</h2>
<p>ScreenHop connects an iPad and a Mac directly on the <strong>same Wi-Fi (same local network)</strong>. There is no internet relay server and no account. If your Mac isn’t listed, see <a href="#trouble">Troubleshooting</a>.</p>
<p class="muted">Connecting by USB cable is not supported at the moment.</p>

<h2 id="outside">Away from home (Tailscale or another VPN)</h2>
<p>Away from home you can set up a VPN such as <strong>Tailscale</strong> yourself. The Mac won’t appear in the list automatically, so <strong>type its address</strong> (its Tailscale IP, e.g. 100.x.x.x) into the iPad.</p>
<ol>
<li>Turn on Tailscale or your VPN on both the Mac and the iPad (same account / same network).</li>
<li>On the connection list in ScreenHop, open <strong>Add Mac by Address</strong> and enter the Mac’s VPN address (IP or host name).</li>
<li>Pairing and connecting then work the same as on the same Wi-Fi.</li>
</ol>
<p class="muted">You set up the VPN yourself; ScreenHop does not provide a VPN or an internet relay. Connect only to Macs you own or are allowed to use.</p>

<h2 id="lock">When the Mac is locked</h2>
<p>ScreenHop works while <strong>a user is logged in on the Mac</strong>. If the Mac is locked or at the login screen, you can’t unlock it from the iPad — <strong>unlock it at the Mac itself</strong>. This is a macOS security limit. Once it is unlocked, the connection continues.</p>
<p>If you’re worried about the Mac sleeping or locking while you’re away, turn on “Keep Mac awake while connected” in the ScreenHop Host menu on the Mac.</p>

<h2 id="trouble">Troubleshooting</h2>
<h3>My Mac isn’t in the list</h3>
<ul>
<li>Check that ScreenHop Host is running on the Mac. Its icon should be in the menu bar, and the menu says “Waiting for iPad on this Wi-Fi”.</li>
<li>Check that the iPad and Mac are on the <strong>same Wi-Fi</strong>. A guest network, or a router’s “client/AP isolation” setting, can keep devices from seeing each other.</li>
<li>Check Settings › ScreenHop › <strong>Local Network</strong> on the iPad.</li>
<li>If you use a VPN (Tailscale, etc.), the Mac won’t be listed. Type its address.</li>
<li>Still nothing? Quit and reopen ScreenHop Host on the Mac, and reopen the iPad app.</li>
</ul>
<h3>It connects, but the screen is black or blank</h3>
<p>On the Mac, check that ScreenHop Host is turned on under System Settings › Privacy &amp; Security › <strong>Screen Recording</strong>. If you just turned it on, reopen ScreenHop Host. Also make sure the Mac isn’t locked.</p>
<h3>I can see the screen but clicks and typing do nothing</h3>
<p>Turn on ScreenHop Host under System Settings › Privacy &amp; Security › <strong>Accessibility</strong>. Some input can be blocked where macOS protects “secure input”, such as password fields.</p>
<h3>It says “Update the Mac helper”</h3>
<p>The iPad app and the Mac helper use different connection (protocol) versions. Get the latest ScreenHop Host from the <a href="download.html">Mac helper page</a> and install it. If the helper is newer instead, update the iPad app.</p>
<h3>It’s slow or keeps disconnecting</h3>
<ul>
<li>Check the Wi-Fi signal between the iPad and the Mac (or router). Prefer the same 5 GHz network if you can.</li>
<li>Make sure the Mac hasn’t gone to sleep.</li>
<li>In the ScreenHop Host menu on the Mac you can try the picture and frame-rate settings (Latency, Balanced, Data saver, and so on).</li>
</ul>
<h3>How do I switch between Korean and English input?</h3>
<p>Input-source switching is handled by the Mac’s input methods. Use the same switch key you use on the Mac (for example Caps Lock or Control-Space).</p>
<h3>Still stuck?</h3>
<p>Tell us your iPad model and iPadOS version, your Mac model and macOS version, whether they are on the same Wi-Fi, and where it stops, then <a href="#contact">contact us</a>.</p>

<h2 id="data">Where does my screen data go?</h2>
<p>Not to our servers. Your screen, keystrokes, clipboard and terminal contents travel <strong>encrypted, only between your iPad and your Mac (or the SSH server you choose)</strong>. There are no accounts, and no ad, analytics or tracking SDKs. See the <a href="privacy.html">privacy policy</a>.</p>

<h2 id="uninstall">Removing ScreenHop</h2>
<ul>
<li><strong>iPad app</strong>: touch and hold ScreenHop on the Home Screen and delete the app. To also clear stored Mac trust keys and SSH details, remove them first under “Paired Macs” and the SSH host and key management screens in the app’s settings.</li>
<li><strong>Mac helper</strong>: see <a href="download.html#uninstall">how to remove the Mac helper</a>.</li>
</ul>

<h2 id="contact">Contact</h2>
<p>Code Black Inc. · {mail("en")}</p>
"""

EN["download"] = f"""
<h1>ScreenHop Host for Mac</h1>
<p class="lead">The <strong>free helper</strong> that lets the ScreenHop app on your iPad use this Mac. It runs in the menu bar and collects no personal information.</p>
@@DLBOX@@
<h2>Requirements</h2>
<ul>
<li>macOS 14 or later (Apple Silicon and Intel), with a user logged in</li>
<li>The <strong>ScreenHop</strong> app on your iPad @@APPSTORE@@</li>
<li>The <strong>same Wi-Fi</strong>. Away from home you can set up a VPN such as Tailscale yourself and type the Mac’s address into the iPad. USB cable connection is not supported.</li>
</ul>
<h2>Install in 3 steps</h2>
<ol>
<li>Open the downloaded <strong>ScreenHop-Host-<em>version</em>.dmg</strong>.</li>
<li>Drag <strong>ScreenHop Host</strong> into the <strong>Applications</strong> folder.</li>
<li>Open ScreenHop Host from Applications and follow the prompts to allow <strong>Screen Recording</strong> and <strong>Accessibility</strong>. After you allow them, macOS may ask you to reopen the app.</li>
</ol>
<p class="muted">ScreenHop Host runs in the menu bar (you may not see a Dock window). Turn on “Open at login” in its menu to have it ready whenever the Mac starts.</p>
<h2>The 2 permissions</h2>
<table><thead><tr><th>Permission</th><th>What it is for</th></tr></thead><tbody>
<tr><td>Screen Recording</td><td>To show this Mac’s screen on the iPad.</td></tr>
<tr><td>Accessibility</td><td>To control the mouse and keyboard from the iPad.</td></tr></tbody></table>
<p>You can turn either on or off at any time under System Settings › Privacy &amp; Security.</p>
<h2>Connecting the first time</h2>
<ol>
<li>On the same Wi-Fi, open ScreenHop on the iPad and tap your Mac in the list.</li>
<li>Check that the iPad and the Mac show the same 6-digit code.</li>
<li>Click <strong>Allow</strong> in the Mac’s menu bar. After that it connects automatically.</li>
</ol>
<p>If the Mac is locked, unlock it at the Mac itself. If it won’t connect, see <a href="index.html#trouble">Troubleshooting</a>.</p>
<h2>Privacy</h2>
<p>Your screen, keystrokes and clipboard go encrypted over the local network to your paired iPad only. Nothing is sent to our servers, and there are no analytics or ad SDKs. <a href="privacy.html">Privacy policy</a></p>
<h2 id="uninstall">Removing it</h2>
<ol>
<li>Before deleting, open the ScreenHop Host menu in the menu bar › <strong>Paired iPads</strong> and choose Remove for your iPad (this deletes the pairing key; that iPad would need to pair again).</li>
<li>Choose <strong>Quit ScreenHop Host</strong> in the menu bar.</li>
<li>Move ScreenHop Host from the Applications folder to the Trash.</li>
<li>Under System Settings › Privacy &amp; Security › <strong>Screen Recording</strong> and <strong>Accessibility</strong>, turn off or remove the ScreenHop Host entries.</li>
</ol>
<h2>Updates</h2>
<p>There is no automatic update for now. Download the new version from this page and install it over the app in Applications. When an update changes the connection protocol, it ships the same day as the iPad app, and this page will say “requires iPad app x.y or later” if needed.</p>
<p>Need help? See the <a href="index.html">support page</a>.</p>
"""

EN["privacy"] = f"""
<h1>ScreenHop Privacy Policy</h1>
<p class="muted">Effective date: {effective("en")} · Version 1.0</p>
<p>Code Black Inc. (“we”) handles your information in the iPad app ScreenHop and the Mac helper ScreenHop Host (together, “the apps”) as described below.</p>

<h2>1. Personal information we collect: none</h2>
<ul>
<li>The apps do not collect personal information and send nothing to our servers. There are no accounts or sign-ups, and we run no relay servers.</li>
<li>The apps use no advertising, analytics or tracking SDKs. They do not show an App Tracking Transparency (ATT) prompt.</li>
<li><strong>Your Mac’s screen contents, keyboard, mouse and touch input, clipboard, sound and SSH terminal contents</strong> travel encrypted only between your iPad and your Mac (or the SSH server you specify). We do not collect them on our servers and do not permanently record session contents to files (except device memory used to display the screen, and content you yourself copy and paste).</li>
</ul>

<h2>2. Information stored only on your devices</h2>
<table><thead><tr><th>Item</th><th>Purpose</th><th>Where</th></tr></thead><tbody>
<tr><td>Names and identifiers of paired Macs, addresses you add yourself</td><td>Showing the connection list, automatic reconnecting</td><td>iPad app data</td></tr>
<tr><td>Device identity key, public keys of paired Macs</td><td>Encrypted connections, preventing other computers from impersonating yours</td><td>iPad Keychain (this device only, not synced with iCloud)</td></tr>
<tr><td>SSH host details (name, address, port, user)</td><td>Terminal connections</td><td>iPad app data</td></tr>
<tr><td>SSH passwords and private keys</td><td>SSH authentication</td><td>iPad Keychain (this device only)</td></tr>
<tr><td>Mac helper: the Mac’s identity key, paired iPads’ names and public keys, settings</td><td>Allow only paired iPads, encrypted connections</td><td>Mac Keychain (this Mac only) and app settings. Removed when you unpair the iPad from the menu bar › Paired iPads</td></tr>
<tr><td>Settings</td><td>App features</td><td>iPad app data</td></tr></tbody></table>
<p>This information is not sent to us. Deleting the app removes its data (Keychain items may remain under iPadOS policy; you can remove a paired Mac’s trust key with Forget under Settings › Paired Macs, SSH passwords by deleting the host, and SSH private keys under Terminal › Key management).</p>

<h2>3. Local network</h2>
<p>The apps ask for the iPadOS Local Network permission to find Macs (and SSH machines) on the same Wi-Fi. Information about discovered devices is used only on your device to show the list.</p>

<h2>4. Children</h2>
<p>The apps are not directed to children and do not collect children’s information.</p>

<h2>5. Contact</h2>
<p>Because we hold no information that can identify you, there is nothing on our side to access or delete on request.</p>
<p>Contact: {mail("en")} · Support: <a href="index.html">{BASE}en/</a></p>

<h2>6. Changes</h2>
<p>If we add features that involve collection, such as advertising, we will update this policy before the app update and tell you in the app.</p>
"""

LANGS = {"ko": KO, "en": EN}


def dlbox(lang):
    h = CFG["host"]
    if h["dmgUrl"]:
        meta = " · ".join(x for x in [("v" + h["version"]) if h["version"] else "", h["size"], h["date"]] if x)
        sha = f'<p class="small">SHA-256: <code>{esc(h["dmgSha256"])}</code></p>' if h["dmgSha256"] else ""
        label = "다운로드" if lang == "ko" else "Download"
        return f'<div class="card dl"><p><a class="btn" href="{esc(h["dmgUrl"])}">{label} ScreenHop-Host-{esc(h["version"])}.dmg</a></p><p class="muted small">{esc(meta)}</p>{sha}</div>'
    if lang == "ko":
        return '<div class="card dl soon"><p><strong>곧 제공됩니다</strong></p><p class="muted">ScreenHop Host의 다운로드 파일을 준비하고 있습니다. 준비되면 이 자리에 받기 버튼이 나타납니다.</p></div>'
    return '<div class="card dl soon"><p><strong>Coming soon</strong></p><p class="muted">The ScreenHop Host download is being prepared. The download button will appear here when it is ready.</p></div>'


def appstore(lang):
    u = CFG["appStoreUrl"]
    if u:
        return f'(<a href="{esc(u)}">App Store</a>)'
    return "(App Store 링크는 출시 후 안내)" if lang == "ko" else "(App Store link after release)"


def page(lang, name):
    L = LANGS[lang]
    other = "en" if lang == "ko" else "ko"
    pre = "" if lang == "ko" else "../"
    # 같은 파일 이름의 반대 언어 페이지로
    page_name = "" if name == "index" else name + ".html"
    sw = ("en/" if lang == "ko" else "../") + page_name
    body = L[name].replace("@@DLBOX@@", dlbox(lang)).replace("@@APPSTORE@@", appstore(lang))
    nav = L["nav"]
    cur = lambda n: ' aria-current="page"' if n == name else ""
    url = BASE + ("en/" if lang == "en" else "") + ("" if name == "index" else name + ".html")
    ko_url = BASE + ("" if name == "index" else name + ".html")
    en_url = BASE + "en/" + ("" if name == "index" else name + ".html")
    foot = (
        f'Code Black Inc. · {mail(lang)}'
        if lang == "en"
        else f'Code Black Inc. · {mail(lang)}'
    )
    return f"""<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'self'; img-src 'self'; base-uri 'none'; form-action 'none'">
<title>{esc(L["title"][name])}</title><meta name="description" content="{esc(L["desc"][name])}">
<link rel="canonical" href="{url}"><link rel="alternate" hreflang="ko" href="{ko_url}"><link rel="alternate" hreflang="en" href="{en_url}">
<link rel="icon" href="{pre}assets/icon.png"><link rel="stylesheet" href="{pre}style.css"></head>
<body><header class="top"><div class="wrap bar"><a class="brand" href="{'index.html' if lang == 'ko' else 'index.html'}"><img src="{pre}assets/icon.png" alt="" width="32" height="32"><span>ScreenHop</span></a>
<nav aria-label="{'메뉴' if lang == 'ko' else 'Menu'}"><a href="index.html"{cur("index")}>{nav["support"]}</a><a href="download.html"{cur("download")}>{nav["download"]}</a><a href="privacy.html"{cur("privacy")}>{nav["privacy"]}</a><a lang="{other}" href="{sw}">{nav["switch"]}</a></nav></div></header>
<main class="wrap">{body}</main>
<footer class="wrap foot">{foot}</footer></body></html>
"""


def main():
    (ROOT / "en").mkdir(exist_ok=True)
    for lang in ("ko", "en"):
        for name in ("index", "download", "privacy"):
            out = ROOT / ("en" if lang == "en" else "") / (name + ".html")
            out.write_text(page(lang, name), encoding="utf-8")
            print("wrote", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
