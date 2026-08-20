---
marp: true
theme: default
paginate: true
size: 16:9
title: 사람들이 AI 에이전트를 쓰고 싶어지는 순간
description: 자동화, 신뢰, 실제문제로 보는 AI 에이전트 사용 조건
---

<style>
section {
  font-family: "Aptos", "Malgun Gothic", "Noto Sans KR", sans-serif;
  background: #f8fafc;
  color: #111827;
  padding: 54px 66px;
}
h1, h2, h3, p, li { letter-spacing: 0; }
h1 { font-size: 55px; line-height: 1.12; margin: 0 0 20px; }
h2 { font-size: 39px; line-height: 1.22; margin: 0 0 28px; }
h3 { font-size: 23px; margin: 0 0 12px; }
p, li { font-size: 22px; line-height: 1.42; }
small { font-size: 17px; color: #64748b; }
.subtitle { font-size: 29px; color: #475569; line-height: 1.35; }
.lead { font-size: 31px; line-height: 1.3; font-weight: 800; }
.muted { color: #64748b; }
.blue { color: #2563eb; }
.split { display: grid; grid-template-columns: 1fr 1fr; gap: 26px; }
.triad { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; }
.quad { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; }
.card, .quote, .case, .panel {
  background: #ffffff;
  border: 1px solid #dbe3ee;
  border-radius: 8px;
  padding: 22px;
  box-shadow: 0 10px 24px rgba(15, 23, 42, 0.06);
}
.case { border-top: 6px solid #2563eb; }
.quote {
  background: #fffbeb;
  border-left: 8px solid #f59e0b;
}
.quote p { margin: 0; font-size: 30px; line-height: 1.28; font-weight: 800; }
.tag {
  display: inline-block;
  padding: 6px 10px;
  border: 1px solid #cbd5e1;
  border-radius: 999px;
  background: #fff;
  color: #475569;
  font-size: 17px;
  margin: 0 8px 10px 0;
}
.flow {
  display: grid;
  grid-template-columns: 1fr 42px 1fr 42px 1fr;
  align-items: stretch;
  gap: 12px;
}
.step {
  background: #ffffff;
  border: 1px solid #dbe3ee;
  border-radius: 8px;
  padding: 20px;
  min-height: 132px;
}
.arrow {
  display: flex;
  align-items: center;
  justify-content: center;
  color: #2563eb;
  font-size: 34px;
  font-weight: 900;
}
.rungs { display: grid; gap: 12px; }
.rung {
  display: grid;
  grid-template-columns: 190px 1fr;
  background: #fff;
  border: 1px solid #dbe3ee;
  border-radius: 8px;
  overflow: hidden;
}
.rung strong {
  background: #eff6ff;
  color: #1d4ed8;
  padding: 18px;
  font-size: 22px;
}
.rung span { padding: 18px; font-size: 22px; }
.matrix {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  border: 1px solid #dbe3ee;
  border-radius: 8px;
  overflow: hidden;
  background: #fff;
}
.matrix div {
  padding: 18px;
  border-right: 1px solid #dbe3ee;
  border-bottom: 1px solid #dbe3ee;
  font-size: 20px;
}
.matrix div:nth-child(3n) { border-right: 0; }
.matrix .head { background: #eff6ff; color: #1d4ed8; font-weight: 800; }
.dark { background: #0f172a; color: #ffffff; }
.dark .subtitle, .dark small, .dark .muted { color: #cbd5e1; }
.dark .card {
  background: rgba(255,255,255,0.08);
  border-color: rgba(255,255,255,0.18);
  color: #ffffff;
  box-shadow: none;
}
.band {
  background: #e0f2fe;
  border: 1px solid #bae6fd;
  border-radius: 8px;
  padding: 20px 24px;
}
.code {
  background: #0f172a;
  color: #e5e7eb;
  border-radius: 8px;
  padding: 18px;
  font-family: Consolas, monospace;
  font-size: 17px;
  line-height: 1.45;
}
</style>

<!-- _class: dark -->

# 사람들이 AI 에이전트를  
# 쓰고 싶어지는 순간

<p class="subtitle">능력보다 중요한 것: 자동화, 신뢰, 실제문제</p>

<div class="triad" style="margin-top:42px">
<div class="card"><h3>일을 줄여야 한다</h3><p>선택과 반복을 줄인다</p></div>
<div class="card"><h3>믿을 수 있어야 한다</h3><p>근거와 정합성을 보인다</p></div>
<div class="card"><h3>문제가 있어야 한다</h3><p>매일 부딪히는 필요를 푼다</p></div>
</div>

---

## 출발점은 단순했다

<div class="split">
<div class="card">
<h3>AI가 강해졌다</h3>
<p>연구, 조사, 글쓰기, 데이터 분석에서 할 수 있는 일이 늘었다.</p>
</div>
<div class="card">
<h3>앱도 만들어 보았다</h3>
<p>주변의 실제 업무 문제를 보고 여러 형태의 AI 앱을 만들었다.</p>
</div>
</div>

<div class="quote" style="margin-top:28px"><p>그런데 좋은 기능이 곧 사용으로 이어지지는 않았다.</p></div>

---

## 질문이 바뀌었다

<div class="flow">
<div class="step"><h3>처음 질문</h3><p class="lead">무엇을 만들 수 있나?</p></div>
<div class="arrow">→</div>
<div class="step"><h3>관찰</h3><p>기능이 좋아도 쓰이지 않을 수 있다.</p></div>
<div class="arrow">→</div>
<div class="step"><h3>지금 질문</h3><p class="lead">언제 쓰고 싶어지나?</p></div>
</div>

<p class="lead" style="margin-top:30px">이 강의는 기술 자랑이 아니라 사용 조건에 대한 이야기다.</p>

---

## 대화창과 에이전트는 다르다

<div class="split">
<div class="card">
<h3>대화창</h3>
<p class="lead">답을 준다.</p>
<p>사람이 묻고, AI가 응답한다.</p>
</div>
<div class="card">
<h3>에이전트</h3>
<p class="lead">과정을 맡는다.</p>
<p>목표를 받고, 실행하고, 확인하고, 다음 행동을 정한다.</p>
</div>
</div>

---

## Research Pilot Academy가 보여준 것

<div class="flow">
<div class="step"><h3>연구문제와 데이터</h3><p>질문과 자료를 받는다.</p></div>
<div class="arrow">→</div>
<div class="step"><h3>분석과 해석</h3><p>방법을 정하고 추가 분석을 판단한다.</p></div>
<div class="arrow">→</div>
<div class="step"><h3>표와 원고</h3><p>결과를 문서로 바꾼다.</p></div>
</div>

<div class="quote" style="margin-top:28px"><p>AI 에이전트의 능력은 분명히 보였다.</p></div>

---

## 그러나 능력만으로는 부족하다

<div class="split">
<div class="card">
<h3>능력의 확인</h3>
<p>에이전트는 복잡한 업무 흐름을 수행할 수 있다.</p>
</div>
<div class="card">
<h3>남은 질문</h3>
<p class="lead">사람은 언제 그 흐름을 맡기고 싶어할까?</p>
</div>
</div>

<p class="lead" style="margin-top:30px">여기서부터 사용 조건을 본다.</p>

---

## 첫 번째 조건: 판단이 들어가야 한다

<div class="flow">
<div class="step"><h3>AI가 만든다</h3><p>초안, 분석, 제안</p></div>
<div class="arrow">→</div>
<div class="step"><h3>사람이 판단한다</h3><p>목적, 방향, 기준, 우선순위</p></div>
<div class="arrow">→</div>
<div class="step"><h3>다음 단계로 간다</h3><p>수정, 확장, 제출</p></div>
</div>

<div class="band" style="margin-top:28px">
<p class="lead">좋은 에이전트는 사람의 판단을 없애지 않는다.</p>
<p>중요한 판단을 제때 넣을 수 있게 해야 한다.</p>
</div>

---

## Proposal Studio: 판단을 단계로 나누었다

<span class="tag">Proposal Studio</span>

<div class="quad">
<div class="case"><h3>목적</h3><p>무엇을 제안하나</p></div>
<div class="case"><h3>대상</h3><p>누구를 설득하나</p></div>
<div class="case"><h3>근거</h3><p>무엇을 제시하나</p></div>
<div class="case"><h3>구성</h3><p>어떤 순서로 말하나</p></div>
</div>

<p class="lead" style="margin-top:30px">의도는 좋았다. 판단을 놓치지 않게 하려 했다.</p>

---

## 그런데 단계가 많으면 부담이 된다

<div class="split">
<div class="card">
<h3>설계자의 생각</h3>
<p>단계별 확인은 품질을 높인다.</p>
<p>사람의 판단도 반영된다.</p>
</div>
<div class="card">
<h3>사용자의 느낌</h3>
<p class="lead">복잡하다.</p>
<p>막상 사용할 때는 선택지를 좋아하지 않았다.</p>
</div>
</div>

<div class="quote" style="margin-top:24px"><p>사람은 판단을 해야 하지만, 모든 순간에 선택하고 싶지는 않다.</p></div>

---

## 두 번째 조건: 자동화가 먼저다

<div class="flow">
<div class="step"><h3>AI가 할 일</h3><p>반복, 정리, 초안, 계산</p></div>
<div class="arrow">→</div>
<div class="step"><h3>사람이 볼 일</h3><p>목적, 기준, 방향, 책임</p></div>
<div class="arrow">→</div>
<div class="step"><h3>좋은 흐름</h3><p>AI가 먼저 처리하고 사람은 핵심을 본다.</p></div>
</div>

<p class="lead" style="margin-top:30px">자동화는 선택권 제거가 아니라 선택 부담의 조정이다.</p>

---

## Plan Builder: 자동화했지만 불안했다

<span class="tag">Plan Builder</span>
<span class="tag">전자동 분석 앱</span>

<div class="split">
<div class="card">
<h3>다음 시도</h3>
<p>사용자가 거의 선택하지 않아도 결과가 나오게 했다.</p>
</div>
<div class="card">
<h3>불안의 이유</h3>
<p class="lead">AI가 사람 대신 선택한다.</p>
<p>무엇을 기준으로 했는지 보이지 않으면 불안하다.</p>
</div>
</div>

<div class="quote" style="margin-top:24px"><p>"미리 물어보지도 않고 한다."</p></div>

---

## 세 번째 조건: 신뢰는 기능 이름으로 생기지 않는다

<span class="tag">gWriter</span>

<div class="split">
<div class="card">
<h3>설계자의 생각</h3>
<p>신뢰가 중요하다. 그래서 검증 기능을 붙였다.</p>
</div>
<div class="card">
<h3>사용자의 반응</h3>
<p>정작 사람들은 검증보다 다른 것에 관심을 두었다.</p>
<p class="lead">오히려 편집기였다.</p>
</div>
</div>

---

## 검증은 신뢰의 이름이 아니라 구조다

<div class="triad">
<div class="card"><h3>코드</h3><p>있다고 분석이 맞는 것은 아니다.</p></div>
<div class="card"><h3>링크</h3><p>있다고 근거가 맞는 것은 아니다.</p></div>
<div class="card"><h3>다운로드</h3><p>가능하다고 공개 가능한 것은 아니다.</p></div>
</div>

<div class="quote" style="margin-top:28px"><p>확인가능성은 필요하다. 그러나 정합성이 중요하다.</p></div>

---

## InsightValidationServer: 정합성을 확인한다

<div class="flow">
<div class="step"><h3>생성 결과</h3><p>그럴듯한 분석 요약</p></div>
<div class="arrow">→</div>
<div class="step"><h3>정합성 검증</h3><p>데이터, 코드, 결과, 해석을 대조한다.</p></div>
<div class="arrow">→</div>
<div class="step"><h3>공개 판단</h3><p>수정 필요 여부를 가른다.</p></div>
</div>

<div class="code" style="margin-top:24px">
BASE_N_MISMATCH &nbsp;&nbsp;&nbsp;&nbsp; 기준 N과 결과 N이 다름<br>
CELL_SUM_MISMATCH &nbsp; 셀 합계가 표 전체와 맞지 않음<br>
do_not_release &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 공개 전 수정 필요
</div>

---

## 네 번째 조건: 실제 문제가 있어야 한다

<span class="tag">KWCS-QC</span>

<div class="split">
<div class="card">
<h3>상황</h3>
<p>매일 데이터가 들어온다.</p>
<p>검증, 분석, 해석이 반복된다.</p>
</div>
<div class="card">
<h3>사용 이유</h3>
<p class="lead">해야 하는 일이 매일 있다.</p>
<p>그래서 앱은 선택이 아니라 필요가 된다.</p>
</div>
</div>

---

## 완전한 신뢰보다 반복되는 필요가 강하다

<div class="flow">
<div class="step"><h3>데이터 수신</h3><p>매일 들어온다.</p></div>
<div class="arrow">→</div>
<div class="step"><h3>QC</h3><p>검증 과정도 완전히 믿기는 어렵다.</p></div>
<div class="arrow">→</div>
<div class="step"><h3>운영 판단</h3><p>그래도 매일 확인해야 한다.</p></div>
</div>

<p class="lead" style="margin-top:30px">실제 문제가 있으면, 완벽하지 않아도 쓰기 시작한다.</p>

---

## 데이터는 분석보다 의미가 필요하다

<span class="tag">ResearchPilot Data</span>

<div class="flow">
<div class="step"><h3>데이터</h3><p>숫자와 변수</p></div>
<div class="arrow">→</div>
<div class="step"><h3>분석</h3><p>표와 통계</p></div>
<div class="arrow">→</div>
<div class="step"><h3>의미</h3><p>그래서 무엇을 말하는가</p></div>
</div>

<div class="quote" style="margin-top:28px"><p>사람들은 데이터를 분석하고 싶은 것이 아니라, 데이터의 의미를 쓰고 싶어 한다.</p></div>

---

## 번역 문제가 아니었다

<span class="tag">Press Release Builder</span>

<div class="split">
<div class="card">
<h3>처음 해결</h3>
<p>번역을 고쳤다. 환각을 줄였다. 영어도 다듬었다.</p>
</div>
<div class="card">
<h3>남은 문제</h3>
<p class="lead">그래도 보도자료로는 부족했다.</p>
<p>문장이 아니라 메시지 구조의 문제였다.</p>
</div>
</div>

---

## 틀 안의 해결. 틀 밖의 해결.

<div class="split">
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

<p class="lead" style="margin-top:30px">혁신은 종종 주변부 질문에서 시작한다.</p>

<!--
발표 메모: Kuhn의 정상과학/패러다임 전환을 짧게 인용한다. 여기서는 큰 철학적 선언보다 "관점 전환"으로 말한다.
-->

---

## 수정 수준을 구분해야 한다

<div class="rungs">
<div class="rung"><strong>문장</strong><span>표현이 어색한가?</span></div>
<div class="rung"><strong>절차</strong><span>작업 순서가 잘못되었는가?</span></div>
<div class="rung"><strong>프레임</strong><span>문제의 틀이 잘못되었는가?</span></div>
<div class="rung"><strong>질문</strong><span>애초에 다른 질문을 해야 하는가?</span></div>
</div>

---

## PR Studio: 판단의 수준을 다룬다

<span class="tag">PR Studio</span>

<div class="quad">
<div class="case"><h3>대상</h3><p>누구에게 말하나</p></div>
<div class="case"><h3>목적</h3><p>무엇을 바꾸나</p></div>
<div class="case"><h3>프레임</h3><p>어떤 문제로 보나</p></div>
<div class="case"><h3>다음 실험</h3><p>무엇을 고치나</p></div>
</div>

<p class="lead" style="margin-top:30px">좋은 에이전트는 생성만 하지 않는다. 판단의 수준을 다룬다.</p>

---

## 쓰이는 에이전트의 조건

<div class="matrix">
<div class="head">조건</div>
<div class="head">질문</div>
<div class="head">실패하면</div>
<div>자동화</div>
<div>정말 일을 줄이는가?</div>
<div>선택지가 늘어난다</div>
<div>신뢰</div>
<div>근거와 정합성이 보이는가?</div>
<div>불안해서 못 맡긴다</div>
<div>실제문제</div>
<div>반복되는 필요가 있는가?</div>
<div>좋은 기능으로 끝난다</div>
</div>

---

## 개발자에게

<div class="rungs">
<div class="rung"><strong>약한 출발</strong><span>어떤 도구를 붙일까?</span></div>
<div class="rung"><strong>중간 출발</strong><span>어떤 기능을 만들까?</span></div>
<div class="rung"><strong>좋은 출발</strong><span>어떤 문제를 해결할까?</span></div>
</div>

<div class="quote" style="margin-top:24px"><p>AI 앱은 도구가 아니라 문제에서 시작해야 한다.</p></div>

---

## 사용자에게

<div class="split">
<div class="card">
<h3>필요 없는 것</h3>
<p>AI 전문가가 될 필요는 없다.</p>
<p>모든 방법론을 알 필요도 없다.</p>
</div>
<div class="card">
<h3>필요한 질문</h3>
<p class="lead">AI가 내 문제의 무엇을 해결해 줄 수 있는가?</p>
</div>
</div>

---

## 결론

<div class="flow">
<div class="step"><h3>능력</h3><p>AI는 많은 일을 할 수 있다.</p></div>
<div class="arrow">→</div>
<div class="step"><h3>조건</h3><p>자동화, 신뢰, 실제문제가 필요하다.</p></div>
<div class="arrow">→</div>
<div class="step"><h3>사용</h3><p>그때 사람은 에이전트를 쓰고 싶어진다.</p></div>
</div>

<div class="quote" style="margin-top:28px"><p>사람은 AI 앱을 쓰기 위해 앱을 쓰지 않는다. 해결해야 할 일이 있을 때 쓴다.</p></div>

---

<!-- _class: dark -->

# 자동화의 목표는  
# 선택권 제거가 아니다.

<p class="subtitle">신뢰 가능한 위임이다.</p>

<div class="triad" style="margin-top:40px">
<div class="card"><h3>무엇을 대신할까</h3><p>자동화</p></div>
<div class="card"><h3>무엇을 확인할까</h3><p>신뢰</p></div>
<div class="card"><h3>왜 써야 할까</h3><p>실제문제</p></div>
</div>
