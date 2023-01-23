%def_disable clang

%define repo dde-session-shell

Name: deepin-session-shell
Version: 5.5.68
Release: alt3
Summary: Deepin desktop-environment - Session shell module
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-session-shell
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz
Source1: pam-deepin-screenlocker
Patch1: deepin-session-shell-5.5.68-alt-lightdm-for-lockscreen.patch
Patch2: deepin-session-shell-5.4.13-hide-sleep-and-hibernate.patch
Patch3: deepin-session-shell-5.5.68-alt-use-previous-encryption.patch

%if_enabled clang
BuildRequires(pre): clang-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires(pre): rpm-build-ninja rpm-build-kf5 rpm-build-xdg
BuildRequires: cmake
BuildRequires: qt5-tools
BuildRequires: qt5-base-devel
BuildRequires: deepin-qt-dbus-factory-devel
BuildRequires: libpam0-devel
BuildRequires: dtk5-widget-devel
BuildRequires: dtk5-common
BuildRequires: qt5-x11extras-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: qt5-svg-devel
BuildRequires: libxcbutil-icccm-devel
BuildRequires: gsettings-qt-devel
BuildRequires: lightdm-devel
BuildRequires: libgmock-devel
BuildRequires: kf5-kwayland-devel
# deepin-gettext-tools dtk5-widget-devel deepin-qt-dbus-factory-devel gsettings-qt-devel libgtk+2-devel lightdm-devel libsystemd-devel qt5-base-devel qt5-svg-devel qt5-x11extras-devel qt5-multimedia-devel libxcbutil-icccm-devel libXcursor-devel libXtst-devel libpam0-devel qt5-linguist

%description
%summary.

%package devel
Summary: %summary
Group: Development/Other

%description devel
%summary.

%prep
%setup -n %repo-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
sed -i 's|/usr/bin|%_K5bin|' \
    files/wayland/kwin_wayland_helper-wayland \
    files/wayland/deepin-greeter-wayland
sed -i 's|/usr/lib/x86_64-linux-gnu/|%_libdir/|' \
    files/wayland/lightdm-deepin-greeter-wayland \
    files/wayland/deepin-greeter-wayland
sed -i 's|/usr/lib/|%_libdir/|' \
    src/global_util/modules_loader.cpp
sed -i 's|lib/|%_lib/|' \
    plugins/one-key-login/CMakeLists.txt
# Fix undefined symbols.
sed -i '/link_libraries(/a Dtk::Core' \
    plugins/one-key-login/CMakeLists.txt
sed -i '/link_libraries(/a Dtk::Widget' \
    plugins/one-key-login/CMakeLists.txt
#sed -i 's|/usr/share/backgrounds/default_background.jpg|/usr/share/design-current/backgrounds/default.png|' \
#    src/widgets/fullscreenbackground.cpp \
#    src/session-widgets/userinfo.h
#sed -i 's|/usr/share/backgrounds/deepin/desktop.jpg|/usr/share/design-current/backgrounds/default.png|' \
#    src/session-widgets/lockcontent.cpp \
#    src/dde-shutdown/view/contentwidget.cpp
#sed -i 's|/usr/share/wallpapers/deepin/desktop.jpg|/usr/share/design-current/backgrounds/default.png|' \
#    src/widgets/fullscreenbackground.cpp
#sed -i 's|theme/background/default_background.jpg|theme/background.png|' \
#    src/dde-lock/logintheme.qrc \
#    src/lightdm-deepin-greeter/logintheme.qrc
# We don't use common-auth in ALT
# sed -i 's/password-auth/system-auth/; s/common-auth/system-auth/' src/libdde-auth/deepinauthframework.cpp
#sed -i 's|m_model->setCurrentModeState(SessionBaseModel::ModeStatus::PasswordMode)|system("dde-swithtogreeter")|' \
#  src/dde-lock/lockworker.cpp

%build
%add_optflags -I%_includedir/dtk5/DCore -I%_includedir/dtk5/DWidget
%if_enabled clang
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
    -DKDE_KSCREENSAVER_PAM_SERVICE="deepin-screenlocker" \
#
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install
chmod +x %buildroot%_bindir/deepin-greeter

# Install deepin pam configuration files
install -d -m 0755 %buildroot%_sysconfdir/pam.d/
install -m 0644 %SOURCE1 %buildroot%_sysconfdir/pam.d/deepin-screenlocker

%files
%config(noreplace) %_sysconfdir/deepin/greeters.d/00-xrandr
%config(noreplace) %_sysconfdir/deepin/greeters.d/lightdm-deepin-greeter
%config(noreplace) %_sysconfdir/deepin/greeters.d/10-cursor-theme
%config(noreplace) %_sysconfdir/pam.d/deepin-screenlocker
%_xdgconfigdir/autostart/dde-lock.desktop
%_sysconfdir/lightdm/deepin/qt-theme.ini
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
%_libdir/dde-session-shell/modules/libone-key-login.so
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/org.deepin.dde.lightdm-deepin-greeter/
%_datadir/dsg/configs/org.deepin.dde.lightdm-deepin-greeter/org.deepin.dde.lightdm-deepin-greeter.json
%dir %_datadir/dsg/configs/org.deepin.dde.lock/
%_datadir/dsg/configs/org.deepin.dde.lock/org.deepin.dde.lock.json

%files devel
%dir %_includedir/dde-session-shell/
%_includedir/dde-session-shell/*.h
%dir %_libdir/cmake/DdeSessionShell/
%_libdir/cmake/DdeSessionShell/DdeSessionShellConfig.cmake

%changelog
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
