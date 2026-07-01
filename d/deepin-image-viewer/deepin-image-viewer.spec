%define sover 1

%def_disable clang

Name: deepin-image-viewer
Version: 6.0.45
Release: alt1

Summary: Image viewer for Deepin

License: GPL-3.0-or-later
Group: Graphics
Url: https://github.com/linuxdeepin/deepin-image-viewer
Vcs: https://github.com/linuxdeepin/deepin-image-viewer

# Source-url: https://github.com/linuxdeepin/deepin-image-viewer/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar
Patch: %name-%version-%release.patch

ExcludeArch: armh

BuildRequires(pre): rpm-macros-dqt6
%if_enabled clang
BuildRequires(pre): clang-devel
%else
BuildRequires(pre): gcc-c++
%endif
# Automatically added by buildreq on Wed Mar 26 2025
# optimized out: cmake cmake-modules dqt6-base-devel dqt6-tools gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libclang-cpp19 libdeepin-ocr-plugin-manager1 libdouble-conversion3 libdqt6-concurrent libdqt6-core libdqt6-dbus libdqt6-gui libdqt6-network libdqt6-opengl libdqt6-printsupport libdqt6-qml libdqt6-qmlmeta libdqt6-qmlmodels libdqt6-qmlworkerscript libdqt6-quick libdqt6-svg libdqt6-waylandclient libdqt6-widgets libdqt6-xml libdtk6core-devel libdtk6gui-devel libdtk6log-devel libglvnd-devel libgpg-error libjson-c5 liblcms2-devel libp11-kit libsasl2-3 libssl-devel libstartup-notification libstdc++-devel libwayland-client libwayland-cursor libxkbcommon-devel llvm19.1-libs ninja-build pkg-config python3 python3-base sh5 vulkan-headers
BuildRequires: dqt6-declarative-devel dqt6-svg-devel dqt6-tools-devel dtk6-common-devel libcups-devel libdeepin-ocr-plugin-manager-devel libdtk6declarative-devel libdtk6widget-devel libraw-devel libncnn-devel deepin-libopencv_world-devel libdqt6-qmlcompiler libwayland-client-devel
BuildRequires: vulkan-headers libdqt6-concurrent

# provide the plugin for dtk
%add_findprov_lib_path %_dqt6_plugindir/imageformats

Requires: libxraw%sover = %EVR
Requires: libdqt6-qml = %_dqt6_version

%description
%summary.

%package -n libxraw%sover
Summary: libxraw plugin for %name
Group: Development/KDE and QT

%description -n libxraw%sover
This package provides libxraw plugin for %name.

%package -n libxraw-devel
Summary: Development package for libxraw
Group: Development/KDE and QT
Provides: %name-devel

%description -n libxraw-devel
This package provides the development files for libxraw.

%prep
%setup
%patch -p1
sed -i 's|/qt${QT_VERSION_MAJOR}/plugins|/dqt${QT_VERSION_MAJOR}/plugins|' \
  qimage-plugins/libraw/CMakeLists.txt
# deepin's opencv_mobile does not have .pc file
sed -i 's| opencv_mobile||' \
  src/CMakeLists.txt

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"
%endif
export CPLUS_INCLUDE_PATH=%_includedir/deepin/opencv4:%_includedir/opencv4:$CPLUS_INCLUDE_PATH
export LIBS=" -L%_libdir/deepin -lopencv_world":$LIBS
%DQ6build \
  -DVERSION=%version \
  -DCMAKE_INSTALL_LIBDIR=%_libdir \
#

%install
%DQ6install
%find_lang --with-qt %name

%files -f %name.lang
%doc LICENSE.txt README.md debian/changelog
%_bindir/%name
%_desktopdir/%name.desktop
%dir %_datadir/%name/
%dir %_datadir/%name/translations/
%_datadir/%name/translations/deepin-image-viewer.qm
%_datadir/applications/context-menus/deepin-print-pictures.conf
%dir %_datadir/deepin-manual/
%dir %_datadir/deepin-manual/manual-assets/
%dir %_datadir/deepin-manual/manual-assets/application/
%dir %_datadir/deepin-manual/manual-assets/application/%name/
%_datadir/deepin-manual/manual-assets/application/%name/image-viewer/
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/dbus-1/services/com.deepin.imageViewer.service

%files -n libxraw%sover
%_dqt6_plugindir/imageformats/libxraw.so.%{sover}*

%files -n libxraw-devel
%_dqt6_plugindir/imageformats/libxraw.so

%changelog
* Wed Jul 01 2026 Leontiy Volodin <lvol@altlinux.org> 6.0.45-alt1
- New version 6.0.45.

* Thu Apr 30 2026 Leontiy Volodin <lvol@altlinux.org> 6.0.40-alt1
- New version 6.0.40.

* Tue Apr 07 2026 Leontiy Volodin <lvol@altlinux.org> 6.0.39-alt1
- New version 6.0.39.

* Fri Feb 27 2026 Leontiy Volodin <lvol@altlinux.org> 6.0.38-alt1
- New version 6.0.38.

* Mon Jan 26 2026 Leontiy Volodin <lvol@altlinux.org> 6.0.37-alt1
- New version 6.0.37.
- Fixed build on dtk 6.7.31.

* Tue Jan 20 2026 Leontiy Volodin <lvol@altlinux.org> 6.0.36-alt1
- New version 6.0.36.

* Thu Oct 30 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.32-alt1
- New version 6.0.32.

* Fri Aug 22 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.31-alt1
- New version 6.0.31.
- Packaged libxraw separately.

* Tue Apr 22 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.19-alt1
- New version 6.0.19.

* Wed Mar 26 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.15-alt1
- New version 6.0.15.
- Added vcs tag.
- Switched to dqt6.

* Wed May 29 2024 Leontiy Volodin <lvol@altlinux.org> 5.9.18-alt1
- New version 5.9.18.
- Built via separate qt5 instead system (ALT #48138).

* Tue Jan 09 2024 Leontiy Volodin <lvol@altlinux.org> 5.9.9-alt3
- Fixed build with APIv23.

* Wed Sep 06 2023 Leontiy Volodin <lvol@altlinux.org> 5.9.9-alt2
- Fixed build with libraw 0.21 (ALT #47425).

* Tue Jan 17 2023 Leontiy Volodin <lvol@altlinux.org> 5.9.9-alt1
- New version (5.9.9).

* Thu Jul 21 2022 Leontiy Volodin <lvol@altlinux.org> 5.9.2-alt1
- New version (5.9.2).

* Thu May 12 2022 Leontiy Volodin <lvol@altlinux.org> 5.8.13-alt1
- New version (5.8.13).
- Not complied for armh architecture.

* Thu Aug 19 2021 Leontiy Volodin <lvol@altlinux.org> 5.8.2-alt1
- New version (5.8.2).

* Wed Jul 14 2021 Leontiy Volodin <lvol@altlinux.org> 5.7.11-alt1
- New version (5.7.11).

* Tue May 18 2021 Leontiy Volodin <lvol@altlinux.org> 5.7.8-alt1
- New version (5.7.8) with rpmgs script.

* Thu Apr 15 2021 Leontiy Volodin <lvol@altlinux.org> 5.7.4-alt1
- New version (5.7.4) with rpmgs script.

* Mon Mar 15 2021 Leontiy Volodin <lvol@altlinux.org> 5.6.3.73-alt2.gitb4da182
- Updated from commit b4da182b92425880e208c127d5712aef840200a4.
- Built with cmake and ninja instead qmake and make.

* Mon Jan 25 2021 Leontiy Volodin <lvol@altlinux.org> 5.6.3.73-alt1
- New version (5.6.3.73) with rpmgs script.

* Fri Dec 11 2020 Leontiy Volodin <lvol@altlinux.org> 5.6.3.69-alt1
- Initial build for ALT Sisyphus.

