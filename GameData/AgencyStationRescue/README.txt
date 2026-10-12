INTER-AGENCY RESCUE & SALVAGE v2.27
===================================

KSP 1.12.5 + Contract Configurator + Kerbalism mission pack.

INSTALL
-------
Copy the AgencyStationRescue folder into GameData, replacing the previous
AgencyStationRescue folder.

CURRENT MISSION PROGRESSION
---------------------------
01. Aurora Haven ................. Station rescue - Kerbin orbit

POST-AURORA MOON PHASE
02A. Mintaka Observatory ......... Station rescue - Minmus orbit
02B. Northstar Frontier Base ..... Surface rescue - Mun
03.  Horizon Frostline Base ...... Surface rescue - Minmus

MAIN RESCUE CHAIN
04. Valles Research Complex ...... Surface rescue - Duna
05. Gilly Far-Side Depot ......... Surface rescue - Gilly
06. Selene Ark ................... Station rescue - Dres orbit

SIDE RESCUE
Ares Meridian .................... Station rescue - Moho orbit
Unlocks after the Mun/Minmus phase and does not gate Duna, Gilly, or Dres.

The Gilly contract intentionally retains the internal ID ASR_IkeFarSideDepot
so existing progression references remain compatible after the Ike -> Gilly
conversion.

MASTER CRAFT / PASSIVE SHIELDING
--------------------------------
All spawned vessels use the user's latest KSP-authored craft files. Physical
part geometry and attachment trees were preserved. Passive Kerbalism Shielding
was loaded by editing only existing Shielding resource amounts:

  Aurora Haven ................... 35%
  Selene Ark (Dres) .............. 80%
  Mintaka Observatory ............ 55%
  Ares Meridian (Moho) ........... 90%
  Northstar Frontier Base ........ 70%
  Horizon Frostline Base ......... 65%
  Valles Research Complex ........ 60%
  Gilly Far-Side Depot ........... 85%

The updated orbital craft retain the Active Shields physically installed by
the user. Surface assets rely primarily on passive shielding.

RESCUE / SALVAGE FLOW
---------------------
Orbital missions spawn a complete damaged station with stranded crew. Dock,
recover the crew to Kerbin, keep the station intact, and successful completion
transfers ownership of the station to KSP.

Surface missions spawn a complete damaged base plus stranded EVA crew nearby.
Reach the waypoint, recover the crew to Kerbin, keep the base intact, and
successful completion transfers ownership of the base to KSP.

All scripted Kerbalism failures remain aboard after salvage and may be repaired
normally with the appropriate Engineer / repair requirements.

LOCATION UPDATES
----------------
Selene Ark is now in Dres orbit.
Ares Meridian is now in Moho orbit.
The former Ike Far-Side Depot design is now deployed on Gilly.

v2.21 progression correction
----------------------------
Main rescue chain:
1. Aurora Haven
2. Mun + both Minmus rescues unlock together
3. Duna after all three are complete
4. Gilly
5. Dres
6. Moho/Ares Meridian is a post-chain epilogue rescue

Group offered/active limit raised to 3 so the Mun/Minmus phase can appear together.
Existing already-offered contracts in an old save are not retroactively withdrawn by
Contract Configurator; decline any stale out-of-order offer once after installing.

v2.22 Mun spawn orientation fix
-------------------------------
Northstar Frontier Base (Mun):
- added roll = 180 to the SpawnVessel placement
- increased spawn height from 0.15 m to 1.00 m
This corrects the inverted surface spawn without modifying the craft file.

v2.23 Northstar orientation correction
--------------------------------------
Northstar Frontier Base (Mun):
- removed the incorrect roll = 180 workaround
- heading changed from 90 to 270
- pitch = 0
- roll = 0
- retained 1.00 m spawn clearance

Reason: Contract Configurator rotates SPH craft using heading about the craft-forward
axis. A 180 degree heading change flips the base top/bottom while preserving the
surface-normal orientation; roll changes the wrong axis.

v2.24 Northstar landing-foot alignment
--------------------------------------
Northstar Frontier Base (Mun): heading = 270, pitch = 0, roll = 45, height = 1.00 m.
The 45-degree roll aligns the base with its landing feet.

v2.25 Horizon Frostline surface orientation fix
------------------------------------------------
Horizon Frostline Base (Minmus): heading = 270, pitch = 0, roll = 45.
This aligns the base landing plane and keeps the docking port off the surface.

v2.26 true command-root surface craft
------------------------------------
Northstar Frontier Base and Horizon Frostline Base were rerooted onto their visible KKAOSS Control command modules.
The hidden ASR-ground-core helper remains installed but is now a child in the vessel tree.
Northstar and Horizon SpawnVessel pitch/roll workarounds were removed; both now use neutral pitch/roll and 1 m surface clearance.
Valles Research Complex and Gilly Far-Side Depot were already correctly rooted on SSPX command cores and were left unchanged.


v2.27 site-coordinate + water-container update
---------------------------------------------
Northstar Frontier Base / Mun site:
  lat = 1.07922678190179
  lon = 22.8564532504125
Horizon Frostline Base / Minmus site:
  lat = 0.457310740769224
  lon = 176.131492263207
Nearby rescue-crew spawn coordinates were translated by the same offsets.
Northstar and Horizon each replace the K&K small Food container with a rescue-pack
K&K small Water variant. The custom variant is cloned from the Kerbalism-compatible
KPBS small container because KPBS's dedicated Water Small part is not loaded under
the pure Kerbalism profile. Existing fullness is preserved in the craft snapshots.
