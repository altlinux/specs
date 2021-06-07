%define dname ru.basealt.alterator

Name: alterator-dbus
Version: 0.0.1
Release: alt1

Summary: D-Bus woo-bus gate
License: GPL-2
Group: System/Configuration/Other

BuildRequires: cmake gcc
BuildRequires: glib2-devel libcurl-devel libdbus-glib-devel libpolkit-devel libsystemd-devel

Source0: %name-%version.tar

%description
D-Bus woo-bus gate.

%prep
%setup -q

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmakeinstall_std

%files
%_sbindir/%name
%_unitdir/%name.service
%_datadir/dbus-1/system.d/%dname.conf
%_datadir/polkit-1/actions/%dname.policy
%_datadir/polkit-1/rules.d/%dname.rules

%changelog
* Wed Apr 21 2021 Valery Sinelnikov <greh@altlinux.org> 0.0.1-alt1
- Initial build

