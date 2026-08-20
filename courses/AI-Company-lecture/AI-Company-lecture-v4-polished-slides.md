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
  padding: 48px 64px;
}
h1, h2, h3, p { letter-spacing: 0; }
h1 { font-size: 58px; line-height: 1.12; margin: 0 0 20px; }
h2 { font-size: 42px; line-height: 1.18; margin: 0 0 20px; }
h3 { font-size: 23px; line-height: 1.24; margin: 0 0 10px; }
p, li { font-size: 23px; line-height: 1.42; }
small { font-size: 17px; color: #64748b; }
strong { color: #0f172a; }
.dark strong, .section strong { color: #ffffff; }
.kicker {
  display: inline-block;
  font-size: 16px;
  font-weight: 800;
  color: #1d4ed8;
  background: #dbeafe;
  border-radius: 999px;
  padding: 5px 14px;
  margin: 0 0 18px;
}
.subtitle { font-size: 30px; color: #475569; line-height: 1.34; }
.lead { font-size: 32px; line-height: 1.28; font-weight: 850; }
.muted { color: #64748b; }
.accent { color: #2563eb; }
.grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: 22px; }
.grid3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px; }
.grid4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; }
.card, .metric, .panel, .quote, .case {
  border: 1px solid #dbe3ee;
  background: #ffffff;
  border-radius: 8px;
  padding: 22px;
  box-shadow: 0 10px 24px rgba(15, 23, 42, 0.06);
}
.metric { min-height: 142px; }
.metric .num {
  display: block;
  font-size: 38px;
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
.claim p { font-size: 29px; font-weight: 850; margin: 0; color: #1d4ed8; }
.quote {
  border-left: 8px solid #f59e0b;
  background: #fffbeb;
}
.quote p { font-size: 30px; font-weight: 850; margin: 0; }
.tag {
  display: inline-block;
  padding: 6px 12px;
  border: 1px solid #bfdbfe;
  border-radius: 999px;
  color: #1d4ed8;
  background: #eff6ff;
  font-weight: 750;
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
.step {
  border: 1px solid #dbe3ee;
  background: #ffffff;
  border-radius: 8px;
  padding: 18px;
  min-height: 118px;
}
.arrow {
  display: flex;
  align-items: center;
  justify-content: center;
  color: #2563eb;
  font-size: 30px;
  font-weight: 900;
}
.split {
  display: grid;
  grid-template-columns: 1.05fr 0.95fr;
  gap: 28px;
  align-items: center;
}
.stack { display: grid; grid-template-columns: 1fr; gap: 12px; }
.line {
  display: grid;
  grid-template-columns: 210px 1fr;
  align-items: center;
  border: 1px solid #dbe3ee;
  background: #fff;
  border-radius: 8px;
  overflow: hidden;
}
.line strong {
  background: #eff6ff;
  color: #1d4ed8;
  padding: 15px 18px;
  height: 100%;
}
.line span { padding: 15px 18px; font-size: 21px; }
.screen {
  border: 1px solid #cbd5e1;
  background: #0f172a;
  color: #e5e7eb;
  border-radius: 8px;
  padding: 18px;
  font-family: Consolas, "Courier New", monospace;
  font-size: 17px;
  line-height: 1.48;
}
.section {
  background: #0f172a;
  color: #ffffff;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.section .kicker,
.dark .kicker { background: rgba(96,165,250,0.18); color: #93c5fd; }
.section h1 { font-size: 64px; margin-bottom: 14px; }
.section .subtitle,
.dark .subtitle,
.dark small,
.dark .muted { color: #cbd5e1; }
.dark { background: #0f172a; color: #ffffff; }
.dark .card,
.dark .metric,
.dark .panel {
  background: rgba(255,255,255,0.08);
  border-color: rgba(255,255,255,0.18);
  color: #ffffff;
  box-shadow: none;
}
.table {
  width: 100%;
  border-collapse: collapse;
  background: #fff;
  border: 1px solid #dbe3ee;
  border-radius: 8px;
  overflow: hidden;
}
.table th, .table td {
  border-bottom: 1px solid #e5e7eb;
  padding: 14px 16px;
  text-align: left;
  font-size: 20px;
  vertical-align: top;
}
.table th { color: #1d4ed8; background: #eff6ff; }
.table tr:last-child td { border-bottom: 0; }
</style>

<!-- _class: dark -->

# 언제 우리는  
# AI 에이전트를 쓰는가

<p class="subtitle">자동화 · 신뢰 · 실제문제</p>

<small>AI 개발자만이 아니라, AI를 업무에 써야 하는 연구자와 실무자를 위한 강의</small>

<!--
오늘은 앱 자랑을 하려는 것이 아닙니다. 제가 여러 앱을 만들고 보여주고 일부 써보게 하면서 본 질문을 다룹니다. 왜 기능이 좋아도 쓰이지 않는가. 언제 사람은 AI 에이전트에게 일을 맡기는가.
-->

---

## 강의의 질문

<span class="kicker">출발점</span>

<div class="grid2">
<div class="card">
<h3>처음 질문</h3>
<p class="lead">무엇을 만들 수 있나?</p>
<p>AI로 가능한 일을 확인했다.</p>
</div>
<div class="card">
<h3>지금 질문</h3>
<p class="lead">언제 쓰고 싶어하나?</p>
<p>기능보다 사용 조건이 중요했다.</p>
</div>
</div>

<div class="claim" style="margin-top:22px"><p>앱이 도움이 되어도, 사람들이 실제로 쓰지 않는 경우가 있었다.</p></div>

<!--
처음에는 무엇을 만들 수 있나가 궁금했습니다. 그런데 직접 만들고 보여주고 일부 써보게 하면서 질문이 바뀌었습니다. 기능이 되는 것과 실제로 쓰이는 것은 달랐습니다.
-->

---

## 강연자의 출발점

<span class="kicker">경험의 범위</span>

<p class="lead">나는 여러 현장에서 AI를 써볼 기회가 있었다.</p>

<div class="grid4" style="margin-top:24px">
<div class="card"><h3>연구</h3><p>문제·자료·논문</p></div>
<div class="card"><h3>조사 현업</h3><p>데이터·검증·보고</p></div>
<div class="card"><h3>강의·글쓰기</h3><p>설명·구성·표현</p></div>
<div class="card"><h3>데이터 분석</h3><p>해석·판단·전달</p></div>
</div>

<p style="margin-top:22px">주변에 앱을 만들어 주기도 했다. 그 과정에서 본 것은 AI 지식의 차이만이 아니었다.</p>

<!--
연구, 조사 현업, 강의와 글쓰기, 데이터 분석에서 AI를 써볼 기회가 있었습니다. 주변에 앱을 만들어 주기도 했습니다. 그런데 AI를 많이 아는 사람만 쓰고 모르는 사람만 안 쓰는 식으로 설명되지 않았습니다.
-->

---

## 세 조건

<span class="kicker">오늘의 답</span>

<div class="grid3">
<div class="metric"><span class="num">①</span><h3>자동화</h3><p>선택 부담을 줄인다.</p></div>
<div class="metric"><span class="num">②</span><h3>신뢰</h3><p>위임할 근거를 보인다.</p></div>
<div class="metric"><span class="num">③</span><h3>실제문제</h3><p>사용할 이유를 만든다.</p></div>
</div>

<div class="claim" style="margin-top:22px"><p>자동화가 먼저다. 그러나 자동화만으로는 부족하다.</p></div>

<!--
오늘의 답은 세 가지입니다. 자동화, 신뢰, 실제문제입니다. 자동화가 먼저입니다. 그러나 자동화만으로는 부족합니다. 신뢰가 필요하고, 실제 문제가 있어야 합니다.
-->

---

<!-- _class: section -->

<span class="kicker">첫 장면</span>

# AI 에이전트는  
# 대화창보다 강력하다

<p class="subtitle">답변이 아니라, 과정을 수행한다.</p>

---

## 연구 과정 전체를 수행한다

<span class="kicker">Research Pilot Academy</span>

<span class="tag">Research Pilot Academy</span>

<div class="flow four">
<div class="step"><h3>연구문제·데이터</h3><p>출발점을 받는다.</p></div>
<div class="arrow">→</div>
<div class="step"><h3>방법 결정</h3><p>분석 전략을 고른다.</p></div>
<div class="arrow">→</div>
<div class="step"><h3>분석·해석</h3><p>결과와 질문을 비교한다.</p></div>
<div class="arrow">→</div>
<div class="step"><h3>표·원고</h3><p>문서로 정리한다.</p></div>
</div>

<p class="lead" style="margin-top:24px">대화창은 답을 준다. 에이전트는 일을 이어 간다.</p>

<!--
Research Pilot Academy는 연구문제와 데이터를 받고, 분석 방법을 결정하고, 결과와 연구문제를 비교하고, 필요한 추가 분석을 수행하고, 해석하고, 표와 원고를 만듭니다. 이것은 대화창의 답변과 다른 차원입니다.
-->

---

## 몇 달짜리 일이 한 흐름이 된다

<span class="kicker">능력의 확대</span>

<div class="quote"><p>과거에는 연구자가 2-3달 걸리던 일이, 짧은 시간 안에 하나의 흐름으로 실행된다.</p></div>

<div class="grid3" style="margin-top:24px">
<div class="card"><h3>분석 방법</h3><p>무엇을 할지 판단한다.</p></div>
<div class="card"><h3>추가 분석</h3><p>결과를 보고 더 본다.</p></div>
<div class="card"><h3>해석·원고</h3><p>쓸 수 있는 형태로 만든다.</p></div>
</div>

<!--
학회에서 이 흐름을 보여주었고 관심이 많았습니다. 아직 공개 전이어서 실제 사용은 더 봐야 합니다. 하지만 이 장면은 에이전트가 왜 대화창보다 강력한지 보여줍니다.
-->

---

## 능력은 보였다

<span class="kicker">질문의 전환</span>

<div class="split">
<div>
<h2>그렇다면 왜 바로 쓰지 않을까?</h2>
<p>능력이 강해도 사용으로 이어지지 않는 경우가 있었다.</p>
<p>이제 질문은 기능이 아니라 조건이다.</p>
</div>
<div class="panel">
<h3>오늘 볼 것</h3>
<div class="stack">
<div class="line"><strong>자동화</strong><span>선택지를 줄인다.</span></div>
<div class="line"><strong>신뢰</strong><span>판단 근거를 보인다.</span></div>
<div class="line"><strong>실제문제</strong><span>써야 할 이유가 있다.</span></div>
</div>
</div>
</div>

<!--
AI 에이전트의 힘은 분명합니다. 그러나 이 강의의 핵심은 능력 과시가 아닙니다. 사람들이 언제 쓰고 싶어하는가입니다.
-->

---

<!-- _class: section -->

<span class="kicker">조건 ①</span>

# 자동화

<p class="subtitle">사용자는 방법론보다 해결된 결과를 원한다.</p>

---

## 단계가 많으면 부담이 된다

<span class="kicker">Proposal Studio</span>

<div class="grid2">
<div class="card">
<span class="tag">Proposal Studio</span>
<h3>처음 설계</h3>
<p>제안서 작성 과정을 8단계로 체계화했다.</p>
<p>구조는 있었다.</p>
</div>
<div class="card">
<h3>사용자 반응</h3>
<p class="lead">복잡하다.</p>
<p>막상 사용할 때는 선택지를 반기지 않았다.</p>
</div>
</div>

<div class="claim" style="margin-top:22px"><p>선택지를 주는 것이 늘 돕는 것은 아니다.</p></div>

<!--
제안서 앱을 8단계로 설계했습니다. 논리적으로는 맞았습니다. 하지만 실제로 써보면 사용자는 복잡하다고 느꼈습니다. 막상 사용할 때는 선택지를 좋아하지 않았습니다.
-->

---

## 선택은 동기일 수도, 부담일 수도 있다

<span class="kicker">선택의 맥락</span>

<div class="grid2">
<div class="card">
<h3>내가 고를 때</h3>
<p>선택이 몰입을 만들 수 있다.</p>
<p>내가 통제한다고 느낀다.</p>
</div>
<div class="card">
<h3>맡길 때</h3>
<p>신뢰하는 누군가가 골라주면 더 편하다.</p>
<p>선택 비용이 줄어든다.</p>
</div>
</div>

<div class="claim" style="margin-top:22px"><p>Iyengar의 선택 연구가 말하듯, 선택은 언제나 좋은 것이 아니다.</p></div>

<p>선택은 동기가 되기도 하고, 부담이 되기도 한다. 상황과 신뢰가 중요하다.</p>

<!--
Iyengar의 선택 연구가 보여주듯, 선택의 효과는 단순하지 않습니다. 잼 선택 실험처럼 선택지가 많아질수록 실제 행동이 줄어드는 경우가 있고, 문화와 관계에 따라 스스로 고를 때와 신뢰하는 사람이 골라줄 때의 효과가 달라질 수 있습니다. 앱도 마찬가지입니다.
-->

---

## 자동화가 먼저다

<span class="kicker">설계 원칙</span>

<div class="claim"><p>AI가 반복해서 할 수 있는 일은, 사용자가 계속 고르지 않아도 되게 한다.</p></div>

<div class="flow">
<div class="step"><h3>사용자</h3><p>목표와 중요한 기준을 말한다.</p></div>
<div class="arrow">→</div>
<div class="step"><h3>에이전트</h3><p>방법과 순서를 처리한다.</p></div>
<div class="arrow">→</div>
<div class="step"><h3>사용자</h3><p>결과와 근거를 검토한다.</p></div>
</div>

<!--
그래서 자동화가 먼저입니다. 사용자는 모든 방법과 단계를 고르고 싶어하지 않습니다. 반복해서 처리할 수 있는 일은 AI가 맡고, 사람은 목표와 기준을 말하고 결과와 근거를 보는 쪽이 자연스럽습니다.
-->

---

## 그러나 보이지 않으면 불안하다

<span class="kicker">Plan Builder</span>

<div class="grid2">
<div class="card">
<span class="tag">Plan Builder</span>
<h3>전자동 시도</h3>
<p>선택 부담을 줄이려고, 거의 한 번에 결과가 나오게 했다.</p>
</div>
<div class="card">
<h3>새 문제</h3>
<p class="lead">미리 물어보지도 않고 한다.</p>
<p>편하지만, 무엇을 기준으로 했는지 보이지 않았다.</p>
</div>
</div>

<p style="margin-top:22px">자동화는 AI가 사람 대신 선택하는 일이다. 그래서 편함과 불안이 함께 온다.</p>

<!--
복잡하다는 반응을 보고 전자동으로 만들었습니다. 그런데 이번에는 불안이 생겼습니다. 자동화는 결국 AI가 사람 대신 선택하는 일입니다. 그래서 판단 근거가 보여야 합니다.
-->

---

## 자동화의 균형

<span class="kicker">사용 조건</span>

<div class="grid3">
<div class="metric"><span class="num">1</span><h3>묻지 않아도 될 것</h3><p>반복 작업과 세부 절차</p></div>
<div class="metric"><span class="num">2</span><h3>보여야 할 것</h3><p>중요한 판단 기준</p></div>
<div class="metric"><span class="num">3</span><h3>멈춰야 할 것</h3><p>책임 있는 선택 지점</p></div>
</div>

<div class="quote" style="margin-top:22px"><p>좋은 자동화는 선택권 제거가 아니라, 선택 부담의 조정이다.</p></div>

<!--
자동화는 필요합니다. 하지만 모든 판단을 숨겨서는 안 됩니다. 묻지 않아도 될 것은 줄이고, 보여야 할 판단은 보이고, 책임 있는 선택은 멈춰야 합니다.
-->

---

<!-- _class: section -->

<span class="kicker">조건 ②</span>

# 신뢰

<p class="subtitle">검증 기능의 이름이 아니라, 판단 근거의 정합성이 필요하다.</p>

---

## 검증 기능만으로는 충분하지 않았다

<span class="kicker">gWriter</span>

<div class="grid2">
<div class="card">
<span class="tag">gWriter</span>
<h3>내 생각</h3>
<p>신뢰가 중요하니 검증 기능을 붙이면 된다고 보았다.</p>
</div>
<div class="card">
<h3>실제 관심</h3>
<p class="lead">오히려 편집기였다.</p>
<p>검증 기능 자체가 사용 동기가 되지는 않았다.</p>
</div>
</div>

<div class="claim" style="margin-top:22px"><p>검증은 기능 목록이 아니라, 사용자가 느끼는 책임 문제를 풀어야 한다.</p></div>

<!--
신뢰가 중요하다고 보고 gWriter에 검증 기능을 붙였습니다. 그런데 사람들은 검증보다 편집기에 더 관심을 보였습니다. 검증 기능이 있다는 사실만으로는 충분하지 않았습니다.
-->

---

## 확인가능성은 충분조건이 아니다

<span class="kicker">정합성</span>

<div class="grid3">
<div class="card"><h3>코드</h3><p>있다고 분석이 맞는 것은 아니다.</p></div>
<div class="card"><h3>다운로드</h3><p>받았다고 결과가 맞는 것은 아니다.</p></div>
<div class="card"><h3>링크</h3><p>있다고 근거가 맞는 것은 아니다.</p></div>
</div>

<p class="lead" style="margin-top:24px">신뢰는 확인가능성보다 넓다. 결과와 근거가 서로 맞아야 한다.</p>

<!--
코드가 있다고 분석의 정확성이 증명되는 것은 아닙니다. 링크가 있다고 결론을 뒷받침하는지도 별도로 봐야 합니다. 확인가능성은 필요하지만 충분하지 않습니다.
-->

---

## 그럴듯함과 공개 가능성은 다르다

<span class="kicker">InsightValidationServer</span>

<span class="tag">InsightValidationServer</span>

<div class="flow">
<div class="step"><h3>생성</h3><p>AI가 분석 요약을 만든다.</p></div>
<div class="arrow">→</div>
<div class="step"><h3>검증</h3><p>데이터·코드·해석을 대조한다.</p></div>
<div class="arrow">→</div>
<div class="step"><h3>판정</h3><p>공개 가능한지 결정한다.</p></div>
</div>

<div class="claim" style="margin-top:22px"><p>좋은 에이전트는 생성과 검증을 분리한다.</p></div>

<!--
InsightValidationServer는 그럴듯한 결과를 바로 믿지 않습니다. 데이터, 기준 N, 셀 합계, 분석 단위, 공개 기준이 서로 맞는지 봅니다. 이것은 점수 계산이 아니라 공개 가능성 판단입니다.
-->

---

## 정합성이 공개 가능성을 만든다

<span class="kicker">판정의 예</span>

<div class="screen">
BASE_N_MISMATCH     기준 N과 결과 N이 다름<br>
CELL_SUM_MISMATCH   셀 합계가 표 전체와 맞지 않음<br>
do_not_release      공개 전 수정 필요
</div>

<p class="lead" style="margin-top:24px">결과가 그럴듯해도, 업무 기준과 맞지 않으면 멈춰야 한다.</p>

<!--
여기서 중요한 것은 검증 기능이 있다는 말이 아닙니다. AI가 만든 결과가 업무 기준과 맞지 않으면 공개하지 않는 구조입니다. 정합성이 공개 가능성을 만듭니다.
-->

---

<!-- _class: section -->

<span class="kicker">조건 ③</span>

# 실제문제

<p class="subtitle">사람은 앱을 쓰기 위해 앱을 쓰지 않는다. 해결해야 할 일이 있을 때 쓴다.</p>

---

## 매일 풀어야 하면 쓴다

<span class="kicker">KWCS-QC</span>

<div class="grid2">
<div class="card">
<span class="tag">KWCS-QC</span>
<h3>상황</h3>
<p>매일 데이터가 들어온다.</p>
<p>검증하고, 분석하고, 해석해야 한다.</p>
</div>
<div class="card">
<h3>사용 이유</h3>
<p class="lead">선택이 아니라 필요다.</p>
<p>해야 할 일이 매일 돌아오기 때문이다.</p>
</div>
</div>

<!--
KWCS-QC는 완전한 신뢰가 먼저 생겨서 쓰는 앱이 아닙니다. 매일 데이터가 들어오고 반드시 봐야 하니까 씁니다. 이때 앱은 선택지가 아니라 필요가 됩니다.
-->

---

## 완전한 신뢰보다 반복되는 필요

<span class="kicker">운영의 힘</span>

<div class="flow four">
<div class="step"><h3>데이터 수신</h3><p>매일 들어온다.</p></div>
<div class="arrow">→</div>
<div class="step"><h3>QC</h3><p>놓치면 안 된다.</p></div>
<div class="arrow">→</div>
<div class="step"><h3>자동 분석</h3><p>반복을 줄인다.</p></div>
<div class="arrow">→</div>
<div class="step"><h3>해석</h3><p>의사결정에 쓴다.</p></div>
</div>

<p class="lead" style="margin-top:24px">실제 문제는 사용 이유를 만든다.</p>

<!--
검증 과정을 완전히 신뢰하기 어렵더라도 매일같이 모니터링해야 합니다. 여기서는 AI 앱을 쓸까 말까가 아니라, 해야 할 일이 있다는 것이 중요합니다.
-->

---

## 데이터는 의미가 필요하다

<span class="kicker">ResearchPilot Data</span>

<div class="split">
<div>
<h2>사람들은 데이터를 분석하고 싶은 것이 아니다.</h2>
<p class="lead">데이터가 무엇을 말하는지 알고 싶어 한다.</p>
</div>
<div class="panel">
<div class="stack">
<div class="line"><strong>분석</strong><span>표와 통계</span></div>
<div class="line"><strong>해석</strong><span>무엇을 말하는가</span></div>
<div class="line"><strong>활용</strong><span>보고서·전략·후속 질문</span></div>
</div>
</div>
</div>

<!--
ResearchPilot Data를 넣는 이유는 분석 버튼을 보여주기 위해서가 아닙니다. 사람들은 자신이 가진 데이터의 의미를 알고 싶어 합니다. 좋은 데이터 분석 에이전트는 분석 방법뿐 아니라 해석 가능성과 활용 가능성까지 판단해야 합니다.
-->

---

## 좋은 데이터 앱은 차트에서 끝나지 않는다

<span class="kicker">해석 장치</span>

<span class="tag">ResearchPilot Data</span>

<div class="grid4">
<div class="card"><h3>상태 확인</h3><p>결측·품질·변수</p></div>
<div class="card"><h3>질문 제안</h3><p>무엇을 물을까</p></div>
<div class="card"><h3>추가 분석</h3><p>더 볼 것이 있나</p></div>
<div class="card"><h3>업무 언어</h3><p>어떻게 설명할까</p></div>
</div>

<div class="quote" style="margin-top:22px"><p>분석 결과를 “그래서 이 데이터가 무엇을 말하는가”로 바꾸어야 한다.</p></div>

<!--
단순한 차트 생성이면 강의에 넣을 이유가 약합니다. 데이터 상태, 분석 목적, 추가 분석 판단, 해석 기준, 업무 언어로의 전환이 보여야 합니다.
-->

---

<!-- _class: section -->

<span class="kicker">한 걸음 더</span>

# 문제의 틀을  
# 바꾸어야 할 때

<p class="subtitle">잘못된 문제 정의 안에서 열심히 고치면, 실패가 반복된다.</p>

---

## 번역 문제가 아니었다

<span class="kicker">Press Release Builder</span>

<div class="grid2">
<div class="card">
<span class="tag">Press Release Builder</span>
<h3>처음에는</h3>
<p>번역을 고쳤다. 환각을 줄였다. 영어 문장을 다듬었다.</p>
</div>
<div class="card">
<h3>그래도</h3>
<p class="lead">보도자료는 아니었다.</p>
<p>배포 가능한 메시지 구조가 필요했다.</p>
</div>
</div>

<!--
처음에는 보도자료 영어 문제를 번역 문제로 보았습니다. 그래서 번역문을 고치고 환각을 줄이고 문장도 다듬었습니다. 그런데 그래도 충분하지 않았습니다.
-->

---

## 문장이 아니라 메시지 구조

<span class="kicker">프레임 전환</span>

<div class="flow">
<div class="step"><h3>번역</h3><p>문장을 옮긴다.</p></div>
<div class="arrow">→</div>
<div class="step"><h3>재작성</h3><p>목적에 맞게 다시 쓴다.</p></div>
<div class="arrow">→</div>
<div class="step"><h3>보도자료</h3><p>배포 가능한 메시지로 만든다.</p></div>
</div>

<div class="claim" style="margin-top:22px"><p>현지화가 아니다. 업무 문제의 프레임을 바꾼 것이다.</p></div>

<!--
이것은 단순 현지화가 아닙니다. 번역을 더 잘한 것이 아니라, 보도자료라는 업무 문제로 다시 푼 것입니다. 번역 문제에서 보도자료 메시지 구조 문제로 바뀌었습니다.
-->

---

## 틀 안의 해결. 틀 밖의 해결.

<span class="kicker">관점 전환</span>

<div class="grid2">
<div class="card">
<h3>틀 안의 해결</h3>
<p class="lead">번역을 더 잘한다.</p>
<p>기존 문제 정의 안에서 품질을 올린다. 개선은 가능하지만, 틀 자체가 문제라면 혁신은 어렵다.</p>
</div>
<div class="card">
<h3>틀 밖의 해결</h3>
<p class="lead">보도자료로 다시 쓴다.</p>
<p>문제를 보는 틀 자체를 바꾼다.</p>
</div>
</div>

<div class="claim" style="margin-top:22px"><p>혁신은 종종 중심의 정답이 아니라, 주변부의 다른 질문에서 시작한다.</p></div>

<!--
Kuhn식으로 말하면 틀 안의 해결은 기존 패러다임 안에서 퍼즐을 더 잘 푸는 것입니다. 틀 밖의 해결은 문제를 보는 틀 자체가 바뀌는 것입니다. 여기서는 번역을 더 잘한다가 틀 안의 해결이고, 보도자료로 다시 쓴다가 틀 밖의 해결입니다. 중심은 기존 규범과 평가 기준에 묶이기 쉽고, 주변부는 다른 조합과 다른 질문을 시도할 여지가 있습니다. 그래서 주변부에서 혁신이 나올 수 있다는 말을 연결합니다.
-->

---

## 수정 수준이 중요하다

<span class="kicker">에이전트의 판단</span>

<div class="stack">
<div class="line"><strong>표현 수준</strong><span>문장이 어색한가?</span></div>
<div class="line"><strong>절차 수준</strong><span>작업 순서가 잘못되었는가?</span></div>
<div class="line"><strong>프레임 수준</strong><span>문제의 틀이 잘못되었는가?</span></div>
<div class="line"><strong>질문 수준</strong><span>애초에 다른 질문을 해야 하는가?</span></div>
</div>

<p class="lead" style="margin-top:20px">실패했을 때, 무조건 다시 생성하지 않는다.</p>

<!--
좋은 에이전트는 그냥 다시 생성하지 않습니다. 표현을 고칠지, 절차를 고칠지, 프레임을 고칠지, 질문 자체를 다시 볼지 판단해야 합니다.
-->

---

## 자동화는 판단의 수준을 포함한다

<span class="kicker">PR Studio</span>

<span class="tag">PR Studio</span>

<div class="grid3">
<div class="card"><h3>대상</h3><p>누구에게 말하나</p></div>
<div class="card"><h3>목적</h3><p>무엇을 바꾸나</p></div>
<div class="card"><h3>메시지 프레임</h3><p>어떤 문제로 보나</p></div>
<div class="card"><h3>배포 가능성</h3><p>내보내도 되나</p></div>
<div class="card"><h3>피드백</h3><p>무엇이 반응했나</p></div>
<div class="card"><h3>다음 실험</h3><p>어디를 고치나</p></div>
</div>

<!--
PR Studio는 단순히 콘텐츠를 생성하는 앱이 아닙니다. 대상, 목적, 메시지 프레임, 배포 가능성, 피드백, 다음 실험을 함께 판단합니다. 이것이 고차원 선택을 포함한 자동화입니다.
-->

---

## 앱들은 하나의 논지를 말한다

<span class="kicker">사례의 역할</span>

<table class="table">
<thead><tr><th>사례</th><th>보여주는 조건</th><th>강의에서의 역할</th></tr></thead>
<tbody>
<tr><td>Research Pilot Academy</td><td>능력</td><td>에이전트는 대화창보다 강력한 업무 흐름을 수행한다.</td></tr>
<tr><td>Proposal Studio / Plan Builder</td><td>자동화</td><td>선택 부담과 보이지 않는 자동화의 불안을 함께 보여준다.</td></tr>
<tr><td>gWriter / InsightValidationServer</td><td>신뢰</td><td>검증 기능보다 정합성 있는 판단 구조가 중요하다.</td></tr>
<tr><td>KWCS-QC / ResearchPilot Data</td><td>실제문제</td><td>반복되는 업무 문제와 데이터 의미가 사용 이유를 만든다.</td></tr>
<tr><td>Press Release Builder / PR Studio</td><td>프레임</td><td>문제의 수준을 바꾸고 다음 실험을 정한다.</td></tr>
</tbody>
</table>

<!--
중요한 것은 앱 목록이 아닙니다. 각각의 앱은 하나의 관찰을 보여주는 증거입니다. 능력, 자동화, 신뢰, 실제문제, 프레임 전환이 연결됩니다.
-->

---

## 만드는 사람이 볼 점

<span class="kicker">만드는 쪽</span>

<div class="stack">
<div class="line"><strong>약한 출발</strong><span>어떤 모델을 붙일까?</span></div>
<div class="line"><strong>보통 출발</strong><span>어떤 기능을 만들까?</span></div>
<div class="line"><strong>좋은 출발</strong><span>어떤 반복 문제를 해결할까?</span></div>
</div>

<div class="quote" style="margin-top:22px"><p>도구보다 문제에서 시작할 때, 앱은 더 강해진다.</p></div>

<!--
AI 앱 개발은 도구에서 시작하면 약해지기 쉽습니다. 어떤 모델을 붙일까보다, 어떤 반복 문제, 책임 문제, 병목 문제를 해결할 것인지에서 시작할 때 앱은 더 강해집니다.
-->

---

## 쓰는 사람이 볼 점

<span class="kicker">쓰는 쪽</span>

<div class="grid2">
<div class="card">
<h3>모든 것을 알 필요는 없다</h3>
<p>모델, 방법론, 파라미터를 모두 배울 필요는 없다.</p>
</div>
<div class="card">
<h3>한 가지는 물어야 한다</h3>
<p class="lead">AI가 내 문제의 무엇을 해결해 주나?</p>
</div>
</div>

<p style="margin-top:22px">문제를 잘 잡아야, 에이전트에게 맡길 일도 선명해진다.</p>

<!--
사용자가 AI 전문가가 될 필요는 없습니다. 그러나 AI가 내 문제의 무엇을 해결해 줄 수 있는지는 물어야 합니다.
-->

---

## 언제 쓰는가

<span class="kicker">결론</span>

<div class="grid3">
<div class="metric"><span class="num">①</span><h3>일을 줄일 때</h3><p>선택 부담을 실제로 줄인다.</p></div>
<div class="metric"><span class="num">②</span><h3>맡길 수 있을 때</h3><p>판단 근거와 정합성이 보인다.</p></div>
<div class="metric"><span class="num">③</span><h3>써야 할 때</h3><p>반복되는 실제 문제가 있다.</p></div>
</div>

<div class="claim" style="margin-top:22px"><p>사람은 AI 앱을 쓰기 위해 앱을 쓰지 않는다. 해결해야 할 일이 있을 때 쓴다.</p></div>

<!--
오늘의 결론입니다. 사람은 AI 앱을 쓰기 위해 앱을 쓰지 않습니다. 해결해야 할 일이 있을 때 씁니다. 자동화는 일을 줄이고, 신뢰는 맡길 근거를 만들고, 실제문제는 사용 이유를 만듭니다.
-->

---

<!-- _class: section -->

# 자동화의 목표는  
# 선택권 제거가 아니다

<p class="subtitle">신뢰 가능한 위임이다.</p>

<div class="grid3" style="margin-top:38px">
<div class="card"><h3>자동화</h3><p>무엇을 대신할까</p></div>
<div class="card"><h3>신뢰</h3><p>무엇을 확인할까</p></div>
<div class="card"><h3>실제문제</h3><p>왜 써야 할까</p></div>
</div>

<!--
쓰이는 AI 에이전트는 자동화, 신뢰, 실제문제를 함께 설계합니다.
-->
