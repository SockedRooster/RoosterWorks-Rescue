# RoosterWorks Rescue

**Rescue, salvage, and interstellar exploration contracts for Kerbal Space Program 1**, by SockedRooster.

RoosterWorks Rescue combines two existing Contract Configurator campaigns into one downloadable addon. It is intended for a heavily modded KSP **1.12.5** installation, especially Kerbalism, SSPXr and the author's Promised Worlds/OPM setup.

| Campaign | Component version | Contracts | Bundled craft |
| --- | --- | ---: | ---: |
| Agency Station & Surface Rescue | **v2.27** | 8 | 8 |
| Interstellar Expansion Campaign | **v1.3** | 11 | 4 |
| **Total** | Unified release **v1.0.0** | **19** | **12** |

## What it adds

**Agency Station & Surface Rescue** includes damaged stations and surface bases, stranded crews and salvage opportunities at Kerbin, Mun, Minmus, Duna, Gilly, Dres and Moho. Complete rescues to recover crews and retain salvage. The Gilly mission deliberately retains the historic internal ID `ASR_IkeFarSideDepot` to preserve progression and save compatibility.

**Interstellar Expansion Campaign** provides exploration/construction progression involving Tuun, Puf, Debdeb, Gurdamma, Donk, Lapat and Umod, along with mysteries at Plock and Bop. Supplied craft include damaged facilities and vessels for scripted salvage encounters.

## Requirements

- KSP 1.12.5, Contract Configurator and Kerbalism
- Station Parts Expansion Redux (SSPXr) for the station rescue missions and relevant craft
- Kerbal Planetary Base Systems (KPBS / `PlanetarySurfaceStructures`) and ModuleManager for the surface rescues and water-container patch
- Promised Worlds for the interstellar system content, and Outer Planets Mod for the Plock event
- Additional mods may be necessary for individual craft because their saved part lists reflect the author's modded installation

The relevant `CONTRACT_TYPE:NEEDS` gates suppress contracts when listed prerequisites are absent. This does not guarantee that all third-party parts used by a saved craft will be installed. The package does **not** distribute third-party mods.

## Installation

1. Exit KSP and back up saves before upgrading.
2. Remove any old `GameData/AgencyStationRescue` and `GameData/InterstellarExpansionCampaign` folders; don't merge older configs.
3. Download the named **`RoosterWorks-Rescue-v1.0.0.zip`** player asset from [Releases](https://github.com/SockedRooster/RoosterWorks-Rescue/releases) when published, and extract it into the **KSP installation root** (the folder containing `GameData`).
4. The game should then contain:
   - `GameData/AgencyStationRescue/AgencyStationRescue.cfg`
   - `GameData/AgencyStationRescue/AgencyGroundRescue.cfg`
   - `GameData/AgencyStationRescue/Craft/`
   - `GameData/InterstellarExpansionCampaign/InterstellarExpansion.cfg`
   - `GameData/InterstellarExpansionCampaign/Craft/`
5. Start KSP with the dependencies installed, and check Contract Configurator for available missions as career progress unlocks them.

**Important:** `RoosterWorks Rescue` is the public project name, but the internal `AgencyStationRescue` and `InterstellarExpansionCampaign` directories and contract IDs are intentionally unchanged. Their contract definitions contain `craftURL` references to those exact directories. Renaming them inside `GameData` would break craft spawning and potentially existing saves.

Do not use GitHub's automatically generated **Source code (zip)** archive as an installer. The game-install ZIP contains only the proper `GameData` tree, a README, and the license.

## Repository and source

- `GameData/AgencyStationRescue/`: the approved Agency v2.27 gameplay configs, craft and history
- `GameData/InterstellarExpansionCampaign/`: the approved Interstellar v1.3 configs, craft and history
- `Tools/validate.py`: static mission counts, craft-path checks and SHA-256 verification
- `CHECKSUMS-SHA256.txt`: hashes for the recovered source assets
- `RELEASE_NOTES.md` and `CHANGELOG.md`: packaging and version notes

The game configs and craft are preserved from the approved v2.27/v1.3 master. This repository preparation changes branding/documentation only, not gameplay. Validation is **static** and cannot replace actual KSP contract/spawn testing.

## Support

Report issues at [GitHub Issues](https://github.com/SockedRooster/RoosterWorks-Rescue/issues). MIT license applies to original RoosterWorks content; Kerbal Space Program and required third-party projects remain separately licensed.
