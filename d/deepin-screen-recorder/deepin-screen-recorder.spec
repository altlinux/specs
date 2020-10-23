Name: deepin-screen-recorder
Version: 5.8.0.57
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

BuildRequires(pre): rpm-build-kf5
BuildRequires: gcc-c++ qt5-base-devel qt5-tools libxcbutil-devel deepin-qt-dbus-factory-devel dtk5-gui-devel dtk5-widget-devel qt5-x11extras-devel qt5-multimedia-devel libprocps-devel libavcodec-devel libavformat-devel libavfilter-devel libswresample-devel libswscale-devel libavdevice-devel libgbm-devel libepoxy-devel
BuildRequires: kf5-kwindowsystem-devel kf5-kwayland-devel kf5-ki18n-devel kf5-kconfig-devel

%description
%summary.

%prep
%setup -n %name-%version
%patch -p2
sed -i 's|lupdate|lupdate-qt5|; s|lrelease|lrelease-qt5|' screen_shot_recorder.pro

%build
%qmake_qt5 \
    CONFIG+=nostrip \
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
