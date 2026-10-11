# Complete the RoosterWorks Rescue GameData upload

The repository documentation and validation tools are prepared. The remaining gameplay files are the two source folders under `GameData/`.

1. Download and extract [the prepared GitHub upload ZIP](https://github.com/SockedRooster/RoosterWorks-Rescue) locally (use the archive supplied in ChatGPT, not GitHub's source archive).
2. In [the repository](https://github.com/SockedRooster/RoosterWorks-Rescue), choose **Add file → Upload files** and drag the extracted **GameData** folder into the upload pane.
3. Commit the folder to `main`. The correct paths include:
   - `GameData/AgencyStationRescue/AgencyStationRescue.cfg`
   - `GameData/AgencyStationRescue/Craft/AuroraHaven.craft`
   - `GameData/InterstellarExpansionCampaign/InterstellarExpansion.cfg`
   - `GameData/InterstellarExpansionCampaign/Craft/BopLeviathan.craft`
4. Verify there is **no nested** `GameData/GameData` folder. Do not rename either internal campaign directory or any `.craft` file.
5. GitHub Actions will verify the 20 GameData file hashes and contract/craft references. The ZIP for players is named `RoosterWorks-Rescue-v1.0.0.zip` and can then be attached to a release.

No gameplay changes are necessary for the repository rename. This manual upload step is required because the connected GitHub file actions do not support directly transferring these large existing local craft files.
