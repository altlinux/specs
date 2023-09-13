%define uds_dir %_datadir/openuds/uds
Name: openuds-installers
Version: 3.6.0
Release: alt2
Summary: openUDS installers
License: BSD-3-Clause
Group: Networking/Remote access
URL: https://github.com/altlinux/openuds-installers

Source1: UDSClientSetup-3.6.0.exe
Source2: UDSActorSetup-3.6.0.exe
Source3: UDSActorUnmanagedSetup-3.6.0.exe

BuildArch: noarch

%description
%summary.

%prep

%install
install -Dp -m 644 %SOURCE1 %buildroot%uds_dir/static/clients/UDSClientSetup-3.6.0.exe
install -Dp -m 644 %SOURCE2 %buildroot%uds_dir/osmanagers/WindowsOsManager/files/UDSActorSetup-3.6.0.exe
install -Dp -m 644 %SOURCE3 %buildroot%uds_dir/osmanagers/WindowsOsManager/files/UDSActorUnmanagedSetup-3.6.0.exe

%files
%uds_dir/static/clients/*
%uds_dir/osmanagers/WindowsOsManager/files/*

%changelog
* Mon Sep 11 2023 Alexander Burmatov <thatman@altlinux.org> 3.6.0-alt2
- Revert 4.0 changes.

* Fri May 19 2023 Alexander Burmatov <thatman@altlinux.org> 3.6.0-alt1
- 3.6.0

* Mon Dec 05 2022 Alexey Shabalin <shaba@altlinux.org> 3.5.0-alt1
- 3.5.0

* Mon Nov 29 2021 Alexey Shabalin <shaba@altlinux.org> 3.0.0-alt2
- Add python3 client.

* Wed Oct 27 2021 Alexey Shabalin <shaba@altlinux.org> 3.0.0-alt1
- Initial build.
