Name: deepin-screen-recorder
Version: 5.8.0.11
Release: alt1
Summary: Default screen recorder application for Deepin
License: GPL-3.0+
Group: Video
Url: https://github.com/linuxdeepin/deepin-screen-recorder
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz
Patch: deepin-screen-recorder_archlinux_qt5.15.patch

BuildRequires: gcc-c++ qt5-base-devel qt5-tools libxcbutil-devel deepin-qt-dbus-factory-devel dtk5-gui-devel dtk5-widget-devel qt5-x11extras-devel qt5-multimedia-devel libprocps-devel

%description
%summary.

%package data
Summary: Data package for %name
Group: Graphical desktop/Other
BuildArch: noarch

%description data
Data files for %name.

%prep
%setup -n %name-%version
%patch -p1
%__subst 's|lupdate|lupdate-qt5|; s|lrelease|lrelease-qt5|' screen_shot_recorder.pro
%__subst '/include <X11.extensions.XTest.h>/a #undef min' src/event_monitor.cpp

%build
%qmake_qt5
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot
%find_lang %name

%files -f %name.lang
%doc LICENSE README.md CHANGELOG.md
%_bindir/%name
%config(noreplace) %_sysconfdir/modprobe.d/%name.conf
%config(noreplace) %_sysconfdir/modules-load.d/%name.conf

%files data
%_desktopdir/%name.desktop
%_datadir/dbus-1/services/com.deepin.ScreenRecorder.service
%_datadir/dbus-1/services/com.deepin.Screenshot.service
%dir %_datadir/dman
%_datadir/dman/%name
%_datadir/%name
%_iconsdir/hicolor/scalable/apps/%name.svg

%changelog
* Wed Aug 05 2020 Leontiy Volodin <lvol@altlinux.org> 5.8.0.11-alt1
- Initial build for ALT Sisyphus (thanks archlinux for the patch).
