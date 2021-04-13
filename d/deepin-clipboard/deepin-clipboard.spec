%define repo dde-clipboard
%def_disable clang

Name: deepin-clipboard
Version: 5.3.15
Release: alt1
Summary: Clipboard for DDE
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-clipboard
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz

%if_enabled clang
BuildRequires(pre): clang11.0-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires(pre): rpm-build-ninja
BuildRequires: qt5-base-devel
BuildRequires: qt5-tools
BuildRequires: dtk5-widget-devel
BuildRequires: libgio-qt-devel
BuildRequires: deepin-qt-dbus-factory-devel
BuildRequires: libgtest-devel
Requires: lcov

%description
%summary.

%prep
%setup -n %repo-%version
sed -i 's|lrelease|lrelease-qt5|' \
    translate_generation.sh
#sed -i 's|/usr/bin/qdbus|/usr/bin/qdbus-qt5|' \
#	dde-clipboard/com.deepin.dde.Clipboard.service

%build
%qmake_qt5 \
%if_enabled clang
	QMAKE_STRIP= -spec linux-clang \
%endif
	CONFIG+=nostrip \
	PREFIX=%_prefix \
#
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot
%find_lang %name

%files -f %name.lang
%doc LICENSE
%_bindir/%repo
%_bindir/%{repo}loader
%_datadir/%repo/
%_desktopdir/%repo.desktop
%_sysconfdir/xdg/autostart/%repo.desktop
%_datadir/dbus-1/services/com.deepin.dde.Clipboard.service

%changelog
* Tue Apr 13 2021 Leontiy Volodin <lvol@altlinux.org> 5.3.15-alt1
- New version (5.3.15) with rpmgs script.

* Fri Mar 19 2021 Leontiy Volodin <lvol@altlinux.org> 5.3.11-alt1
- Initial build for ALT Sisyphus.
