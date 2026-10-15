# Active Wireless MEMS

Board-only product concept from the privately supplied `SENSOR.stp`, identified
by Alex as the new wireless MEMS board on 15 October 2026. The STEP assembly is
labelled `202606r1`; this is not evidence of production approval.

The exact STEP envelope is **20 × 16 × 3.227 mm**. `parts-eval.json` records the
source fingerprint, source-part paths and bounds. Tessellation uses 0.035 mm
linear tolerance; glTF converts millimetres to metres and rotates Z-up to Y-up
without reflection or physical resizing. Small curved extrema can differ from
the exact CAD bounds within that tolerance.

The source contains a named BMP390 pressure-sensor model, U3 antenna model and
J1 connector model. U1 is only a package envelope. The fitted parts, UWB versus
Bluetooth PAwR variant, power source and pressure connection remain unconfirmed.
See `spec-check.html`. No enclosure, battery, RF performance, sensor performance
or compliance is inferred from the CAD.

## Build and verify

1. In a private job directory on ai-tools, place the original STEP and run
   `tools/wireless-mems/export_step.FCMacro` under FreeCAD/xvfb, setting
   `WIRELESS_MEMS_JOB` to that directory. The exporter produces `meshes.json`
   and `parts-eval.json`; never add the STEP to this repository.
2. Run Blender on ai-tools with
   `blender -b -t 6 --python tools/wireless-mems/build_assets.py -- JOB`.
   Add `--cpu` when avoiding an existing GPU workload. This builds the coloured
   GLB and three Cycles renders. Transfer only the derived assets and evaluation
   report to this concept folder.
3. `prepare_site.py` records the initial site integration against the preceding
   gallery. It is a one-time migration, not a command to rerun on an already
   integrated gallery. Keep its generated manifest and Inspector changes aligned.
4. Serve the repository locally and run `tools/wireless-mems/check_site.cjs`
   with Playwright available in Node's module path. Optionally set
   `PLAYWRIGHT_CHROMIUM_EXECUTABLE` to an installed Chromium executable. It checks
   Look loading, component controls, explode, Still, gallery discovery and
   browser/network errors, and saves screenshots for visual inspection.
5. Review the three renders and Inspector/Look screenshots. Keep U1 labelled as
   an envelope, not an identified radio. Verify the GLB hash in `manifest.json`
   and build records. The gallery entry follows the existing WIP visibility rule.

The primary public paths are `wireless-mems/` (Look), `assembly.html` (Inspect)
and `../still.html?c=wireless-mems` (Still). The share image uses the approved
Active-Edge lockup. No raw STEP download is exposed.

Assisted-by: Briar
