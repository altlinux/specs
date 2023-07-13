Name: dbus-broker
Version: 33
Release: alt1
Summary: Linux D-Bus Message Broker
License: ASL 2.0
Group: System/Servers
Url: https://github.com/bus1/dbus-broker
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar.xz

BuildRequires: meson pkgconfig(audit) pkgconfig(expat) pkgconfig(dbus-1) pkgconfig(libcap-ng)
BuildRequires: pkgconfig(libselinux) pkgconfig(libsystemd) pkgconfig(systemd) python3-module-docutils

%description
dbus-broker is an implementation of a message bus as defined by the D-Bus
specification. Its aim is to provide high performance and reliability, while
keeping compatibility to the D-Bus reference implementation. It is exclusively
written for Linux systems, and makes use of many modern features provided by
recent Linux kernel releases.

%prep
%setup -q

%build
%meson \
	-Dselinux=true \
	-Daudit=true \
	-Ddocs=true \
	-Dlauncher=true \
	-Dlinux-4-17=true

%meson_build

%install
%meson_install

%files
%_unitdir/%name.service
%_bindir/*
%_prefix/lib/systemd/catalog/*.catalog
%_prefix/lib/systemd/user/%name.service
%_man1dir/*.1*

%changelog
* Mon Jul 03 2023 Valery Inozemtsev <shrek@altlinux.ru> 33-alt1
- initial release

