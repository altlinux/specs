%def_without clang

%define repo dde-session-ui

Name: deepin-session-ui
Version: 6.0.18
Release: alt1

Summary: Deepin desktop-environment - Session UI module

License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-session-ui

Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz

BuildRequires(pre): rpm-build-ninja rpm-macros-dqt5
# Automatically added by buildreq on Wed Oct 25 2023
# optimized out: bash5 bashrc cmake-modules gcc-c++ glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libX11-devel libXext-devel libcrypt-devel libdouble-conversion3 libdtkcore-devel libdtkgui-devel libglvnd-devel libgmock-devel libgpg-error libgsettings-qt libp11-kit libdqt5-concurrent libdqt5-core libdqt5-dbus libdqt5-gui libdqt5-network libdqt5-printsupport libdqt5-sql libdqt5-svg libdqt5-test libdqt5-widgets libdqt5-x11extras libdqt5-xml libsasl2-3 libssl-devel libstartup-notification libstdc++-devel libxcb-devel libxcbutil-icccm pkg-config python3 python3-base dqt5-base-devel sh5 xorg-proto-devel
BuildRequires: cmake dtk6-common-devel dtkcore gsettings-qt-devel libdeepin-pw-check-devel libdtkwidget-devel libgio-devel libgtest-devel libsystemd-devel libxcbutil-icccm-devel dqt5-svg-devel dqt5-tools dqt5-x11extras-devel
BuildRequires: deepin-dock-devel
%if_with clang
BuildRequires: clang-devel
%else
BuildRequires: gcc-c++
%endif

%description
This project include those sub-project:
- dde-switchtogreeter: The tools to switch the user to login in.
- dde-license-dialog.
- dde-pixmix.
- dde-wm-chooser.
- dmemory-warning-dialog.

%prep
%setup -n %repo-%version
#sed -i 's|default_background.jpg|deepin/desktop.jpg|' \
#    widgets/fullscreenbackground.cpp \
#    lightdm-deepin-greeter/logintheme.qrc \
#    dde-lock/logintheme.qrc
sed -i 's|lib/dde-dock/|%_lib/dde-dock/|' CMakeLists.txt

%build
export PATH=%_dqt5_bindir:$PATH
export CMAKE_PREFIX_PATH=%_dqt5_libdir/cmake:$CMAKE_PREFIX_PATH
export PKG_CONFIG_PATH=%_dqt5_libdir/pkgconfig:$PKG_CONFIG_PATH
export CPLUS_INCLUDE_PATH=%_includedir/qt5:$CPLUS_INCLUDE_PATH
%if_with clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"
%endif
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=OFF \
    -DCMAKE_INSTALL_RPATH=%_dqt5_libdir \
%ifarch aarch64 armh ppc64le
    -DSHUTDOWN_NO_QUIT=YES \
    -DLOCK_NO_QUIT=YES \
    -DDISABLE_DEMO_VIDEO=YES \
    -DDISABLE_TEXT_SHADOW=YES \
    -DDISABLE_ANIMATIONS=YES \
    -DUSE_CURSOR_LOADING_ANI=YES \
%endif
#
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install
%find_lang --with-qt %repo

%files -f %repo.lang
%doc README.md
%doc LICENSE
%_bindir/dde-license-dialog
%_bindir/dde-pixmix
%_bindir/dde-switchtogreeter
%_bindir/dde-wm-chooser
%_bindir/dde-hints-dialog
%dir %_libexecdir/deepin-daemon/
%_libexecdir/deepin-daemon/dde-bluetooth-dialog
%_libexecdir/deepin-daemon/dde-lowpower
%_libexecdir/deepin-daemon/dde-osd
%_libexecdir/deepin-daemon/dde-suspend-dialog
%_libexecdir/deepin-daemon/dde-warning-dialog
%_libexecdir/deepin-daemon/dde-touchscreen-dialog
%_libexecdir/deepin-daemon/dde-welcome
%_libexecdir/deepin-daemon/dnetwork-secret-dialog
%dir %_libexecdir/dde-control-center/
%_libexecdir/dde-control-center/reset-password-dialog
%_iconsdir/hicolor/scalable/devices/computer.svg
%_datadir/dbus-1/services/*.service
# outside %%find_lang
%dir %_datadir/%repo/
%dir %_datadir/%repo/translations/
%_datadir/%repo/translations/dde-session-ui_es_419.qm
%_datadir/%repo/translations/dde-session-ui_ky@Arab.qm

%changelog
* Thu May 23 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.18-alt1
- New version 6.0.18.
- Built via separate qt5 instead system (ALT #48138).

* Wed Mar 27 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.16-alt1
- New version 6.0.16.

* Tue Jan 16 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.14-alt1
- New version 6.0.14.

* Wed Oct 25 2023 Leontiy Volodin <lvol@altlinux.org> 6.0.10-alt1
- New version 6.0.10.
- Cleanup BRs.

* Wed Jan 11 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.2-alt1
- New version.

* Fri Dec 16 2022 Leontiy Volodin <lvol@altlinux.org> 5.6.1-alt1
- New version.

* Mon Oct 31 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.37-alt1
- New version.
- Upstream:
  + fix: wayland the touch screen collapses.
  + fix: After repairing the special effects under the arm structure,
  switching the capital and tabloid caused the white box display
  in the upper left corner of the screen.
  + fix: The silent state of the prompt does not match the control center.
  + feat: Increase backlight mode switching.
  + fix: The lock screen interface does not show notice.
  + fix: Solve the problem of system notification collapse.
  + fix: Notify the window to get the focus when locking the screen,
  and interrupt the current focus input.
  + fix: wayland lock screen does not show OSD.
  + chore: adapt license and copyright.
  + fix: Modify the start method of the dde-osd program.
  + fix: Problems not shown by osd in the case of repair part.
  + fix: Repair the Bluetooth connection with PIN code problem.
  + fix: Switch user anomalies.
  + fix: Abnormal interaction between low-volume interface and lock screen.
  + fix: Repair the A user's activation or no-touch board, and enter
  the B user's login page, which will automatically pop the osd bullet
  window problem.
  + fix: Correct and participate in the correction of the number
  of Bluetooth bullet window parameters.
  + fix: It is necessary to readjust the interface size when displaying
  different types of OSD.
  + fix: The version prompts incorrect information when logging
  on the desktop in the community version.
  + fix: memory leak.
  + fix: After repairing standby sleep, osd cannot show the problem.
  + chore: Update translation.
  + fix: Repair notification center mouse click or roller will cause
  hidden problems.
  + fix: The window attributes need to be set according to X11 or wayland.

* Fri Jun 10 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.23-alt1
- New version.
- Upstream:
  + refactor: qmake to cmake.
  + fix: Notify the window of abnormalities when the low power is activated.
  + fix: No notice of news will be ejected when the Display interface service
  is invalid.
  + fix: dde-session-ui ASAN problem handling.
  + fix: More than two apps alternately send message notices, which will cause
  the message notices to be repeated.
  + fix: Recommended indentation ratio error in repair calculation.
  + fix: Repair The problem of opening the flight mode OSD in a dark mode
  does not show the aircraft icon.
  + fix: The insertion of the repair notice prompts the lack of blank on both
  sides.
  + fix: Set the initial height of Bubble to 1.
  + fix: Repair the notice above the screen does not support the problem
  of clicking on the blank area to achieve default operation.
  + fix(display): Repair cannot distinguish two touch screens of the same model.
  + chore: Remove the translation warning.
  + fix: Repair the problem of OSD display error in different situations
  of left and right screen resolution.
  + fix: The back-end display module adds TouchscreensV2 attributes
  and AssociateTouchByUUID interface.
  + fix(dnetwork-secret-dialog): Modify the untranslated password window
  Password connection problem.
  + fix: The problem of pulling out the USB flash drive and stuck
  in the mission column after awakening.
  + fix: Safety reinforcement of compilation options.
  + fix: Notification center window did not follow the task column.
  + fix: When calculating the width of the task column, you need to consider
  the screen indentation ratio.
  + fix: Increase the processing of the meta key flag sign under wayland.
  + fix: filter out the judgment of meta status under wayland.
  + fix: Repair the problem of the synchronous change of the silent icon
  on the dde-osd panel.

* Fri Feb 11 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.6-alt1
- New version (5.5.6).

* Fri Aug 20 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.29-alt1
- New version (5.4.29).

* Wed Jul 14 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.20-alt1
- New version (5.4.20).

* Tue May 18 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.7-alt1
- New version (5.4.7) with rpmgs script.

* Fri Apr 09 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.6-alt1
- New version (5.4.6) with rpmgs script.

* Thu Mar 25 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.5-alt1
- New version (5.4.5) with rpmgs script.

* Tue Jan 26 2021 Leontiy Volodin <lvol@altlinux.org> 5.3.35-alt1
- New version (5.3.35) with rpmgs script.

* Tue Jan 12 2021 Leontiy Volodin <lvol@altlinux.org> 5.3.0.30-alt1
- New version (5.3.0.30) with rpmgs script.

* Fri Dec 04 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.26-alt1
- New version (5.3.0.26) with rpmgs script.

* Wed Nov 18 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.22-alt1
- New version (5.3.0.22) with rpmgs script.

* Thu Nov 05 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.18-alt1
- New version (5.3.0.18) with rpmgs script.

* Wed Oct 07 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.17-alt1
- New version (5.3.0.17) with rpmgs script.

* Mon Aug 17 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.2-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
