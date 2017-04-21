Name: xorg-conf-libinput-touchpad
Version: 0.1
Release: alt1
Summary: Config file for libinput touchpads
License: %pubdomain
Group: System/Configuration/Hardware
Source0: libinput-touchpad.conf
BuildArch: noarch

BuildRequires(pre): rpm-build-licenses

Requires: xorg-drv-libinput

%description
This package contains configuratin file for libinput touchpads
with some frequently used options.
Left mouse button by tapping is enabled by default.

%install
install -Dm0644 %SOURCE0 %buildroot/%_sysconfdir/X11/xorg.conf.d/50-libinput-touchpad.conf

%files
%config(noreplace) %_sysconfdir/X11/xorg.conf.d/50-libinput-touchpad.conf

%changelog
* Fri Apr 21 2017 Mikhail Efremov <sem@altlinux.org> 0.1-alt1
- Initial build.
