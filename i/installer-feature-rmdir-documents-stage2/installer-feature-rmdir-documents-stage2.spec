%define preinstall %_datadir/install2/preinstall.d/
Name: installer-feature-rmdir-documents-stage2
Version: 0.1
Release: alt1

Summary: Remove Documents dir from skel
License: GPL
Packager: Lenar Shakirov <snejok@altlinux.org>
Url: http://www.altlinux.org/
Group: System/Configuration/Other
BuildArch: noarch
Source: %name-%version.tar
Requires: installer-common-stage2

%description
This package contains script for delete Documents dir from skel.

%prep
%setup

%install
mkdir -p %buildroot%preinstall/
install -pm755 40-rmdir-documents %buildroot%preinstall/

%files
%preinstall/*

%changelog
* Tue Nov 09 2010 Lenar Shakirov <snejok@altlinux.ru> 0.1-alt1
- Initial build

