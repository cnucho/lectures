from __future__ import annotations

import html
import json
import os
import re
import shutil
import subprocess
from dataclasses import asdict, dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
COURSE_ROOT = REPO_ROOT / "courses" / "AI-Company-lecture"
DROPBOX_ROOT = Path(r"C:\Users\ciadmin\Dropbox\gitwork_data\AI Company_lecture")
PR_STUDIO_ROOT = Path(r"C:\git-app\pr-studio")

SOURCE_MD = COURSE_ROOT / "AI-Company-lecture-full-slides.md"
DROPBOX_SLIDES_MD = DROPBOX_ROOT / "slides-md" / "AI-Company-lecture-full-slides.md"
RENDER_MD = DROPBOX_ROOT / "slides-md" / "AI-Company-lecture-full-slides-video-render.md"

OUT_ROOT = DROPBOX_ROOT / "lecture-video" / "slide-lecture-ko"
SLIDE_IMAGE_ROOT = OUT_ROOT / "slides"
DEMO_THUMB_ROOT = OUT_ROOT / "demo-thumbnails"
NARRATION_ROOT = OUT_ROOT / "narration"
AUDIO_ROOT = OUT_ROOT / "audio"
SEGMENT_ROOT = OUT_ROOT / "segments"

FINAL_VIDEO = OUT_ROOT / "AI-Company-lecture-slide-lecture-ko.mp4"
SUBTITLE_FILE = OUT_ROOT / "AI-Company-lecture-key-captions-ko.srt"
MANIFEST_FILE = OUT_ROOT / "lecture-video-manifest.json"
CONCAT_FILE = OUT_ROOT / "concat.txt"

SYNTH_SCRIPT = PR_STUDIO_ROOT / "scripts" / "synthesize-speech.mjs"
FPS = 30
EXTRA_HOLD_SECONDS = 0.6

NOTE_OVERRIDES_BY_TITLE = {
    "AI Agent는 강력합니다.": (
        "오늘은 결론으로 바로 가지 않고, 왜 이 질문이 생겼는지, "
        "앱 제작 경험에서 무엇을 배웠는지, 데모를 통해 무엇을 보아야 하는지 순서대로 보겠습니다."
    ),
    "오늘의 핵심 질문": (
        "이 질문은 작동한다는 것과 실제 업무에서 계속 쓰인다는 것 사이의 차이를 묻습니다."
    ),
    "정리: 세 가지 긴장": "이 세 가지 긴장이 강의 전체의 구조입니다.",
    "DEMO 1. 텍스트 분석 에이전트": (
        "이 데모에서 볼 것은 AI가 단순히 수정한다는 사실이 아니라, 수정할 층위를 판단한다는 점입니다."
    ),
    "DEMO 2. PR Studio 보도자료": (
        "보도자료는 좋은 번역이나 좋은 문장만으로 끝나지 않습니다. "
        "정책 핵심, SNS 요약, 언론 대응 포인트, 대상 독자, 배포 목적이 함께 맞아야 합니다."
    ),
}


@dataclass
class SlidePlan:
    index: int
    title: str
    caption: str
    narration: str
    image: str
    audio: str
    segment: str
    duration_seconds: float = 0.0
    start_seconds: float = 0.0
    end_seconds: float = 0.0


def run(args: list[str], cwd: Path | None = None, env: dict[str, str] | None = None) -> None:
    print(" ".join(str(arg) for arg in args))
    subprocess.run(args, cwd=str(cwd) if cwd else None, env=env, check=True)


def capture_json(args: list[str]) -> dict:
    result = subprocess.run(args, check=True, capture_output=True, text=True, encoding="utf-8")
    return json.loads(result.stdout or "{}")


def ensure_dirs() -> None:
    for path in [
        DROPBOX_SLIDES_MD.parent,
        OUT_ROOT,
        SLIDE_IMAGE_ROOT,
        DEMO_THUMB_ROOT,
        NARRATION_ROOT,
        AUDIO_ROOT,
        SEGMENT_ROOT,
    ]:
        path.mkdir(parents=True, exist_ok=True)


def strip_front_matter(markdown: str) -> str:
    lines = markdown.splitlines()
    if not lines or lines[0].strip() != "---":
        return markdown

    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            return "\n".join(lines[index + 1 :])

    return markdown


def split_slides(markdown: str) -> list[str]:
    body = strip_front_matter(markdown)
    chunks = re.split(r"(?m)^\s*---\s*$", body)
    slides: list[str] = []
    for chunk in chunks:
        cleaned = chunk.strip()
        if not cleaned:
            continue
        if "<style>" in cleaned and not re.search(r"(?m)^#{1,6}\s+", cleaned):
            continue
        slides.append(cleaned)
    return slides


def extract_notes(markdown: str) -> tuple[str, list[str]]:
    notes: list[str] = []

    def replace_comment(match: re.Match[str]) -> str:
        comment = match.group(1).strip()
        if "발표 메모:" in comment:
            note = comment.split("발표 메모:", 1)[1].strip()
            note = re.sub(r"\s+", " ", note)
            notes.append(note)
        return ""

    return re.sub(r"<!--(.*?)-->", replace_comment, markdown, flags=re.S), notes


def clean_inline(text: str) -> str:
    text = html.unescape(text)
    text = re.sub(r"<br\s*/?>", " ", text, flags=re.I)
    text = re.sub(r"</(p|div|h[1-6]|li)>", "\n", text, flags=re.I)
    text = re.sub(r"<video[^>]*src=[\"']([^\"']+)[\"'][^>]*></video>", r"데모 영상: \1", text, flags=re.I)
    text = re.sub(r"!\[([^\]]*)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = text.replace("**", "").replace("__", "")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def plain_lines(markdown: str) -> list[str]:
    markdown, _ = extract_notes(markdown)
    markdown = re.sub(r"<style>.*?</style>", "", markdown, flags=re.S | re.I)
    markdown = re.sub(r"<script>.*?</script>", "", markdown, flags=re.S | re.I)

    lines: list[str] = []
    for raw in markdown.splitlines():
        line = raw.strip()
        if not line:
            continue
        line = re.sub(r"^#{1,6}\s+", "", line)
        line = re.sub(r"^[-*]\s+", "", line)
        line = re.sub(r"^\d+\.\s+", "", line)
        line = re.sub(r"^>\s*", "", line)
        line = clean_inline(line)
        if line and line not in {"---", "controls"}:
            lines.append(line)
    return lines


def title_for(markdown: str, fallback_index: int) -> str:
    for raw in markdown.splitlines():
        match = re.match(r"^\s{0,3}#{1,6}\s+(.+?)\s*$", raw)
        if match:
            return clean_inline(match.group(1))
    lines = plain_lines(markdown)
    return lines[0] if lines else f"Slide {fallback_index}"


def first_lead_text(markdown: str) -> str | None:
    lead = re.search(r"<p[^>]*class=[\"']lead[\"'][^>]*>(.*?)</p>", markdown, flags=re.S | re.I)
    if lead:
        return clean_inline(lead.group(1))
    return None


def small_text(markdown: str) -> str | None:
    small = re.search(r"<small>(.*?)</small>", markdown, flags=re.S | re.I)
    if small:
        return clean_inline(small.group(1))
    return None


def bold_text(markdown: str) -> str | None:
    match = re.search(r"\*\*(.+?)\*\*", markdown, flags=re.S)
    if match:
        return clean_inline(match.group(1))
    return None


def shorten_caption(text: str, max_chars: int = 78) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= max_chars:
        return text

    cut = text[:max_chars].rstrip()
    for marker in [".", "?", "!", "다", "요", "가", "은", "는"]:
        pos = cut.rfind(marker)
        if pos >= 28:
            return cut[: pos + 1]
    return f"{cut.rstrip()}..."


def caption_for(markdown: str, title: str) -> str:
    video_hint = small_text(markdown) if "<video" in markdown else None
    candidates = [
        video_hint,
        first_lead_text(markdown),
        bold_text(markdown),
        title,
    ]
    for candidate in candidates:
        if candidate:
            return shorten_caption(candidate)
    return title


def narration_for(markdown: str, title: str) -> str:
    cleaned_markdown, notes = extract_notes(markdown)
    lines = plain_lines(cleaned_markdown)
    body_lines = [line for line in lines if line != title]
    body = " ".join(body_lines)
    note = NOTE_OVERRIDES_BY_TITLE.get(title)
    spoken_title = title if title.endswith((".", "?", "!")) else f"{title}입니다."

    if "<video" in markdown:
        parts = [
            spoken_title,
            "이 지점에서는 별도 데모 영상을 보여주는 것이 원칙입니다.",
        ]
        if note:
            parts.append(note)
        elif body:
            parts.append(body)
        parts.append("본편 강의 영상에서는 데모의 논점만 짚고, 실제 데모 영상은 별도로 확인합니다.")
        return " ".join(parts)

    parts = [spoken_title]
    if note:
        parts.append(note)
    if body:
        parts.append(body)
    elif notes:
        parts.append(" ".join(notes))

    narration = " ".join(parts)
    narration = re.sub(r"\s+", " ", narration).strip()
    return narration


def generate_demo_thumbnails(markdown: str) -> str:
    def replace_video(match: re.Match[str]) -> str:
        src = match.group(1)
        video_path = (DROPBOX_SLIDES_MD.parent / src).resolve()
        thumb_path = DEMO_THUMB_ROOT / f"{video_path.stem}.jpg"
        if video_path.exists():
            run([
                "ffmpeg",
                "-y",
                "-loglevel",
                "error",
                "-ss",
                "00:00:02",
                "-i",
                str(video_path),
                "-frames:v",
                "1",
                "-q:v",
                "2",
                str(thumb_path),
            ])
            rel = os.path.relpath(thumb_path, RENDER_MD.parent).replace("\\", "/")
            return f"![{video_path.stem}]({rel})\n\n<small>별도 데모 영상: {video_path.name}</small>"

        return f"<small>별도 데모 영상: {src}</small>"

    return re.sub(
        r"<video\s+controls\s+src=[\"']([^\"']+)[\"']\s*></video>",
        replace_video,
        markdown,
        flags=re.I,
    )


def prepare_markdown() -> str:
    markdown = SOURCE_MD.read_text(encoding="utf-8")
    shutil.copy2(SOURCE_MD, DROPBOX_SLIDES_MD)
    render_markdown = generate_demo_thumbnails(markdown)
    RENDER_MD.write_text(render_markdown, encoding="utf-8")
    return markdown


def render_slide_images() -> list[Path]:
    for old in SLIDE_IMAGE_ROOT.glob("slide.*.png"):
        old.unlink()

    npx = shutil.which("npx.cmd") or shutil.which("npx")
    if not npx:
        raise RuntimeError("npx was not found on PATH.")

    run([
        npx,
        "--yes",
        "@marp-team/marp-cli@latest",
        str(RENDER_MD),
        "--images",
        "png",
        "--image-scale",
        "2",
        "--allow-local-files",
        "-o",
        str(SLIDE_IMAGE_ROOT / "slide.png"),
    ], cwd=REPO_ROOT)

    images = sorted(SLIDE_IMAGE_ROOT.glob("slide.*.png"))
    if not images:
        images = sorted(SLIDE_IMAGE_ROOT.glob("slide.*"))
    if not images:
        raise RuntimeError("Marp did not produce slide images.")
    return images


def synthesize_audio(text_path: Path, audio_path: Path) -> None:
    env = os.environ.copy()
    env.setdefault("PR_STUDIO_TTS_PROVIDER_KO", "google")
    env.setdefault("PR_STUDIO_TTS_LANGUAGE", "ko")
    env.setdefault("GOOGLE_APPLICATION_CREDENTIALS", r"C:\secure\pr-studio-google-tts.json")
    env.setdefault("GOOGLE_TTS_VOICE_KO", "ko-KR-Chirp3-HD-Kore")
    env.setdefault("GOOGLE_TTS_SPEAKING_RATE", "0.94")
    run(["node", str(SYNTH_SCRIPT), "--input", str(text_path), "--output", str(audio_path)], cwd=PR_STUDIO_ROOT, env=env)


def media_duration(path: Path) -> float:
    data = capture_json([
        "ffprobe",
        "-v",
        "error",
        "-show_entries",
        "format=duration",
        "-of",
        "json",
        str(path),
    ])
    return float(data.get("format", {}).get("duration", 0.0))


def render_segment(image_path: Path, audio_path: Path, segment_path: Path, duration: float) -> None:
    run([
        "ffmpeg",
        "-y",
        "-loglevel",
        "error",
        "-loop",
        "1",
        "-framerate",
        str(FPS),
        "-t",
        f"{duration:.3f}",
        "-i",
        str(image_path),
        "-i",
        str(audio_path),
        "-vf",
        "scale=1920:1080,format=yuv420p",
        "-af",
        f"apad=pad_dur={EXTRA_HOLD_SECONDS:.2f}",
        "-c:v",
        "libx264",
        "-preset",
        "veryfast",
        "-tune",
        "stillimage",
        "-r",
        str(FPS),
        "-c:a",
        "aac",
        "-b:a",
        "160k",
        "-t",
        f"{duration:.3f}",
        "-shortest",
        str(segment_path),
    ])


def srt_time(seconds: float) -> str:
    milliseconds = int(round(seconds * 1000))
    hours, rem = divmod(milliseconds, 3_600_000)
    minutes, rem = divmod(rem, 60_000)
    secs, millis = divmod(rem, 1000)
    return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"


def write_srt(plans: list[SlidePlan]) -> None:
    entries: list[str] = []
    cue_number = 1
    for plan in plans:
        start = plan.start_seconds + 0.8
        end = min(plan.start_seconds + 8.8, plan.end_seconds - 0.4)
        if end <= start:
            start = plan.start_seconds
            end = plan.end_seconds
        entries.append(
            "\n".join([
                str(cue_number),
                f"{srt_time(start)} --> {srt_time(end)}",
                plan.caption,
            ])
        )
        cue_number += 1

    SUBTITLE_FILE.write_text("\n\n".join(entries) + "\n", encoding="utf-8")


def concat_segments(plans: list[SlidePlan]) -> None:
    lines = []
    for plan in plans:
        path = Path(plan.segment).resolve().as_posix().replace("'", "'\\''")
        lines.append(f"file '{path}'")
    CONCAT_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")

    temp_video = FINAL_VIDEO.with_suffix(".tmp.mp4")
    run([
        "ffmpeg",
        "-y",
        "-loglevel",
        "error",
        "-f",
        "concat",
        "-safe",
        "0",
        "-i",
        str(CONCAT_FILE),
        "-c",
        "copy",
        str(temp_video),
    ])
    temp_video.replace(FINAL_VIDEO)


def build_plans(slides: list[str], images: list[Path]) -> list[SlidePlan]:
    if len(slides) != len(images):
        raise RuntimeError(f"Slide/image count mismatch: {len(slides)} slides, {len(images)} images.")

    plans: list[SlidePlan] = []
    elapsed = 0.0
    for index, slide_markdown in enumerate(slides, start=1):
        title = title_for(slide_markdown, index)
        caption = caption_for(slide_markdown, title)
        narration = narration_for(slide_markdown, title)

        text_path = NARRATION_ROOT / f"{index:02d}.txt"
        audio_path = AUDIO_ROOT / f"{index:02d}.wav"
        segment_path = SEGMENT_ROOT / f"{index:02d}.mp4"
        text_path.write_text(narration + "\n", encoding="utf-8")

        if (
            not audio_path.exists()
            or audio_path.stat().st_size < 1000
            or audio_path.stat().st_mtime < text_path.stat().st_mtime
        ):
            synthesize_audio(text_path, audio_path)

        audio_duration = media_duration(audio_path)
        duration = max(audio_duration + EXTRA_HOLD_SECONDS, 4.0)
        render_segment(images[index - 1], audio_path, segment_path, duration)

        plan = SlidePlan(
            index=index,
            title=title,
            caption=caption,
            narration=narration,
            image=str(images[index - 1]),
            audio=str(audio_path),
            segment=str(segment_path),
            duration_seconds=round(duration, 3),
            start_seconds=round(elapsed, 3),
            end_seconds=round(elapsed + duration, 3),
        )
        elapsed += duration
        plans.append(plan)

    return plans


def main() -> None:
    ensure_dirs()
    markdown = prepare_markdown()
    slides = split_slides(markdown)
    images = render_slide_images()
    plans = build_plans(slides, images)
    concat_segments(plans)
    write_srt(plans)

    video_duration = media_duration(FINAL_VIDEO)
    manifest = {
        "source_slide_markdown": str(SOURCE_MD),
        "render_markdown": str(RENDER_MD),
        "slide_count": len(plans),
        "narration_provider": "Google Cloud TTS via pr-studio scripts/synthesize-speech.mjs",
        "caption_policy": "Key emphasis captions only, not a full transcript.",
        "demo_policy": "Demo clips remain separate videos; lecture slides mark the insertion points.",
        "final_video": str(FINAL_VIDEO),
        "subtitle_file": str(SUBTITLE_FILE),
        "duration_seconds": round(video_duration, 3),
        "slides": [asdict(plan) for plan in plans],
    }
    MANIFEST_FILE.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(json.dumps({
        "final_video": str(FINAL_VIDEO),
        "subtitle_file": str(SUBTITLE_FILE),
        "duration_seconds": round(video_duration, 3),
        "slide_count": len(plans),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
