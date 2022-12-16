%def_disable clang

%define repo dde-session-ui

Name: deepin-session-ui
Version: 5.6.1
Release: alt1
Summary: Deepin desktop-environment - Session UI module
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-session-ui
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz

%if_enabled clang
BuildRequires(pre): clang-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires(pre): rpm-build-ninja
BuildRequires: cmake
BuildRequires: deepin-gettext-tools
BuildRequires: dtk5-common
BuildRequires: dtk5-widget-devel
BuildRequires: deepin-qt-dbus-factory-devel
BuildRequires: gsettings-qt-devel
BuildRequires: libgtk+2-devel
BuildRequires: lightdm-devel
BuildRequires: libsystemd-devel
BuildRequires: qt5-base-devel
BuildRequires: qt5-tools
BuildRequires: qt5-svg-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: libxcbutil-icccm-devel
BuildRequires: libXcursor-devel
BuildRequires: libXtst-devel
BuildRequires: libpam0-devel
BuildRequires: qt5-linguist
BuildRequires: deepin-dock-devel
BuildRequires: libgio-qt-devel
BuildRequires: libgtest-devel

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
export PATH=%_qt5_bindir:$PATH
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"
%endif
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DARCHITECTURE=%_arch \
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

%files
%doc README.md
%doc LICENSE
%_bindir/dde-license-dialog
%_bindir/dde-pixmix
%_bindir/dde-switchtogreeter
%_bindir/dde-wm-chooser
%_bindir/dmemory-warning-dialog
%_bindir/dde-hints-dialog
%dir %_libexecdir/deepin-daemon
%_libexecdir/deepin-daemon/dde-bluetooth-dialog
%_libexecdir/deepin-daemon/dde-lowpower
%_libexecdir/deepin-daemon/dde-osd
%_libexecdir/deepin-daemon/dde-suspend-dialog
%_libexecdir/deepin-daemon/dde-warning-dialog
%_libexecdir/deepin-daemon/dde-touchscreen-dialog
%_libexecdir/deepin-daemon/dde-welcome
%_libexecdir/deepin-daemon/dnetwork-secret-dialog
%_datadir/%repo/
%_desktopdir/dde-osd.desktop
#_iconsdir/hicolor/*/apps/deepin-*
%_iconsdir/hicolor/scalable/devices/computer.svg
%_datadir/dbus-1/services/*.service
%_datadir/glib-2.0/schemas/com.deepin.dde.dock.module.notifications.gschema.xml
%dir %_libdir/dde-dock
%dir %_libdir/dde-dock/plugins
%_libdir/dde-dock/plugins/libnotifications.so

%changelog
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
