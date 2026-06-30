#Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%def_enable	build_test

Name: opencpn
Version: 5.14.0
Release: alt1
Summary: A free and open source software for marine navigation

License: GPL-2.0-or-later AND LGPL-2.0-or-later
Group: Other

URL: https://opencpn.org
VCS: https://github.com/OpenCPN/OpenCPN

Source: OpenCPN-%version.tar
Patch1: opencpn-5.14.0-exclude-install-docs.patch
Patch2: opencpn-5.14.0-init-app-fixes.patch

Requires: %name-data = %EVR

Buildrequires(pre): rpm-macros-cmake
BuildRequires: /proc
BuildRequires: rpm-build-cmake
Buildrequires: gcc-c++
Buildrequires: libgtk+3-devel
Buildrequires: libEGL-devel
Buildrequires: libwxBase3.2-devel
Buildrequires: libGLEW-devel
BuildRequires: libudev-devel
BuildRequires: libshape-devel
BuildRequires: bzlib-devel
BuildRequires: tinyxml-devel
BuildRequires: libarchive-devel
BuildRequires: liblz4-devel
BuildRequires: lsb-release
BuildRequires: asciidoc
BuildRequires: libssl-devel
BuildRequires: rapidjson-devel
BuildRequires: libcurl-devel
BuildRequires: liblzma-devel
BuildRequires: libelf-devel
BuildRequires: libusb-devel
BuildRequires: libgtest-devel
BuildRequires: libXrandr-devel
BuildRequires: libsqlite3-devel
BuildRequires: libsndfile-devel
BuildRequires: libportaudio2-devel
BuildRequires: libjasper-devel
# Use git core tools to upstream-patch source under the build local libdnet-1.18.0
# Sisyphus - libdnet-16.2
BuildRequires: git-core

%description
OpenCPN is a free software project to create a concise chart plotter
and navigation software, for use underway or as a planning tool.
OpenCPN is developed by a team of active sailors using real world
conditions for program testing and refinement. Files developed in
this project are copyright (c) The OpenCPN developers and distributed
using a GPLv2+ license. OpenCPN also uses code from other sources
with other licenses (look to the LICENSING file).

%package data
Summary: Architecture independent files for OpenCPN
Group: Other
BuildArch: noarch
Requires: %name = %EVR
Requires: icon-theme-hicolor

%description data
%summary.

%prep
%setup -n OpenCPN-%version
%patch1 -p1
%patch2 -p1

%build

# -DOCPN_BUILD_TEST=ON - default
# https://github.com/OpenCPN/OpenCPN/blob/Release_5.14.0/CMakeLists.txt#L168
%cmake -DOCPN_BUNDLE_DOCS=OFF \
       -DOCPN_BUNDLE_TCDATA=ON \
       -DOCPN_BUNDLE_GSHHS=ON \
       -DQT_ANDROID=OFF \
%if_disabled build_test
       -DOCPN_BUILD_TEST=OFF
%endif

%cmake_build

%install
%cmake_install

%find_lang %name
%find_lang --append --output=%name.lang %name-dashboard_pi
%find_lang --append --output=%name.lang %name-grib_pi
%find_lang --append --output=%name.lang %name-wmm_pi
%find_lang --append --output=%name.lang %name-chartdldr_pi

%files
%doc COPYING.* LICENSING *.md README
%doc data/*.pdf

%_bindir/%name
%_bindir/%name-cmd

%dir %_libdir/%name
%_libdir/%name/*_pi.so
%prefix/libexec/%name-glutil

%files data -f %name.lang
%_man1dir/*.1.*
%_datadir/metainfo/*.xml
%_datadir/%name
%_iconsdir/hicolor/*/apps/*.png
%_iconsdir/hicolor/*/apps/*.svg
%_desktopdir/%name.desktop

%changelog
* Tue Jun 30 2026 Polina Poidenko <polipoki@altlinux.org> 5.14.0-alt1
- New version 5.14.0.
- Update buildreqs.
- Enable build tests.
- CmakeLists.txt: Exclude installation of documentation in not standard dir.
- ocpn_frame.cpp: Fix "Segmentation fault" in first run app
  when clicking Tools -> Settings.

* Fri Jun 23 2023 Anton Midyukov <antohami@altlinux.org> 5.8.2-alt1
- new version 5.8.2

* Sun Oct 30 2022 Sergey Y. Afonin <asy@altlinux.org> 5.7.1-alt0.2
- changes in spec file:
  + removed build time switch for switching gtk+2/gtk+3
  + added build time switch for enable build tests

* Sat Oct 29 2022 Sergey Y. Afonin <asy@altlinux.org> 5.7.1-alt0.1
- New (development) version, 20221029 snapshot (due to build with libwxGTK 3.2)
- removed patches:
  + opencpn-5.0.0-mga-missing_glx_include.patch
  + opencpn-5.2.4-dashboard.cpp.patch
- switched to libpcre2-devel (due to same change of glib-2.0)

* Wed Apr 28 2021 Arseny Maslennikov <arseny@altlinux.org> 5.2.4-alt1.1
- NMU: spec: adapted to new cmake macros.

* Sun Feb 07 2021 Sergey Y. Afonin <asy@altlinux.org> 5.2.4-alt1
- New version
- added opencpn-5.2.4-dashboard.cpp.patch

* Wed Feb 03 2021 Sergey Y. Afonin <asy@altlinux.org> 5.2.0-alt1
- New version
- added icon-theme-hicolor to Requires of data subpackage
- removed patches:
  + opencpn-5.0.0-aarch64-plugindir.patch
  + opencpn-5.0.0-detection_of_wxWebview.patch

* Thu Apr 30 2020 Sergey Y. Afonin <asy@altlinux.org> 5.0.0-alt5
- built with GTK+3 (due to same change of libwxsvg-1.5.22-alt2)
- updated %%description

* Tue Apr 28 2020 Sergey Y. Afonin <asy@altlinux.org> 5.0.0-alt4
- updated License tag to SPDX syntax, changed to GPL-2.0-or-later
- built with GTK+2
- added patches from https://github.com/OpenCPN/OpenCPN/issues/1494
  + opencpn-5.0.0-mga-missing_glx_include.patch (fixed build with wxGTK 3.1.3)
  + opencpn-5.0.0-aarch64-plugindir.patch

* Tue Apr 21 2020 Sergey Y. Afonin <asy@altlinux.org> 5.0.0-alt3
- fixed FTBFS: added opencpn-5.0.0-detection_of_wxWebview.patch
- added build time switch for switching gtk+2/gtk+3 (in spec-file)

* Tue Aug 20 2019 Anton Midyukov <antohami@altlinux.org> 5.0.0-alt2
- add_optflags (pkg-config --cflags pango) (Fix FTBFS)
- ExcludeArch: ppc64le

* Thu Mar 28 2019 Sergey Y. Afonin <asy@altlinux.ru> 5.0.0-alt1
- New version (thanx to TEAM)
- Built with wxGTK3.1
- Added some system libraries for building (ALT #36402)
- Disabled opencpn-4.4.0-fix_library_path.patch

* Wed Aug 22 2018 Grigory Ustinov <grenka@altlinux.org> 4.4.0-alt2
- Fix library path.
- Little cleanup spec.
- Fix bogus date in changelog.

* Thu Dec 01 2016 Sergey Y. Afonin <asy@altlinux.ru> 4.4.0-alt1
- New version

* Sun Feb 16 2014 Sergey Y. Afonin <asy@altlinux.ru> 3.2.2-alt1
- New version
- Moved architecture-independent data to noarch subpackage %name-data

* Wed Apr 03 2013 Sergey Y. Afonin <asy@altlinux.ru> 3.2.0-alt1
- Initial build for ALT Linux

* Sat Sep 22 2012 Eric 'Sparks' Christensen <sparks@fedoraproject.org> - 3.0.2-1
- Initial package.
