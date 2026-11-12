# GPR surface & bed picking tool

A lightweight, browser-based tool for manually picking the **glacier surface** and **bed**
in ground-penetrating radar (GPR) radargrams. It was built for an inter-analyst experiment
in which 40 analysts picked the same 15 UAV-borne GPR radargrams from Eastern-Alpine
glaciers, to quantify how much manual picking contributes to ice-thickness uncertainty.

**Live:** https://anna7br.github.io/gpr-picking-experiment/ (the experiment is closed; the tool stays online as a demo)

| | |
|---|---|
| 📄 **Paper** | Siebenbrunner and others: *The human factor in GPR-derived ice thickness: Inter-analyst variability as a benchmark for automated boundary layer picking* (submitted to the Annals of Glaciology). Preprint: [link coming soon](#) <!-- TODO-PREPRINT --> |
| 🗂 **Dataset** | Analyst picks, model picks, human consensus and the radargrams (CC BY 4.0): [Zenodo, DOI coming soon](#) <!-- TODO-ZENODO: https://doi.org/10.5281/zenodo.XXXXXXX --> |
| 💻 **Code** | This repository (MIT licence) |

## Features

- Single static HTML file with plain JavaScript: no installation, build step, server or dependencies.
- Two horizons per radargram (surface and bed), with a *bed not interpretable* flag.
- Click to add vertices, drag to move them, undo, zoom (wheel) and pan (right-drag).
- Grayscale or seismic (blue–white–red) colour map.
- Images are opened from the user's disk (**Open images…**) or from a hosted list. Nothing is uploaded anywhere.
- Picks are exported as a CSV in the format of the [VGG Image Annotator (VIA) 2.x](https://www.robots.ox.ac.uk/~vgg/software/via/),
  so they can be read with existing VIA tooling.

## Usage

1. Open https://anna7br.github.io/gpr-picking-experiment/bed_pick_annotator.html, or download this repository
   and double-click `bed_pick_annotator.html`.
2. Click **Open images…** and select one or more radargram images (PNG/JPG). To repeat the
   experiment, use `radargrams_png.zip` from the Zenodo dataset.
3. Choose **Surface (s)** or **Bed (b)** and left-click along the reflection, left to right.
   Move between images with **Prev/Next** or the arrow keys.
4. Click **Download my results (CSV)**. The file is saved as `analyst_<name>.csv`.

The participant instructions used in the experiment are archived on the [landing page](https://anna7br.github.io/gpr-picking-experiment/).

> The seismic colour map needs pixel access to the image. It works on the hosted site and with
> images opened via **Open images…**. It does not work with images loaded from a hosted list
> when the page itself is opened from disk (`file://`).

### Hosting a fixed image set

To have the tool load a predefined set of images automatically (as in the experiment), put
the images in an `images/` folder next to `bed_pick_annotator.html` and run

```
python make_images_json.py
```

This writes `images.js` (repository root) and `images/images.json`. Then host the folder on any
static web space (GitHub Pages, Netlify, institutional web server). To load images from another
location, change `BASE_URL` at the top of the script in `bed_pick_annotator.html`.
`.gitignore` excludes images on purpose: publish research data in a data repository, not here.

## Output format

One row per drawn horizon, with the VIA 2.x CSV columns:

| Column | Content |
|---|---|
| `filename` | Image file name |
| `file_size` | Always `-1` (not used) |
| `file_attributes` | JSON: `uninterpretable` (`"yes"` or `""`), `img_w`, `img_h` (image size in pixels) |
| `region_count` | `1` for a horizon row (`0` for a flag-only row) |
| `region_id` | Index of the horizon on this image (`0`, `1`) |
| `region_shape_attributes` | JSON polyline: `{"name":"polyline","all_points_x":[...],"all_points_y":[...]}` in image pixels, ordered left to right |
| `region_attributes` | JSON: `{"boundary":"surface"}` or `{"boundary":"bed"}` |

An image flagged *bed not interpretable* with no lines drawn gets one row with empty shape attributes.
Converting pixels to two-way travel time or depth requires the vertical scale of the exported
images; for the experiment radargrams this is described in the Zenodo dataset.

## Citation

If you use this tool, please cite the paper (see above) and this repository; citation metadata
are in [`CITATION.cff`](CITATION.cff).

## Licence

The code in this repository is released under the [MIT licence](LICENSE).
The radargrams and picks are **not** part of this repository; they are published on Zenodo under CC BY 4.0.

## Acknowledgements

Developed at [GEORESEARCH](https://www.georesearch.ac.at) within the
[MELT.AI](https://www.georesearch.ac.at/en/areas/research/research-projects/project-meltai/) project,
as part of a PhD at the Technical University of Munich. The CSV format follows the VGG Image Annotator
(Dutta and Zisserman, 2019). Many thanks to all participants of the picking experiment.

## Contact

Anna Siebenbrunner, GEORESEARCH Forschungsgesellschaft mbH, Austria –
[ORCID 0000-0002-2255-2354](https://orcid.org/0000-0002-2255-2354) –
anna.siebenbrunner@georesearch.ac.at
