# Madoka Kaname × Homura Akemi Codex Pets

> An unofficial fan-made ChatGPT / Codex Pets collection released for Madoka Kaname's October 3 birthday. It includes complete v2 sprite sheets for Madoka Kaname and Homura Akemi in a black dress.

[简体中文](README.md) · [Official Pets documentation](https://learn.chatgpt.com/docs/pets)

<p align="center">
  <img src="pets/madoka-kaname/previews/preview.gif" width="192" alt="Madoka Kaname Codex Pet animation preview">
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="pets/homura-akemi/previews/preview.gif" width="192" alt="Homura Akemi Codex Pet animation preview">
</p>

## Included pets

| Pet | Description | Download |
| --- | --- | --- |
| Madoka Kaname | A gentle work companion in her pink-and-white magical-girl outfit | [spritesheet.png](pets/madoka-kaname/spritesheet.png) |
| Homura Akemi | A quiet work companion in a black dress | [spritesheet.png](pets/homura-akemi/spritesheet.png) |

Both assets pass the official ChatGPT Pets structural preflight:

- v2 transparent PNG at `1536 × 2288`;
- an `8 × 11` grid of `192 × 208` cells;
- 73 required animation frames and 15 fully transparent reserved cells;
- idle, directional movement, wave, jump, failure, waiting, working, review, and 16 look-direction animations.

Each pet directory contains previews and a `metadata.json` file with its SHA-256 digest.

## Latest update

- `v1.0.1`: corrected the oversized raised and extended hands in both waving animations. Pet IDs, file format, and all other animation rows remain unchanged.
- See [CHANGELOG.md](CHANGELOG.md) for the full release history.

## Installation

1. Download `spritesheet.png` from the desired pet directory.
2. Open Pets settings in a ChatGPT surface that supports custom pets.
3. Choose the custom-pet upload/create option and use the downloaded sprite sheet.
4. If the product UI or format changes, follow the [official Pets documentation](https://learn.chatgpt.com/docs/pets).

## Contributing

Issues, compatibility reports, and preview improvements are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request. Do not contribute artwork with unclear provenance or conflicting usage restrictions.

## Rights and disclaimer

This is an unofficial, non-commercial fan project. It is not affiliated with or endorsed by OpenAI, Magica Quartet, Aniplex, SHAFT, or any other rights holder. Characters and related properties belong to their respective owners.

Repository scripts and original documentation are available under the [MIT License](LICENSE-CODE). Character sprite sheets are excluded from the MIT license; see [ASSET-LICENSE.md](ASSET-LICENSE.md).
