%define _unpackaged_files_terminate_build 1

Name: swclock-offset
Version: 0.3.0
Release: alt1
Summary: Workaround for non-writable RTC clocks
License: GPLv3
Group: System/Kernel and hardware
URL: https://gitlab.postmarketos.org/postmarketOS/swclock-offset
VCS: https://gitlab.postmarketos.org/postmarketOS/swclock-offset.git

BuildArch: noarch

Source: %name-%version.tar
Patch0: 0.3.0-make-disable-openrc-install.patch

BuildRequires(pre): rpm-macros-systemd

%description
Some devices have a working but non-writable real-time clock (RTC).
This package contains two services: One writes the offset between
'hwclock' and 'swclock' to a file at shutdown, another one reads the
offset from the file at boot and sets the 'swclock'. This way the system
time in userspace is kept in present time.

%prep
%setup
%autopatch -p 1

%install
%makeinstall_std systemddir=%_unitdir bindir=%_sbindir cachedir=%_localstatedir

%files
%_sbindir/%name-*
%_unitdir/%name-*.service
%_unitdir/%name.target

%changelog
* Mon Jul 06 2026 Vasiliy Doylov <neko@altlinux.org> 0.3.0-alt1
- Initial build for ALT
