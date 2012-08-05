Name: madwifi-utils
Version: 0.9.4
Release: alt2
Epoch: 1

Summary: Utilities for Atheros-based WiFi .11a/b/g adapters
License: Dual: GPL or BSD
Group: System/Kernel and hardware
Url: http://madwifi-project.org/
Packager: Konstantin A. Lepikhov <lakostis@altlinux.org>

%define srcname madwifi-0.9.4-r4180-20120803
Source: http://snapshots.madwifi-project.org/%srcname.tar.gz
Patch: %name-0.9.2-alt.patch

%description
This software contains a utilites for Atheros-based Wireless LAN devices.

A full list of product solutions utilizing Atheros chips can be found
at http://www.atheros.com/partners/solutions.html

%prep
%setup -n %srcname
%patch -p1

%build
%make_build -C tools

%install
%makeinstall_std -C tools STRIP=:

%files
%_sbindir/*
%_mandir/man8/*
%doc COPYRIGHT README SNAPSHOT THANKS

%changelog
* Sun Aug 05 2012 Dmitry V. Levin <ldv@altlinux.org> 1:0.9.4-alt2
- Rebuilt.

* Sat Mar 08 2008 L.A. Kostis <lakostis@altlinux.ru> 1:0.9.4-alt1
- rebuild for 0.9.4.

* Sun Nov 04 2007 L.A. Kostis <lakostis@altlinux.ru> 1:0.9.3.3-alt1
- rebuild for 0.9.3.3.

* Wed May 23 2007 Konstantin A. Lepikhov <lakostis@altlinux.org> 1:0.9.3.1-alt1
- 0.9.3.1 release fixing serious security bugs.

* Fri May 11 2007 Konstantin A. Lepikhov <lakostis@altlinux.org> 1:0.9.3-alt1
- 0.9.3 release.

* Sat Sep 02 2006 Alexei Takaseev <taf@altlinux.ru> 1:0.9.2-alt1
- 0.9.2 release
- Transition to the official name of versions

* Tue Apr 11 2006 Alexei Takaseev <taf@altlinux.ru> 0.9.4.5-alt3
- 20060411 snapshot

* Wed Feb 01 2006 Alexei Takaseev <taf@altlinux.ru> 0.9.4.5-alt2
- 20060201 snapshot

* Sun Dec 11 2005 Alexei Takaseev <taf@altlinux.ru> 0.9.4.5-alt1
- Initial release
