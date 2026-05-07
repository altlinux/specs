Name: volumes-profile-alt-platform
Version: 1.0
Release: alt1

Summary: Volumes description for ALT Platform Builder
License: GPL
Group: System/Configuration/Other

Url: http://www.altlinux.org/Installer/beans
Source: %name-%version.tar

BuildArch: noarch

%description
%summary

%prep
%setup

%install
%define hook1dir %_datadir/install2/initinstall.d
mkdir -p %buildroot%hook1dir
install -pm755 10-*.sh %buildroot%hook1dir/

%files
%hook1dir/*

%changelog
* Sun May 03 2026 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build with one root partition.
