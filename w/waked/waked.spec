Name: waked
Version: 0.1.1
Release: alt1
Summary: Waked Daemon
Group: System/Servers
License: GPLv2
URL: https://gitlab.com/seath1/waked.git

Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: cmake gcc-c++ libsdbus-cpp-devel

%description
Waked is a daemon which lets Apps wake the system from suspend at requested times

%prep
%setup -q
%patch0 -p1

%build
cd src
%cmake
%cmake_build

%install
install -pD -m0755 src/%_target_platform/%name %buildroot%_bindir/%name
install -pD -m0644 de.seath.Waked.conf %buildroot%_datadir/dbus-1/system.d/de.seath.Waked.conf
install -pD -m0644 %name.service %buildroot%systemd_unitdir/%name.service

%files
%_bindir/%name
%systemd_unitdir/%name.service
%_datadir/dbus-1/system.d/de.seath.Waked.conf

%changelog
* Fri Oct 20 2023 Valery Inozemtsev <shrek@altlinux.ru> 0.1.1-alt1
- initial release

