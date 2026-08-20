---
marp: true
theme: default
paginate: true
size: 16:9
title: 언제 우리는 AI 에이전트를 쓰는가
description: 자동화, 신뢰, 실제문제로 보는 AI 에이전트의 사용 조건
---

<style>
section {
  font-family: "Aptos", "Malgun Gothic", "Noto Sans KR", sans-serif;
  color: #111827;
  background: #f8fafc;
  padding: 52px 64px;
}
h1, h2, h3, p { letter-spacing: 0; }
h1 { font-size: 56px; line-height: 1.12; margin: 0 0 22px; }
h2 { font-size: 40px; line-height: 1.18; margin: 0 0 22px; }
h3 { font-size: 22px; margin: 0 0 10px; }
p, li { font-size: 23px; line-height: 1.42; }
small { font-size: 17px; color: #64748b; }
.kicker {
  display: inline-block;
  font-size: 16px;
  font-weight: 800;
  letter-spacing: 1px;
  color: #2563eb;
  background: #e0ecff;
  border-radius: 999px;
  padding: 5px 14px;
  margin: 0 0 18px;
}
.subtitle { font-size: 29px; color: #475569; line-height: 1.35; }
.lead { font-size: 32px; line-height: 1.28; font-weight: 800; }
.muted { color: #64748b; }
.accent { color: #2563eb; }
.grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: 22px; }
.grid3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px; }
.grid4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; }
.card, .metric, .quote, .panel {
  border: 1px solid #dbe3ee;
  background: #ffffff;
  border-radius: 8px;
  padding: 22px;
  box-shadow: 0 10px 24px rgba(15, 23, 42, 0.06);
}
.metric { min-height: 140px; }
.metric .num {
  display: block;
  font-size: 36px;
  font-weight: 900;
  color: #2563eb;
  line-height: 1;
  margin-bottom: 12px;
}
.claim {
  border-left: 8px solid #2563eb;
  background: #eef4ff;
  border-radius: 0 8px 8px 0;
  padding: 18px 24px;
  margin: 0 0 22px;
}
.claim p { font-size: 28px; font-weight: 800; margin: 0; color: #1d4ed8; }
.quote {
  border-left: 8px solid #f59e0b;
  background: #fffbeb;
}
.quote p { font-size: 30px; font-weight: 800; margin: 0; }
.tag {
  display: inline-block;
  padding: 6px 12px;
  border: 1px solid #cbd5e1;
  border-radius: 999px;
  color: #1d4ed8;
  background: #eff6ff;
  font-weight: 700;
  font-size: 17px;
  margin: 0 8px 12px 0;
}
.flow {
  display: grid;
  grid-template-columns: 1fr 40px 1fr 40px 1fr;
  align-items: stretch;
  gap: 12px;
  margin-top: 12px;
}
.flow.four { grid-template-columns: 1fr 32px 1fr 32px 1fr 32px 1fr; }
.flow .step {
  border: 1px solid #dbe3ee;
  background: #ffffff;
  border-radius: 8px;
  padding: 18px;
  min-height: 116px;
}
.arrow {
  display: flex;
  align-items: center;
  justify-content: center;
  color: #2563eb;
  font-size: 30px;
  font-weight: 900;
}
.ladder { display: grid; grid-template-columns: 1fr; gap: 10px; }
.ladder .rung {
  display: grid;
  grid-template-columns: 190px 1fr;
  align-items: center;
  border: 1px solid #dbe3ee;
  background: #fff;
  border-radius: 8px;
  overflow: hidden;
}
.rung strong {
  background: #eff6ff;
  color: #1d4ed8;
  padding: 15px 18px;
  height: 100%;
}
.rung span { padding: 15px 18px; font-size: 21px; }
.screen {
  border: 1px solid #cbd5e1;
  background: #0f172a;
  color: #e5e7eb;
  border-radius: 8px;
  padding: 18px;
  font-family: Consolas, monospace;
  font-size: 17px;
  line-height: 1.5;
}
.band {
  background: #e0f2fe;
  border: 1px solid #bae6fd;
  border-radius: 8px;
  padding: 18px 24px;
}
.dark { background: #0f172a; color: #ffffff; }
.dark .subtitle, .dark small, .dark .muted { color: #cbd5e1; }
.dark .kicker { background: rgba(96,165,250,0.18); color: #93c5fd; }
.dark .card {
  background: rgba(255,255,255,0.08);
  border-color: rgba(255,255,255,0.18);
  color: #ffffff;
  box-shadow: none;
}
.section {
  background: #0f172a;
  color: #ffffff;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.section .kicker { background: rgba(96,165,250,0.18); color: #93c5fd; }
.section h1 { font-size: 64px; margin-bottom: 14px; }
.section .subtitle { color: #cbd5e1; }
</style>

<!-- _class: dark -->

# 언제 우리는  
# AI 에이전트를 쓰는가

<p class="subtitle">자동화 · 신뢰 · 실제문제</p>

<small>AI를 자기 업무에 써야 하는 연구자 · 실무자 · 관리자 · 기획자를 위한 강의</small>

<!--
오늘은 AI를 잘 쓰자는 이야기가 아닙니다. AI 에이전트가 언제 실제 업무에 들어오는지를 보려 합니다. 두 가지를 묻습니다. 왜 기능이 좋아도 잘 안 쓰이는가. 그리고 어떻게 해야 실제로 쓰이는 앱을 만들 수 있는가.
-->

---

## 자동화. 신뢰. 실제문제.

<span class="kicker">세 축</span>

<div class="grid3">
<div class="metric"><span class="num">①</span><h3>자동화</h3><p>선택 부담을 줄인다.</p></div>
<div class="metric"><span class="num">②</span><h3>신뢰</h3><p>위임을 가능하게 한다.</p></div>
<div class="metric"><span class="num">③</span><h3>실제문제</h3><p>사용 이유를 만든다.</p></div>
</div>

<div class="claim" style="margin-top:22px"><p>자동화가 먼저다. 그러나 자동화만으로는 부족하다.</p></div>

<!--
세 축을 먼저 제시합니다. 자동화가 먼저입니다. 그러나 자동화만으로는 부족합니다. 신뢰가 필요합니다. 그리고 실제 문제가 있어야 합니다.
-->

---

## 만들고, 학회에서 소개하고, 쓰기 시작했다

<span class="kicker">출발점</span>

<div class="claim"><p>여러 앱을 만들어 학회에서 소개했고, 주변에서 쓰기 시작했다. 그 과정에서 본 차이는 AI 지식의 많고 적음이 아니었다.</p></div>

<div class="grid4">
<div class="card"><h3>연구</h3><p>질문·데이터·원고</p></div>
<div class="card"><h3>조사 현업</h3><p>자료·검증·보고</p></div>
<div class="card"><h3>강의·글쓰기</h3><p>설명·구성·표현</p></div>
<div class="card"><h3>데이터 분석</h3><p>해석·표·판단</p></div>
</div>

<!--
이 앱들은 직접 만들었고, 학회 등에서 소개했으며, 공개를 준비하면서 주변에서 일부 쓰기 시작했다. 그 경험에서 본 질문은 '무엇이 쓰고 싶은 앱을 만드는가'였고, 그 차이는 AI 지식의 많고 적음으로 설명되지 않았다.
-->

---

## 무엇을 만드나 → 언제 쓰나

<span class="kicker">질문의 변화</span>

<div class="flow">
<div class="step"><h3>처음 질문</h3><p class="lead">무엇을 만들 수 있나?</p></div>
<div class="arrow">→</div>
<div class="step"><h3>지금 질문</h3><p class="lead">언제 쓰고 싶어하나?</p></div>
<div class="arrow">→</div>
<div class="step"><h3>그래서 보는 것</h3><p>기능 목록이 아니라 사용 조건.</p></div>
</div>

<!--
처음 질문은 무엇을 만들 수 있나였습니다. 지금 질문은 다릅니다. 사람들이 언제 AI 에이전트를 사용하고 싶어하는가. 이제부터 사용 조건을 봅니다.
-->

---

## 연구 과정 전체를 수행한다

<span class="kicker">능력 · Research Pilot Academy</span>

<span class="tag">Research Pilot Academy</span>

<div class="flow four">
<div class="step"><h3>연구문제·데이터</h3><p>출발점을 받는다.</p></div>
<div class="arrow">→</div>
<div class="step"><h3>분석·추가 분석</h3><p>방법을 정하고 판단한다.</p></div>
<div class="arrow">→</div>
<div class="step"><h3>결과·해석</h3><p>연구문제와 비교한다.</p></div>
<div class="arrow">→</div>
<div class="step"><h3>표·원고</h3><p>문서로 만든다.</p></div>
</div>

<!--
대화창은 답을 줍니다. 에이전트는 과정을 수행합니다. 연구문제와 데이터를 받고, 분석 방법을 정하고, 결과를 연구문제와 비교하고, 필요한 추가 분석을 하고, 해석하고, 표와 원고까지 만듭니다. 이 과정이 1분 이내에 자동으로 진행됩니다.
-->

---

## 몇 달짜리 일을 한 흐름으로

<span class="kicker">능력 · 에이전트의 차원</span>

<div class="quote"><p>과거 연구자가 2–3달 걸리던 일을, 에이전트가 매우 짧은 시간에 하나의 흐름으로 수행한다.</p></div>

<p style="margin-top:24px">분석 방법 결정, 추가 분석 판단, 결과 도출, 해석, 표·원고 작성이 끊기지 않고 이어진다. 이것이 대화창과 다른 <strong class="accent">에이전트의 차원</strong>이다.</p>

<!--
학회에서 이 흐름을 소개했고 관심이 많았다. 지금은 공개를 준비 중이다. 여기서 먼저 보는 것은 대화창과 다른 에이전트의 차원이다.
-->

---

## 능력은 보였다. 이제 사용 조건이다.

<span class="kicker">전환</span>

<div class="grid2">
<div class="card">
<h3>확인한 것</h3>
<p class="lead">에이전트는 복잡한 과정을 수행한다.</p>
<p>Research Pilot Academy가 그 능력을 보여준다.</p>
</div>
<div class="card">
<h3>이 강의의 질문</h3>
<p class="lead">그렇다면 언제 쓰고 싶어지나?</p>
<p>능력이 아니라 사용 조건이다.</p>
</div>
</div>

<!--
Research Pilot Academy는 에이전트의 능력을 보여줍니다. 그러나 이 발표의 질문은 능력이 아닙니다. 사람들이 언제 사용하고 싶어하는가입니다. 이제부터 사용 조건을 봅니다.
-->

---

<!-- _class: section -->

<span class="kicker">조건 ①</span>

# 자동화

<p class="subtitle">선택은 부담. 그러나 보이지 않는 자동화는 불안.</p>

---

## 단계가 많으면 부담이 된다

<span class="kicker">자동화 · Proposal Studio</span>

<span class="tag">Proposal Studio</span>

<div class="grid2">
<div class="card">
<h3>설계</h3>
<p>제안서 앱을 8단계 프로세스로 만들었다. 체계는 분명했다.</p>
</div>
<div class="card">
<h3>설계하며 본 것</h3>
<p class="lead">단계가 많을수록 무거워진다.</p>
<p>직접 써 보고 일부 사용자와 써 보니, 선택이 도움보다 부담이 되기도 했다.</p>
</div>
</div>

<div class="claim" style="margin-top:20px"><p>선택지를 주는 것이 늘 돕는 것은 아니다. 사용자는 방법론보다 해결된 결과를 원한다.</p></div>

<!--
제안서 앱을 8단계로 설계했다. 체계는 분명했다. 그러나 직접 써 보고 일부 사용자와 함께 써 보니, 단계가 많을수록 부담이 됐다. 선택지를 많이 주는 것이 늘 돕는 것은 아니라는 설계 교훈을 얻었다.
-->

---

## 선택의 효과는 맥락적이다

<span class="kicker">자동화 · 단서</span>

<div class="grid2">
<div class="card">
<h3>직접 고를 때</h3>
<p>스스로 선택해야 더 잘하는 사람이 있다.</p>
</div>
<div class="card">
<h3>맡길 때</h3>
<p>신뢰하는 누군가가 골라줄 때 더 잘하는 사람도 있다.</p>
</div>
</div>

<p class="lead" style="margin-top:22px">사용자는 선택권 자체보다 적절한 위임을 원할 수 있다.</p>

<!--
선택의 효과는 단순하지 않습니다. 직접 고를 때 더 잘하는 사람이 있고, 신뢰하는 사람이 골라줄 때 더 잘하는 사람도 있습니다. Iyengar의 선택 연구도 선택이 늘 동기가 되는 건 아니라는 점을 보여줍니다. 사용자는 선택권 자체보다 적절한 위임을 원할 수 있습니다.
-->

---

## 자동화는 필요하다

<span class="kicker">자동화 · 원칙</span>

<div class="claim"><p>AI가 할 수 있으면, 사용자에게 고르게 하지 말고 AI가 한다.</p></div>

<div class="flow">
<div class="step"><h3>사용자 판단</h3><p>핵심 기준만 남긴다.</p></div>
<div class="arrow">→</div>
<div class="step"><h3>반복 작업</h3><p>AI가 먼저 처리한다.</p></div>
<div class="arrow">→</div>
<div class="step"><h3>결과 검토</h3><p>사람은 요점만 본다.</p></div>
</div>

<!--
그래서 자동화가 먼저입니다. 선택지가 많으면 부담이 됩니다. AI가 할 수 있으면 AI가 해야 합니다. 앱은 선택지를 많이 보여주기보다, 원한 결과에 가까운 자동 흐름을 먼저 제공해야 합니다.
-->

---

## 그러나 보이지 않으면 불안하다

<span class="kicker">자동화 · 역설</span>

<div class="grid2">
<div class="card">
<span class="tag">Plan Builder</span>
<h3>전자동 시도</h3>
<p>부담을 줄이려고, 거의 선택하지 않아도 한 번에 결과가 나오게 했다.</p>
</div>
<div class="card">
<h3>그런데 불안하다</h3>
<p class="lead">무엇을 기준으로 했는지 보이지 않는다.</p>
<p>직접 써 보고, 일부 사용자도 같은 불안을 말했다.</p>
</div>
</div>

<div class="quote" style="margin-top:18px"><p>“미리 물어보지도 않고 한다.”</p></div>

<!--
부담을 줄이려고 전자동으로 만들었다. 거의 선택하지 않아도 결과가 나오게 했다. 그러나 무엇을 기준으로 했는지 보이지 않으니, 직접 써 보고 일부 사용자도 불안하다고 느꼈다. 자동화는 AI가 사람 대신 선택하는 일이므로, 판단 근거는 보여야 한다.
-->

---

<!-- _class: section -->

<span class="kicker">조건 ②</span>

# 신뢰

<p class="subtitle">확인가능성만으로는 부족하다. 정합성이 신뢰를 만든다.</p>

---

## 관심은 검증보다 편집에 있었다

<span class="kicker">신뢰 · gWriter</span>

<div class="grid2">
<div class="card">
<span class="tag">gWriter</span>
<h3>설계자의 생각</h3>
<p>신뢰가 중요하니, 검증 기능을 붙이면 되리라 보았다.</p>
</div>
<div class="card">
<h3>다시 본 것</h3>
<p>검증 기능을 붙인 것만으로 사용 동기가 되지는 않았다.</p>
<p class="lead">가치를 준 건 편집 경험이었다.</p>
</div>
</div>

<div class="claim" style="margin-top:20px"><p>검증은 기능 목록이 아니라, 사용자의 불안과 책임 문제를 푸는 장치여야 한다.</p></div>

<!--
신뢰가 중요하다고 보아 gWriter에 검증 기능을 붙였다. 그러나 검증 기능을 붙인 것만으로 사용 동기가 되지는 않았다. 정작 가치를 준 것은 편집 경험이었다. 검증은 기능 목록이 아니라 불안과 책임 문제를 푸는 장치로 설계되어야 한다.
-->

---

## 확인가능성만으로는 부족하다

<span class="kicker">신뢰 · 정합성</span>

<div class="grid3">
<div class="card"><h3>코드</h3><p>있다고 분석이 맞는 것은 아니다.</p></div>
<div class="card"><h3>다운로드</h3><p>받았다고 결과가 맞는 것은 아니다.</p></div>
<div class="card"><h3>링크</h3><p>걸렸다고 근거가 맞는 것은 아니다.</p></div>
</div>

<div class="claim" style="margin-top:22px"><p>확인가능성은 필요조건이다. 그러나 중요한 것은 정합성이다.</p></div>

<!--
코드와 다운로드가 있다고 분석이 맞는 것은 아닙니다. 링크가 있다고 근거가 맞는 것도 아닙니다. 확인가능성은 필요합니다. 그러나 데이터, 분석, 코드, 해석, 공개 기준 사이의 정합성이 중요합니다.
-->

---

## 그럴듯한 결과를 검증한다

<span class="kicker">신뢰 · InsightValidationServer</span>

<span class="tag">InsightValidationServer</span>

<div class="flow">
<div class="step"><h3>생성</h3><p>그럴듯한 분석·요약</p></div>
<div class="arrow">→</div>
<div class="step"><h3>검증</h3><p>코드·데이터·결과·해석 대조</p></div>
<div class="arrow">→</div>
<div class="step"><h3>판정</h3><p>공개 가능 / 수정 필요</p></div>
</div>

<p class="lead" style="margin-top:22px">생성과 검증은 분리되어야 한다.</p>

<!--
좋은 에이전트는 생성과 검증을 분리해야 합니다. AI가 만든 결과가 그럴듯하다고 바로 업무 결과가 되는 것은 아닙니다. 그럴듯함과 공개 가능성은 다릅니다. 그래서 결과를 바로 믿지 않고 별도의 검증 절차로 넘깁니다.
-->

---

## 정합성이 공개 가능성을 만든다

<span class="kicker">신뢰 · 판정</span>

<p>정답률만으로는 부족하다. 기준 N, 셀 합계, 분석 단위, 공개 기준이 서로 맞아야 한다.</p>

<div class="screen" style="margin-top:16px">
BASE_N_MISMATCH &nbsp;&nbsp;&nbsp;&nbsp; 기준 N과 결과 N이 다름<br>
CELL_SUM_MISMATCH &nbsp; 셀 합계가 표 전체와 맞지 않음<br>
do_not_release &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 공개 전 수정 필요
</div>

<!--
정합성이 맞지 않으면 공개 가능한 결과가 아닙니다. 검증은 단순 점수 계산이 아닙니다. 결과가 업무 기준과 맞는지 확인하는 절차입니다. 기준 N, 셀 합계, 분석 단위, 공개 기준이 서로 맞아야 합니다.
-->

---

<!-- _class: section -->

<span class="kicker">조건 ③</span>

# 실제문제

<p class="subtitle">완전한 신뢰가 없어도, 매일 풀어야 할 문제가 있으면 쓴다.</p>

---

## 실제 문제가 있으면 쓴다

<span class="kicker">실제문제 · KWCS-QC</span>

<div class="grid2">
<div class="card">
<span class="tag">KWCS-QC</span>
<h3>상황</h3>
<p>매일 데이터가 들어온다. 검증·분석·해석이 반복된다.</p>
</div>
<div class="card">
<h3>사용 이유</h3>
<p class="lead">선택이 아니라 필요다.</p>
<p>매일 해야 하는 일이 있기 때문이다.</p>
</div>
</div>

<!--
최근 KWCS 관련 앱을 만들었습니다. 매일 데이터가 들어오고, 반드시 모니터링해야 하는 실제 문제가 있었습니다. 분석과 해석 기능이 필요했습니다. 이때 앱은 선택이 아니라 필요가 됩니다.
-->

---

## 매일 들어오는 데이터를 놓치지 않는다

<span class="kicker">실제문제 · 운영</span>

<div class="flow four">
<div class="step"><h3>수신</h3><p>매일 데이터가 온다.</p></div>
<div class="arrow">→</div>
<div class="step"><h3>QC</h3><p>검증한다.</p></div>
<div class="arrow">→</div>
<div class="step"><h3>자동 분석</h3><p>분석을 돌린다.</p></div>
<div class="arrow">→</div>
<div class="step"><h3>해석 준비</h3><p>의미로 잇는다.</p></div>
</div>

<p class="lead" style="margin-top:22px">완전한 신뢰가 어려워도, 해야 할 일이 있어서 쓴다.</p>

<!--
검증 과정을 완전히 신뢰하기 어렵더라도 매일같이 모니터링을 해야 합니다. 여기서는 AI 앱을 쓰느냐 마느냐가 문제가 아닙니다. 해야 할 일이 있습니다. 그래서 씁니다.
-->

---

## 데이터는 의미가 필요하다

<span class="kicker">실제문제 · ResearchPilot Data</span>

<div class="flow">
<div class="step"><h3>데이터</h3><p>숫자와 변수</p></div>
<div class="arrow">→</div>
<div class="step"><h3>분석</h3><p>표와 통계</p></div>
<div class="arrow">→</div>
<div class="step"><h3>의미</h3><p>무엇을 말하는가</p></div>
</div>

<div class="quote" style="margin-top:22px"><p>사람들은 데이터를 분석하고 싶은 게 아니라, 데이터가 무엇을 말하는지 알고 싶어 한다.</p></div>

<!--
사람들은 데이터를 단순히 분석하고 싶은 것이 아닙니다. 이미 가진 데이터의 의미를 알고 싶어 합니다. 그 의미를 의사결정에 쓰고 싶어 합니다. 보고서와 전략에도 쓰고 싶어 합니다.
-->

---

## 데이터의 의미를 업무 언어로

<span class="kicker">실제문제 · 해석 장치</span>

<span class="tag">ResearchPilot Data</span>

<div class="grid4">
<div class="card"><h3>상태 확인</h3><p>결측·변수·품질</p></div>
<div class="card"><h3>질문 제안</h3><p>무엇을 물을까</p></div>
<div class="card"><h3>해석</h3><p>결과의 의미</p></div>
<div class="card"><h3>연결</h3><p>보고서·전략·후속 질문</p></div>
</div>

<p class="lead" style="margin-top:22px">좋은 데이터 앱은 차트를 만드는 데서 끝나지 않는다.</p>

<!--
좋은 데이터 분석 앱은 차트를 만드는 데서 끝나지 않습니다. 데이터 상태를 점검하고, 분석 질문을 제안하고, 결과를 해석하고, 그 해석을 어디에 쓸 수 있는지까지 함께 판단합니다. 분석 도구가 아니라, 데이터의 의미를 업무 언어로 바꾸는 해석 장치입니다.
-->

---

<!-- _class: section -->

<span class="kicker">한 걸음 더</span>

# 좋은 앱은  
# 문제에서 출발한다

<p class="subtitle">때로는 틀 안의 해결이 아니라, 틀 밖의 해결이 필요하다.</p>

---

## 번역 문제가 아니었다

<span class="kicker">프레임 · Press Release Builder</span>

<div class="grid2">
<div class="card">
<span class="tag">Press Release Builder</span>
<h3>처음 해결</h3>
<p>번역을 고쳤다. 환각을 줄였다. 어색한 영어를 다듬었다.</p>
</div>
<div class="card">
<h3>남은 문제</h3>
<p class="lead">그래도 부족했다.</p>
<p>보도자료는 배포 가능한 메시지 구조여야 했다.</p>
</div>
</div>

<!--
처음에는 문제를 번역 문제로 보았습니다. 그래서 번역문을 고쳤습니다. 환각을 줄였습니다. 어색한 영어도 고쳤습니다. 문장 라이브러리도 만들었습니다. 그래도 충분하지 않았습니다. 문제는 번역 품질만이 아니었습니다.
-->

---

## 문장은 좋아졌지만 보도자료는 아니었다

<span class="kicker">프레임 · 재구성</span>

<div class="flow">
<div class="step"><h3>번역</h3><p>문장을 옮긴다.</p></div>
<div class="arrow">→</div>
<div class="step"><h3>재작성</h3><p>목적에 맞게 다시 쓴다.</p></div>
<div class="arrow">→</div>
<div class="step"><h3>메시지 재구성</h3><p>보도자료 구조로 바꾼다.</p></div>
</div>

<div class="claim" style="margin-top:22px"><p>번역을 고친 것이 아니다. 문제의 틀을 바꾸었다.</p></div>

<!--
번역을 고친 것이 아닙니다. 문제의 틀을 바꾸었습니다. 번역에서 재작성으로, 재작성에서 보도자료 메시지 재구성으로 옮겼습니다. 번역 문제가 아니라, 배포 가능한 메시지 구조의 문제였습니다.
-->

---

## 틀 안의 해결. 틀 밖의 해결.

<span class="kicker">프레임 · 관점 전환</span>

<div class="grid2">
<div class="card">
<h3>틀 안의 해결</h3>
<p class="lead">번역을 더 잘한다.</p>
<p>기존 문제 정의 안에서 품질을 올린다.</p>
</div>
<div class="card">
<h3>틀 밖의 해결</h3>
<p class="lead">보도자료로 다시 쓴다.</p>
<p>문제 정의 자체를 바꾼다.</p>
</div>
</div>

<p class="lead" style="margin-top:22px">혁신은 중심의 정답이 아니라 주변부의 다른 질문에서 시작한다.</p>

<!--
문제가 번역 품질이라고 보면 계속 문장을 고치게 됩니다. 이것은 틀 안의 해결입니다. 그러나 실제 문제는 보도자료로서 메시지가 작동하는가였습니다. 이것은 틀 밖의 해결입니다.
발표 메모: 큰 철학적 패러다임 전환이 아니라 업무 프레임 전환이다. Kuhn — 정상과학은 기존 패러다임 안의 퍼즐 풀이, 누적된 이상 현상이 전환의 계기. Cattani & Ferriani의 core/periphery — 중심은 규범에 묶이고 주변부는 새 조합의 자유가 크다. Painter·Daniels·Laubichler — 혁신은 과학 네트워크 주변부에서 더 불균형적으로 나타난다.
-->

---

## 수정 수준이 중요하다

<span class="kicker">프레임 · 판단</span>

<div class="ladder">
<div class="rung"><strong>표현</strong><span>문장이 어색한가?</span></div>
<div class="rung"><strong>절차</strong><span>작업 순서가 잘못되었는가?</span></div>
<div class="rung"><strong>프레임</strong><span>문제의 틀이 잘못되었는가?</span></div>
<div class="rung"><strong>질문</strong><span>애초에 다른 질문을 해야 하는가?</span></div>
</div>

<small>실패했을 때 무조건 다시 생성하지 않는다. 어느 수준을 고칠지 먼저 본다.</small>

<!--
실패가 생겼을 때 무조건 문장만 고치면 안 됩니다. 무엇을 고칠지 먼저 봐야 합니다. 표현 수준인가, 절차 수준인가, 업무 프레임 수준인가, 문제 정의 수준인가. 어떤 문제는 작업의 틀을 바꾸어야 해결됩니다.
-->

---

## 자동화는 판단의 수준을 포함한다

<span class="kicker">프레임 · PR Studio</span>

<span class="tag">PR Studio</span>

<div class="grid3">
<div class="card"><h3>대상</h3><p>누구에게 말하나</p></div>
<div class="card"><h3>목적</h3><p>무엇을 바꾸나</p></div>
<div class="card"><h3>메시지 프레임</h3><p>어떤 문제로 보나</p></div>
<div class="card"><h3>배포 가능성</h3><p>내보내도 되나</p></div>
<div class="card"><h3>피드백</h3><p>무엇이 반응하나</p></div>
<div class="card"><h3>다음 실험</h3><p>어디를 고치나</p></div>
</div>

<p class="lead" style="margin-top:20px">자동으로 실행하되, 어느 차원의 문제를 푸는지 판단한다.</p>

<!--
PR Studio는 단순히 보도자료나 유튜브 콘텐츠를 생성하는 앱이 아닙니다. 대상, 목적, 메시지 프레임, 배포 가능성, 피드백, 다음 실험을 함께 판단합니다. 좋은 에이전트는 단순 자동화가 아닙니다. 사람 대신 많은 일을 하되, 어느 차원의 문제를 풀고 있는지 판단합니다.
-->

---

## 세 조건

<span class="kicker">종합</span>

<div class="grid3">
<div class="metric"><span class="num">①</span><h3>자동화</h3><p>선택 부담을 줄인다.</p></div>
<div class="metric"><span class="num">②</span><h3>신뢰</h3><p>위임을 가능하게 한다.</p></div>
<div class="metric"><span class="num">③</span><h3>실제문제</h3><p>사용 이유를 만든다.</p></div>
</div>

<div class="claim" style="margin-top:22px"><p>하나만으로는 부족하다. 세 조건이 함께 설계되어야 한다.</p></div>

<!--
자동화는 선택 부담을 줄입니다. 신뢰는 위임을 가능하게 합니다. 실제문제는 사용 이유를 만듭니다. 하나만으로는 부족합니다.
-->

---

## 개발자에게: 도구보다 문제

<span class="kicker">권고 · 만드는 쪽</span>

<div class="ladder">
<div class="rung"><strong>약함</strong><span>어떤 도구를 붙일까?</span></div>
<div class="rung"><strong>보통</strong><span>어떤 기능을 만들까?</span></div>
<div class="rung"><strong>강함</strong><span>어떤 문제를 해결할까?</span></div>
</div>

<div class="quote" style="margin-top:20px"><p>앱 개발은 도구에서 시작하면 약하다. 문제에서 시작해야 한다.</p></div>

<!--
AI 앱 개발은 도구에서 시작하면 약합니다. 해결할 반복 문제, 책임 문제, 병목 문제에서 시작해야 합니다.
-->

---

## 사용자에게: 한 가지 질문

<span class="kicker">권고 · 쓰는 쪽</span>

<div class="grid2">
<div class="card">
<h3>필요 없는 것</h3>
<p>AI 전문가가 될 필요는 없다.</p>
<p>모든 방법론을 알 필요도 없다.</p>
</div>
<div class="card">
<h3>필요한 질문</h3>
<p class="lead">AI가 내 문제의 무엇을 해결해 주나?</p>
</div>
</div>

<!--
사용자는 모든 방법론을 알 필요가 없습니다. 그러나 AI가 내 문제의 무엇을 해결해 줄 수 있는지는 물어야 합니다.
-->

---

## 결론

<span class="kicker">정리</span>

<div class="flow">
<div class="step"><h3>앱</h3><p>기능을 제공한다.</p></div>
<div class="arrow">→</div>
<div class="step"><h3>에이전트</h3><p>일을 맡는다.</p></div>
<div class="arrow">→</div>
<div class="step"><h3>쓰이는 에이전트</h3><p>실제 문제를 해결한다.</p></div>
</div>

<div class="quote" style="margin-top:22px"><p>사람은 AI 앱을 쓰기 위해 앱을 쓰지 않는다. 해결할 일이 있을 때 쓴다.</p></div>

<!--
오늘의 질문은 두 가지였습니다. 왜 기능이 좋은 앱도 안 쓰이는가. 어떻게 실제로 쓰이는 앱을 만드는가. 답은 자동화, 신뢰, 실제문제입니다. 사람은 AI 앱을 쓰기 위해 앱을 쓰지 않습니다. 해결해야 할 일이 있을 때 씁니다.
-->

---

<!-- _class: section -->

# 자동화의 목표는  
# 선택권 제거가 아니다.

<p class="subtitle">신뢰 가능한 위임이다.</p>

<div class="grid3" style="margin-top:38px">
<div class="card"><h3>자동화</h3><p>무엇을 대신할까</p></div>
<div class="card"><h3>신뢰</h3><p>무엇을 확인할까</p></div>
<div class="card"><h3>실제문제</h3><p>왜 써야 할까</p></div>
</div>

<!--
쓰이는 AI 에이전트는 자동화, 신뢰, 실제문제를 함께 설계합니다.
-->
