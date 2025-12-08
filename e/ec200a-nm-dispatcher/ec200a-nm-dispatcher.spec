%global _unpackaged_files_terminate_build 1

Name:		ec200a-nm-dispatcher
Version:	0.1
Release:	alt1
Summary:	Quectel EC200A control interface dispatcher rules for the NetworkManager

Group:		System/Configuration/Networking
License:	GPLv3+
URL:		none
Source:     %name-%version.tar

Requires:   NetworkManager-daemon
BuildArch:  noarch

%define nmd_dir %_sysconfdir/NetworkManager/dispatcher.d

%description
This package provides the NetworkManager dispatcher script to fix
Quectel EC200A control interface problem by removing extra default
gateway rote provided by the modem.

%prep
%setup -q

%build
install -Dpm 0755 -t %buildroot%nmd_dir 01-Quectel-EC200A

%files
%nmd_dir/01-Quectel-EC200A

%changelog
* Mon Dec 08 2025 Andrew Savchenko <bircoph@altlinux.org> 0.1-alt1
- Initial version, code by shrek@altlinux.ru
