%def_enable check

Name: dbus-broker
Version: 37
Release: alt1

Summary: Linux D-Bus Message Broker
License: Apache-2.0
Group: System/Servers
Url: https://github.com/bus1/dbus-broker
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: https://github.com/bus1/dbus-broker/releases/download/v%version/%name-%version.tar.xz

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson pkgconfig(audit) pkgconfig(expat) pkgconfig(dbus-1) pkgconfig(libcap-ng)
BuildRequires: pkgconfig(libselinux) pkgconfig(libsystemd) pkgconfig(systemd) python3-module-docutils

%description
dbus-broker is an implementation of a message bus as defined by the D-Bus
specification. Its aim is to provide high performance and reliability, while
keeping compatibility to the D-Bus reference implementation. It is exclusively
written for Linux systems, and makes use of many modern features provided by
recent Linux kernel releases.

%prep
%setup

%build
%meson \
    -Dselinux=true \
    -Daudit=true \
    -Ddocs=true \
    -Dlauncher=true \
    -Dlinux-4-17=true
%nil
%meson_build

%install
%meson_install

%check
%__meson_test

%files
%_bindir/%name
%_bindir/%name-launch
%_unitdir/%name.service
%_journal_catalogdir/*.catalog
%_userunitdir/%name.service
%_man1dir/*.1*
%doc README* NEWS*

%changelog
* Sat Jun 28 2025 Yuri N. Sedunov <aris@altlinux.org> 37-alt1
- 37
- enabled %%check

* Fri Jun 14 2024 Yuri N. Sedunov <aris@altlinux.org> 36-alt1
- 36

* Thu Jan 11 2024 Valery Inozemtsev <shrek@altlinux.ru> 35-alt1
- update to v35

* Mon Jul 03 2023 Valery Inozemtsev <shrek@altlinux.ru> 33-alt1
- initial release

