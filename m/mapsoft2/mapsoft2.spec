Name:         mapsoft2
Version:      1.4
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

%description
mapsoft2 - programs for working with maps and geodata

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
%_datadir/mapsoft2/*

%changelog
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
