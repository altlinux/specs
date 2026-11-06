%define _unpackaged_files_terminate_build 1

Name: 81voltd
Version: 1.2.0
Release: alt1
Summary: Simple implementation of the IMS Data service on QMI/QRTR
License: GPL-2.0-or-later
Group: System/Kernel and hardware
Url: https://gitlab.nura.eco/modem/81voltd
VCS: https://gitlab.nura.eco/modem/81voltd.git
ExclusiveArch: aarch64

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: pkgconfig(mm-glib)
BuildRequires: pkgconfig(qmi-glib)
BuildRequires: pkgconfig(qrtr)

%description
This is a simple implementation of the IMS Data service on QMI/QRTR. It handles
the known and important requests to start and stop a connection through the
ModemManager D-Bus API, treating other requests as no operation.

%prep
%setup

%build
%meson
%meson_build -v

%install
%meson_install

%files
%doc README.md
%_bindir/%name
%_unitdir/%name.service
%exclude %_sysconfdir/init.d/%name
%_man1dir/*

%changelog
* Fri Nov 06 2026 Vasiliy Doylov <neko@altlinux.org> 1.2.0-alt1
- Initial build for ALT.
