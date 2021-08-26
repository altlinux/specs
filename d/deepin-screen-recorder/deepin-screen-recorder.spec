%def_disable clang
%def_disable cmake

Name: deepin-screen-recorder
Version: 5.10.2
Release: alt1
Summary: Default screen recorder application for Deepin
License: GPL-3.0+
Group: Video
Url: https://github.com/linuxdeepin/deepin-screen-recorder
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

Provides: %name-data = %version
Obsoletes: %name-data < %version

%if_enabled clang
BuildRequires(pre): clang12.0-devel
%else
BuildRequires(pre): gcc-c++
%endif
%if_enabled cmake
BuildRequires(pre): cmake rpm-build-ninja
%endif
BuildRequires(pre): rpm-build-kf5
BuildRequires: qt5-base-devel
BuildRequires: qt5-tools-devel
BuildRequires: libxcbutil-devel
BuildRequires: deepin-qt-dbus-factory-devel
BuildRequires: deepin-dock-devel
BuildRequires: dtk5-gui-devel
BuildRequires: dtk5-widget-devel
BuildRequires: gsettings-qt-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: qt5-svg-devel
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
sed -i 's|/usr/lib/|%_libdir/|' src/dde-dock-plugins/recordtime/recordtime.pro
sed -i 's|/etc/due-shell|/etc/dde-shell|' src/src.pro
# X11 header's weirdness with GCC 10
sed -i '/#include <X11.extensions.XTest.h>/a #undef min' src/event_monitor.cpp
sed -i '/#include <iostream>/d;1i #include <iostream>' src/screen_shot_event.cpp
sed -i '/#include <X11.extensions.shape.h>/a #undef None' src/utils.cpp

%build
export PATH=%_qt5_bindir:$PATH
%if_enabled cmake
%cmake \
	-GNinja \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
#
%cmake_build
%else
%qmake_qt5 \
    CONFIG+=nostrip \
%if_enabled clang
    QMAKE_STRIP= -spec linux-clang \
%endif
#
%make_build
%endif

%install
%if_enabled cmake
%cmake_install
%else
%makeinstall INSTALL_ROOT=%buildroot
%endif
%find_lang %name

%files -f %name.lang
%doc LICENSE README.md CHANGELOG.md
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/%name/
%dir %_libdir/dde-dock/
%dir %_libdir/dde-dock/plugins/
%_libdir/dde-dock/plugins/libdeepin-screen-recorder-plugin.so
%_iconsdir/hicolor/scalable/apps/%name.svg
%_iconsdir/hicolor/scalable/apps/deepin-screenshot.svg
%_datadir/dbus-1/services/com.deepin.ScreenRecorder.service
%_datadir/dbus-1/services/com.deepin.Screenshot.service
%dir %_sysconfdir/dde-shell/
%dir %_sysconfdir/dde-shell/json/
%_sysconfdir/dde-shell/json/screenRecorder.json
%dir %_datadir/deepin-manual/
%dir %_datadir/deepin-manual/manual-assets/
%dir %_datadir/deepin-manual/manual-assets/application/
%dir %_datadir/deepin-manual/manual-assets/application/%name/
%_datadir/deepin-manual/manual-assets/application/%name/screen-capture/

%changelog
* Fri Aug 20 2021 Leontiy Volodin <lvol@altlinux.org> 5.10.2-alt1
- New version (5.10.2).

* Wed Jul 14 2021 Leontiy Volodin <lvol@altlinux.org> 5.9.10-alt1
- New version (5.9.10).

* Tue May 18 2021 Leontiy Volodin <lvol@altlinux.org> 5.9.6-alt1
- New version (5.9.6) with rpmgs script.

* Mon Apr 26 2021 Leontiy Volodin <lvol@altlinux.org> 5.9.3-alt1
- New version (5.9.3) with rpmgs script.

* Thu Apr 15 2021 Leontiy Volodin <lvol@altlinux.org> 5.8.1-alt1
- New version (5.8.1).

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
