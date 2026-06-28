# AI Company_lecture

This folder is the standalone git-tracked source folder for the AI company lecture materials.

## Lecture Theme

Working title: `AI Company_lecture`

Core question:

> Why do people still avoid using an agent app even when its features work well?

Core answer:

- Users want solved outcomes, not many methodological choices.
- Full automation creates anxiety when users cannot verify the result.
- The next step is not just better execution, but agent-level judgment about which layer should be repaired: code, rule, model/theory, or the question itself.
- Guardrails are necessary, but the lecture should distinguish guardrails from correction-level judgment.
- Coherence/validity checks are the bridge between impressive AI output and usable real-world work.

## Git Materials

These files are small, text-based, and should remain in git:

- `courses/AI-Company-lecture/README.md`
- `courses/AI-Company-lecture/demo-script-ko.md`
- `courses/AI-Company-lecture/AI-Company-lecture-full-slides.md`
- `courses/AI-Company-lecture/demo-index-ko.md`
- `courses/AI-Company-lecture/demo-narration/02-pr-studio-press-release.txt`
- `courses/AI-Company-lecture/slide-outline-ko.md`
- `courses/AI-Company-lecture/blog-column-ko.md`
- `courses/AI-Company-lecture/article-agent-era-marketing-planners-ko.md`
- `courses/AI-Company-lecture/final-handoff-ko.md`
- `courses/AI-Company-lecture/materials-manifest.json`
- `courses/AI-Company-lecture/scripts/build_lecture_main_video.py`

## Dropbox Materials

Large generated outputs are stored outside git:

```text
C:\Users\ciadmin\Dropbox\gitwork_data\AI Company_lecture
```

Expected Dropbox contents:

- `slides-md/AI-Company-lecture-full-slides.md`
- `slides-md/demo-index-ko.md`
- `column/article-agent-era-marketing-planners-ko.md`
- `git_materials/final-handoff-ko.md`
- `demos/demo-01-text-analysis-repair.mp4`
- `demos/demo-02-pr-studio-press-release.mp4`
- `demos/demo-03-pr-studio-feedback-repair.mp4`
- `demos/demo-04-validation-server-ui.mp4`
- `demos/demo-05-validation-result.mp4`
- `screens/assets/`
- `slides/AI Company_lecture_deck.pptx`
- `slides/AI Company_lecture_deck_contact_sheet.png`
- `slides/build-ai-company-lecture-deck.mjs`
- `slides/preview/`
- `column/blog-column-ko.md`
- `video/correction-level-agent-demo.mp4`
- `lecture-video/slide-lecture-ko/AI-Company-lecture-slide-lecture-ko.mp4`
- `lecture-video/slide-lecture-ko/AI-Company-lecture-key-captions-ko.srt`
- `lecture-video/slide-lecture-ko/lecture-video-manifest.json`
- `metadata/render-report.json`
- `metadata/sample-frame.png`
- `screens/raw/`
- `screens/slides/`
- `audio/`
- `narration/`
- `clips/`
- `git_materials/`

## Regenerate Slide Lecture Video

The main lecture video must be generated from the full Markdown slide deck, not from the compact PPT summary.

Command:

```powershell
cd C:\git-app\lectures
python .\courses\AI-Company-lecture\scripts\build_lecture_main_video.py
```

Output:

```text
C:\Users\ciadmin\Dropbox\gitwork_data\AI Company_lecture\lecture-video\slide-lecture-ko\AI-Company-lecture-slide-lecture-ko.mp4
C:\Users\ciadmin\Dropbox\gitwork_data\AI Company_lecture\lecture-video\slide-lecture-ko\AI-Company-lecture-key-captions-ko.srt
```

Current output:

- Slide source: full Markdown deck, 55 slides
- Duration: `1269.933984` seconds
- Resolution: `1920x1080`
- Audio: Korean narration generated through Google TTS
- Caption policy: key emphasis captions only, not a full transcript
- Demo policy: demo clips remain separate videos; the lecture slides mark the insertion points

## Regenerate Demo Video

Required local apps:

- Text Analysis Copilot: `http://127.0.0.1:5173/?view=reflection&demo=repair-hard`
- PR Studio: `http://127.0.0.1:3026/?tab=performance`
- Insight Validation Server: `http://127.0.0.1:4020`

Command:

```powershell
cd C:\git-app\pr-studio
npm run render:correction-demo
```

Output:

```text
C:\git-app\pr-studio\out\correction-level-agent-demo\correction-level-agent-demo.mp4
```

## Current Demo Render

- Duration: `132.604333` seconds
- Resolution: `1920x1080`
- Audio: Korean narration generated through Google TTS
- Validation demo case: `cell_sum_001`
- Validation result: `do_not_release`
- Blocking evidence: `BASE_N_MISMATCH`, `CELL_SUM_MISMATCH`

## Current Lecture Deck

- Primary Markdown deck: `C:\Users\ciadmin\Dropbox\gitwork_data\AI Company_lecture\slides-md\AI-Company-lecture-full-slides.md`
- Main slide lecture video: `C:\Users\ciadmin\Dropbox\gitwork_data\AI Company_lecture\lecture-video\slide-lecture-ko\AI-Company-lecture-slide-lecture-ko.mp4`
- Key-caption SRT: `C:\Users\ciadmin\Dropbox\gitwork_data\AI Company_lecture\lecture-video\slide-lecture-ko\AI-Company-lecture-key-captions-ko.srt`
- Demo index: `C:\Users\ciadmin\Dropbox\gitwork_data\AI Company_lecture\slides-md\demo-index-ko.md`
- Demo clips: `C:\Users\ciadmin\Dropbox\gitwork_data\AI Company_lecture\demos`
- Deck: `C:\Users\ciadmin\Dropbox\gitwork_data\AI Company_lecture\slides\AI Company_lecture_deck.pptx`
- Contact sheet: `C:\Users\ciadmin\Dropbox\gitwork_data\AI Company_lecture\slides\AI Company_lecture_deck_contact_sheet.png`
- Preview PNGs: `C:\Users\ciadmin\Dropbox\gitwork_data\AI Company_lecture\slides\preview`
- Build script backup: `C:\Users\ciadmin\Dropbox\gitwork_data\AI Company_lecture\slides\build-ai-company-lecture-deck.mjs`
- Markdown structure: 50+ slides, Korean, professional-user audience
- PPTX structure: 10-slide compact deck retained as a short summary only
- Main demos: PR Studio press release, PR Studio YouTube, PR Studio feedback repair, Text Analysis Copilot repair-level example

## Column Draft

- Git source: `courses/AI-Company-lecture/blog-column-ko.md`
- Dropbox copy: `C:\Users\ciadmin\Dropbox\gitwork_data\AI Company_lecture\column\blog-column-ko.md`
- Audience: professional AI users who are not AI specialists
- Message: AI agents are powerful, but only well-designed agents become useful work systems.

## Marketing Planner Article Draft

- Git source: `courses/AI-Company-lecture/article-agent-era-marketing-planners-ko.md`
- Dropbox copy: `C:\Users\ciadmin\Dropbox\gitwork_data\AI Company_lecture\column\article-agent-era-marketing-planners-ko.md`
- Audience: marketing and planning professionals who use survey data
- Message: the AI-agent era changes work from asking better prompts to delegating, validating, and deciding the proper level of correction.

## Final Handoff

- Git source: `courses/AI-Company-lecture/final-handoff-ko.md`
- Dropbox copy: `C:\Users\ciadmin\Dropbox\gitwork_data\AI Company_lecture\git_materials\final-handoff-ko.md`
- Purpose: summarizes the lecture/article/demo/channel strategy and identifies what belongs in git versus Dropbox.
