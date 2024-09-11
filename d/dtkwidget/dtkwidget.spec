%def_disable clang
%def_enable docs

Name: dtkwidget
Version: 5.6.34.0.2.38e3
Release: alt1
Summary: Deepin tool kit widget modules
License: LGPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dtkwidget
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz
Patch: dtkwidget-5.6.28-alt-pkgconfig-find-requires.patch

# for webp (dci) icons
Requires: dqt5-imageformats

# find libraries
%add_findprov_lib_path %_dqt5_libdir

%if_enabled clang
BuildRequires(pre): clang-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires(pre): rpm-build-ninja rpm-macros-dqt5
# Automatically added by buildreq on Thu Oct 19 2023
# optimized out: cmake-modules gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libX11-devel libXext-devel libXfixes-devel libXi-devel libdouble-conversion3 libdtkcore-devel libglvnd-devel libgpg-error libgsettings-qt libp11-kit libdqt5-concurrent libdqt5-core libdqt5-dbus libdqt5-gui libdqt5-help libdqt5-network libdqt5-printsupport libdqt5-sql libdqt5-svg libdqt5-widgets libdqt5-x11extras libdqt5-xml libsasl2-3 libssl-devel libstartup-notification libstdc++-devel libxcb-devel pkg-config python3 python3-base dqt5-base-common dqt5-base-devel dqt5-tools sh5 xorg-proto-devel
BuildRequires: cmake doxygen dtk6-common-devel gsettings-qt-devel libcups-devel libdtkgui-devel libstartup-notification-devel libxcbutil-devel dqt5-svg-devel dqt5-tools-devel dqt5-x11extras-devel

%description
DtkWidget is Deepin graphical user interface for deepin desktop development.

%package -n lib%{name}5
Summary: Libraries for %name
Group: System/Libraries
Provides: libdtk5-widget = %EVR
Obsoletes: libdtk5-widget < %EVR
Requires: libdqt5-core = %_dqt5_version
Requires: libdqt5-gui = %_dqt5_version
Requires: libdqt5-printsupport = %_dqt5_version
Requires: libdqt5-widgets = %_dqt5_version

%description -n lib%{name}5
DtkWidget is Deepin graphical user interface for deepin desktop development.
Libraries for %name.

%package -n lib%name-devel
Summary: Development package for %name
Group: Development/KDE and QT
Provides: dtk5-widget-devel = %EVR
Obsoletes: dtk5-widget-devel < %EVR

%description -n lib%name-devel
Header files and libraries for %name.

%package examples
Summary: Examples for %name
Group: Development/KDE and QT
Provides: dtk5-widget-examples = %EVR
Obsoletes: dtk5-widget-examples < %EVR

%description examples
DtkWidget is Deepin graphical user interface for deepin desktop development.
Examples for %name.

%if_enabled docs
%package doc
Summary: %name documantation
Group: Documentation
BuildArch: noarch
Provides: dtk5-widget-doc = %EVR
Obsoletes: dtk5-widget-doc < %EVR

%description doc
This package provides %name documantation.
%endif

%prep
%setup
%patch -p1

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"
%endif
export PATH=%_dqt5_bindir:$PATH
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=None \
  -DCMAKE_PREFIX_PATH=%_dqt5_libdir/cmake \
  -DCMAKE_SKIP_INSTALL_RPATH:BOOL=no \
  -DCMAKE_INSTALL_RPATH=%_dqt5_libdir \
  -DMKSPECS_INSTALL_DIR=%_dqt5_archdatadir/mkspecs/modules/ \
%if_enabled docs
  -DBUILD_DOCS=ON \
  -DQCH_INSTALL_DESTINATION=%_dqt5_docdir \
%else
  -DBUILD_DOCS=OFF \
%endif
  -DCMAKE_INSTALL_PREFIX=%_prefix \
  -DCMAKE_INSTALL_LIBDIR=%_lib \
  -DDTK_VERSION=5.6.34 \
  -DBUILD_PLUGINS=OFF \
#
cmake --build %_cmake__builddir -j%__nprocs

%install
%cmake_install

%files
%doc README.md LICENSE
%dir %_libdir/dtk5/
%dir %_libdir/dtk5/DWidget/
%_libdir/dtk5/DWidget/bin/
%dir %_datadir/dtk5/
%_datadir/dtk5/DWidget/

%files -n lib%{name}5
%_libdir/lib%name.so.5*

%files -n lib%name-devel
%dir %_includedir/dtk5/
%_includedir/dtk5/DWidget/
%_dqt5_archdatadir/mkspecs/modules/*.pri
%_libdir/cmake/DtkWidget/
%_pkgconfigdir/%name.pc
%_libdir/lib%name.so

%files examples
%dir %_libdir/dtk5/DWidget/
%_libdir/dtk5/DWidget/examples/

%files doc
%_dqt5_docdir/dtkwidget.qch

%changelog
* Wed Sep 11 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.34.0.2.38e3-alt1
- New version 5.6.34-2-g38e3cc14.

* Wed May 08 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.28-alt1
- New version 5.6.28.
- Built via separate qt5 instead system (ALT #48138).

* Fri Mar 29 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.26-alt1
- New version 5.6.26.

* Fri Mar 29 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.25-alt2
- Fixed update from libdtk5-widget.

* Wed Mar 20 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.25-alt1
- New version 5.6.25.

* Tue Mar 05 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.23-alt2
- Required on current qt5 version.

* Fri Mar 01 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.23-alt1
- New version 5.6.23.

* Tue Jan 16 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.22-alt1
- New version 5.6.22.

* Thu Nov 30 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.20-alt1
- New version 5.6.20.
- Cleanup BRs.
- Removed obsoleted patch.
- Fixed missing icons.
- Disabled plugins.
- Renamed subpackages:
  + libdtk5-widget -> dtkwidget.
  + dtk5-widget-devel -> libdtkwidget-devel.
  + dtk5-widget-examples -> dtkwidget-examples.
  + dtk5-widget-doc -> dtkwidget-doc.

* Fri Mar 10 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.8-alt1
- New version.

* Tue Feb 21 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.7-alt1
- New version.

* Mon Feb 13 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.5-alt1
- Fixed version.
- Applied fixed from master branch.

* Wed Jan 25 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.4-alt2.gitd2cb0fb
- Fixed missing icon on titlebar button.

* Fri Jan 20 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.4-alt1.gitd2cb0fb
- New version.
- Spec:
  + Added config subpackage.
  + Added docs switcher.
  + Fixed broken configs.
- Patches:
  + Fixed build using gcc.

* Thu Nov 24 2022 Leontiy Volodin <lvol@altlinux.org> 5.6.0.2-alt2
- Fixed translations.

* Mon Oct 17 2022 Leontiy Volodin <lvol@altlinux.org> 5.6.0.2-alt1
- New version.
- Upstream:
  + use cmake instead qmake.

* Wed Jun 08 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.46-alt1
- New version.
- Upstream:
  + fix: wayland environmental network link dialogue box click invalid.
  + fix: print preview titlebar does not follow the theme changes.
  + fix: abandoned interface update.

* Mon May 23 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.45-alt1
- New version.

* Wed May 04 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.44-alt1
- New version (5.5.44).

* Tue Mar 22 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.42-alt1
- New version (5.5.42).

* Tue Feb 08 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.37-alt1
- New version (5.5.37).

* Tue Jul 06 2021 Leontiy Volodin <lvol@altlinux.org> 5.5.17.1-alt1
- New version (5.5.17.1).

* Mon Jun 28 2021 Leontiy Volodin <lvol@altlinux.org> 5.5.7-alt1
- New version (5.5.7) with rpmgs script.

* Mon May 17 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.20-alt1
- New version (5.4.20) with rpmgs script.

* Thu Apr 08 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.16-alt1
- New version (5.4.16) with rpmgs script.

* Tue Mar 09 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.10-alt1
- New version (5.4.10) with rpmgs script.

* Mon Nov 30 2020 Leontiy Volodin <lvol@altlinux.org> 5.4.1-alt1
- New version (5.4.1) with rpmgs script.

* Wed Oct 28 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0-alt1
- New version (5.3.0) with rpmgs script.

* Mon Oct 05 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.2.15-alt1
- New version (5.2.2.15) with rpmgs script.

* Mon Aug 17 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.2.3-alt1
- Initial build for ALT Sisyphus (thanks fedora and archlinux for this spec).
