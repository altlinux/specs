Name: deepin-topbar
Version: 0.7.0
Release: alt2
Summary: Topbar for Deepin desktop environment
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/justforlxz/deepin-topbar
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

BuildRequires(pre): rpm-build-ninja desktop-file-utils
BuildRequires: cmake gcc-c++ dtk5-core-devel dtk5-common dtk5-widget-devel deepin-qt-dbus-factory-devel deepin-network-utils-devel gsettings-qt-devel libdbusmenu-qt5-devel libpolkitqt5-qt5-devel libxcb-devel libxcbutil-icccm-devel libxcbutil-image-devel libxcbutil-devel libX11-devel libXext-devel libXtst-devel qt5-base-devel qt5-svg-devel qt5-x11extras-devel qt5-linguist libprocps-devel
Requires: icon-theme-hicolor

%description
%summary.

%prep
%setup
%__subst 's|lrelease|lrelease-qt5|' translate_generation.sh

%build
%cmake_insource -GNinja
%ninja_build

%install
%ninja_install

%check
desktop-file-validate %buildroot%_desktopdir/%name.desktop

%files
%doc README.md
%doc LICENSE
%_bindir/%name
%_datadir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/*.svg
%_datadir/dbus-1/services/*.service
%_datadir/polkit-1/actions/*.service

%changelog
* Fri Apr 09 2021 Leontiy Volodin <lvol@altlinux.org> 0.7.0-alt2
- Fixed build with dtk 5.4.13.

* Fri Jul 31 2020 Leontiy Volodin <lvol@altlinux.org> 0.7.0-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).

