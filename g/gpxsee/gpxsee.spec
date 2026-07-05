%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: gpxsee
Version: 16.11
Release: alt1

Summary: GPS log file viewer and analyzer
License: GPL-3.0
Group: Sciences/Geosciences
Url: https://github.com/tumic0/gpxsee

Source: %name-%version.tar

BuildRequires: qt6-base-devel
BuildRequires: qt6-tools
BuildRequires: qt6-positioning-devel
BuildRequires: qt6-serialport-devel
BuildRequires: qt6-svg-devel
BuildRequires: qt6-multimedia-devel
BuildRequires: pkgconfig(zlib)

Requires: qtpbfimageplugin-qt6

%description
GPXSee is a Qt-based GPS log file viewer and analyzer that supports all
common GPS log file formats.

Features
- Opens GPX, TCX, FIT, KML, NMEA, IGC, CUP, SIGMA SLF, Suunto SML, LOC,
  GeoJSON, OziExplorer (PLT, RTE, WPT), Garmin GPI&CSV, TomTom OV2&ITN,
  ONmove OMD/GHP, TwoNav (TRK, RTE, WPT), GPSDump WPT, Velocitek VTK,
  Vakaros VKX, 70mai GPS logs and geotagged JPEG files.
- Opens geo URIs (RFC 5870).
- User-definable online maps (OpenStreetMap/Google tiles, WMTS, WMS,
  TMS, QuadTiles).
- Offline maps (MBTiles, OziExplorer maps, TrekBuddy maps/atlases,
  Garmin IMG/GMAP & JNX maps, TwoNav RMaps, GeoTIFF images, BSB charts,
  ENC charts, KMZ maps, AlpineQuest maps, Locus/OsmAnd/RMaps SQLite maps,
  Mapsforge vector maps, QCT maps, GEMF maps, Osmdroid SQLite maps, Orux
  maps,
  ESRI World-File georeferenced images).
- Elevation, speed, heart rate, cadence, power, temperature and gear
  ratio/shifts graphs.
- Support for DEM files (SRTM HGT).
- Support for multiple tracks in one view.
- Support for POI files.
- Print/export to PDF/PNG.
- Full-screen mode.
- HiDPI/Retina displays & maps support.
- Real-time GPS position.
- Windows, macOS, Linux and Android builds.

%prep
%setup
mv -v licence.txt license.txt
sed -i 's|^Categories=.*|Categories=Science;Maps;Geography;|' pkg/linux/gpxsee.desktop

%build
lrelease-qt6 gpxsee.pro
qmake-qt6 \
          PREFIX=%_prefix \
          CONFIG+=nostrip \
          QMAKE_CXXFLAGS="%optflags" \
          gpxsee.pro
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot

%find_lang %name

%files -f %{name}.lang
%doc license.txt CONTRIBUTING.md README.md
%_bindir/%name
%_desktopdir/%{name}.desktop
%dir %_datadir/%{name}
%_datadir/%{name}/*
%_iconsdir/hicolor/*/*/*
%_datadir/metainfo/%{name}.appdata.xml
%_datadir/mime/packages/%{name}.xml

%changelog
* Sun Jul 05 2026 Nikolay Strelkov <snk@altlinux.org> 16.11-alt1
- New version 16.11.

* Sat Jun 27 2026 Nikolay Strelkov <snk@altlinux.org> 16.10-alt1
- New version 16.10.

* Wed Jun 17 2026 Nikolay Strelkov <snk@altlinux.org> 16.9-alt1
- New version 16.9.

* Sun Jun 07 2026 Nikolay Strelkov <snk@altlinux.org> 16.8-alt1
- New version 16.8.

* Sat May 16 2026 Nikolay Strelkov <snk@altlinux.org> 16.7-alt1
- New version 16.7.

* Sun Apr 26 2026 Nikolay Strelkov <snk@altlinux.org> 16.6-alt1
- New version 16.6.

* Wed Apr 22 2026 Nikolay Strelkov <snk@altlinux.org> 16.5-alt1
- New version 16.5.

* Fri Apr 17 2026 Nikolay Strelkov <snk@altlinux.org> 16.3-alt1
- New version 16.3.

* Wed Apr 08 2026 Nikolay Strelkov <snk@altlinux.org> 16.2-alt1
- New version 16.2.

* Sun Apr 05 2026 Nikolay Strelkov <snk@altlinux.org> 16.1-alt1
- New version 16.1.

* Sun Mar 15 2026 Nikolay Strelkov <snk@altlinux.org> 16.0-alt1
- New version 16.0.

* Wed Feb 25 2026 Nikolay Strelkov <snk@altlinux.org> 15.11-alt1
- New version 15.11.

* Fri Jan 30 2026 Nikolay Strelkov <snk@altlinux.org> 15.10-alt1
- New version 15.10.

* Mon Jan 12 2026 Nikolay Strelkov <snk@altlinux.org> 15.8-alt1
- New version 15.8.

* Sat Dec 20 2025 Nikolay Strelkov <snk@altlinux.org> 15.7-alt1
- New version 15.7.

* Sat Dec 13 2025 Nikolay Strelkov <snk@altlinux.org> 15.6-alt1
- New version 15.6.

* Fri Nov 28 2025 Nikolay Strelkov <snk@altlinux.org> 15.5-alt1
- New version 15.5.

* Sun Nov 23 2025 Nikolay Strelkov <snk@altlinux.org> 15.4-alt1
- New version 15.4.

* Sun Nov 09 2025 Nikolay Strelkov <snk@altlinux.org> 15.3-alt1
- New version 15.3.

* Thu Oct 30 2025 Nikolay Strelkov <snk@altlinux.org> 15.0-alt1
- New version 15.0.

* Thu Oct 16 2025 Nikolay Strelkov <snk@altlinux.org> 14.1-alt1
- New version 14.1.

* Fri Sep 12 2025 Nikolay Strelkov <snk@altlinux.org> 13.47-alt1
- New version 13.47.

* Mon Aug 18 2025 Nikolay Strelkov <snk@altlinux.org> 13.46-alt1
- New version 13.46.

* Wed Jul 23 2025 Nikolay Strelkov <snk@altlinux.org> 13.45-alt1
- New version 13.45.

* Fri Jun 27 2025 Nikolay Strelkov <snk@altlinux.org> 13.44-alt2
- Applied repocop fix for freedesktop-desktop

* Tue Jun 24 2025 Nikolay Strelkov <snk@altlinux.org> 13.44-alt1
- Initial build for Sisyphus
