# Upload RoosterWorks Rescue gameplay — one ZIP

The GitHub repository setup is already committed. Only the **20 gameplay files** (including 12 large saved craft) need importing.

1. Download **`RoosterWorks-Rescue-GitHub-Upload.zip`** from the ChatGPT link in our conversation. **Keep its exact filename.**
2. Open https://github.com/SockedRooster/RoosterWorks-Rescue and choose **Add file → Upload files**.
3. Select **the single ZIP file itself**, not its extracted contents, and commit the upload to `main`.
4. The [Import RoosterWorks Rescue gameplay ZIP](https://github.com/SockedRooster/RoosterWorks-Rescue/actions/workflows/import-gameplay.yml) GitHub Action will automatically:
   - inspect the archive and reject unexpected `GameData` filenames or modified file hashes;
   - extract the two original campaign folders under `GameData/`;
   - run the static mission/craft validation script; and
   - commit the approved gameplay files and remove the temporary ZIP from the current branch.
5. Refresh the repository after the import Action succeeds. You should see `GameData/AgencyStationRescue/` and `GameData/InterstellarExpansionCampaign/`.

If Actions are disabled or the import fails, you can instead extract the ZIP on a computer and use **Add file → Upload files** to upload just the `GameData` folder. Do not rename the internal campaign folders or create `GameData/GameData`.

The named **`RoosterWorks-Rescue-v1.0.0.zip`** is a *separate player installer* for the GitHub Releases page. It is not the repository-import file.
