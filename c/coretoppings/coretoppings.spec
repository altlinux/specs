%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%global __find_debuginfo_files %nil

%define _libdir %_prefix/lib
%define _libexecdir %_prefix/libexec

Name: coretoppings
Version: 5.0.0
Release: alt1

Summary: Additional features, plugins, widgets etc for C Suite
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://gitlab.com/cubocore/coreapps/coretoppings

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(cprime-core)
BuildRequires: pkgconfig(csys)

# TODO - find the exact root of the problems shown below
#            error: file /usr/lib64/libQt6Core.so.6()(64bit): No such file or directory
#            lib.req: WARNING: /usr/lib64/libQt6Core.so.6()(64bit) is not yet set-versioned
#            error: file /usr/lib64/libQt6DBus.so.6()(64bit): No such file or directory
#            lib.req: WARNING: /usr/lib64/libQt6DBus.so.6()(64bit) is not yet set-versioned
#            error: file /usr/lib64/libQt6Gui.so.6()(64bit): No such file or directory
#            lib.req: WARNING: /usr/lib64/libQt6Gui.so.6()(64bit) is not yet set-versioned
#            error: file /usr/lib64/libQt6Widgets.so.6()(64bit): No such file or directory
#            lib.req: WARNING: /usr/lib64/libQt6Widgets.so.6()(64bit) is not yet set-versioned
#            error: file /usr/lib64/libc.so.6()(64bit): No such file or directory
#            lib.req: WARNING: /usr/lib64/libc.so.6()(64bit) is not yet set-versioned
#            error: file /usr/lib64/libgcc_s.so.1()(64bit): No such file or directory
#            lib.req: WARNING: /usr/lib64/libgcc_s.so.1()(64bit) is not yet set-versioned
#            error: file /usr/lib64/libstdc++.so.6()(64bit): No such file or directory
#            lib.req: WARNING: /usr/lib64/libstdc++.so.6()(64bit) is not yet set-versioned
#        and then remove the below HACK-y line
AutoReq: nolib

Requires: libqt6-core
Requires: libqt6-dbus
Requires: libqt6-gui
Requires: libqt6-network
Requires: libqt6-widgets
Requires: libqt6-svgwidgets

# TODO - find the exact root of the problem like
#            phdr[5]: unknown object file note type 1951465473 with owner name 'qt-project!' at offset 144
#            section [19] '.note.qt.metadata': unknown object file note type 1951465473 with owner name 'qt-project!' at offset 80
#            verify-elf: WARNING: ./usr/lib/coreapps/shareit/libimageconv.so: eu-elflint failed
#        and then remove the below HACK-y line
%set_verify_elf_method none

Requires: corefm

Requires: ffmpeg
Requires: qv4l2
Requires: wf-recorder
Requires: playerctl
Requires: xrandr
Requires: iio-sensor-proxy
Requires: inotify-tools
Requires: bluez
Requires: rfkill
Requires: notify-send

%filter_from_requires /connman/d

Requires: NetworkManager-daemon
Requires: redshift
Requires: xinput
Requires: polkit
Requires: wmctrl
Requires: ffplay

%filter_from_requires /nvidia-settings/d

%description
%summary.

%prep
%setup
%patch -p1
sed -i "s|Utility;|Utility;FileTools;|" shareit/shareit.desktop

%build
%cmake
%cmake_build

%install
%cmake_install
chmod a+x %buildroot%_datadir/coreapps/scripts/*.sh

%files
%doc LICENSE README.md
%_bindir/shareIT
%_libdir/coreapps/plugins/libbacklight.so
%_libdir/coreapps/plugins/libleave.so
%_libdir/coreapps/plugins/libmedia.so
%_libdir/coreapps/plugins/libmicvolume.so
%_libdir/coreapps/plugins/libnetworking.so
%exclude %_libdir/coreapps/plugins/libplayerctlqt.so
%_libdir/coreapps/plugins/libqwikaccess.so
%_libdir/coreapps/plugins/librotation.so
%_libdir/coreapps/plugins/libvolume.so
%_libdir/coreapps/shareit/libimageconv.so
%_libexecdir/coreapps/corepkit
%_desktopdir/shareit.desktop
%_datadir/coreapps/scripts/airplane-off.sh
%_datadir/coreapps/scripts/airplane-on.sh
%_datadir/coreapps/scripts/albumart.sh
%_datadir/coreapps/scripts/audio-recorder.sh
%_datadir/coreapps/scripts/autorotate-off.sh
%_datadir/coreapps/scripts/autorotate-on.sh
%_datadir/coreapps/scripts/bt-off.sh
%_datadir/coreapps/scripts/bt-on.sh
%_datadir/coreapps/scripts/camera-off.sh
%_datadir/coreapps/scripts/camera-on.sh
%_datadir/coreapps/scripts/camera.sh
%_datadir/coreapps/scripts/check-airplane.sh
%_datadir/coreapps/scripts/check-backlight.sh
%_datadir/coreapps/scripts/check-bt.sh
%_datadir/coreapps/scripts/check-camera.sh
%_datadir/coreapps/scripts/check-keyboard.sh
%_datadir/coreapps/scripts/check-nightmode.sh
%_datadir/coreapps/scripts/check-rotation.sh
%_datadir/coreapps/scripts/check-touchpad.sh
%_datadir/coreapps/scripts/check-touchscreen.sh
%_datadir/coreapps/scripts/check-wifi.sh
%_datadir/coreapps/scripts/dpms-off.sh
%_datadir/coreapps/scripts/dpms-on.sh
%_datadir/coreapps/scripts/flashlight-off.sh
%_datadir/coreapps/scripts/flashlight-on.sh
%_datadir/coreapps/scripts/gps-off.sh
%_datadir/coreapps/scripts/gps-on.sh
%_datadir/coreapps/scripts/hibernate.sh
%_datadir/coreapps/scripts/hotspot-off.sh
%_datadir/coreapps/scripts/hotspot-on.sh
%_datadir/coreapps/scripts/hybrid-sleep.sh
%_datadir/coreapps/scripts/kbd-backlight-off.sh
%_datadir/coreapps/scripts/kbd-backlight-on.sh
%_datadir/coreapps/scripts/keyboard-off.sh
%_datadir/coreapps/scripts/keyboard-on.sh
%_datadir/coreapps/scripts/lockscreen.sh
%_datadir/coreapps/scripts/logout.sh
%_datadir/coreapps/scripts/nightmode-off.sh
%_datadir/coreapps/scripts/nightmode-on.sh
%_datadir/coreapps/scripts/performance.sh
%_datadir/coreapps/scripts/playerctl-metadata.sh
%_datadir/coreapps/scripts/poweroff.sh
%_datadir/coreapps/scripts/powersave.sh
%_datadir/coreapps/scripts/reboot-to-uefi.sh
%_datadir/coreapps/scripts/reboot.sh
%_datadir/coreapps/scripts/rotate-invert.sh
%_datadir/coreapps/scripts/rotate-left.sh
%_datadir/coreapps/scripts/rotate-normal.sh
%_datadir/coreapps/scripts/rotate-right.sh
%_datadir/coreapps/scripts/screen-recorder.sh
%_datadir/coreapps/scripts/screencam-recorder.sh
%_datadir/coreapps/scripts/screenshot.sh
%_datadir/coreapps/scripts/stop-recorder.sh
%_datadir/coreapps/scripts/suspend-then-hibernate.sh
%_datadir/coreapps/scripts/suspend.sh
%_datadir/coreapps/scripts/toggle_always_above.sh
%_datadir/coreapps/scripts/touchpad-off.sh
%_datadir/coreapps/scripts/touchpad-on.sh
%_datadir/coreapps/scripts/touchscreen-off.sh
%_datadir/coreapps/scripts/touchscreen-on.sh
%_datadir/coreapps/scripts/wifi-off.sh
%_datadir/coreapps/scripts/wifi-on.sh
%_datadir/polkit-1/actions/cc.cubocore.coreapps.policy

%changelog
* Tue Dec 30 2025 Nikolay Strelkov <snk@altlinux.org> 5.0.0-alt1
- Initial build for Sisyphus
