%def_disable clang

Name: deepin-draw
Version: 6.5.41
Release: alt1
Epoch: 1

Summary: A lightweight drawing tool for Linux Deepin

License: GPL-3.0-or-later and BSD-3-Clause
# deepin-draw-plugins/: BSD-3-Clause
# src/qtsingleapplication/: BSD-3-Clause
Group: Graphics
Url: https://github.com/linuxdeepin/deepin-draw
VCS: https://github.com/linuxdeepin/deepin-draw

Packager: Leontiy Volodin <lvol@altlinux.org>

# Source-url: https://github.com/linuxdeepin/deepin-draw/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar
Patch: %name-%version-%release.patch

%if_enabled clang
BuildRequires: clang-devel lld-devel
%else
BuildRequires: gcc-c++
%endif
BuildRequires(pre): rpm-build-ninja util-linux rpm-macros-dqt6
BuildRequires: cmake libfreeimage-devel dtk6-common-devel libdtk6widget-devel libexif-devel libxcbutil-devel dqt6-base-devel dqt6-svg-devel dqt6-tools dqt6-multimedia-devel dqt6-tools-devel
BuildRequires: libdqt6-test libdqt6-concurrent libwayland-client-devel vulkan-headers libcups-devel
# Requires: deepin-session-shell deepin-dqt6integration
Requires: icon-theme-deepin

%description
A lightweight drawing tool for Linux Deepin.

%prep
%setup
%patch -p1

%build
%if_enabled clang
export CC=clang
export CXX=clang++
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%else
export CC=gcc
export CXX=g++
%endif
%DQ6build \
  -DVERSION=%version \
  -DLIB_INSTALL_DIR=%_libdir \
#

%install
%DQ6install
%find_lang --with-qt %name

%files -f %name.lang
%doc README.md LICENSE.txt
%_bindir/%name
%_desktopdir/%name.desktop
%dir %_iconsdir/deepin/
%dir %_iconsdir/deepin/apps/
%dir %_iconsdir/deepin/apps/scalable/
%_iconsdir/deepin/apps/scalable/%name.svg
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/mime/packages/%name.xml
%_datadir/dbus-1/services/com.deepin.Draw.service
%dir %_datadir/%name/
%dir %_datadir/%name/translations/
%_datadir/%name/translations/%name.qm
%dir %_datadir/deepin-manual/
%dir %_datadir/deepin-manual/manual-assets/
%dir %_datadir/deepin-manual/manual-assets/application/
%dir %_datadir/deepin-manual/manual-assets/application/%name/
%_datadir/deepin-manual/manual-assets/application/%name/draw/

%changelog
* Fri Jun 26 2026 Leontiy Volodin <lvol@altlinux.org> 1:6.5.41-alt1
- New version 6.5.41.

* Wed Apr 01 2026 Leontiy Volodin <lvol@altlinux.org> 1:6.5.38-alt1
- New version 6.5.38.

* Mon Mar 02 2026 Leontiy Volodin <lvol@altlinux.org> 1:6.5.36-alt1
- New version 6.5.36.
- Updated license tag.
- Switched to dqt6.

* Tue Feb 18 2025 Leontiy Volodin <lvol@altlinux.org> 7.0.5-alt1
- New version 7.0.5.
- Added vcs tag.

* Tue Sep 10 2024 Leontiy Volodin <lvol@altlinux.org> 7.0.2-alt1
- New version 7.0.2.

* Wed May 29 2024 Leontiy Volodin <lvol@altlinux.org> 7.0.1-alt1
- New version 7.0.1.
- Cleanup spec.
- Packed new subpackages.
- Built via separate qt5 instead system (ALT #48138).

* Fri Oct 20 2023 Ivan A. Melnikov <iv@altlinux.org> 5.10.6-alt1.1
- NMU: remove (pre) from conditional BR's, they don't
  work like that and are not needed (fixes build on loongarch64).

* Wed Feb 09 2022 Leontiy Volodin <lvol@altlinux.org> 5.10.6-alt1
- New version (5.10.6).

* Thu Aug 19 2021 Leontiy Volodin <lvol@altlinux.org> 5.9.7-alt1
- New version (5.9.7).

* Mon Jun 07 2021 Leontiy Volodin <lvol@altlinux.org> 5.9.4-alt1
- New version (5.9.4).
- Built with gcc-c++ and cmake instead clang and qmake.

* Fri Oct 16 2020 Leontiy Volodin <lvol@altlinux.org> 5.8.0.20-alt1
- New version (5.8.0.20) with rpmgs script.

* Thu Jul 30 2020 Leontiy Volodin <lvol@altlinux.org> 5.8.0.19-alt1
- Initial build for ALT Sisyphus (thanks fedora and archlinux for this spec).
