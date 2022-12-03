Name:         mapsoft2
Version:      2.0
Release:      alt1

Summary:      mapsoft2 - programs for working with maps and geodata
Group:        Sciences/Geosciences
Url:          https://slazav.github.io/mapsoft2/
Packager:     Vladislav Zavjalov <slazav@altlinux.org>
License:      GPL3.0

Source:        %name-%version.tar

BuildRequires: gcc-c++ libgtkmm3-devel libcairomm-devel
BuildRequires: libjansson-devel libxml2-devel libzip-devel zlib-devel libproj-devel
BuildRequires: libjpeg-devel libgif-devel libtiff-devel libpng-devel libdb4.7-devel
BuildRequires: librsvg-devel libcurl-devel
BuildRequires: /usr/bin/pod2man /usr/bin/pod2html /usr/bin/unzip
BuildRequires: transfig ImageMagick-tools

%description
mapsoft2 - programs for working with maps and geodata

%package vmap-data
Summary: mapsoft-vmap-data - example of data and scripts for vector map handling
Group: Sciences/Geosciences
Requires: %name = %version-%release
BuildArch: noarch

%description vmap-data
Example of data, scripts, xfig libraries for vector map handling.


%prep
%setup -q

%build
tar -xvf modules.tar
export SKIP_IMG_DIFFS=1
%make

%install
%makeinstall initdir=%buildroot%_initdir

%files
%_bindir/ms2*
%_mandir/man1/ms2*
%_mandir/man5/mapsoft2*
%dir %_datadir/mapsoft2
%_datadir/mapsoft2/mapsoft2.css
%_datadir/mapsoft2/maps_menu.json

%files vmap-data
%_datadir/mapsoft2/render.cfg
%_datadir/mapsoft2/types.cfg
%_datadir/mapsoft2/pics
%_datadir/xfig/Libraries/*

%changelog
* Sat Dec 03 2022 Vladislav Zavjalov <slazav@altlinux.org> 2.0-alt1
This is a major update with many incompatable and not very
well tested changes, mostly in vector map system.
- New vector map system: vmap2 and vmap2db formats,
  mapdb database is obsoleted.
- New programs ms2vmap and ms2vmapdb instead of ms2mapdb.
- Install all default data and scripts for map rendering.
- New ms2render program for rendering geodata, DEM, vector
  and raster maps; remove this code from ms2conv.
- New syntax of define command in vmap render configuration
  (everything else should work as before).
- ms2geofig: new actions: make_ref, get.
- Update documentation, examples and man pages.

* Sun Oct 23 2022 Vladislav Zavjalov <slazav@altlinux.org> 1.8-alt1
- switch to new libproj API;
- ms2conv: modify --join option
- ms2geofig: add srtm data, add raster maps
- ms2view: a few fixes of panoramic veiw

* Thu Jun 16 2022 Vladislav Zavjalov <slazav@altlinux.org> 1.7-alt1
- Drawing tracks: --trk_draw_width option
- Downloading tiled maps: --insecure, --user_agent, --http_ref options
- Making map reference: --coords_nom, --coords_file options
- TIFF: --tiff_compression option -- support many compression types
- better support for ALOS DEM files
- FIG/GeoFIG support
- fix build with gcc12.1.1

* Sun Apr 18 2021 Vladislav Zavjalov <slazav@altlinux.org> 1.6-alt1
- Drawing maps, tracks, waypoints, srtm-data:
    Fix projection setting if map boundaries can not be converted.
    Fix adjusting waypolit lable positions, avoid infinite loops.
    Fix multi-thread locking in waypoint rendering.
    Fix default track color (blue).
    Fix drawing summit labels on tiles (srtm layer).
    Use srtm_bgcolor if picture is out-of-scale
    When drawing tiled maps do not fail at empty images, return color 0
- Geodata, geo-conversions:
  - Read-only support for Polygon/MultiPolygon features in GeoJSON.
  - New alias: SU<n>N for soviet grid without zone prefix.
- Creating map references (mkref):
  - Allow floating-point arguments in --mag and --dpi options when creating a map.
  - Add --north option for --mkref=nom.
  - Set default border in "tiles" and "proj" modes.
- Vector maps:
  - Add `clip` drawing feature: set clipping for all following steps
  - Value of --clip-border setting is not changing then configuring `brd`
    step, it also affects out-of-scale filling.
  - Add `fit_patt_size` drawing option.
  - Always load patterns at original size.
  - Fix a few problems with pattern rendering.
  - Support lable scaling (import/export/rendering).
- Rendering tiles:
  - Always crop tile range to [0,0,2^z,2^z]
  - Create sub-directories when creating tiles, allow tile templates with subdirs
    (thanks to @ioctl).
  - A few optimizations for creating tile maps (thanks to @ioctl):
    do not create empty tiles, do not re-assemble old tiles in --tmap_scale mode,
    a bit faster color quantization.
- geo_nom, geo_tiles:
  - ms2nom: -W option: use WGS coordinates in calculations.
  - Fix problems with crossing lon=+180/-180 
  - Add --cover option with figure or geo-file argument (thanks to @ioctl).

* Thu Dec 03 2020 Vladislav Zavjalov <slazav@altlinux.org> 1.5-alt1
- Reading/writing geodata:
  - use filename as a waypoint list name when reading waypolints from gpx or wpt,
  - fix writing Ozi map files (Projection Setup line),
  - fix reading track comments from GeoJSON.
- Geodata filtering:
  - add name parameter to --join filter,
  - add --rescale_maps and --shift_maps filters (same as in mapsoft1)
- Update documentation; add geodata_ru.htm text.
- Map rendering:
  - add --map_min_sc, --map_max_sc, --map_def_col options,
  - fix and optimize drawing of multiple maps combined in a single map list.
- ms2view: many tools for editing geodata. Interface is not finished,
  but a few operations are possible: adding/moving/deleting track points,
  adding/moving/deleting/editing waypoints, adding/deleting/editing tracks.
- Fix error handling in libtiff interface.

* Sun Nov 15 2020 Vladislav Zavjalov <slazav@altlinux.org> 1.4-alt1
- GeoJSON format: add extension for writing/reading maps. Now mapsoft2
  geodata structure can be stored in json without losses.
- SRTM layer: fix a few problems: parameter dialog, tile drawing,
  coordinate calculation, srtm_width file reading. Add GeoTiff support.
- Track layer: fix error in color setting. Adding new tracks in the viewer.
- Map layer: fix handling of map lists with multiple maps, fix a few
  problems with switching different viewer projections.
- Maps menu: use {/usr/share/,${HOME}/.}mapsoft2/maps_menu.json
  instead of hardcoded list of maps.
- ms2conv: --srtm option, --htm option. --name, --comm filters.
- Rendering raster images: --add,--title,--title_size options,
  Fix paths in map-files. Fix --mag option. Fix border handling for
  multiple maps.
- MapDB: change configuration file format for MP import/export
  (similar to VMAP import/export). Fix error in geohash calculation.
  Fix label rendering (scale max_text_size properly).
- ANSI escape sequences (\n, \t etc.) and empty words ("") in all
  configuration files (in read_words).
- Avoid throwing c++ exceptions through c code (in image/io_jpeg,io_tiff),
  remove ExcludeArch: armh.
- Fix difference between 32- and 64-bit systems (in image/image_remap).
- Add ms2img program: converting raster images with mapsoft2 libraries.

* Fri Sep 11 2020 Vladislav Zavjalov <slazav@altlinux.org> 1.3-alt1
- viewer: fix a few problems with tiled maps, rescaling and bounding box setting;
  faster srtm layers.
- geodata rendering: fix border rendering, modify options for border setting.
  Allow rendering of tile sets.
- image/colors: fix color handling, add options for loading/saving colormaps.
- mapdb rendering: change reference, border, scale settings.
- spec: add /home/sla/mapsoft2ir %_datadir/mapsoft2 to files section

* Sat Aug 29 2020 Vladislav Zavjalov <slazav@altlinux.org> 1.2-alt1
Viewer:
- SRTM data support (map layer, panoramic view, drowing options dialog)
- Tile map support, improve viewer geo-reference algorythms
- "Track drawing options" dialog
- "Show point information" dialog
- "Use map reference" action
Other:
- fix error with reading integer values from GeoJSON
- `SU` projection: Pulkovo CS with automatic zone number
- fix loading PNG images with depth<8

* Mon Jun 22 2020 Vladislav Zavjalov <slazav@altlinux.org> 1.1.1-alt2
- ExcludeArch: armh (libjpeg + c++ exceptions problem)

* Sun Jun 21 2020 Vladislav Zavjalov <slazav@altlinux.org> 1.1.1-alt1
- update documentation, add GB projection alias, further development

* Sat Apr 04 2020 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt2
- fix build on i586 (rounding errors in modules/geom_tools/np.test.cpp)

* Sat Apr 04 2020 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt1
- add ms2mapdb program - work with mapsoft2 vector maps
  (conversion to/from mp/vmap, rendering)
- basic support for mapdb in ms2view
- ms2proj: --scale, --shift options
- update documentation
- change packaging, use git-submodules, fix a few errors.

* Wed Oct 09 2019 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt1
- v1.0 - first release, first build for altlinux
