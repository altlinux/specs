%def_disable clang

Name: dtkwidget
Version: 5.6.0.2
Release: alt2
Summary: Deepin tool kit widget modules
License: LGPL-3.0+ and GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dtkwidget
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz
Patch: 0001-fixtranslate-path-of-translate.patch

%if_enabled clang
BuildRequires(pre): clang-devel
%endif
BuildRequires(pre): rpm-build-ninja
BuildRequires: cmake
BuildRequires: qt5-linguist
BuildRequires: qt5-base-devel-static
BuildRequires: qt5-tools-devel
BuildRequires: qt5-svg-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: dtk5-core-devel
BuildRequires: dtk5-gui-devel
BuildRequires: dtk5-common
BuildRequires: gsettings-qt-devel
BuildRequires: deepin-qt-dbus-factory-devel
BuildRequires: libudev-devel
BuildRequires: librsvg-devel
BuildRequires: libstartup-notification-devel
BuildRequires: libXi-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libxcbutil-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libXrender-devel
BuildRequires: libcups-devel
BuildRequires: libgtest-devel
BuildRequires: doxygen qt5-tools
# libQt5Gui.so.5(Qt_5_PRIVATE_API) needed by dtkwidget
BuildRequires: libqt5-gui

%description
DtkWidget is Deepin graphical user interface for deepin desktop development.

%package -n libdtk5-widget
Summary: Libraries for %name
Group: System/Libraries

%description -n libdtk5-widget
DtkWidget is Deepin graphical user interface for deepin desktop development.
Libraries for %name.

%package -n dtk5-widget-devel
Summary: Development package for %name
Group: Development/KDE and QT

%description -n dtk5-widget-devel
Header files and libraries for %name.

%package -n dtk5-widget-examples
Summary: Examples for %name
Group: Development/KDE and QT

%description -n dtk5-widget-examples
DtkWidget is Deepin graphical user interface for deepin desktop development.
Examples for %name.

%package -n dtk5-widget-doc
Summary: %name documantation
Group: Documentation
BuildArch: noarch

%description -n dtk5-widget-doc
This package provides %name documantation.

%prep
%setup
%patch -p1
sed -i "s|'/lib'|'/%_lib'|" conanfile.py
sed -i 's|CMAKE_INSTALLL_PREFIX|CMAKE_INSTALL_PREFIX|' \
  docs/CMakeLists.txt

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"
%endif
export PATH=%_qt5_bindir:$PATH
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DMKSPECS_INSTALL_DIR=%_qt5_archdatadir/mkspecs/modules/ \
  -DCMAKE_INSTALL_PREFIX=%_prefix \
  -DCMAKE_INSTALL_LIBDIR=%_libdir \
  -DDTK_VERSION=%version \
  -DVERSION=%version \
  -DLIB_INSTALL_DIR=%_libdir \
#
cmake --build %_cmake__builddir -j%__nprocs

%install
%cmake_install

%files -n libdtk5-widget
%doc README.md LICENSE
%_libdir/lib%name.so.5*
%dir %_libdir/libdtk-5*/
%dir %_libdir/libdtk-5*/DWidget/
%_libdir/libdtk-5*/DWidget/bin/
%_datadir/libdtk-5*/

%files -n dtk5-widget-devel
%_includedir/libdtk-5*/
%_qt5_archdatadir/mkspecs/modules/*.pri
%_libdir/cmake/DtkWidget/
%_pkgconfigdir/%name.pc
%_libdir/lib%name.so

%files -n dtk5-widget-examples
%dir %_libdir/libdtk-5*/DWidget/
%_libdir/libdtk-5*/DWidget/examples/

%files -n dtk5-widget-doc
%_qt5_datadir/doc/dtkwidget.qch

%changelog
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
