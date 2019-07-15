Name: deepin-compressor
Version: 5.8.0.15
Release: alt1
Summary: Archive Manager for Deepin Desktop Environment
License: GPL-3.0+ and (GPL-2.0+ and LGPL-2.1+ and MPL-1.1) and BSD-2-Clause and Apache-2.0
Group: Archiving/Compression
Url: https://github.com/linuxdeepin/deepin-compressor
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz
Patch: deepin-compressor_5.8.0.15_alt_cmake.patch

BuildRequires(pre): desktop-file-utils rpm-build-kf5 rpm-build-ninja
BuildRequires: gcc-c++ cmake qt5-base-devel dtk5-widget-devel kf5-kcodecs-devel kf5-karchive-devel qt5-multimedia-devel qt5-x11extras-devel libarchive-devel libsecret-devel libpoppler-cpp-devel udisks2-qt5-devel disomaster-devel libzip-devel libminizip-devel qt5-tools-devel deepin-gettext-tools qt5-svg-devel gsettings-qt-devel
# Requires: icon-theme-hicolor

%description
%summary.

%package devel
Summary: Development files for %name
Group: Development/Other

%description devel
This package provides the development files for %name.

%package devel-static
Summary: Static files for %name
Group: Development/Other

%description devel-static
This package provides the static files for %name.

%prep
%setup
%patch -p2
sed -i 's|lrelease|lrelease-qt5|' deepin-compressor/translate_generation.sh deepin-compressor/deepin-compressor.pro
sed -i '/include <QPainter>/a #include <QPainterPath>' deepin-compressor/source/src/openwithdialog/openwithdialog.cpp deepin-compressor/source/src/logviewheaderview.cpp
sed -i 's|#include <zip.h>|#include <libzip/zip.h>|' 3rdparty/libzipplugin/libzipplugin.h
# cmake fixes with patch
sed -i 's|lib/|%_lib/|' CMakeLists.txt
# remove unbuilded translation
rm -rf translations/deepin-compressor*.ts

%build
%cmake -GNinja
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
%dir %_datadir/deepin/
%dir %_datadir/deepin/dde-file-manager/
%dir %_datadir/deepin/dde-file-manager/oem-menuextensions/
%_datadir/deepin/dde-file-manager/oem-menuextensions/*.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/mime/packages/%name.xml

%files devel
%dir %_libdir/%name/
%dir %_libdir/%name/plugins/
%_libdir/%name/plugins/*.so

%files devel-static
%dir %_libdir/%name/
%dir %_libdir/%name/plugins/
%_libdir/%name/plugins/*.a

%changelog
* Wed Sep 02 2020 Leontiy Volodin <lvol@altlinux.org> 5.8.0.15-alt1
- Initial build for ALT Sisyphus.
