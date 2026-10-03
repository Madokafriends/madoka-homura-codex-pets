#!/usr/bin/env python3
"""Render repository previews from ChatGPT Pets v2 sprite sheets."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import imageio.v2 as imageio
import numpy as np
from PIL import Image, ImageDraw, ImageFont


CELL_W = 192
CELL_H = 208
SHEET_W = 1536
SHEET_H = 2288
ROWS = [
    ("idle", 6, 130),
    ("running-right", 8, 85),
    ("running-left", 8, 85),
    ("waving", 4, 150),
    ("jumping", 5, 125),
    ("failed", 8, 135),
    ("waiting", 6, 145),
    ("working", 6, 125),
    ("review", 6, 145),
]


def load_frames(sheet: Image.Image, row: int, count: int) -> list[Image.Image]:
    return [
        sheet.crop((col * CELL_W, row * CELL_H, (col + 1) * CELL_W, (row + 1) * CELL_H))
        for col in range(count)
    ]


def save_gif(frames: list[Image.Image], path: Path, duration: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    frames[0].save(
        path,
        save_all=True,
        append_images=frames[1:],
        duration=duration,
        loop=0,
        disposal=2,
        optimize=True,
    )


def checkerboard(size: tuple[int, int], tile: int = 16) -> Image.Image:
    image = Image.new("RGB", size, "#f8f8fa")
    draw = ImageDraw.Draw(image)
    for y in range(0, size[1], tile):
        for x in range(0, size[0], tile):
            if (x // tile + y // tile) % 2:
                draw.rectangle((x, y, x + tile - 1, y + tile - 1), fill="#e9e9ee")
    return image


def flatten(frame: Image.Image) -> Image.Image:
    background = checkerboard(frame.size)
    background.paste(frame, mask=frame.getchannel("A"))
    return background


def save_contact_sheet(sheet: Image.Image, path: Path) -> None:
    label_w = 150
    canvas = checkerboard((label_w + SHEET_W, SHEET_H), tile=24)
    canvas.paste(sheet, (label_w, 0), sheet)
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.load_default()
    labels = [name for name, _, _ in ROWS] + ["look 000-157.5", "look 180-337.5"]
    for row, label in enumerate(labels):
        y = row * CELL_H
        draw.rectangle((0, y, label_w - 1, y + CELL_H - 1), fill="#202027")
        draw.text((12, y + 94), f"{row:02d}  {label}", font=font, fill="white")
    path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(path, optimize=True)


def save_mp4(frames: list[Image.Image], path: Path, fps: int = 9) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with imageio.get_writer(
        path,
        fps=fps,
        codec="libx264",
        quality=8,
        macro_block_size=None,
        ffmpeg_log_level="error",
        output_params=["-pix_fmt", "yuv420p"],
    ) as writer:
        for frame in frames:
            writer.append_data(np.asarray(flatten(frame)))


def render_pet(pet_dir: Path) -> dict[str, object]:
    source = pet_dir / "spritesheet.png"
    with Image.open(source) as opened:
        sheet = opened.convert("RGBA")
    if sheet.size != (SHEET_W, SHEET_H):
        raise ValueError(f"{source}: expected {(SHEET_W, SHEET_H)}, got {sheet.size}")

    preview_dir = pet_dir / "previews"
    row_frames: dict[str, list[Image.Image]] = {}
    for row, (name, count, duration) in enumerate(ROWS):
        frames = load_frames(sheet, row, count)
        row_frames[name] = frames
        save_gif(frames, preview_dir / "states" / f"{name}.gif", duration)

    look_frames = load_frames(sheet, 9, 8) + load_frames(sheet, 10, 8)
    save_gif(look_frames, preview_dir / "look-directions.gif", 130)

    showcase_names = ["idle", "waving", "jumping", "waiting", "working", "review"]
    showcase = []
    for name in showcase_names:
        showcase.extend(row_frames[name])
        showcase.extend([row_frames[name][-1]] * 2)
    save_gif(showcase, preview_dir / "preview.gif", 125)
    save_mp4(showcase, preview_dir / "preview.mp4")

    idle_jump = row_frames["idle"][:3] + row_frames["jumping"] + row_frames["idle"][3:]
    save_gif(idle_jump, preview_dir / "idle-jump-idle.gif", 130)
    save_contact_sheet(sheet, preview_dir / "contact-sheet.png")

    stills = {
        "idle": row_frames["idle"][0],
        "wave": row_frames["waving"][1],
        "waiting": row_frames["waiting"][2],
        "look-right": look_frames[4],
    }
    for name, frame in stills.items():
        frame.save(preview_dir / f"still-{name}.png", optimize=True)

    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    metadata = {
        "file": "spritesheet.png",
        "sha256": digest,
        "sprite_version": 2,
        "dimensions": {"width": SHEET_W, "height": SHEET_H},
        "cell": {"width": CELL_W, "height": CELL_H},
        "frames_per_row": [6, 8, 8, 4, 5, 8, 6, 6, 6, 8, 8],
    }
    (pet_dir / "metadata.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return {"pet": pet_dir.name, **metadata}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = Path(args.root).resolve()
    manifests = [render_pet(path) for path in sorted((root / "pets").iterdir()) if path.is_dir()]
    (root / "manifest.json").write_text(
        json.dumps({"format": "chatgpt-pets-v2", "pets": manifests}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(manifests, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
