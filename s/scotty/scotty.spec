%def_enable debug
%define tkinedver 1.5.0

Name: scotty
Version: 3.0.0
Release: alt5
Serial: 2

Summary: A Tcl extension to build network management applications
License: BSD
Group: Development/Tcl
Url: http://www.ibr.cs.tu-bs.de/projects/scotty

Source: %name-%version-%release.tar
BuildRequires(pre): rpm-build-tcl
BuildRequires: tk-devel >= 8.5.0 zlib-devel

Requires: tcl >= 8.5.0 nmicmpd

%package tkined
Summary: an interactive network editor for network management applications
Requires: scotty = %serial:%version-%release tk >= 8.5.0
Group: Networking/Other

%package -n nmicmpd
Summary: ICMP echo/mask/timestamp/traceroute server 
Group: System/Servers
PreReq: shadow-utils
Requires: /etc/xinetd.d
Requires: /var/resolv

# {{{ descriptions

%description
Scotty is a Tcl extension to build network management applications
using Tcl (and Tk). The scotty extension provides new Tcl commands to:
 - send and receive ICMP packets
 - query the Domain Name System (DNS)
 - access UDP sockets from Tcl
 - probe and use some selected SUN RPCs
 - retrieve and serve documents via HTTP
 - send and reveice SNMP messages (SNMPv1, SNMPv2USEC, SNMPv2C)
 - write special purpose SNMP agents in Tcl
 - parse and access SNMP MIB definitions
 - schedule jobs that are to be done regularly

%description tkined
Tkined is a network editor which allows to draw maps showing your
network configuration. The most important feature of Tkined is its
programming interface which allows network management applications to
extend the capabilities of Tkined. Most applications for Tkined are
written using scotty.

%description -n nmicmpd
%name is a ICMP echo/mask/timestamp/traceroute server, which can be used
by other programs as well as long as they use the protocol defined in the
nmicmpd(n) man page. This program allows processing of parallel probes
which makes ICMP requests to multiple hosts very efficient.

# }}}

%prep
%setup
 
%build
%add_optflags -Wno-unused
cd unix
autoconf
%configure
%make_build

%install
%makeinstall -C unix
ln -sf scotty%version %buildroot%_bindir/scotty
ln -sf tkined%tkinedver %buildroot%_bindir/tkined
sed -i 's@%buildroot@@' %buildroot%_tcldatadir/*/pkgIndex.tcl
cp -pr %buildroot%_tcldatadir/tnm%version/examples .
rm -rf %buildroot%_tcldatadir/tnm%version/examples
mv unix/README README.unix
mv tnm/changes tnm.changes
mv tkined/changes tkined.changes
install -p -m0640 -D unix/nmicmpd.xinetd %buildroot%_sysconfdir/xinetd.d/nmicmpd

%post -n nmicmpd
/usr/sbin/groupadd -rf nmicmpd
/usr/sbin/useradd -r -g nmicmpd -d /dev/null -s /dev/null -n nmicmpd >/dev/null 2>&1 ||:

%files
%doc README README.unix license.terms tnm.changes examples
%exclude %_sbindir/nmicmpd
%_sbindir/nmtrapd
%_bindir/scotty
%_bindir/scotty%version
%_tcllibdir/tnm%version.so
%_tcldatadir/tnm%version
%_man1dir/scotty.1*
%_man8dir/nmtrapd.8*
%_mandir/mann/*

%files tkined
%doc README README.unix license.terms tkined.changes
%_bindir/tkined
%_bindir/tkined%tkinedver
%_tcllibdir/tkined%tkinedver.so
%_tcldatadir/tkined%tkinedver
%_man1dir/tkined.1*

%files -n nmicmpd
%_sysconfdir/xinetd.d/nmicmpd
%_sbindir/nmicmpd
%_man8dir/nmicmpd.8*

%changelog
* Sun Dec 23 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 2:3.0.0-alt5
- rebuilt against tcl 8.5

* Fri Jun  1 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 2:3.0.0-alt4
- shapshot @ 20070227

* Sat Nov 13 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 2:3.0.0-alt3
- nmicmpd separated to subpackage

* Wed Oct 13 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 2:3.0.0-alt2
- snapshot @ 20041013
- rebuilt with new shiny reqprov finder

* Tue Jun  8 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 2:3.0.0-alt1
- 3.0.0 (snapshot @ 20040608)

* Fri Oct  4 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 2.1.11-alt4
- rebuilt with tcl 8.4

* Sat Jun 15 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 2.1.11-alt3
- rebuilt in new env

* Fri Jan 25 2002 Rider <rider@altlinux.ru> 2.1.11-alt2
- fix bug #348
- BuildReq fix

* Tue Oct 09 2001 Rider <rider@altlinux.ru> 2.1.11-alt1
- 2.1.11

* Fri Aug 17 2001 Rider <rider@altlinux.ru> 2.1.10-alt2
- bugfix (pkgIndex.tcl)

* Fri Aug 17 2001 Rider <rider@altlinux.ru>
- build next CVS version
- fix SNMP-Monitor default variable sync time option
- ssh support in tkined/ip_trouble added

* Fri Jan 19 2001 AEN <aen@logic.ru>
- build cvs for RE

* Wed May 03 2000 Lenny Cartier <lenny@mandrakesoft.com> 2.1.9-2mdk
- fix group
- bzip2 patch

* Tue Feb 29 2000 Lenny Cartier <lenny@mandrakesoft.com>
- used srpm provided by Sandor Takacs <taki@cloud.matav.sulinet.hu>
- fixed the files section
- bzip2 archive

