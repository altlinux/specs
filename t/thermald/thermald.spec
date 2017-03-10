Name: thermald
Version: 1.6
Release: alt1

Summary: Thermal daemon for IA

License: GPLv2+
Group: Development/Other
Url: https://github.com/01org/thermal_daemon
# Source-url: https://github.com/01org/thermal_daemon/archive/v%version.tar.gz

Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar.gz
Source1: thermald.init

Buildrequires: gcc-c++ glib-devel libdbus-glib-devel libgio-devel libgomp-devel libxml2-devel
Requires: dbus

%description
Thermal issues are important to handle proactively to reduce performance impact.

The project provides a Linux user mode daemon to system developers, reducing
time to market with controlled thermal management using P-states, T-states, and
the Intel power clamp driver. The Thermal Daemon uses the existing Linux kernel
infrastructure and can be easily enhanced.

%description -l ru_RU.UTF-8
thermald представляет собой службу, которая управляет питанием с помощью
Р-состояний, Т-состояния и Intel power clamp driver. thermald использует
существующую инфраструктуру ядра Linux, и его возможности могут быть легко
расширены.

%prep
%setup
sed 's/@sbindir@/\/usr\/sbin/g' data/thermald.service.in > data/thermald.service

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
install -pD -m644 data/%name.service %buildroot%_unitdir/%name.service
install -pD -m644 data/org.freedesktop.%name.service.in %buildroot%_datadir/dbus-1/system-services/org.freedesktop.%name.service
install -pD -m755 %SOURCE1 %buildroot%_initdir/%name

%post
%post_service thermald

%preun
%preun_service thermald

%files
%_sbindir/%name
%_datadir/dbus-1/system-services/org.freedesktop.%name.service
%_unitdir/%name.service
%_initdir/%name
%exclude %_sysconfdir/init/%name.conf
%dir %_sysconfdir/%name
%_sysconfdir/%name/*
%_sysconfdir/dbus-1/system.d/*
%_man5dir/*
%_man8dir/*

%changelog
* Fri Mar 10 2017 Anton Midyukov <antohami@altlinux.org> 1.6-alt1
- new version (1.6) with rpmgs script

* Sat Dec 10 2016 Anton Midyukov <antohami@altlinux.org> 1.5.4-alt1
- new version (1.5.4) with rpmgs script

* Wed Oct 05 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5.3-alt2
- Fixed the adaption of the Debian-style .init for ALT:
  + .init: condrestart/condstop implemented in a simple way;
  + .init: status cmd added;
  + .init: do not print DONE when printing the usage.
- (.spec) Do not own dbus and systemd dirs.

* Fri May 27 2016 Anton Midyukov <antohami@altlinux.org> 1.5.3-alt1
- New version.

* Mon Mar 21 2016 Anton Midyukov <antohami@altlinux.org> 1.4.3-alt2
- Remove init-condrestart.

* Tue Feb 16 2016 Anton Midyukov <antohami@altlinux.org> 1.4.3-alt1
- Initial build for Altlinux Sisyphus.
