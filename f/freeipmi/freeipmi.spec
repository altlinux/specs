# vim: set ft=spec: -*- rpm-spec -*-

%define docdir %_defaultdocdir/%name-%version

Name: freeipmi
Version: 1.6.1
Release: alt1

Summary: GNU FreeIPMI - Intelligent Platform Management System
Group: Monitoring
License: GPL
Url: http://www.gnu.org/software/freeipmi/

PreReq: lib%name = %version-%release

Source: %name-%version.tar
Source1: %name.watch
Patch: %name-%version-alt.patch

BuildRequires: libgcrypt-devel texinfo
BuildRequires(pre): rpm-build-ubt

%description
This project provides "Remote-Console" (out-of-band) and
"System Management Software" (in-band) based on Intelligent
Platform Management Interface (IPMI v1.5/2.0) specification.

%package -n lib%name
Summary: FreeIPMI shared libraries
Group: System/Libraries

%description -n lib%name
FreeIPMI shared libraries.

%package -n lib%name-devel
Summary: GNU FreeIPMI development files
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
GNU FreeIPMI development files.

%package bmc-watchdog
Summary: GNU FreeIPMI BMC watchdog
Group: Monitoring
PreReq: lib%name = %version-%release

%description bmc-watchdog
Watchdog daemon for OS monitoring and recovery.

%package ipmidetectd
Summary: GNU FreeIPMI Detection daemon
Group: Monitoring
PreReq: lib%name = %version-%release

%description ipmidetectd
The ipmidetectd daemon regularly ipmipings remote nodes.
The ipmidetect tool and library will determine detected vs. undetected
ipmi systems based on the most recent ipmipings received.

%package ipmiseld
Summary: FreeIPMI SEL syslog logging daemon
Group: Monitoring
PreReq: lib%name = %version-%release

%description ipmiseld
IPMI SEL syslog logging daemon.

%package doc
Summary: GNU FreeIPMI documentation
Group: Documentation
Conflicts: lib%name < %version-%release
Conflicts: lib%name > %version-%release
BuildArch: noarch

%description doc
GNU FreeIPMI documentation.

%prep
%setup
%add_optflags -D_GNU_SOURCE
%patch -p1

%build
%autoreconf

%configure \
	--localstatedir=%_var \
	--disable-static
%make_build

%install
%make_install DESTDIR=%buildroot \
	docdir=%docdir \
	install

find %buildroot%docdir/ -type f -size +4k \( -iname changelog\* -or -iname COPYING\* -or -iname \*ipmi\* \) -print0 |
xargs -r0 bzip2 -9f --

%post -n lib%name
touch %_localstatedir/%name/ipckey

%preun -n lib%name
[ "$1" -eq 0 ] && rm -f %_localstatedir/%name/ipckey ||: >/dev/null 2>&1

%post ipmidetectd
%post_service ipmidetectd

%preun ipmidetectd
%preun_service ipmidetectd

%post bmc-watchdog
%post_service bmc-watchdog

%preun bmc-watchdog
%preun_service bmc-watchdog

%post ipmiseld
%post_service bmc-watchdog

%preun ipmiseld
%preun_service bmc-watchdog

%files
%_sbindir/*
%exclude %_sbindir/ipmiseld
%exclude %_sbindir/bmc-watchdog
%exclude %_sbindir/ipmidetectd
%_man8dir/*.8*
%exclude %_man8dir/ipmiseld.8*
%exclude %_man8dir/bmc-watchdog.8*
%exclude %_man8dir/*detectd*.8*
%_man5dir/*.5*
%exclude %_man5dir/*detectd*.5*
%exclude %_man5dir/*ipmiseld*.5*
%config %_sysconfdir/%name/freeipmi.conf
%config %_sysconfdir/%name/ipmidetect.conf
%config %_sysconfdir/%name/freeipmi_interpret_sel.conf
%config %_sysconfdir/%name/freeipmi_interpret_sensor.conf
%_man7dir/*.7*

%files -n lib%name
%_libdir/lib*.so.*
%dir %_sysconfdir/%name
%config %_sysconfdir/%name/libipmiconsole.conf
%dir %_localstatedir/%name
%ghost %_localstatedir/%name/ipckey

%files -n lib%name-devel
%_libdir/lib*.so
%_includedir/*
%_pkgconfigdir/*.pc
%_man3dir/*

%files bmc-watchdog
%config(noreplace) %_sysconfdir/sysconfig/bmc-watchdog
%config %_initdir/bmc-watchdog
%_sbindir/bmc-watchdog
%_man8dir/bmc-watchdog.8*

%files ipmidetectd
%_sbindir/ipmidetectd
%config %_initdir/ipmidetectd
%_man5dir/*detectd*.5*
%_man8dir/*detectd*.8*
%config %_sysconfdir/%name/ipmidetectd.conf

%files ipmiseld
%_sbindir/ipmiseld
%config %_initdir/ipmiseld
%_man5dir/*ipmiseld*.5*
%_man8dir/ipmiseld*.8*
%config %_sysconfdir/%name/ipmiseld.conf

%files doc
%docdir
%_infodir/%name-faq.info*

%changelog
* Mon Feb 26 2018 Anton Farygin <rider@altlinux.ru> 1.6.1-alt1
- new version 1.6.1

* Mon Aug 21 2017 Anton Farygin <rider@altlinux.ru> 1.5.7-alt1%ubt
- new version 1.5.7

* Tue Aug 08 2017 Anton Farygin <rider@altlinux.ru> 1.5.6-alt1%ubt
- new version 1.5.6

* Tue May 02 2017 Anton Farygin <rider@altlinux.ru> 1.5.5-alt1%ubt
- new version 1.5.5

* Sun Oct 02 2016 Anton Farygin <rider@altlinux.ru> 1.5.4-alt1
- new version 1.5.4

* Tue Jun 14 2016 Anton Farygin <rider@altlinux.ru> 1.5.2-alt1
- new version 1.5.2

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 1.4.9-alt1.1
- NMU: added BR: texinfo

* Fri Jun 19 2015 Anton Farygin <rider@altlinux.ru> 1.4.9-alt1
- new version 1.4.9

* Thu Jan 15 2015 Anton Farygin <rider@altlinux.ru> 1.4.8-alt1
- new version 1.4.8

* Mon Sep 08 2014 Anton Farygin <rider@altlinux.ru> 1.4.5-alt1
- new version 1.4.5

* Mon Jun 30 2014 Anton Farygin <rider@altlinux.ru> 1.4.4-alt1
- new version 1.4.4

* Fri Jun 06 2014 Anton Farygin <rider@altlinux.ru> 1.4.3-alt1
- new version

* Tue Mar 25 2014 Anton Farygin <rider@altlinux.ru> 1.4.1-alt1
- new version

* Thu Feb 20 2014 Anton Farygin <rider@altlinux.ru> 1.3.4-alt1
- new version

* Tue Nov 12 2013 Anton Farygin <rider@altlinux.ru> 1.3.3-alt1
- new version

* Fri Oct 11 2013 Anton Farygin <rider@altlinux.ru> 1.3.2-alt1
- new version

* Mon Jul 15 2013 Anton Farygin <rider@altlinux.ru> 1.2.8-alt1
- new version

* Thu Jun 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.10-alt1.1
- Fixed build

* Thu Dec 15 2011 Michael Shigorin <mike@altlinux.org> 1.0.10-alt1
- new version

* Tue Sep 13 2011 Anton Farygin <rider@altlinux.ru> 1.0.6-alt1
- new version

* Mon Apr 18 2011 Anton Farygin <rider@altlinux.ru> 1.0.3-alt2
- use noarch for documentation package

* Fri Apr 15 2011 Anton Farygin <rider@altlinux.ru> 1.0.3-alt1
- new version

* Wed Oct 06 2010 Anton Farygin <rider@altlinux.ru> 0.8.10-alt1
- new version

* Fri Aug 20 2010 Anton Farygin <rider@altlinux.ru> 0.8.8-alt1
- new version

* Mon Jun 28 2010 Anton Farygin <rider@altlinux.ru> 0.8.7-alt1
- new version

* Mon Feb 15 2010 Anton Farygin <rider@altlinux.ru> 0.8.3-alt1
- new version

* Wed Dec 23 2009 Anton Farygin <rider@altlinux.ru> 0.8.1-alt1
- new version

* Fri Dec 12 2008 Stanislav Ievlev <inger@altlinux.org> 0.6.4-alt2
- fix build

* Fri Jul 11 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.6.4-alt1
- 0.6.4 release.

* Thu Mar 13 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.5.5-alt1
- 0.5.5 release.

* Tue Nov 06 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.4.6-alt1
- 0.4.6 release.

* Fri Sep 21 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.4.4-alt1
- 0.4.4 release.

* Thu Aug 16 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.4.3-alt1
- 0.4.3 release.

* Tue Jul 10 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.4.0-alt0.beta1
- 0.4.0 beta 1.

* Mon Apr 09 2007 Sir Raorn <raorn@altlinux.ru> 0.3.2-alt1
- Built for Sisyphus

