# https://bugzilla.altlinux.org/36391
%def_without	devel

%define _runtimedir /run

%if_with devel
%def_with	libnfdump
%else
%def_without	libnfdump
%endif

Name: nfdump
Version: 1.7.4
Release: alt1
Summary: collect and process netflow data
Group: Monitoring
%if_without libnfdump
License: GPL-2.0-or-later
%else
License: BSD-3-Clause
%endif
#Url: http://sourceforge.net/projects/nfdump/
Url: https://github.com/phaag/nfdump/releases

Source: %name-%version.tar
Source2: nfcapd.init
Source3: nfcapd.sysconfig
Source4: nfcapd.service
Source5: %name.tmpfiles
Source6: sfcapd.init
Source7: sfcapd.sysconfig
Source8: sfcapd.service

Packager: Vladimir Lettiev <crux@altlinux.org>

BuildRequires: librrd-devel libpcap-devel flex bison bzlib-devel libzstd-devel

%description
Nfdump is a set of tools to collect and process netflow data.
It's fast and has a powerful filter pcap like syntax. Nfdump
supports netflow versions v5, v7, v9 and IPFIX as well as a
limited set of sflow and is IPv6 compatible.
%if_without libnfdump
Binaries was built with the LZ4 code under the BSD-2-Clause License and
the mini subset of the LZO code under the GPL-2.0-or-later License.
%endif

%package nfprofile
Summary: nfprofile - netflow profiler
Group: Monitoring

%description nfprofile
nfprofile is the netflow profiler program for NfSen. It reads
the netflow data from the files stored by nfcapd and creates
the corresponding output files for every channel required.
This program is run only by NfSen.
%if_without libnfdump
Binaries was built with the LZ4 code under the BSD-2-Clause License and
the mini subset of the LZO code under the GPL-2.0-or-later License.
%endif

%package nftrack
Summary: nftrack - Port tracking decoder for NfSen plugin PortTracker.
Group: Monitoring

%description nftrack
nftrack - Port tracking decoder for NfSen plugin PortTracker.
%if_without libnfdump
Binaries was built with the LZ4 code under the BSD-2-Clause License and
the mini subset of the LZO code under the GPL-2.0-or-later License.
%endif

%if_with libnfdump
%package -n libnfdump
Summary: nfdump shared library
License: GPL-2.0-or-later
Group: System/Libraries

%description -n libnfdump
nfdump shared library; it built with LZ4 code under the BSD-2-Clause License
and mini subset of the LZO code under the GPL-2.0-or-later License.
%endif

%if_with devel
%package -n libnfdump-devel
Summary: nfdump development files
Group: Development/C

%description -n libnfdump-devel
nfdump development files

%endif

%prep
%setup -q

%build
%autoreconf
%configure \
%if_without libnfdump
	--disable-shared \
	--enable-static \
%else
	--enable-shared \
	--disable-static \
%endif
%if_with devel
	--enable-devel \
%endif
	--enable-nfprofile \
	--enable-nftrack \
	--enable-sflow \
	--enable-readpcap \
	--enable-nfpcapd \
	--enable-nsel

%make_build

%install
%makeinstall_std
mkdir -p %buildroot{%_cachedir/{nfcapd,sfcapd},%_sysconfdir/sysconfig,%_initdir,%_unitdir,%_tmpfilesdir,%_runtimedir/{nfcapd,sfcapd}}

install -m0755 %SOURCE2 %buildroot%_initdir/nfcapd
install -m0644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/nfcapd
install -m0644 %SOURCE4 %buildroot%_unitdir/nfcapd.service
install -m0644 %SOURCE5 %buildroot%_tmpfilesdir/%name.conf
install -m0755 %SOURCE6 %buildroot%_initdir/sfcapd
install -m0644 %SOURCE7 %buildroot%_sysconfdir/sysconfig/sfcapd
install -m0644 %SOURCE8 %buildroot%_unitdir/sfcapd.service

%if_without devel
rm -f %buildroot%_libdir/libnfdump.so
%endif

%if_without libnfdump
rm -f %buildroot%_libdir/libnfdump.a
%endif

rm -f  %buildroot%_sysconfdir/nfdump.conf.dist

%pre
%_sbindir/useradd -r -d %_cachedir/nfcapd -s /bin/false nfcapd >/dev/null 2>&1 ||:
%_sbindir/useradd -r -d %_cachedir/sfcapd -s /bin/false sfcapd >/dev/null 2>&1 ||:

%post
%post_service nfcapd
%post_service sfcapd

%preun
%preun_service nfcapd
%preun_service sfcapd

%files
%exclude %_bindir/nfprofile
%exclude %_man1dir/nfprofile.1.*
%exclude %_bindir/nftrack
%_bindir/*
%_man1dir/*
%_initdir/*
%_unitdir/*
%_tmpfilesdir/*
%config(noreplace) %_sysconfdir/sysconfig/*
%attr(770,root,nfcapd) %dir %_cachedir/nfcapd
%attr(775,root,nfcapd) %dir %_runtimedir/nfcapd
%attr(770,root,sfcapd) %dir %_cachedir/sfcapd
%attr(775,root,sfcapd) %dir %_runtimedir/sfcapd
%doc README NEWS AUTHORS ChangeLog COPYING

%files nfprofile
%_bindir/nfprofile
%_man1dir/nfprofile.1.*

%files nftrack
%_bindir/nftrack

%if_with libnfdump
%files -n libnfdump
%_libdir/libnfdump-%version.so
%endif

%if_with devel
%files -n libnfdump-devel
%_libdir/libnfdump.so
%endif

%changelog
* Fri Aug 30 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.7.4-alt1
- 1.7.4

* Thu Oct 12 2023 Sergey Y. Afonin <asy@altlinux.org> 1.7.3-alt1
- 1.7.3
- built with libzstd-devel

* Wed Oct 04 2023 Sergey Y. Afonin <asy@altlinux.org> 1.7.2-alt2
- use -w option instead of deprecated -l
- use /run instead of /var/run

* Tue Jul 18 2023 Sergey Y. Afonin <asy@altlinux.org> 1.7.2-alt1
- 1.7.2

* Mon Dec 05 2022 Sergey Y. Afonin <asy@altlinux.org> 1.6.25-alt1
- 1.6.25
- removed -w option from default configuration (behaviour will be changed in 1.7)
- -w option is not used by nfcapd, this behavior has been migrated to sfcapd

* Wed Jun 23 2021 Sergey Y. Afonin <asy@altlinux.org> 1.6.23-alt1
- 1.6.23

* Wed Feb 10 2021 Sergey Y. Afonin <asy@altlinux.org> 1.6.22-alt1
- 1.6.22

* Wed Aug 12 2020 Sergey Y. Afonin <asy@altlinux.org> 1.6.21-alt1
- 1.6.21

* Mon Apr 13 2020 Sergey Y. Afonin <asy@altlinux.org> 1.6.20-alt1
- 1.6.20

* Wed Mar 25 2020 Sergey Y. Afonin <asy@altlinux.org> 1.6.19-alt1
- 1.6.19
- disabled libnfdump subpackage (ALT #36391, second stage)
- added separate License tag for libnfdump subpackage
- the value of the main License tag is selected depending
  on the libnfdump subpackage building status
- removed zlib-devel from BuildRequires

* Thu Dec 12 2019 Grigory Ustinov <grenka@altlinux.org> 1.6.18-alt2
- NMU: Fix license.

* Sun Sep 01 2019 Sergey Y. Afonin <asy@altlinux.org> 1.6.18-alt1
- 1.6.18 (removed 1.5 compat code)
- built without --enable-compat15
- don't packed devel subpackage (ALT #36391)

* Fri Jun 22 2018 Sergey Y. Afonin <asy@altlinux.ru> 1.6.17-alt1
- 1.6.17
- changed Url

* Tue Oct 31 2017 Sergey Y. Afonin <asy@altlinux.ru> 1.6.15-alt2
- rebuilt with librrd8

* Sat Jul 09 2016 Sergey Y. Afonin <asy@altlinux.ru> 1.6.15-alt1
- 1.6.15 (Security update)
- added libnfdump and libnfdump-devel packages

* Thu Jul 16 2015 Alexey Shabalin <shaba@altlinux.ru> 1.6.13-alt3
- fixed init and unit names

* Fri Jul 03 2015 Alexey Shabalin <shaba@altlinux.ru> 1.6.13-alt2
- add nftrack package

* Thu Jul 02 2015 Alexey Shabalin <shaba@altlinux.ru> 1.6.13-alt1
- 1.6.13
- add --enable-nsel configure options
- add sfcapd init script
- add systemd unit and tmpfiles files

* Wed May 07 2014 Sergey Y. Afonin <asy@altlinux.ru> 1.6.12-alt1
- New version 1.6.12

* Sat Dec 07 2013 Sergey Y. Afonin <asy@altlinux.ru> 1.6.11-alt1
- New version 1.6.11

* Sat Apr 06 2013 Sergey Y. Afonin <asy@altlinux.ru> 1.6.9-alt1
- New version 1.6.9

* Wed Apr 11 2012 Sergey Y. Afonin <asy@altlinux.ru> 1.6.6-alt2
- added %%post_service/%%preun_service
- fixed line for chkconfig in init script
- added lsb init header in init script

* Fri Mar 30 2012 Sergey Y. Afonin <asy@altlinux.ru> 1.6.6-alt1
- New version 1.6.6
- moved nfprofile to separated subpackage

* Tue Nov 08 2011 Sergey Y. Afonin <asy@altlinux.ru> 1.6.4-alt2
- enabled compatibility with data of nfdump 1.5

* Mon Sep 19 2011 Sergey Y. Afonin <asy@altlinux.ru> 1.6.4-alt1
- New version 1.6.4 (ALT #25699)

* Sat Feb 12 2011 Vladimir Lettiev <crux@altlinux.ru> 1.6.3-alt1
- New version 1.6.3

* Sun Sep 12 2010 Vladimir Lettiev <crux@altlinux.ru> 1.6.2-alt1
- New version 1.6.2

* Thu Jun 10 2010 Vladimir Lettiev <crux@altlinux.ru> 1.6.1-alt1
- initial build
