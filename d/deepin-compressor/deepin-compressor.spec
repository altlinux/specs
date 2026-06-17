%def_disable clang

Name: deepin-compressor
Version: 6.5.30
Release: alt2
Epoch: 1

Summary: Archive Manager for Deepin Desktop Environment

License: GPL-3.0-or-later and GPL-2.0-or-later and LGPL-2.0-or-later and BSD-2-Clause
Group: Archiving/Compression
Url: https://github.com/linuxdeepin/deepin-compressor
VCS: https://github.com/linuxdeepin/deepin-compressor

Provides: %name-devel = %version
Obsoletes: %name-devel < %version

# Source-url: https://github.com/linuxdeepin/deepin-compressor/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar
Patch: %name-%version-%release.patch

Requires: 7-zip deepin-qt6integration
# Requires: icon-theme-hicolor

%if_enabled clang
BuildRequires(pre): clang-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires(pre): desktop-file-utils rpm-macros-dqt6
# Automatically added by buildreq on Thu Apr 24 2025
# optimized out: cmake cmake-modules dqt6-base-common dqt6-base-devel dqt6-tools gcc-c++ glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libdouble-conversion3 libdqt6-concurrent libdqt6-core libdqt6-core5compat libdqt6-dbus libdqt6-gui libdqt6-network libdqt6-printsupport libdqt6-waylandclient libdqt6-widgets libdqt6-xml libdtk6core-devel libdtk6gui-devel libdtk6log-devel libglvnd-devel libgpg-error libp11-kit libsasl2-3 libssl-devel libstartup-notification libstdc++-devel libwayland-client libwayland-cursor libxkbcommon-devel ninja-build pkg-config python3 python3-base sh5 vulkan-headers zlib-devel
BuildRequires: dqt6-5compat-devel dqt6-svg-devel dqt6-tools-devel dtk6-common-devel kf6-karchive-devel kf6-kcodecs-devel libarchive-devel libcups-devel libdtk6widget-devel libgio-devel libminizip-devel libmount-devel libzip-devel
BuildRequires: vulkan-headers libdqt6-concurrent libwayland-client-devel

%description
%summary.

%prep
%setup
%autopatch -p1
sed -i 's|/usr/lib|%_libdir|' \
    src/source/common/pluginmanager.cpp \
    tests/UnitTest/CMakeLists.txt
sed -i 's|include <zip.h>|include <libzip/zip.h>|' \
    3rdparty/libzipplugin/libzipplugin.h

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"
%endif
%DQ6build \
    -DVERSION=%version \
    -DCMAKE_INSTALL_LIBDIR=%_libdir \
    -DLIB_INSTALL_DIR=%_libdir \
    -DCOMPRESSOR_PLUGIN_PATH=%_libdir/%name/plugins \
#

%install
%DQ6install
%find_lang --with-qt %name

%check
desktop-file-validate %buildroot%_desktopdir/%name.desktop

%files -f %name.lang
%doc README.md
%doc LICENSE
%doc debian/changelog
%_bindir/%name
%_desktopdir/%name.desktop
%dir %_datadir/%name/
%dir %_datadir/%name/translations/
%_datadir/%name/translations/%name.qm
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/mime/packages/%name.xml
%dir %_datadir/applications/context-menus/
%_datadir/applications/context-menus/*.conf
%dir %_libdir/%name/
%dir %_libdir/%name/plugins/
%_libdir/%name/plugins/*.so
%ifarch x86_64 aarch64
# pzip is only available on x86_64 and aarch64 -- see deepin-compressor/src/CMakeLists.txt
%dir %_libexecdir/%name/
%_libexecdir/%name/pzip
%_libexecdir/%name/punzip
%endif
%_datadir/dbus-1/interfaces/com.deepin.Compressor.xml
%_datadir/dbus-1/services/com.deepin.Compressor.service
%dir %_datadir/deepin-manual/
%dir %_datadir/deepin-manual/manual-assets/
%dir %_datadir/deepin-manual/manual-assets/application/
%dir %_datadir/deepin-manual/manual-assets/application/%name/
%_datadir/deepin-manual/manual-assets/application/%name/archive-manager/
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/org.deepin.compressor/
%_datadir/dsg/configs/org.deepin.compressor/org.deepin.compressor.method.json

%changelog
* Wed Jun 17 2026 Leontiy Volodin <lvol@altlinux.org> 1:6.5.30-alt2
- Fixed segmentation error when adding a file (ALT #59465).

* Fri Jun 05 2026 Leontiy Volodin <lvol@altlinux.org> 1:6.5.30-alt1
- New version 6.5.30.

* Thu Jun 04 2026 Leontiy Volodin <lvol@altlinux.org> 1:6.5.29-alt1
- New version 6.5.29.
- Updated requires (p7zip is obsoleted).

* Wed Apr 01 2026 Leontiy Volodin <lvol@altlinux.org> 1:6.5.23-alt1
- New version 6.5.23.

* Mon Mar 02 2026 Ivan A. Melnikov <iv@altlinux.org> 1:6.5.22-alt2
- NMU: fix FTBFS on loongarch64 and riscv64.

* Mon Mar 02 2026 Leontiy Volodin <lvol@altlinux.org> 1:6.5.22-alt1
- New version 6.5.22.
- Built on dqt6 again (by upstream).

* Mon Jan 26 2026 Leontiy Volodin <lvol@altlinux.org> 1:6.5.21-alt1
- New version 6.5.21.
- Built on dqt5 again (by upstream).

* Wed Dec 10 2025 Leontiy Volodin <lvol@altlinux.org> 1:6.5.17-alt1
- New version 6.5.17.

* Mon Jul 21 2025 Leontiy Volodin <lvol@altlinux.org> 1:6.5.12-alt1
- New version 6.5.12.

* Thu Apr 24 2025 Leontiy Volodin <lvol@altlinux.org> 1:6.5.4-alt1
- New version 6.5.4.
- Switched to dqt6.

* Thu Dec 05 2024 Leontiy Volodin <lvol@altlinux.org> 1:6.0.4-alt1
- New version 6.0.4.
- Added vcs tag.

* Thu May 30 2024 Leontiy Volodin <lvol@altlinux.org> 1:6.0.3-alt1
- New version 6.0.3.
- Built via separate qt5 instead system (ALT #48138).

* Fri Apr 05 2024 Leontiy Volodin <lvol@altlinux.org> 1:6.0.1-alt1
- New version 6.0.1.

* Thu Mar 07 2024 Leontiy Volodin <lvol@altlinux.org> 1:5.12.25-alt1
- New version 5.12.25.

* Sat Dec 30 2023 Leontiy Volodin <lvol@altlinux.org> 1:5.12.21-alt1
- New version 5.12.21.
- Fixed build with dtk 5.6.20 (thanks archlinux for the patch).
- Cleanup BRs.
- Updated license tag.

* Fri Jan 20 2023 Leontiy Volodin <lvol@altlinux.org> 6.0.0-alt1
- New version (6.0.0).

* Wed Nov 02 2022 Leontiy Volodin <lvol@altlinux.org> 5.12.10-alt1
- New version (5.12.10).

* Tue Apr 19 2022 Leontiy Volodin <lvol@altlinux.org> 5.12.5-alt1
- New version (5.12.5).
- Checkout from euler to dev/1050 branch.

* Thu Jul 08 2021 Leontiy Volodin <lvol@altlinux.org> 5.10.5-alt2
- Fixed build with libgmock.so.1.11.0.

* Wed Jun 16 2021 Leontiy Volodin <lvol@altlinux.org> 5.10.5-alt1
- New version (5.10.5) with rpmgs script.
- NMU: spec: adapted to new cmake macros.

* Mon Apr 26 2021 Leontiy Volodin <lvol@altlinux.org> 5.10.0.15-alt1
- New version (5.10.0.15) with rpmgs script.

* Sat Dec 26 2020 Leontiy Volodin <lvol@altlinux.org> 5.10.0.7-alt2
- Built with gcc10.

* Wed Dec 23 2020 Leontiy Volodin <lvol@altlinux.org> 5.10.0.7-alt1
- New version (5.10.0.7) with rpmgs script.

* Fri Oct 09 2020 Leontiy Volodin <lvol@altlinux.org> 5.9.0.2-alt1
- New version (5.9.0.2) with rpmgs script.

* Wed Sep 02 2020 Leontiy Volodin <lvol@altlinux.org> 5.8.0.15-alt1
- Initial build for ALT Sisyphus.
