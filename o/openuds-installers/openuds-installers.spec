%define uds_dir %_datadir/openuds/uds
Name: openuds-installers
Version: 3.0.0
Release: alt1
Summary: openUDS installers
License: BSD-3-Clause
Group: Networking/Remote access
URL: https://github.com/altlinux/openuds-installers

Source1: openUDS-Client_Installer-3.0.0-py27.exe
Source2: openUDS-Managed_Installer-3.0.0.exe
Source3: openUDS-Unmanaged_Installer-3.0.0.exe

BuildArch: noarch

%description
%summary.

%prep

%install
install -Dp -m 644 %SOURCE1 %buildroot%uds_dir/static/clients/openUDS-Client_Installer-3.0.0-py27.exe
install -Dp -m 644 %SOURCE2 %buildroot%uds_dir/osmanagers/WindowsOsManager/files/openUDS-Managed_Installer-3.0.0.exe
install -Dp -m 644 %SOURCE2 %buildroot%uds_dir/osmanagers/WindowsOsManager/files/openUDS-Unmanaged_Installer-3.0.0.exe

%files
%uds_dir/static/clients/*
%uds_dir/osmanagers/WindowsOsManager/files/*

%changelog
* Wed Oct 27 2021 Alexey Shabalin <shaba@altlinux.org> 3.0.0-alt1
- Initial build.
