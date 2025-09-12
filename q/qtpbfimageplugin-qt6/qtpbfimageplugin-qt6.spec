%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: qtpbfimageplugin-qt6
Version: 4.7
Release: alt1

Summary: Qt image plugin for displaying Mapbox vector tiles
License: LGPL-3.0
Group: System/Libraries
Url: https://github.com/tumic0/QtPBFImagePlugin

Source: %name-%version.tar

BuildRequires: qt6-base-devel
BuildRequires: qt6-tools
BuildRequires: pkgconfig(zlib)

%description
QtPBFImagePlugin is a Qt image plugin that enables applications capable
of displaying raster MBTiles maps or raster XYZ online maps to also
display PBF(MVT) vector tiles without (almost, see usage) any
application modifications.

Standard Mapbox GL Styles are used for styling the maps. Most relevant
style features used by Maputnik are supported. A default fallback 
style (OSM-Liberty) for OpenMapTiles is part of the plugin.

"Plain" PBF files as well as gzip compressed files (as used in MBTiles)
are supported by the plugin. The tile size is (since version 2.0 of the
plugin) 512px to fit the styles and available data (OpenMapTiles, Mapbox
tiles).

%prep
%setup

%build
qmake-qt6 \
          PREFIX=%_prefix \
          CONFIG+=nostrip \
          QMAKE_CXXFLAGS="%optflags"
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot

%files
%doc LICENSE README.md
%_qt6_plugindir/imageformats/libpbf.so

%changelog
* Fri Sep 12 2025 Nikolay Strelkov <snk@altlinux.org> 4.7-alt1
- New version 4.7.

* Sat Aug 23 2025 Nikolay Strelkov <snk@altlinux.org> 4.6-alt1
- New version 4.6.

* Mon Aug 18 2025 Nikolay Strelkov <snk@altlinux.org> 4.5-alt1
- New version 4.5.

* Thu Jul 31 2025 Nikolay Strelkov <snk@altlinux.org> 4.4-alt1
- New version 4.4.

* Wed Jul 23 2025 Nikolay Strelkov <snk@altlinux.org> 4.3-alt1
- New version 4.3.

* Tue Jun 24 2025 Nikolay Strelkov <snk@altlinux.org> 4.2-alt1
- Initial build for Sisyphus
