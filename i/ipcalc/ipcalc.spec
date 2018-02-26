# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: ipcalc
Version: 0.41
Release: alt1

Summary: IP subnet calculator
License: %gpl2plus
Group: Networking/Other
Url:  http://jodies.de/ipcalc
BuildArch: noarch

Packager: Artem Zolochevskiy <azol@altlinux.ru>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses

%description
ipcalc takes an IP address and netmask and calculates the resulting broadcast,
network, Cisco wildcard mask, and host range. By giving a second netmask, you
can design subnets and supernets. It is also intended to be a teaching tool
and presents the subnetting results as easy-to-understand binary values.

%prep
%setup

%install
install -D ipcalc %buildroot%_bindir/ipcalc

%files
%doc changelog contributors license
%_bindir/*

%changelog
* Sun Oct 19 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.41-alt1
- initial build for Sisyphus
  + console version (without cgi wrapper)

