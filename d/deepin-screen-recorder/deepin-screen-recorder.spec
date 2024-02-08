%def_without clang
# Not actual CMakeLists.txt
%def_without cmake

Name: deepin-screen-recorder
Version: 5.12.17
Release: alt1

Summary: Default screen recorder application for Deepin

License: GPL-3.0-or-later
# 3rdparty/googletest: BSD-3-Clause and Apache-2.0
Group: Video
Url: https://github.com/linuxdeepin/deepin-screen-recorder

Source: %url/archive/%version/%name-%version.tar.gz
Patch: %name-%version-%release.patch

Provides: %name-data = %version
Obsoletes: %name-data < %version

BuildRequires(pre): rpm-macros-qt5
# Automatically added by buildreq on Fri Dec 15 2023
# optimized out: gcc-c++ glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 gstreamer1.0-devel libX11-devel libXcursor-devel libXext-devel libXfixes-devel libXi-devel libXtst-devel libavcodec-devel libavformat-devel libavutil-devel libdouble-conversion3 libdtkcore-devel libdtkgui-devel libglvnd-devel libgpg-error libgsettings-qt libgst-plugins1.0 libp11-kit libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-multimedia libqt5-network libqt5-printsupport libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libstartup-notification libstdc++-devel libswscale-devel libudev-devel libxcb-devel pkg-config python3 python3-base python3-dev python3-module-setuptools qt5-base-devel qt5-declarative-devel qt5-tools sh5 tbb-devel xorg-proto-devel
BuildRequires: deepin-dock-devel deepin-qt-dbus-factory-devel dwayland-devel gst-plugins1.0-devel kf5-kconfig-devel kf5-ki18n-devel kf5-kwayland-devel kf5-kwindowsystem-devel libdtkwidget-devel libffmpegthumbnailer-devel libimagevisualresult-devel libopencv-devel libportaudio2-devel libswresample-devel libusb-devel libv4l-devel libxcbutil-devel qt5-multimedia-devel qt5-svg-devel qt5-tools-devel qt5-x11extras-devel

# /etc/uos-version detection
BuildRequires: deepin-desktop-base

%if_with clang
BuildRequires: clang-devel lld-devel
%else
BuildRequires: gcc-c++
%endif

%if_with cmake
BuildRequires: cmake rpm-build-ninja
%endif

Requires: libqt5-core = %_qt5_version

%description
%summary.

%prep
%setup -n %name-%version
%patch -p1

%build
export PATH=%_qt5_bindir:$PATH
%if_enabled clang
%define optflags_lto -flto=thin
%endif
%if_enabled cmake
    %if_enabled clang
    export CC=clang
    export CXX=clang++
    export LDFLAGS="-fuse-ld=lld $LDFLAGS"
    %endif
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DVERSION=%version \
    -DLIB_INSTALL_DIR=%_libdir \
    -DDEFINES+="VERSION=%version" \
    %nil
cmake --build "%_cmake__builddir" -j%__nprocs
%else
%qmake_qt5 \
    CONFIG+=nostrip \
    VERSION=%version \
    DEFINES+="VERSION=%version" \
    LIB_INSTALL_DIR=%_libdir \
    LIBDIR=%_libdir \
    unix:LIBS+=" -L/%_lib -ludev" \
    %if_enabled clang
        QMAKE_STRIP= -spec linux-clang \
    %endif
    %nil
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
%_bindir/deepin-pin-screenshots
%_desktopdir/%name.desktop
%_datadir/%name/
%dir %_libdir/dde-dock/
%dir %_libdir/dde-dock/plugins/
%_libdir/dde-dock/plugins/libdeepin-screen-recorder-plugin.so
%_libdir/dde-dock/plugins/libshot-start-plugin.so
%_iconsdir/hicolor/scalable/apps/%name.svg
%_iconsdir/hicolor/scalable/apps/deepin-screenshot.svg
%_datadir/dbus-1/services/com.deepin.ScreenRecorder.service
%_datadir/dbus-1/services/com.deepin.Screenshot.service
%_datadir/dbus-1/services/com.deepin.PinScreenShots.service
%_datadir/glib-2.0/schemas/com.deepin.dde.dock.module.shot-start-plugin.gschema.xml
%dir %_datadir/deepin-manual/
%dir %_datadir/deepin-manual/manual-assets/
%dir %_datadir/deepin-manual/manual-assets/application/
%dir %_datadir/deepin-manual/manual-assets/application/%name/
%_datadir/deepin-manual/manual-assets/application/%name/screen-capture/
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/org.deepin.screen-recorder/
%_datadir/dsg/configs/org.deepin.screen-recorder/org.deepin.screen-recorder.record.json

%changelog
* Thu Feb 08 2024 Leontiy Volodin <lvol@altlinux.org> 5.12.17-alt1
- New version 5.12.17.

* Fri Jan 19 2024 Leontiy Volodin <lvol@altlinux.org> 5.12.15-alt2
- Requires: libqt5-core = %%_qt5_version.

* Tue Jan 16 2024 Leontiy Volodin <lvol@altlinux.org> 5.12.15-alt1
- New version 5.12.15.

* Wed Dec 21 2023 Leontiy Volodin <lvol@altlinux.org> 5.12.13.0.6.bc51-alt1
- New version 5.12.13-6-gbc51a0c.

* Tue Dec 05 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 5.10.22-alt2
- NMU: fixed FTBFS (build without libprocps-devel, no longer available).
  Thanks to iv@.

* Thu May 19 2022 Leontiy Volodin <lvol@altlinux.org> 5.10.22-alt1
- New version (5.10.22).

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
