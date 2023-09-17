%def_disable static

Name: ipmiutil
Version: 3.1.9
Release: alt1

Summary: IPMI server management utilities
License: BSD
Group: System/Kernel and hardware

Url: http://ipmiutil.sf.net
Source: http://prdownloads.sf.net/ipmiutil/%name-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
# optimized out: libstdc++-devel
BuildRequires: gcc-c++ libssl-devel openssl

%add_findreq_skiplist %_datadir/%name/*

%description
The ipmiutil component package provides utilities to view the SEL
(showsel), perform a hardware reset (hwreset), set up the BMC LAN
and Platform Event Filter entry to allow SNMP alerts (pefconfig),
and other IPMI tasks.  These can be invoked with the metacommand,
ipmiutil, as well.  Man pages are provided.

An IPMI driver can be provided by either the Intel IPMI driver
(/dev/imb) or the OpenIPMI driver (/dev/ipmi0).  If used locally
and no driver is detected, ipmiutil will use user-space register
I/Os instead.

%package -n lib%name
Group: System/Libraries
Summary:  Includes libraries and headers for the ipmiutil package

%description -n lib%name
The package contains libraries which are
useful for building custom IPMI applications.

%package -n lib%name-devel
Group: Development/C
Summary:  Includes libraries and headers for the ipmiutil package
Requires: lib%name = %EVR

%description -n lib%name-devel
The ipmiutil-devel package contains headers and libraries which are
useful for building custom IPMI applications.

%package -n lib%name-devel-static
Group: Development/C
Summary:  Includes static libraries for the ipmiutil package
Requires: lib%name-devel = %EVR

%description -n lib%name-devel-static
The ipmiutil-static package contains static libraries which are
useful for building custom IPMI applications.

%package cronjob
Summary: A periodic job to syslog and clear SEL records
Group: Monitoring
BuildArch: noarch

%description cronjob
This package contains a daily cron script which runs ipmiutil sel,
writing any new records to syslog, and will then clear the SEL
if free space is low.

The IPMI SEL should not normally be cleared, because the history
of the events is important, but if the IPMI SEL fills up, no new
events are logged, so saving the previous SEL events and clearing
the SEL must be done occasionally, as needed.

%prep
%setup
# Makefile uses the TMPDIR environment variable, the same is used
# by the Elbrus compiler to set the directory for temporary files.
sed -i "s|TMPDIR|TMPDIR1|g" Makefile*

%build
./beforeconf.sh
%configure --enable-gpl %{subst_enable static}
#make_build
# SMP incompatible build, see #27254 (2 shaba: still true as of 2022)
make

%install
%makeinstall_std
install -pDm755 scripts/checksel %buildroot%_sysconfdir/cron.daily/checksel
install -dm700 %buildroot%_localstatedir/%name
# configure is broken with --disable-static
%if_disabled static
rm -v %buildroot%_libdir/*.a
%endif

%files
%_bindir/*
%_sbindir/*
%_man8dir/*
%attr(700,root,root) %_localstatedir/%name/

%files -n lib%name
%_libdir/libipmiutil.so.*

%files -n lib%name-devel
%_datadir/%name
%_libdir/libipmiutil.so
%_includedir/ipmicmd.h

%if_enabled static
%files -n lib%name-devel-static
%_libdir/libipmiutil.a
%endif

%files cronjob
%_sysconfdir/cron.daily/checksel

%changelog
* Sun Sep 17 2023 Arseny Maslennikov <arseny@altlinux.org> 3.1.9-alt1
- 3.1.3 -> 3.1.9.

* Sat Oct 08 2022 Michael Shigorin <mike@altlinux.org> 3.1.3-alt4
- *disable* parallel build: it's still broken (the same #27254)

* Tue Sep 21 2021 Vitaly Lipatov <lav@altlinux.ru> 3.1.3-alt3
- disable devel-static subpackage

* Thu Jul 08 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 3.1.3-alt2
- fixed Elbrus build

* Tue Oct 02 2018 Alexey Shabalin <shaba@altlinux.org> 3.1.3-alt1
- 3.1.3
- add packages: libipmiutils, devel, static

* Thu Nov 27 2014 Michael Shigorin <mike@altlinux.org> 2.8.3-alt2
- added %_localstatedir/%name (closes: #30515)

* Sun May 06 2012 Michael Shigorin <mike@altlinux.org> 2.8.3-alt1
- 2.8.3
- single-threaded build (closes: #27254)
- despammed Summary:

* Sat Apr 21 2012 Michael Shigorin <mike@altlinux.org> 2.8.2-alt1
- 2.8.2
  + install checksel cronjob by hand (stupid RH#752319)
  + NB: some utils moved from %_sbindir to %_bindir

* Sun Oct 09 2011 Michael Shigorin <mike@altlinux.org> 2.7.9-alt2
- cronjob subpackage made noarch

* Sat Oct 08 2011 Michael Shigorin <mike@altlinux.org> 2.7.9-alt1
- 2.7.9
- introduced cronjob subpackage
- spec cleanup

* Wed May 13 2009 Pavlov Konstantin <thresh@altlinux.ru> 2.3.7-alt1
- 2.3.7 release.
- Remove libraries subpackages as they don't exist anymore.

* Tue Nov 06 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.0.3-alt1
- 2.0.3 release.

* Fri Jul 13 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.9.8-alt2
- Fix %%files, added libraries subpackages.

* Wed Jul 11 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.9.8-alt1
- Initial build for ALT Linux.

