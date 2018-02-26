%define cvs 0

%define	quagga_user	quagga
%define	quagga_gid	quagga
%define	vty_gid		quaggavty

Name: quagga

%define baseversion 0.99.20.1
Release: alt2

%if %cvs
%define cvsdate 20060505
Version: %baseversion.%cvsdate
%define quaggadir %name-%baseversion
%else
Version: %baseversion
%define quaggadir %name-%version
%endif

Packager: Sergey Y. Afonin <asy@altlinux.ru>

Summary: Quagga routing suite (a fork of the GNU Zebra)

License: %gpl2only
Group: Networking/Other
Url: http://www.quagga.net/

%if %cvs
Source0:	%name-%baseversion-%cvsdate.tar.gz
%else
Source0:	%name-%version.tar.bz2
%endif
Source1:	%name.logrotate
Source2:	%name.pam
Source3:	%name.sysconfig

Source10:	%name-zebra.init
Source11:	%name-ripd.init
Source12:	%name-ripngd.init
Source13:	%name-ospfd.init
Source14:	%name-ospf6d.init
Source15:	%name-bgpd.init
Source16:	%name-isisd.init

Source19:	%name-watchquagga.init

Source20:	%name-zebra.conf
Source21:	%name-ripd.conf
Source22:	%name-ripngd.conf
Source23:	%name-ospfd.conf
Source24:	%name-ospf6d.conf
Source25:	%name-bgpd.conf
Source26:	%name-isisd.conf

Patch1:		quagga-libzebra_to_libospf.patch
Patch2:		quagga-libospf_to_libospfclient.patch
Patch3:    	quagga-man.patch

#Errata
Patch1001: quagga-0.99.20-dryrun.patch
Patch1002: quagga-CVE-2012-1820-790d1e263e8800bc49d0038d481591ecb4e37b88.patch

Conflicts:	zebra

Requires:	libquagga = %{version}-%{release}

BuildRequires:	/proc
BuildRequires: rpm-build-licenses

BuildRequires: gcc-c++ libcap-devel libpam-devel libpcap-devel libreadline-devel libtinfo-devel libnet-snmp-devel texi2html

%description
Quagga is a free software that manages TCP/IP based routing protocol.
It takes multi-server and multi-thread approach to resolve the current
complexity of the Internet.

Quagga supports BGP4, BGP4+, OSPFv2, OSPFv3, RIPv1, RIPv2, RIPng,
                IS-SI and MPLS-VPN.

Quagga is intended to be used as a Route Server and a Route Reflector. It is
not a toolkit, it provides full routing power under a new architecture.
Quagga by design has a process for each protocol.

Quagga is a fork of the GNU Zebra (forked after 2002-07-07).

%package -n libquagga
Summary: Quagga shared library.
Copyright: %lgpl2only
Group: System/Libraries

%description -n libquagga
The runtime library of Quagga

%package devel
Summary: Header and object files for Quagga development
Group: Development/C
Requires: libquagga = %{version}-%{release}

%description devel
The quagga-devel package contains the header and object files neccessary for
developing OSPF-API and quagga applications.

%package tools
Summary: Quagga tools (zc.pl only)
Copyright: %gpl2only
Group: System/Configuration/Other
BuildRequires: perl-Net-Telnet
BuildArch: noarch

%description tools
Quagga tools
zc.pl: Zebra interactive console

%package ospfclient
Summary: Simple program to demonstrate how OSPF API can be used.
Copyright: %gpl2only
Group: Development/Other
Requires: libquagga = %{version}-%{release}

%description ospfclient
This application retrieves the LSDB from the OSPF daemon and thenoriginates,
updates and finally deletes an application-specificopaque LSA. You can use
this application as a template when writingyour own application.

%package doc
Summary: Quagga documentation
Copyright: %gpl2only
Group: Development/Other
BuildArch: noarch

%description doc
Quagga documentation

%prep

%setup -q -n %quaggadir

# disabled quagga-libzebra_to_libospf.patch and quagga-libospf_to_libospfclient.patch
# (/usr/bin/ld: cannot find -lzebra in hasher build)

#patch1 -p1
#patch2 -p1
%patch3 -p0

#Errata
%patch1001 -p1
%patch1002 -p1

#verify-elf: WARNING: ./usr/lib/libzebra.so.0.0.0: undefined symbol: master
#verify-elf: WARNING: ./usr/lib/libospf.so.0.0.0: undefined symbol: ospfd_privs
#verify-elf: WARNING: ./usr/lib/libospf.so.0.0.0: undefined symbol: master
#
# master in sbin/zebra
# ospfd_privs in sbin/ospfclient
#
%set_verify_elf_method unresolved=relaxed
#export LDFLAGS="$LDFLAGS -Wl,--no-as-needed"

%build

#undefine __libtoolize

# fixed libraries path in RPATH (on x86_64)
%autoreconf

export LIBS="-lcap"

export IPFORWARD=ipforward_proc.o; export zebra_ipforward_path=proc; %configure \
	--enable-ipv6 \
	--enable-multipath=32 \
	--enable-tcp-zebra \
	--enable-nssa \
	--enable-opaque-lsa \
	--enable-ospf-te \
	--enable-vtysh \
	--enable-ospfclient=yes \
	--enable-ospfapi=yes \
	--enable-irdp=yes \
	--enable-isisd \
	--with-libpam \
	--enable-user=%quagga_user \
	--enable-group=%quagga_gid \
	--enable-vty-group=%vty_gid \
	--enable-netlink --enable-gcc-rdynamic \
	--sysconfdir=%_sysconfdir/%name \
	--localstatedir=%_localstatedir/%name

%make

pushd doc
texi2html -number quagga.texi
popd

%install

install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig,logrotate.d,pam.d} \
        $RPM_BUILD_ROOT%_logdir/%name $RPM_BUILD_ROOT%_infodir \
	$RPM_BUILD_ROOT%_localstatedir/%name 

make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%_libdir/lib*.a
rm -f $RPM_BUILD_ROOT%_sysconfdir/%name/*.sample*

install -m 644 %SOURCE1 $RPM_BUILD_ROOT%_sysconfdir/logrotate.d/%name
install -m 644 %SOURCE2 $RPM_BUILD_ROOT%_sysconfdir/pam.d/%name
install -m 644 %SOURCE3 $RPM_BUILD_ROOT%_sysconfdir/sysconfig/%name

install %SOURCE20 $RPM_BUILD_ROOT%_sysconfdir/%name/zebra.conf
install %SOURCE21 $RPM_BUILD_ROOT%_sysconfdir/%name/ripd.conf
install %SOURCE22 $RPM_BUILD_ROOT%_sysconfdir/%name/ripngd.conf
install %SOURCE23 $RPM_BUILD_ROOT%_sysconfdir/%name/ospfd.conf
install %SOURCE24 $RPM_BUILD_ROOT%_sysconfdir/%name/ospf6d.conf
install %SOURCE25 $RPM_BUILD_ROOT%_sysconfdir/%name/bgpd.conf
install %SOURCE26 $RPM_BUILD_ROOT%_sysconfdir/%name/isisd.conf

install -m 755 %SOURCE10 $RPM_BUILD_ROOT%_initdir/zebra
install -m 755 %SOURCE11 $RPM_BUILD_ROOT%_initdir/ripd
install -m 755 %SOURCE12 $RPM_BUILD_ROOT%_initdir/ripngd
install -m 755 %SOURCE13 $RPM_BUILD_ROOT%_initdir/ospfd
install -m 755 %SOURCE14 $RPM_BUILD_ROOT%_initdir/ospf6d
install -m 755 %SOURCE15 $RPM_BUILD_ROOT%_initdir/bgpd
install -m 755 %SOURCE16 $RPM_BUILD_ROOT%_initdir/isisd

install -m 755 %SOURCE19 $RPM_BUILD_ROOT%_initdir/watchquagga

cp -f tools/zc.pl $RPM_BUILD_ROOT%_bindir

%pre
/usr/sbin/groupadd -rf %quagga_gid
/usr/sbin/useradd -r -g %quagga_gid -d /dev/null -s /dev/null -n %quagga_user &>/dev/null ||:

/usr/sbin/groupadd -rf %vty_gid

%post
# "&>/dev/null" used for restarting when connection lost
{
%post_service zebra
%post_service ripd
%post_service ospfd
%post_service ospf6d
%post_service ripngd
%post_service bgpd
%post_service isisd
%post_service watchquagga
} &>/dev/null

%preun
%preun_service watchquagga
%preun_service ripd
%preun_service ospfd
%preun_service ospf6d
%preun_service ripngd
%preun_service bgpd
%preun_service isisd
%preun_service zebra

%files
%attr(3750,root,%quagga_gid) %dir %_sysconfdir/%name
%attr(3775,root,%quagga_gid) %dir %_localstatedir/%name
%attr(3770,root,%quagga_gid) %dir %_logdir/%name

%config %_initdir/*
%config(noreplace) %attr(0660, root, %quagga_gid) %_sysconfdir/%name/*
%config(noreplace) %_sysconfdir/logrotate.d/%name
%config %_sysconfdir/pam.d/%name
%config %_sysconfdir/sysconfig/%name

%exclude %_bindir/zc.pl
%_bindir/*
%exclude %_sbindir/ospfclient
%_sbindir/*

%_mandir/man?/*
%doc AUTHORS README SERVICES NEWS

%files -n libquagga
%_libdir/lib*.so.*

%files devel
%_libdir/lib*.so
%dir %_includedir/%name
%dir %_includedir/%name/ospfd
%dir %_includedir/%name/ospfapi
%_includedir/%name/*.h
%_includedir/%name/ospfd/*.h
%_includedir/%name/ospfapi/*.h

%files tools
%_bindir/zc.pl

%files ospfclient
%_sbindir/ospfclient

%files doc
%_infodir/*
%doc tools ChangeLog INSTALL TODO
%doc doc/quagga.html
%doc */*.sample*
%doc doc/mpls
%doc bgpd/BGP4-MIB.txt ospfd/OSPF-MIB.txt ospfd/OSPF-TRAP-MIB.txt
%doc ripd/RIPv2-MIB.txt zebra/GNOME-PRODUCT-ZEBRA-MIB zebra/GNOME-SMI
%doc doc/draft-zebra-00.* doc/BGP-TypeCode

%changelog
* Wed Jun 06 2012 Sergey Y. Afonin <asy@altlinux.ru> 0.99.20.1-alt2
- added patch for CVE-2012-1820

* Wed Mar 14 2012 Sergey Y. Afonin <asy@altlinux.ru> 0.99.20.1-alt1
- new version (CVE-2012-0249, CVE-2012-0250, CVE-2012-0255)

* Thu Oct 13 2011 Sergey Y. Afonin <asy@altlinux.ru> 0.99.20-alt2
- attempted to fix Quagga Bug #622 (previous fix broke listen on
  port 179)

* Fri Sep 30 2011 Sergey Y. Afonin <asy@altlinux.ru> 0.99.20-alt1
- new version (patch for CVE-2011-3325 fully included)
- attempted to fix Quagga Bug #622 (bgpd --dryrun)
- splitted "restart" and "reload" in init scripts of routing daemons

* Tue Sep 27 2011 Sergey Y. Afonin <asy@altlinux.ru> 0.99.19-alt1
- new version (CVE-2011-3325 still partialy fixed)

* Mon Sep 26 2011 Sergey Y. Afonin <asy@altlinux.ru> 0.99.18-alt2
- security update
  (CVE-2011-3323, CVE-2011-3324, CVE-2011-3326, CVE-2011-3327;
   CVE-2011-3325 partialy fixed: quagga-master-514838.2.patch
   ignored because ospfd crashed with it)

* Fri Jun 03 2011 Sergey Y. Afonin <asy@altlinux.ru> 0.99.18-alt1
- new version (CVE-2010-1674, CVE-2010-1675)

* Thu Sep 23 2010 Sergey Y. Afonin <asy@altlinux.ru> 0.99.17-alt1
- new version
- added checking of configs when restarting services
- configurable permissions for /etc/quagga (ALT #23467)

* Mon Mar 22 2010 Sergey Y. Afonin <asy@altlinux.ru> 0.99.16-alt1
- new version

* Fri Dec 25 2009 Sergey Y. Afonin <asy@altlinux.ru> 0.99.15-alt3
- Removed Prereq: /sbin/install-info
- Removed runlevels list from start/stop sections of lsb init header
  in init-scripts

* Tue Oct 13 2009 Sergey Y. Afonin <asy@altlinux.ru> 0.99.15-alt2
- Changed tetex-core to texi2html in BuildRequires
- Removed %%__ macroses
- Changed Group of package and subpackages

* Mon Aug 31 2009 Sergey Y. Afonin <asy@altlinux.ru> 0.99.15-alt1
- new version

* Fri Jul 24 2009 Sergey Y. Afonin <asy@altlinux.ru> 0.99.14-alt1
- new version (1.0.0 Release Candidate 1)

* Fri Jun 26 2009 Sergey Y. Afonin <asy@altlinux.ru> 0.99.13-alt1
- new version

* Wed May 06 2009 Sergey Y. Afonin <asy@altlinux.ru> 0.99.11-alt4
- updated 4-byte-ASN patch (ALT #19849)
  http://lists.quagga.net/pipermail/quagga-dev/2009-April/006541.html

* Tue Nov 18 2008 Sergey Y. Afonin <asy@altlinux.ru> 0.99.11-alt3
- fixed bgpd crash on long asn32 in aspath (ALT #19849)
  http://lists.quagga.net/pipermail/quagga-dev/2009-February/006396.html
- added "BuildArch: noarch" for doc and tools packages again

* Fri Nov 14 2008 Sergey Y. Afonin <asy@altlinux.ru> 0.99.11-alt2
- removed ldconfig calling due to new rpm
- fixed fletcher checksum error by
  Joakim Tjernlund <joakim.tjernlund#transmode.se>

* Fri Oct 17 2008 Sergey Y. Afonin <asy@altlinux.ru> 0.99.11-alt1
- new version
- "BuildArch: noarch" for tools and doc packages
- moved "ospfclient" to separate package

* Mon Jun 30 2008 Sergey Y. Afonin <asy@altlinux.ru> 0.99.10-alt0
- new version
  bgpd: 4-Byte AS Number support (RFC4893)
- removed patchset from Denis Ovsienko (all in mainstream now)

* Tue Nov 13 2007 Sergey Y. Afonin <asy@altlinux.ru> 0.99.9-alt4
- added patchset from Denis Ovsienko <pilot@altlinux>
  patch 10

* Mon Nov 05 2007 Sergey Y. Afonin <asy@altlinux.ru> 0.99.9-alt3
- added patchset from Denis Ovsienko <pilot@altlinux>
  patches 6-9

* Wed Sep 19 2007 Sergey Y. Afonin <asy@altlinux.ru> 0.99.9-alt2
- added patchset from Denis Ovsienko <pilot@altlinux>
  patches 1-5

* Thu Sep 13 2007 Sergey Y. Afonin <asy@altlinux.ru> 0.99.9-alt1
- new version, security fix
  (Multiple Denial of Service Vulnerabilities, SA26744)

* Fri Aug 10 2007 Sergey Y. Afonin <asy@altlinux.ru> 0.99.8-alt3
- fixed --expect-user for watchquagga (changed to root)

* Tue Aug 07 2007 Sergey Y. Afonin <asy@altlinux.ru> 0.99.8-alt2
- fixed ALT #12440 (quagga system is built without libcap support)
- fixed calling of %%post_service in remote session
- added watchquagga's init script to binary package

* Thu Aug 02 2007 Sergey Y. Afonin <asy@altlinux.ru> 0.99.8-alt1
- new version
- fixed ALT #12437 (Severe typo in %%post/%%preun scripts in quagga-doc)
- fixed ALT #12438 (Wrong references in manual pages)

* Wed May 16 2007 Sergey Y. Afonin <asy@altlinux.ru> 0.99.7-alt1
- new version (CVE-2007-1995, the bgpd daemon is vulnerable to a
  Denial-of-Service)

* Thu Apr 05 2007 Sergey Y. Afonin <asy@altlinux.ru> 0.99.6-alt3
- moved "-s 1024000" to sysconfig/quagga

* Sat Mar 24 2007 Sergey Y. Afonin <asy@altlinux.ru> 0.99.6-alt2
- added "-s 1024000" to zebra init
  (http://lists.quagga.net/pipermail/quagga-users/2006-March/006686.html
   ZEBRA: netlink-listen recvmsg overrun: No buffer space available)

* Sat Dec 16 2006 Sergey Y. Afonin <asy@altlinux.ru> 0.99.6-alt1
- new version

* Tue Oct 03 2006 Sergey Y. Afonin <asy@altlinux.ru> 0.99.5-alt1
- new version
- changed: remove --disable-snmp (ALT #9217)

* Mon May 08 2006 Sergey Y. Afonin <asy@altlinux.ru> 0.99.3.20060505-alt1
- new cvs (ripd secutity fix and some other changes)
- fixed: add isisd init script to binary package
- changed: remove (noreplace) for init scripts
- changed: disable quagga-libzebra_to_libospf.patch and
  quagga-libospf_to_libospfclient.patch
  (/usr/bin/ld: cannot find -lzebra in hasher build)

* Mon Mar 20 2006 Sergey Y. Afonin <asy@altlinux.ru> 0.99.3-alt5
- add: quagga-libzebra_to_libospf.patch and
  quagga-libospf_to_libospfclient.patch

* Thu Mar 09 2006 Sergey Y. Afonin <asy@altlinux.ru> 0.99.3-alt4
- changed: --disable-snmp (ALT #9217)
- changed: add %%set_verify_elf_method unresolved=relaxed
  (libzebra.so: undefined symbol "master" in sbin/zebra)

* Thu Mar 09 2006 Sergey Y. Afonin <asy@altlinux.ru> 0.99.3-alt3
- added: export IPFORWARD=ipforward_proc.o; export zebra_ipforward_path=proc;
  for build for linux without /proc

* Sun Mar 05 2006 Sergey Y. Afonin <asy@altlinux.ru> 0.99.3-alt2
- fixed: change PID file location to /var/lib/quagga in quagga.logrotate
  and init scripts

* Thu Mar 02 2006 Sergey Y. Afonin <asy@altlinux.ru> 0.99.3-alt1
- Initial build for AltLinux 
  (used some ALT specific files from zebra-0.95-alt2)
