Name: deepin-editor
Version: 5.9.0.12
Release: alt1
Summary: Simple editor for Linux Deepin
License: GPL-3.0+
Group: Editors
Url: https://github.com/linuxdeepin/deepin-editor
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

BuildRequires(pre): rpm-build-ninja desktop-file-utils
BuildRequires: gcc-c++ cmake libfreeimage-devel kf5-kcodecs-devel kf5-syntax-highlighting-devel dtk5-widget-devel libexif-devel libexif-devel libxcbutil-devel libXtst-devel libpolkitqt5-qt5-devel qt5-base-devel qt5-svg-devel qt5-x11extras-devel qt5-linguist deepin-qt-dbus-factory-devel
# Requires: deepin-session-shell deepin-qt5integration

%description
%summary.

%prep
%setup
%__subst 's|lrelease|lrelease-qt5|' translate_generation.sh

%build
%cmake_insource -GNinja -DCMAKE_INSTALL_PREFIX=%_prefix -DCMAKE_BUILD_TYPE=Release
%ninja_build

%install
%ninja_install
%find_lang %name

%check
desktop-file-validate %buildroot%_desktopdir/%name.desktop ||:

%files -f %name.lang
%doc README.md
%doc LICENSE
%_bindir/dedit
%_bindir/%name
%_datadir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg

%changelog
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
