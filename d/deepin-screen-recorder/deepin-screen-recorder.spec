%def_disable clang

Name: deepin-screen-recorder
Version: 5.8.0.61
Release: alt1
Summary: Default screen recorder application for Deepin
License: GPL-3.0+
Group: Video
Url: https://github.com/linuxdeepin/deepin-screen-recorder
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz
Patch: deepin-screen-recorder_5.8.0.57_alt_qt5.15.patch

Provides: %name-data = %version
Obsoletes: %name-data < %version

%if_enabled clang
BuildRequires(pre): clang11.0-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires(pre): rpm-build-kf5
BuildRequires: qt5-base-devel
BuildRequires: qt5-tools
BuildRequires: libxcbutil-devel
BuildRequires: deepin-qt-dbus-factory-devel
BuildRequires: dtk5-gui-devel
BuildRequires: dtk5-widget-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: libprocps-devel
BuildRequires: libavcodec-devel
BuildRequires: libavformat-devel
BuildRequires: libavfilter-devel
BuildRequires: libswresample-devel
BuildRequires: libswscale-devel
BuildRequires: libavdevice-devel
BuildRequires: libgbm-devel
BuildRequires: libepoxy-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: kf5-kwayland-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kconfig-devel

%description
%summary.

%prep
%setup -n %name-%version
%patch -p2
sed -i 's|lupdate|lupdate-qt5|; s|lrelease|lrelease-qt5|' screen_shot_recorder.pro
# X11 header's weirdness with GCC 10
sed -i '/include <X11.extensions.XTest.h>/a #undef min' src/event_monitor.cpp
sed -i '/#include <iostream>/d;1i #include <iostream>' src/screen_shot_event.cpp

%build
%qmake_qt5 \
    CONFIG+=nostrip \
%if_enabled clang
    QMAKE_STRIP= -spec linux-clang \
%endif
    QT.KWindowSystem.libs=%_K5link \
    QT.KWaylandClient.libs=%_K5link \
    QT.KI18n.libs=%_K5link \
    QT.KConfigCore.libs=%_K5link
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot
%find_lang %name

%files -f %name.lang
%doc LICENSE README.md CHANGELOG.md
%_bindir/%name
%_desktopdir/%name.desktop
%dir %_datadir/dman
%_datadir/dman/%name/
%_datadir/%name/
%_iconsdir/hicolor/scalable/apps/%name.svg
%_iconsdir/hicolor/scalable/apps/deepin-screenshot.svg
%config(noreplace) %_sysconfdir/modprobe.d/%name.conf
%config(noreplace) %_sysconfdir/modules-load.d/%name.conf
%_datadir/dbus-1/services/com.deepin.ScreenRecorder.service
%_datadir/dbus-1/services/com.deepin.Screenshot.service

%changelog
* Thu Dec 31 2020 Leontiy Volodin <lvol@altlinux.org> 5.8.0.61-alt1
- New version (5.8.0.61) with rpmgs script.

* Thu Dec 10 2020 Leontiy Volodin <lvol@altlinux.org> 5.8.0.60-alt1
- New version (5.8.0.60) with rpmgs script.
- Fixed build with gcc10 (thanks archlinux).

* Fri Oct 23 2020 Leontiy Volodin <lvol@altlinux.org> 5.8.0.57-alt1
- New version (5.8.0.57) with rpmgs script.
- Rewritten patch for qt5.15 compatibility.

* Fri Oct 16 2020 Leontiy Volodin <lvol@altlinux.org> 5.8.0.17-alt1
- New version (5.8.0.17) with rpmgs script.
- Enabled debuginfo.
- Added new BR.
- Obsoleted data package.

* Wed Aug 05 2020 Leontiy Volodin <lvol@altlinux.org> 5.8.0.11-alt1
- Initial build for ALT Sisyphus (thanks archlinux for the patch).
