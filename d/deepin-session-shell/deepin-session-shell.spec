%def_without clang

%define repo dde-session-shell

Name: deepin-session-shell
Version: 6.0.14
Release: alt1

Summary: Deepin desktop-environment - Session shell module

License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-session-shell

Source: %url/archive/%version/%repo-%version.tar.gz
Patch: %name-%version-%release.patch

Requires: pam0_tcb

BuildRequires(pre): rpm-build-ninja rpm-build-kf5 rpm-build-xdg deepin-gettext-tools
# Automatically added by buildreq on Wed Oct 25 2023
# optimized out: alt-os-release bash5 bashrc cmake-modules gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libX11-devel libXcursor-devel libXext-devel libXfixes-devel libXi-devel libXrandr-devel libXrender-devel libXtst-devel libcap-ng libdouble-conversion3 libdtkcore-devel libdtkgui-devel libglvnd-devel libgpg-error libgsettings-qt liblightdm-gobject liblightdm-qt5 libp11-kit libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libssl-devel libstartup-notification libstdc++-devel libxcb-devel libxcbutil-icccm pkg-config python3 python3-base qt5-base-common qt5-base-devel sh5 xorg-proto-devel
BuildRequires: cmake dtkcore gsettings-qt-devel libdeepin-pw-check-devel libdtkwidget-devel libgtest-devel libpam-devel libxcbutil-icccm-devel lightdm-devel qt5-svg-devel qt5-tools qt5-x11extras-devel
%if_with clang
BuildRequires: clang-devel
%else
BuildRequires: gcc-c++
%endif

%description
%summary.

%package devel
Summary: %summary
Group: Development/Other

%description devel
%summary.

%prep
%setup -n %repo-%version
%patch -p1
sed -i '/kwin_wayland/s|/usr/bin/||' \
    files/wayland/kwin_wayland_helper-wayland \
    files/wayland/deepin-greeter-wayland
sed -i 's|/usr/lib/x86_64-linux-gnu/|%_libdir/|' \
    files/wayland/lightdm-deepin-greeter-wayland \
    files/wayland/deepin-greeter-wayland
sed -i '/QT_QPA_PLATFORM_PLUGIN_PATH/s|/usr/plugins/platforms|%_libdir/qt5/plugins/platforms|' \
    files/wayland/lightdm-deepin-greeter-wayland
sed -i 's|/usr/lib/|%_libdir/|' \
    src/global_util/modules_loader.cpp
sed -i 's|lib/|%_lib/|' \
    modules/*/CMakeLists.txt
# We don't use common-auth in ALT
# sed -i 's|password-auth|pam_tcb|' src/libdde-auth/deepinauthframework.cpp
# sed -i -e '/account/d; s|common-auth|system-auth|;' files/pam.d/dde-lock

%build
%add_optflags -I%_includedir/dtk5/DCore -I%_includedir/dtk5/DWidget
%if_with clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"
%endif
export PATH=%_qt5_bindir:$PATH
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_INSTALL_SYSCONFDIR=%_sysconfdir \
#
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install
chmod +x %buildroot%_bindir/deepin-greeter

%files
%config(noreplace) %_sysconfdir/deepin/greeters.d/00-xrandr
%config(noreplace) %_sysconfdir/deepin/greeters.d/lightdm-deepin-greeter
%config(noreplace) %_sysconfdir/deepin/greeters.d/10-cursor-theme
%config(noreplace) %_sysconfdir/pam.d/dde-lock
%_bindir/deepin-greeter
%_bindir/lightdm-deepin-greeter
%_bindir/dde-lock
%_datadir/%repo/
%_desktopdir/dde-lock.desktop
%_datadir/dbus-1/services/*.service
%_datadir/xgreeters/lightdm-deepin-greeter.desktop
%_datadir/glib-2.0/schemas/com.deepin.dde.session-shell.gschema.xml
%dir %_datadir/deepin-authentication/
%dir %_datadir/deepin-authentication/privileges/
%_datadir/deepin-authentication/privileges/lightdm-deepin-greeter.conf
%dir %_libdir/dde-session-shell/
%dir %_libdir/dde-session-shell/modules/
%_libdir/dde-session-shell/modules/libvirtualkeyboard.so
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/org.deepin.dde.lightdm-deepin-greeter/
%_datadir/dsg/configs/org.deepin.dde.lightdm-deepin-greeter/org.deepin.dde.lightdm-deepin-greeter.json
%dir %_datadir/dsg/configs/org.deepin.dde.lock/
%_datadir/dsg/configs/org.deepin.dde.lock/org.deepin.dde.lock.json
%_sysconfdir/lightdm/deepin/qt-theme.ini

%files devel
%dir %_includedir/dde-session-shell/
%_includedir/dde-session-shell/*.h
%dir %_libdir/cmake/DdeSessionShell/
%_libdir/cmake/DdeSessionShell/DdeSessionShellConfig.cmake

%changelog
* Tue Dec 12 2023 Leontiy Volodin <lvol@altlinux.org> 6.0.14-alt1
- New version 6.0.14.
- Cleanup spec, patches and BRs.
- Fixed session unlock.

* Mon Jan 23 2023 Leontiy Volodin <lvol@altlinux.org> 5.5.68-alt3
- Fixed build with dtkwidget 5.6.4.
- Updated deepin-screenlocker.

* Thu Jan 19 2023 Leontiy Volodin <lvol@altlinux.org> 5.5.68-alt2
- Fixed build with dtkcore 5.6.4.

* Thu Aug 25 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.68-alt1
- New version (5.5.68).

* Wed Jul 14 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.42-alt1
- New version (5.4.42).

* Thu Jul 08 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.13-alt2
- Fixed build with libgmock.so.1.11.0.

* Mon Jun 28 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.13-alt1
- New version (5.4.13).

* Thu Jun 17 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.5-alt4
- Fixed lockscreen.

* Fri Apr 09 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.5-alt3
- Fixed build with dtk 5.4.13.

* Thu Mar 11 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.5-alt2
- Fixed backgrounds.

* Tue Mar 09 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.5-alt1
- New version (5.4.5) with rpmgs script.

* Tue Jan 12 2021 Leontiy Volodin <lvol@altlinux.org> 5.3.0.45-alt1
- New version (5.3.0.45) with rpmgs script.

* Fri Dec 25 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.41-alt2
- Fixed background.
- Fixed qdbus generations.

* Fri Dec 04 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.41-alt1
- New version (5.3.0.41) with rpmgs script.

* Wed Nov 18 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.24-alt1
- New version (5.3.0.24) with rpmgs script.

* Wed Oct 07 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.22-alt1
- New version (5.3.0.22) with rpmgs script.

* Mon Aug 17 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.5-alt1
- Initial build for ALT Sisyphus.
