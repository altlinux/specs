Name: thermald
Version: 1.4.3
Release: alt1

Summary: Thermal daemon for IA

License: GPLv2+
Group: Development/Other
Url: https://github.com/01org/thermal_daemon

Packager: Anton Midyukov <antohami@altlinux.org>

Source: https://github.com/01org/thermal_daemon/releases/%name-%version.tar.gz
Source1: thermald.init

Buildrequires: gcc-c++ glib-devel libdbus-glib-devel libgio-devel libgomp-devel libxml2-devel

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
/sbin/service thermald condrestart ||:

%preun
%preun_service thermald
/sbin/service thermald condstop ||:

%files
%_sbindir/%name
%dir %_datadir/dbus-1/
%dir %_datadir/dbus-1/system-services/
%_datadir/dbus-1/system-services/org.freedesktop.%name.service
%dir %_unitdir/
%_unitdir/%name.service
%_initdir/%name
%dir %_sysconfdir/%name
%_sysconfdir/%name/*
%_sysconfdir/dbus-1/system.d/*
%_man5dir/*
%_man8dir/*

%changelog
* Tue Feb 16 2016 Anton Midyukov <antohami@altlinux.org> 1.4.3-alt1
- Initial build for Altlinux Sisyphus.
