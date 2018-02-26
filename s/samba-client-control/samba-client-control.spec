Name: samba-client-control
Version: 1.2
Release: alt2

Summary: Facilities control for samba client helpers
License: GPL
Group: System/Servers
BuildArch: noarch
Packager: Dmitry V. Levin <ldv@altlinux.org>

PreReq: control
Conflicts: samba-client < 3.0.5-alt2

Source0: smbmount.control
Source1: cifsmount.control
Source2: cifsumount.control

%description
This package contains control rules for samba client helpers.
See control(8) for details.

%install
install -pD -m755 %_sourcedir/smbmount.control %buildroot%_controldir/smbmount
install -pD -m755 %_sourcedir/cifsmount.control %buildroot%_controldir/cifsmount
install -pD -m755 %_sourcedir/cifsumount.control %buildroot%_controldir/cifsumount

%files
%config %_controldir/*

%changelog
* Mon Sep 22 2008 Dmitry V. Levin <ldv@altlinux.org> 1.2-alt2
- Fixed typo in specfile.

* Tue Apr 17 2007 Dmitry V. Levin <ldv@altlinux.org> 1.2-alt1
- Added cifsumount control script (#11124).
- Updated cifsmount control script to support new binary path.
- Updated smbmount control script to support new binary paths.
- Added summary to control scripts.

* Sat Oct 02 2004 Dmitry V. Levin <ldv@altlinux.org> 1.1-alt1
- Added help to control scripts.

* Mon Sep 13 2004 Dmitry V. Levin <ldv@altlinux.org> 1.0-alt1
- Initial revision.
