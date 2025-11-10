%def_without clang

%define repo dde-session-shell

Name: deepin-session-shell
Version: 5.6.12.0.316.e888
Release: alt2
Epoch: 1

Summary: Deepin desktop-environment - Session shell module

License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-session-shell
VCS: https://github.com/linuxdeepin/dde-session-shell

# Source-url: https://github.com/linuxdeepin/dde-session-shell/archive/%version/%repo-%version.tar.gz
Source: %repo-%version.tar
Patch: %name-%version-%release.patch

# Requires: chkpwd-pam

BuildRequires(pre): deepin-gettext-tools
BuildRequires: cmake dqt6-svg-devel dqt6-tools-devel dtk6-common-devel libXcursor-devel libXrandr-devel libXtst-devel libcups-devel libdtk6widget-devel libgtest-devel libpam-devel libxcbutil-icccm-devel dde-lightdm-devel
%if_with clang
BuildRequires: clang-devel lld-devel
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

%package -n lightdm-deepin-greeter-enable
Summary: Enable config for own lightdm theme
Group: System/Configuration/Other
BuildArch: noarch
Requires: deepin-session-shell

%description -n lightdm-deepin-greeter-enable
The package provides the configuration file
for enabling the deepin theme for lightdm.

%prep
%setup -n %repo-%version
%autopatch -p1
# sed -i '/kwin_wayland/s|/usr/bin/||' \
#     files/wayland/kwin_wayland_helper-wayland \
#     files/wayland/launch-kwin-wayland
sed -i 's|/usr/lib/x86_64-linux-gnu/qt5|%_libdir/dqt6|' \
    files/wayland/lightdm-deepin-greeter-wayland \
    files/wayland/launch-kwin-wayland
sed -i '/QT_QPA_PLATFORM_PLUGIN_PATH/s|/usr/plugins/platforms|%_libdir/dqt6/plugins/platforms|' \
    files/wayland/lightdm-deepin-greeter-wayland
sed -i 's|/usr/lib/|%_libdir/|g' \
    src/global_util/plugin_manager/modules_loader.cpp
sed -i '/execute_process/s|/usr/lib/qt${QT_VERSION_MAJOR}/bin|%_dqt6_bindir|' \
    CMakeLists.txt
sed -i '/LIBRARY DESTINATION/s|lib/|${LIB_DESTINATION}/|' \
    $(find ./plugins -name CMakeLists.txt)

%build
%if_with clang
export CC="clang"
export CXX="clang++"
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif
%DQ6build \
  -DCMAKE_INSTALL_SYSCONFDIR=%_sysconfdir \
  -DLIB_DESTINATION=%_lib \
  -DCMAKE_EXE_LINKER_FLAGS='-L%_dqt6_libdir -L%_libdir' \
#

%install
%DQ6install

%files
%dir %_sysconfdir/deepin/
%dir %_sysconfdir/deepin/greeters.d/
%config(noreplace) %_sysconfdir/deepin/greeters.d/00-xrandr
%config(noreplace) %_sysconfdir/deepin/greeters.d/lightdm-deepin-greeter
%config(noreplace) %_sysconfdir/deepin/greeters.d/10-cursor-theme
%dir %_sysconfdir/lightdm/deepin/
%config(noreplace) %_sysconfdir/lightdm/deepin/qt-theme.ini
%config(noreplace) %_sysconfdir/pam.d/dde-lock
%config(noreplace) %_sysconfdir/pam.d/deepin-lightdm-autologin
%_bindir/deepin-greeter
%_bindir/lightdm-deepin-greeter
%_bindir/dde-lock
%_datadir/%repo/
%_desktopdir/dde-lock.desktop
%_datadir/dbus-1/services/*.service
%_datadir/xgreeters/lightdm-deepin-greeter.desktop
%dir %_datadir/deepin-authentication/
%dir %_datadir/deepin-authentication/privileges/
%_datadir/deepin-authentication/privileges/lightdm-deepin-greeter.conf
%_libdir/security/pam_inhibit_autologin.so
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/org.deepin.dde.lightdm-deepin-greeter/
%_datadir/dsg/configs/org.deepin.dde.lightdm-deepin-greeter/org.deepin.dde.lightdm-deepin-greeter.json
%dir %_datadir/dsg/configs/org.deepin.dde.lock/
%_datadir/dsg/configs/org.deepin.dde.lock/org.deepin.dde.lock.json
%dir %_datadir/dsg/configs/org.deepin.dde.session-shell/
%_datadir/dsg/configs/org.deepin.dde.session-shell/org.deepin.dde.session-shell.json
%dir %_datadir/deepin-debug-config/
%dir %_datadir/deepin-debug-config/deepin-debug-config.d/
%_datadir/deepin-debug-config/deepin-debug-config.d/org.deepin.dde.session-shell.json
%dir %_datadir/deepin-log-viewer/
%dir %_datadir/deepin-log-viewer/deepin-log.conf.d/
%_datadir/deepin-log-viewer/deepin-log.conf.d/org.deepin.dde.session-shell.json

%files -n lightdm-deepin-greeter-enable
%_datadir/lightdm/lightdm.conf.d/50-deepin.conf

%files devel
%dir %_includedir/dde-session-shell/
%_includedir/dde-session-shell/*.h
%dir %_libdir/cmake/DdeSessionShell/
%_libdir/cmake/DdeSessionShell/DdeSessionShellConfig.cmake

%changelog
* Mon Nov 10 2025 Leontiy Volodin <lvol@altlinux.org> 1:5.6.12.0.316.e888-alt2
- Restored the option to use the system lightdm
  (moved the config to lightdm-deepin-greeter-enable).

* Tue Oct 28 2025 Leontiy Volodin <lvol@altlinux.org> 1:5.6.12.0.316.e888-alt1
- New version 5.6.12-316-ge88849d6.

* Thu Oct 09 2025 Leontiy Volodin <lvol@altlinux.org> 1:5.6.4.0.433.86a0-alt2
- Built with another liblightdm-qt6 (use Qt for DDE only).

* Wed Aug 06 2025 Leontiy Volodin <lvol@altlinux.org> 1:5.6.4.0.433.86a0-alt1
- New version 5.6.4-433-g86a050b4.

* Wed Jun 25 2025 Leontiy Volodin <lvol@altlinux.org> 1:5.6.4.0.420.59e7-alt1
- New version 5.6.4-420-g59e74747 (all new tags are gone).
- Added VCS tag.
- Switched to Qt6.

* Thu May 23 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.18-alt2
- Built via separate qt5 instead system (ALT #48138).

* Mon Apr 08 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.18-alt1
- New version 6.0.18.

* Thu Feb 08 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.17-alt1
- New version 6.0.17.

* Fri Dec 29 2023 Leontiy Volodin <lvol@altlinux.org> 6.0.14-alt2
- Updated fixes for session unlock.

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
