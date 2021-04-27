%def_disable clang

Name: deepin-compressor
Version: 5.10.0.15
Release: alt1
Summary: Archive Manager for Deepin Desktop Environment
License: GPL-3.0+ and (GPL-2.0+ and LGPL-2.1+ and MPL-1.1) and BSD-2-Clause and Apache-2.0
Group: Archiving/Compression
Url: https://github.com/linuxdeepin/deepin-compressor
Packager: Leontiy Volodin <lvol@altlinux.org>

Provides: %name-devel = %version
Obsoletes: %name-devel < %version

Source: %url/archive/%version/%name-%version.tar.gz

%if_enabled clang
BuildRequires(pre): clang11.0-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires(pre): desktop-file-utils rpm-build-kf5 rpm-build-ninja
BuildRequires: cmake
BuildRequires: qt5-base-devel
BuildRequires: dtk5-widget-devel
BuildRequires: kf5-kcodecs-devel
BuildRequires: kf5-karchive-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: libarchive-devel
BuildRequires: libsecret-devel
BuildRequires: libpoppler-cpp-devel
BuildRequires: udisks2-qt5-devel
BuildRequires: disomaster-devel
BuildRequires: libzip-devel
BuildRequires: libminizip-devel
BuildRequires: qt5-tools-devel
BuildRequires: deepin-gettext-tools
BuildRequires: qt5-svg-devel
BuildRequires: gsettings-qt-devel
BuildRequires: libgtest-devel
# Requires: icon-theme-hicolor
# Requires: p7zip

%description
%summary.

%prep
%setup
sed -i 's|/usr/bin/cp|/bin/cp|' \
    tests/FuzzyTest/libfuzzer/CMakeLists.txt
sed -i 's|/usr/lib|%_libdir|' \
    src/source/common/pluginmanager.cpp \
    tests/UnitTest/CMakeLists.txt
sed -i 's|#include <zip.h>|#include <libzip/zip.h>|' \
    3rdparty/libzipplugin/libzipplugin.h
sed -i 's|lib/|%_lib/|' \
    CMakeLists.txt
# remove unbuilded translation
rm -rf translations/deepin-compressor*.ts

# %if_disabled clang
# sed -i 's|int myshowWarningDialog|void myshowWarningDialog|' \
#     tests/UnitTest/deepin-compressor/source/src/uncompresspage_test.cpp
# %endif

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"
%endif
export PATH=%_qt5_bindir:$PATH
%K5cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_LIBDIR=%_libdir \
    -DAPP_VERSION=%version \
    -DVERSION=%version
%ninja_build -C BUILD

%install
%ninja_install -C BUILD

%check
desktop-file-validate %buildroot%_desktopdir/%name.desktop

%files
%doc README.md
%doc LICENSE
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/%name/
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/mime/packages/%name.xml
%dir %_datadir/applications/context-menus/
%_datadir/applications/context-menus/*.conf
%dir %_libdir/%name/
%dir %_libdir/%name/plugins/
%_libdir/%name/plugins/*.so
%dir %_datadir/deepin-manual/
%dir %_datadir/deepin-manual/manual-assets/
%dir %_datadir/deepin-manual/manual-assets/application/
%dir %_datadir/deepin-manual/manual-assets/application/%name/
%_datadir/deepin-manual/manual-assets/application/%name/archive-manager/

%changelog
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
