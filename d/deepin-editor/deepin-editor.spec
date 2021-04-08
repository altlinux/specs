Name: deepin-editor
Version: 5.9.0.49
Release: alt1
Summary: Simple editor for Linux Deepin
License: GPL-3.0+
Group: Editors
Url: https://github.com/linuxdeepin/deepin-editor
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

BuildRequires(pre): rpm-build-ninja desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: libfreeimage-devel
BuildRequires: kf5-kcodecs-devel
BuildRequires: kf5-syntax-highlighting-devel
BuildRequires: dtk5-widget-devel
BuildRequires: libexif-devel
BuildRequires: libexif-devel
BuildRequires: libxcbutil-devel
BuildRequires: libXtst-devel
BuildRequires: libpolkitqt5-qt5-devel
BuildRequires: qt5-base-devel
BuildRequires: qt5-tools
BuildRequires: qt5-svg-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: qt5-linguist
BuildRequires: deepin-qt-dbus-factory-devel
BuildRequires: libgtest-devel
BuildRequires: libgmock-devel
BuildRequires: dtk5-common
# use system libuchardet.a
BuildRequires: libuchardet-devel-static
# Requires: deepin-session-shell deepin-qt5integration

%description
%summary.

%prep
%setup
sed -i 's|lrelease|lrelease-qt5|; s|lupdate|lupdate-qt5|' translate_generation.sh
# use system libuchardet.a
sed -i 's|${CMAKE_CURRENT_SOURCE_DIR}/../3rdparty/lib/lib/libuchardet.a|%_libdir/libuchardet.a|' \
	src/CMakeLists.txt \
	tests/CMakeLists.txt

%build
%cmake_insource \
    -GNinja \
    -DCMAKE_INSTALL_PREFIX=%_prefix \
    -DCMAKE_BUILD_TYPE=Release \
    -DAPP_VERSION=%version \
    -DVERSION=%version \
    -DCMAKE_INSTALL_LIBDIR=%_libdir
%ninja_build

%install
%ninja_install
%find_lang %name

%check
desktop-file-validate %buildroot%_desktopdir/%name.desktop ||:

%files -f %name.lang
%doc README.md LICENSE
%_bindir/%name
%_datadir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/deepin-manual/manual-assets/application/%name/editor/*/*

%changelog
* Thu Apr 08 2021 Leontiy Volodin <lvol@altlinux.org> 5.9.0.49-alt1
- New version (5.9.0.49) with rpmgs script.

* Fri Mar 12 2021 Leontiy Volodin <lvol@altlinux.org> 5.9.0.32-alt1
- New version (5.9.0.32) with rpmgs script.

* Wed Dec 30 2020 Leontiy Volodin <lvol@altlinux.org> 5.9.0.16-alt1
- New version (5.9.0.16) with rpmgs script.

* Tue Dec 29 2020 Leontiy Volodin <lvol@altlinux.org> 5.9.0.12-alt1
- New version (5.9.0.12) with rpmgs script.

* Tue Nov 17 2020 Leontiy Volodin <lvol@altlinux.org> 5.9.0.11-alt1
- New version (5.9.0.11) with rpmgs script.

* Fri Oct 23 2020 Leontiy Volodin <lvol@altlinux.org> 5.9.0.6-alt1
- New version (5.9.0.6) with rpmgs script.

* Thu Oct 22 2020 Leontiy Volodin <lvol@altlinux.org> 5.6.37-alt1
- New version (5.6.37) with rpmgs script.

* Fri Oct 16 2020 Leontiy Volodin <lvol@altlinux.org> 5.6.36-alt1
- New version (5.6.36) with rpmgs script.
- Added new BR.

* Tue Aug 18 2020 Leontiy Volodin <lvol@altlinux.org> 5.6.28-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
