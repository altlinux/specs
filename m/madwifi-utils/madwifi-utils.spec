%define module_name	madwifi
%define module_version	0.9.4
%define module_release	alt1

Summary: Utilities for Atheros-based WiFi .11a/b/g adapters
Name: madwifi-utils
Version: %module_version
Release: alt1
Serial: 1
License: Dual: GPL or BSD
Group: System/Kernel and hardware
Url: http://www.madwifi.org/

BuildRequires: perl sharutils
BuildRequires: kernel-build-tools >= 0.7
BuildRequires: kernel-source-%module_name = %module_version
BuildRequires: glibc-kernheaders


PreReq: coreutils
PreReq: modutils
Patch0: %name-0.9.2-alt.patch

Packager: Konstantin A. Lepikhov <lakostis@altlinux.org>

%description
This software contains a utilites for Atheros-based Wireless LAN devices.

A full list of product solutions utilizing Atheros chips can be found
at http://www.atheros.com/partners/solutions.html

%prep
rm -rf kernel-source-%module_name-%module_version

tar -jxvf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2

%setup -D -T -n kernel-source-%module_name-%module_version
%patch0 -p1

%build
%make_build -C tools

%install
%makeinstall -C tools DESTDIR=%buildroot

%files
%_sbindir/*
%_mandir/man8/*
%doc docs/users-guide.pdf docs/WEP-HOWTO.txt COPYRIGHT README THANKS

%changelog
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
