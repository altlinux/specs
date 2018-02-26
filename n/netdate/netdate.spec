Name: netdate
License: Public Domain
Group: Networking/Other
Version: 1.2
Release: alt2
Summary: Set Date and Time by ARPA Internet RFC 868
#Url: http://www.ibiblio.org/pub/linux/system/network/sunacm/Other/netdate/
Url: ftp://ftp.suse.com/pub/people/kukuk/ipv6/
Source: %name-%version.tar.bz2
Source1: sysconfig.%name
Source2: rc.%name
Patch: %name-1.2.dif
Packager: Fr. Br. George <george@altlinux.ru>

%description
Netdate takes a list of names of Internet hosts as arguments, selects
the one that supplies the best time, and sets the system time
accordingly.

The "best" time is chosen by polling the named hosts once each to find
their times and taking their differences from the local host's time.
These differences are used to find the largest group of hosts whose
times agree with each other within a certain limit. The first host in
the largest group is picked as the best host.

%prep
%setup -n %name
%patch

%build
%make

%install
install -d -m 755 %buildroot/usr/sbin
install -d -m 755 %buildroot%_mandir/man8
install -d -m 755 %buildroot%_sysconfdir/sysconfig
install -d -m 755 %buildroot%_initdir
make DESTDIR=%buildroot/ install
install %SOURCE1 %buildroot%_sysconfdir/sysconfig/%name
install -m 755 %SOURCE2 %buildroot%_initdir/%name

%files
%doc COPYRIGHT
%doc %_mandir/man?/*
%config(noreplace) %_sysconfdir/sysconfig/%name
%_initdir/%name
/usr/sbin/netdate

%changelog
* Tue Apr 29 2008 Fr. Br. George <george@altlinux.ru> 1.2-alt2
- Fix unmets

* Mon Oct 15 2007 Fr. Br. George <george@altlinux.ru> 1.2-alt1
- Initial build for ALT

* Mon May 22 2006 - schwab@suse.de
- Don't strip binaries.
* Wed Jan 25 2006 - mls@suse.de
- converted neededforbuild to BuildRequires
* Tue Feb 10 2004 - postadal@suse.cz
- added RPM_OPT_FLAGS to CFLAGS and CXXFLAGS
* Sun Jan 11 2004 - adrian@suse.de
- build as user
* Wed Nov 13 2002 - kukuk@suse.de
- fix wtmp corruption [Bug #21740]
* Thu Feb 28 2002 - bk@suse.de
- fix 64-bit bug: don't use signed when assinging to unsigned long
* Tue Apr 10 2001 - kukuk@suse.de
- Add IPv6 support
* Thu Mar 22 2001 - ro@suse.de
- added split-aliases as provides
* Mon Feb 19 2001 - cihlar@suse.cz
- compile with $RPM_OPT_FLAGS and -D_GNU_SOURCE
- fixed file list
* Fri Dec 01 2000 - smid@suse.cz
- new version 1.2
* Sat Apr 15 2000 - kukuk@suse.de
- Initial package, split from nkitb.
