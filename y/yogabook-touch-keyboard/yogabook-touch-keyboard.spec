Name: yogabook-touch-keyboard
Summary: Userspace driver for touchpad-based keyboard
Version: 1.4.1
Release: alt1
Group: System/Configuration/Hardware
License: BSD
Url: https://salsa.debian.org/debian/touch-keyboard

BuildRequires(pre): rpm-build-cmake
BuildRequires: gcc-c++

Source: %name-%version.tar
Patch: touch-keyboard-alt.patch

%description
The userspace driver to support touch keyboard based on touchpad. Such
keyboard may be found in some tablets (Lenovo Yoga Book YB1-X9* for example).

This package is fork of touch keyboard driver from ChromiumOS. It contains
keyboard geometry description for Lenovo Yoga Book but can be reconfigured for
any touch keyboad.

%prep
%setup
%patch -p1

%build
%cmake \
	-DCMAKE_INSTALL_SYSCONFDIR=%_sysconfdir \
	-DSYSTEMD_UNIT_DIR=%_unitdir \
	-DUDEV_DIR=%prefix/lib/udev

%cmake_build

%install
%cmakeinstall_std

# set default layout to PC-104-like layout (Russian, US)
pushd %buildroot%_sysconfdir/touch_keyboard
ln -s layouts/YB1-X9x-pc104.csv layout.csv
popd

%files
%doc README* layouts/README
%_unitdir/touch-keyboard-handler.service
%_udevrulesdir/60-touch-keyboard.rules
%_udevhwdbdir/61-evdev-yogabook.hwdb
%_sysconfdir/touch_keyboard
%_sbindir/touch_keyboard_handler

%changelog
* Thu Jan 02 2025 L.A. Kostis <lakostis@altlinux.ru> 1.4.1-alt1
- 1.4.1.

* Thu Dec 26 2024 L.A. Kostis <lakostis@altlinux.ru> 1.2-alt1
- Initial build for ALTLinux.

