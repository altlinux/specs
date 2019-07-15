Name: deepin-menu
Version: 5.0.1
Release: alt1
Summary: Deepin menu service
License: GPL-3.0-only
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-menu
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

BuildRequires(pre): desktop-file-utils
BuildRequires: dtk5-widget-devel deepin-qt-dbus-factory-devel qt5-base-devel qt5-multimedia-devel qt5-x11extras-devel

%description
Deepin menu service for building beautiful menus.

%prep
%setup

# Modify lib path to reflect the platform
%__subst 's|/usr/bin|%_libexecdir|' data/com.deepin.menu.service \
    deepin-menu.desktop deepin-menu.pro

%build
%qmake_qt5 DEFINES+=QT_NO_DEBUG_OUTPUT
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

%files
%doc README.md
%doc LICENSE
%_libexecdir/%name
%_datadir/dbus-1/services/com.deepin.menu.service

%changelog
* Tue Jul 21 2020 Leontiy Volodin <lvol@altlinux.org> 5.0.1-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
