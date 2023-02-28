%define abiversion 40
%define _name net-snmp
%def_disable mibs
%def_with mysql
%def_with systemd
# XXX tests fail
%def_without test

Name: %_name%abiversion
Version: 5.9.3
Release: alt1

Summary: Tools and servers for the SNMP protocol
License: BSD-like
Group: System/Servers
Url: http://net-snmp.sourceforge.net

Source0: %name-%version.tar
#git clone git://net-snmp.git.sourceforge.net/gitroot/net-snmp/net-snmp
Source1: %_name.init
Source2: %_name.conf
Source3: %_name.logrotate
Source4: snmptrapd.init
Source5: net-snmpd.sysconfig
Source6: net-snmptrapd.sysconfig
Source7: net-snmp-tmpfs.conf
Source8: snmpd.service
Source9: snmptrapd.service

Patch: %name-%version-%release.patch

# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %_var
%define persistentdir %_var/lib/%_name

%def_enable static
BuildRequires: librpm-devel >= 4.0.4 libssl-devel
# Automatically added by buildreq on Wed Oct 13 2010
BuildRequires: libnl-devel librpm-devel libsensors3-devel pdksh perl-devel python3-module-setuptools perl-Tk perl-Term-ReadLine-Gnu perl-libnet perl-XML-Simple perl-JSON perl-Mail-Sender
%{?_enable_static:BuildRequires: glibc-devel-static}
%{?_with_mysql:BuildRequires: libmysqlclient-devel}
%{?_with_systemd:BuildRequires: systemd-devel}
BuildRequires: perl-podlators chrpath

%package -n %_name-common
Summary: Common dirs and files for the SNMP protocol
Group: System/Servers
BuildArch: noarch
Requires: snmp-mibs-std
%if_enabled mibs
Requires: %_name-mibs = %version-%release
%endif

%package -n %_name
Summary: Virtual package for install snmpd server and clients of the SNMP protocol
Group: System/Servers
BuildArch: noarch
Requires: %_name-snmpd %_name-snmptrapd %_name-clients

%package -n %_name-snmpd
Summary: Snmpd server for the SNMP protocol
Group: System/Servers
Requires: lib%_name = %version-%release %_name-common
Obsoletes: cmu-snmp ucd-snmp

%package -n %_name-snmptrapd
Summary: Snmptrapd and server for the SNMP protocol
Group: System/Servers
Requires: lib%_name = %version-%release %_name-common
Obsoletes: cmu-snmp ucd-snmp

%package -n %_name-clients
Summary: Tools for use SNMP, from the Net-SNMP project
Group: Networking/Other
Requires: lib%_name = %version-%release %_name-common

%package -n %_name-utils
Summary: Network management utilities using SNMP, from the Net-SNMP project
Group: Networking/Other
BuildArch: noarch
Requires: lib%_name = %version-%release %_name-common perl-SNMP
Obsoletes: cmu-snmp-utils ucd-snmp-utils

%package -n %_name-bridge-mib
Summary: Provide Linux bridge information via SNMP
Group: Networking/Other
BuildArch: noarch
Requires: %_name-snmpd

%package -n %_name-cert
Summary: Creates, signs, installs and displays X.509 certificates used in the operation of Net-SNMP/(D)TLS
Group: Networking/Other
BuildArch: noarch
Requires: %_name-common

%package -n lib%name
Summary: The shared libraries for the Net-SNMP project
Group: System/Libraries
Provides: lib%_name = %version-%release

%package -n lib%name-agent
Summary: The shared agent libraries for the Net-SNMP project
Group: System/Libraries
Provides: lib%_name-agent = %version-%release
Provides: lib%name-snmptrapd = %version-%release
Provides: lib%_name-snmptrapd = %version-%release
Obsoletes: lib%name-snmptrapd < %version-%release
Obsoletes: lib%_name-snmptrapd < %version-%release

%package -n lib%_name-devel
Summary: The development environment for the Net-SNMP project
Group: Development/C
Requires: lib%_name = %version-%release lib%_name-agent = %version-%release %_name-common
Provides: lib%name-devel = %version-%release
Requires: libssl-devel libsensors3-devel libnl-devel

%package -n lib%_name-devel-static
Summary: static libraries for lib%_name
Group: Development/C
Requires: lib%_name-devel = %version-%release

%if_enabled mibs
%package -n %_name-mibs
Summary: MIB files from the Net-SNMP project
Group: Networking/Other
%endif

%package -n perl-SNMP
Summary: Perl SNMP Extension Module
Group: Development/Perl
Requires: lib%_name = %version-%release %_name-common

%package -n python3-module-netsnmp
Summary: Python SNMP Extension Module
Group: Development/Python3
Requires: lib%_name = %version-%release

%description
SNMP (Simple Network Management Protocol) is a protocol used for network
management (hence the name).  The Net-SNMP project includes various SNMP
tools; an extensible agent, an SNMP library, tools for requesting or
setting information from SNMP agents, tools for generating and handling
SNMP traps, a version of the netstat command which uses SNMP, and a
Tk/Perl mib browser.  This package contains the snmpd and snmptrapd
daemons, documentation, etc.

Install the %_name package if you need network management tools.
You will probably also want to install the %_name-utils package, which
contains Net-SNMP utilities.

%description -n %_name-common
SNMP (Simple Network Management Protocol) is a protocol used for network
management (hence the name).  The Net-SNMP project includes various SNMP
tools; an extensible agent, an SNMP library, tools for requesting or
setting information from SNMP agents, tools for generating and handling
SNMP traps, a version of the netstat command which uses SNMP, and a
Tk/Perl mib browser.  This package contains the snmpd and snmptrapd
daemons, documentation, etc.

%_name-common package contain common files and dirs

%description -n %_name
SNMP (Simple Network Management Protocol) is a protocol used for network
management (hence the name).  The Net-SNMP project includes various SNMP
tools; an extensible agent, an SNMP library, tools for requesting or
setting information from SNMP agents, tools for generating and handling
SNMP traps, a version of the netstat command which uses SNMP, and a
Tk/Perl mib browser.  This package contains the snmpd and snmptrapd
daemons, documentation, etc.

%_name is virtual package for quick install %_name-snmpd %_name-snmptrapd %_name-clients

%description -n %_name-snmpd
SNMP (Simple Network Management Protocol) is a protocol used for network
management (hence the name).  The Net-SNMP project includes various SNMP
tools; an extensible agent, an SNMP library, tools for requesting or
setting information from SNMP agents, tools for generating and handling
SNMP traps, a version of the netstat command which uses SNMP, and a
Tk/Perl mib browser.  This package contains the snmpd and snmptrapd
daemons, documentation, etc.

%_name-snmpd package contain snmpd server

%description -n %_name-snmptrapd
SNMP (Simple Network Management Protocol) is a protocol used for network
management (hence the name).  The Net-SNMP project includes various SNMP
tools; an extensible agent, an SNMP library, tools for requesting or
setting information from SNMP agents, tools for generating and handling
SNMP traps, a version of the netstat command which uses SNMP, and a
Tk/Perl mib browser.  This package contains the snmpd and snmptrapd
daemons, documentation, etc.

%_name-snmptrapd package contain snmptrapd server

%description -n %_name-clients
The %_name-clients package contains various tools for use with the
Net-SNMP network management project.

Install this package if you need utilities for managing your network
using the SNMP protocol.

%description -n %_name-utils
The %_name-utils package contains various utilities for use with the
Net-SNMP network management project.

Install this package if you need utilities for managing your network
using the SNMP protocol.

%description -n %_name-bridge-mib
Provide Linux bridge information via SNMP

%description -n %_name-cert
net-snmp-cert creates, signs, installs and displays X.509
certificates used in the operation of Net-SNMP/(D)TLS

%description -n lib%name
The lib%_name package contains the shared libraries required for
Net-SNMP software.

%description -n lib%name-agent
The lib%name-agent package contains the shared agent libraries required for
Net-SNMP software.

%description -n lib%_name-devel
This package contains include files required for development
applications for use with the Net-SNMP project's network management
tools. You'll also need to have the lib%_name and %_name-utils packages
installed.

%description -n lib%_name-devel-static
This package contains static libraries required for development
statically linked applications for use with the Net-SNMP project's
network management tools. You'll also need to have the lib%_name-devel
package installed.


%if_enabled mibs
%description -n %_name-mibs
The %_name package contains various MIB files for use with the
Net-SNMP network management project.
%endif

%description -n perl-SNMP
This is the Perl 'SNMP' extension module. The SNMP module provides
a full featured, tri-lingual SNMP (SNMPv3, SNMPv2c, SNMPv1) API.
The SNMP module also provides an interface to the SMI MIB parse-tree
for run-time access to parsed MIB data.

%description -n python3-module-netsnmp
This is the Python 'SNMP' extension module. The SNMP module provides
a full featured, tri-lingual SNMP (SNMPv3, SNMPv2c, SNMPv1) API.
The SNMP module also provides an interface to the SMI MIB parse-tree
for run-time access to parsed MIB data.

%prep
%setup
%patch -p1

%build
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%autoreconf
#export NETSNMP_DONT_CHECK_VERSION=1
#export LIBS='-lcrypto'

MIBS="host agentx smux \
     ucd-snmp/diskio tcp-mib udp-mib mibII/mta_sendmail \
     ip-mib/ipv4InterfaceTable ip-mib/ipv6InterfaceTable \
     ip-mib/ipAddressPrefixTable/ipAddressPrefixTable \
     ip-mib/ipDefaultRouterTable/ipDefaultRouterTable \
     ip-mib/ipv6ScopeZoneIndexTable ip-mib/ipIfStatsTable \
     sctp-mib rmon-mib etherlike-mib"

%ifnarch s390 s390x ppc64le
# there are no lm_sensors on s390
MIBS="$MIBS ucd-snmp/lmsensorsMib"
%endif

%configure %{subst_enable static} \
	--with-defaults \
	--enable-shared \
	--enable-as-needed \
	--enable-blumenthal-aes \
	--enable-embedded-perl \
	--enable-ipv6 \
	--enable-local-smux \
	--enable-mfd-rewrites \
	--enable-ucd-snmp-compatibility \
	--with-sys-location="Unknown" \
	--with-sys-contact="root@localhost" \
	--with-logfile="/var/log/snmpd.log" \
	--with-mib-modules="$MIBS" \
	--with-mibdirs="%_datadir/snmp/mibs:%_datadir/mibs/net-snmp:%_datadir/mibs/iana:%_datadir/mibs/ietf:%_datadir/mibs/tubs:%_datadir/mibs/cisco:%_datadir/pibs/ietf:%_datadir/pibs/tubs:" \
	--with-persistent-directory="%persistentdir" \
	--with-temp-file-pattern=/run/net-snmp/snmp-tmp-XXXXXX \
	--without-root-access \
	--without-rpm \
	--with-openssl \
	--with-zlib \
	--with-nl \
	--with-security-modules=tsm \
	--with-transports="TLSTCP DTLSUDP" \
	--with-perl-modules="INSTALLDIRS=vendor" \
	--with-python-modules \
	--without-pcre \
	%{subst_with mysql} \
	%{subst_with systemd}

# non-SMP-safe build
make
rm -f `find ./ -name 'libnetsnmpagent*'`
%make ADD_HELPER="-L$PWD/agent/helpers/.libs -lnetsnmphelpers"


%install
# DO NOT replace with %%makeinstall_std: breaks build
# (libnetsnmp.so.30 gets built but not installed)
%make DESTDIR=%buildroot install

mkdir -p %buildroot%_initdir
mkdir -p %buildroot%_sysconfdir/sysconfig
mkdir -p %buildroot%persistentdir
mkdir -p %buildroot%_defaultdocdir/perl-SNMP-%version

install -p -m755 -D %SOURCE1 %buildroot%_initdir/snmpd
install -p -m640 -D %SOURCE2 %buildroot%_sysconfdir/snmp/snmpd.conf
install -p -m644 -D %SOURCE3 %buildroot%_sysconfdir/logrotate.d/snmpd
install -p -m755 -D %SOURCE4 %buildroot%_initdir/snmptrapd
install -p -m644 -D %SOURCE5 %buildroot%_sysconfdir/sysconfig/snmpd
install -p -m644 -D %SOURCE6 %buildroot%_sysconfdir/sysconfig/snmptrapd


# systemd stuff
install -m 755 -d %buildroot%_tmpfilesdir
install -m 644 %SOURCE7 %buildroot%_tmpfilesdir/net-snmp.conf
install -m 755 -d %buildroot%_unitdir
install -m 644 %SOURCE8 %SOURCE9 %buildroot%_unitdir/

# perl loadable objects contain $RPM_BUILD_DIR-dependent RPATH
#hrpath -d `find %buildroot%perl_vendor_autolib -type f -name '*.so'`

xz ChangeLog

#Fix net-snmp-create-v3-user
sed -i "s|ps -acx|ps acx|g" %buildroot%_bindir/net-snmp-create-v3-user
sed -i "s|/usr/share/snmp/snmpd.conf|%_sysconfdir/snmp/snmpd.conf|g" %buildroot%_bindir/net-snmp-create-v3-user


find %buildroot%_datadir/snmp/mibs/ -name "*.txt" -type f | while read file; do mv "$file" "${file%%.txt}"; done

#tar MIBS for simple update
tar -cjf net-snmp-mibs.tar.bz2 -C %buildroot%_datadir/snmp mibs/
rm -rf %buildroot%_datadir/snmp/mibs

#Fix rpath
find %buildroot%perl_vendor_autolib/SNMP -type f -name *.so -print0 | xargs -r0 chrpath -d
find %buildroot%perl_vendor_autolib/NetSNMP -type f -name *.so -print0 | xargs -r0 chrpath -d

# remove things we don't want to distribute
rm -f %buildroot%_bindir/snmpinform
ln -s snmptrap %buildroot%_bindir/snmpinform
rm -f %buildroot%_bindir/snmpcheck
rm -f %buildroot%_bindir/fixproc
rm -f %buildroot%_mandir/man1/fixproc*
rm -f %buildroot%_bindir/ipf-mod.pl
rm -f %buildroot%_libdir/*.la
rm -f %buildroot%_libdir/libsnmp*

# remove special perl files
find %buildroot -name perllocal.pod \
    -o -name .packlist \
    -o -name "*.bs" \
    -o -name Makefile.subs.pl \
    | xargs -ri rm -f {}

%check
%ifarch ppc64le
rm -vf testing/fulltests/default/T200snmpv2cwalkall_simple
%endif
chmod 755 local/passtest

echo "===== start test ====="
LD_LIBRARY_PATH=%buildroot/%_libdir %make test

%pre -n %_name-common
%_sbindir/groupadd -r -f snmp &>/dev/null
%_sbindir/useradd -r -g snmp -d /dev/null -s /dev/null \
        -c "SNMP pseudo user" -M -n snmp &>/dev/null ||:
%_sbindir/usermod -g proc snmp &>/dev/null ||:

%post -n %_name-snmpd
%post_service snmpd

%post -n %_name-snmptrapd
%post_service snmptrapd

%preun -n %_name-snmpd
%preun_service snmpd

%preun -n %_name-snmptrapd
%preun_service snmptrapd

%files -n %_name

%files -n %_name-common
%doc AGENT.txt COPYING ChangeLog* EXAMPLE.conf FAQ NEWS PORTING README* TODO
%doc local/passtest local/ipf-mod.pl
%dir %_sysconfdir/snmp
%dir %_datadir/snmp
%attr(0770,snmp,root) %persistentdir

%files -n %_name-snmpd
%_tmpfilesdir/net-snmp.conf
%_initdir/snmpd
%_unitdir/snmpd.service
%config(noreplace) %_sysconfdir/sysconfig/snmpd
%config(noreplace) %_sysconfdir/logrotate.d/snmpd
%config(noreplace) %attr(0640,snmp,root) %_sysconfdir/snmp/snmpd.conf
%_sbindir/snmpd
%_bindir/net-snmp-create-v3-user
%_bindir/encode_keychange
%_man5dir/snmpd.conf.*
%_man5dir/snmpd.examples.*
%_man5dir/snmpd.internal*
%_man5dir/snmp_config.*
%_man5dir/variables.*
%_man8dir/snmpd.*

%files -n %_name-snmptrapd
%_initdir/snmptrapd
%_unitdir/snmptrapd.service
%config(noreplace) %_sysconfdir/sysconfig/snmptrapd
%_sbindir/snmptrapd
%_man5dir/snmptrapd.conf.*
%_man8dir/snmptrapd.*

%files -n %_name-clients
%_bindir/agentxtrap
%_bindir/snmpbulkget
%_bindir/snmpbulkwalk
%_bindir/snmpdelta
%_bindir/snmpdf
%_bindir/snmpget
%_bindir/snmpgetnext
%_bindir/snmpinform
%_bindir/snmpnetstat
%_bindir/snmpset
%_bindir/snmpstatus
%_bindir/snmptable
%_bindir/snmptest
%_bindir/snmptls
%_bindir/snmptranslate
%_bindir/snmptrap
%_bindir/snmpusm
%_bindir/snmpvacm
%_bindir/snmpwalk
%_bindir/snmpping
%_bindir/snmpps
%_bindir/snmptop

%_man1dir/agentxtrap.*
%_man1dir/encode_keychange*
%_man1dir/net-snmp-create-v3-user.*
%_man1dir/snmpbulkget.*
%_man1dir/snmpbulkwalk.*
%_man1dir/snmpcmd.*
%_man1dir/snmpdelta.*
%_man1dir/snmpdf.*
%_man1dir/snmpget.*
%_man1dir/snmpgetnext.*
%_man1dir/snmpinform.*
%_man1dir/snmpnetstat.*
%_man1dir/snmpset.*
%_man1dir/snmpstatus.*
%_man1dir/snmptable.*
%_man1dir/snmptest.*
%_man1dir/snmptranslate.*
%_man1dir/snmptrap.*
%_man1dir/snmpusm.*
%_man1dir/snmpvacm.*
%_man1dir/snmpwalk.*
%_man1dir/snmpps.*
%_man1dir/snmptop.*
%_man5dir/snmp.conf.*

%files -n %_name-utils
%doc local/README.mib2c
%_datadir/snmp/mib2c-data
%_datadir/snmp/mib2c.*.conf
%_datadir/snmp/mib2c.conf
%_datadir/snmp/snmpconf-data

%_bindir/checkbandwidth
%_bindir/mib2c
%_bindir/mib2c-update
%_bindir/snmpconf
%_bindir/tkmib
%_bindir/traptoemail

%_man1dir/mib2c*
%_man1dir/snmpconf.*
%_man1dir/tkmib.*
%_man1dir/traptoemail.*
%_man5dir/mib2c.*

%files -n %_name-bridge-mib
%_bindir/snmp-bridge-mib
%_man1dir/snmp-bridge-mib.*

%files -n %_name-cert
%_bindir/net-snmp-cert

%files -n lib%name
%_libdir/libnetsnmp.so.*

%files -n lib%name-agent
%_libdir/libnetsnmpagent.so.*
%_libdir/libnetsnmphelpers.so.*
%_libdir/libnetsnmpmibs.so.*
%_libdir/libnetsnmptrapd.so.*

%files -n lib%_name-devel
%doc net-snmp-mibs.tar.bz2
%_libdir/*.so
%_includedir/*
%_man3dir/*
%_pkgconfigdir/*.pc
%_bindir/net-snmp-config
%_man1dir/net-snmp-config.*

%if_enabled static
%files -n lib%_name-devel-static
%_libdir/libnetsnmp.a
%_libdir/libnetsnmpagent.a
%_libdir/libnetsnmphelpers.a
%_libdir/libnetsnmpmibs.a
%_libdir/libnetsnmptrapd.a
%endif

%if_enabled mibs
%files -n %_name-mibs
%_datadir/snmp/mibs
%endif

%files -n perl-SNMP
%doc perl/SNMP/{examples,README,BUG,TODO}
%_datadir/snmp/snmp_perl.pl
%_datadir/snmp/snmp_perl_trapd.pl
%perl_vendor_archlib/SNMP*
%perl_vendor_autolib/SNMP*
%perl_vendor_archlib/NetSNMP*
%perl_vendor_autolib/NetSNMP*
%perl_vendor_archlib/Bundle/MakefileSubs.pm

%files -n python3-module-netsnmp
%python3_sitelibdir/*
%doc python/README

%changelog
* Tue Feb 21 2023 Alexey Shabalin <shaba@altlinux.org> 5.9.3-alt1
- 5.9.3
- Fixes: CVE-2022-44792, CVE-2022-44793
- Add patches from fedora.
- Drop libucd-snmp and libucd-snmp-devel packages.
- Drop net-snmp-config package and move script net-snmp-config to devel.
- Add libnet-snmp-agent package and move agent library.

* Mon Oct 04 2021 Egor Ignatov <egori@altlinux.org> 5.8-alt2
- Fix build with LTO

* Wed Aug 28 2019 Alexey Shabalin <shaba@altlinux.org> 5.8-alt1
- 5.8

* Sun Apr 07 2019 L.A. Kostis <lakostis@altlinux.ru> 5.7.3-alt6.1
- Rebuild w/ new lm_sensors.

* Fri Mar 01 2019 Nikolai Kostrigin <nickel@altlinux.org> 5.7.3-alt6
- Fix FTBFS against libmysqlclient21

* Thu Jan 24 2019 Stanislav Levin <slev@altlinux.org> 5.7.3-alt5
- Applied patches from upstream (closes: #35969).

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 5.7.3-alt4.1
- rebuild with new perl 5.28.1

* Thu Aug 30 2018 Terechkov Evgenii <evg@altlinux.org> 5.7.3-alt4
- Build without libwrap (tcp_wrappers)
- Fix build with openssl1.1 (patch9)

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 5.7.3-alt3.1
- rebuild with new perl 5.26.1

* Wed Feb 22 2017 Michael Shigorin <mike@altlinux.org> 5.7.3-alt3
- fixed build without systemd, see also:
  https://bugs.mageia.org/show_bug.cgi?id=13761
  https://patchwork.openembedded.org/patch/51041/
- compress ChangeLog with xz instead of bzip2
- minor spec cleanup
- dropped (non-)Packager

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 5.7.3-alt2.1
- rebuild with new perl 5.24.1

* Thu Feb 02 2017 Igor Vlasenko <viy@altlinux.ru> 5.7.3-alt2
- NMU: updated upstream V5-7-patches branch to fix build
- added gear remotes

* Sun Jan 10 2016 Terechkov Evgenii <evg@altlinux.org> 5.7.3-alt1.1
- fix typo in spec

* Sat Jan  9 2016 Terechkov Evgenii <evg@altlinux.org> 5.7.3-alt1
- 5.7.3
- add patch7 to fix group->gid resolving (ALT#30926)
- source /etc/sysconfig/snmptrapd on sysv (just like on systemd) systemd (ALT#30927)
- spec cleanup (ALT#29545)
- patch6 (systemd) adapted to 5.7.3
- remove bogus noreplace flag on sysv/systemd initscripts
- move verndor-specific tmpfiles manifest to %%_tmpfilesdir

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 5.7.2-alt5.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 5.7.2-alt5.1
- rebuild with new perl 5.20.1

* Thu Oct 24 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 5.7.2-alt5
- Update patches from V5-7-patches branch
- Fix (ALT#29516) - move snmp.conf(5) to net-snmp-clients

* Mon Sep 09 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 5.7.2-alt4
- Update patches from V5-7-patches branch
- Fix (ALT #29319) - add README to python-module-netsnmp
- Add support for systemd - net-snmp-5.7.2-systemd.patch

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 5.7.2-alt3
- built for perl 5.18

* Wed Feb 20 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 5.7.2-alt2
- Rebuild with new libnl

* Thu Feb 07 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 5.7.2-alt1
- 5.7.2 release
- Update patches from V5-7-patches branch

* Tue Sep 04 2012 Vladimir Lettiev <crux@altlinux.ru> 5.7.1-alt9
- rebuilt for perl-5.16

* Fri May 25 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 5.7.1-alt8
- Update patches from V5-7-patches branch
- Fix DSO linking
- Fix CVE-2012-2141

* Mon May 07 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 5.7.1-alt7
- Update patches from V5-7-patches branch

* Mon Dec 19 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 5.7.1-alt6
- Update patches from V5-7-patches branch
- Fix RPATH

* Tue Nov 22 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 5.7.1-alt5
- Update patches from V5-7-patches branch
- Fix (ALT #26587) (thx led@ and mike@)

* Sun Oct 30 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.7.1-alt4.1
- Rebuild with Python-2.7

* Sat Oct 29 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 5.7.1-alt4
- Update patches from V5-7-patches branch

* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 5.7.1-alt3
- rebuilt for perl-5.14

* Sun Oct 09 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 5.7.1-alt2
- 5.7.1 release

* Sat Sep 03 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 5.7.1-alt1.rc1
- 5.7.1 release candidate
- Enable ipv6 support

* Mon Jul 18 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 5.6.1.1-alt3
- Remove noarch for net-snmp-config

* Sat Jul 16 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 5.6.1.1-alt2
- Allocated libnetsnmptrapd.so.* to separate subpackage (ALT #25904)

* Sat Jul 16 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 5.6.1.1-alt1
- 5.6.1.1 release
- Add new subpackage net-snmp-config for fix (ALT #25904)

* Thu Apr 28 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 5.6.1-alt2
- Update patches from V5-6-patches branch

* Mon Mar 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.1-alt1.1
- Rebuilt for debuginfo

* Fri Jan 21 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 5.6.1-alt1
- 5.6.1 release
- Update patches from V5-6-patches branch
- Add Requires: perl-SNMP in %_name-utils (ALT #24402)

* Tue Nov 09 2010 Vladimir Lettiev <crux@altlinux.ru> 5.6-alt5.1
- rebuilt with perl 5.12

* Tue Nov 09 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 5.6-alt5
- Add Requires: %_name-common in lib%_name-devel

* Tue Nov 09 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 5.6-alt4
- Set BuildArch: noarch for net-snmp net-snmp-bridge-mib net-snmp-cert net-snmp-utils

* Sat Nov 06 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 5.6-alt3
- Update patches from V5-6-patches branch. Fix (ALT #24493)
- Separate snmpd and snmptrapd in separate subpackage
- Add new subpackage net-snmp-clients and net-snmp-common net-snmp-bridge-mib net-snmp-cert
- Make net-snmp virtual package for quick install
- Disable smux (obsolete?)

* Sat Oct 30 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 5.6-alt2
- Update patches from V5-6-patches branch
- Add %_sysconfdir/sysconfig/snmpd (ALT #24402)
- Update spec: Relocation of often used utilities in net-snmp
- Add --with-security-modules=tsm and --with-transports="DTLSUDP TLSTCP"
  For configuration read http://www.net-snmp.org/wiki/index.php/TUT:Using_TLS
- snmpd is again single-threaded

* Tue Oct 12 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 5.6-alt1
- 5.6 release
- Update patches from V5-6-patches branch
- Enable MYSQL Trap Logging
- Enable tests
- Build python-module

* Sat Sep 18 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 5.5-alt4
- Update patches from V5-5-patches branch
- Add mibs tunnel misc/ipfwacc etherlike-mib
- tar %_datadir/snmp/mibs/* for simple update snmp-mibs

* Thu Mar 04 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 5.5-alt3
- Use svn upstream
- Apply patches from V5-5-patches branch
- Add to Requires snmp-mibs
- Set --with-mibdirs=...
- Fix preinstall section
- Delete .txt from name of mibs
- Disable build net-snmp-mibs

* Sat Feb 13 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 5.5-alt2
- Fix repocop tests

* Wed Dec 09 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 5.5-alt1
- 5.5 release
- Update spec
- Apply net-snmp-proxy.patch and net-snmp-trunk-2.patch
- Enable ucd-snmp/diskio and ucd-snmp/lmsensorsMib
- Rename subpackage according to SharedLibsPolicy

* Sat Nov 07 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.2.1-alt4
- Fixed unsafe-tmp-usage-in-scripts, rpm-obsolete-self, big-changelog,
  big-changelog and repocop warnings

* Tue Jul 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.2.1-alt3
- Linked libnetsnmpagent with libnetsnmphelpers

* Fri May 22 2009 Pavlov Konstantin <thresh@altlinux.ru> 5.4.2.1-alt2
- Fix #19780: CVE-2008-6123.
- Dropped obsolete post_* macros.

* Mon Nov 10 2008 Pavlov Konstantin <thresh@altlinux.ru> 5.4.2.1-alt1
- 5.4.2.1 release (fixes CVE-2008-4309).

* Tue Sep 23 2008 Pavlov Konstantin <thresh@altlinux.ru> 5.4.2-alt1
- 5.4.2 release.
- Enable static library build.

* Thu Aug 14 2008 Pavlov Konstantin <thresh@altlinux.ru> 5.4.1.2-alt1
- 5.4.1.2 release.

* Mon Jun 16 2008 Pavlov Konstantin <thresh@altlinux.ru> 5.4.1.1-alt1
- 5.4.1.1 security bugfix release.
- Fix CVE-2008-0960.
- Fix #13126.

* Fri Dec 21 2007 Pavlov Konstantin <thresh@altlinux.ru> 5.4.1-alt2
- Enable smux module build.
- Force autoconf version to 2.5.

* Wed Aug 01 2007 Pavlov Konstantin <thresh@altlinux.ru> 5.4.1-alt1
- 5.4.1 release.

* Tue Jul 03 2007 Pavlov Konstantin <thresh@altlinux.ru> 5.4.1-alt0.rc1
- 5.4.1 release candidate 1.

* Wed May 30 2007 Pavlov Konstantin <thresh@altlinux.ru> 5.4.1-alt0.pre1
- 5.4.1 prerelease 1.

* Tue Jan 30 2007 Pavlov Konstantin <thresh@altlinux.ru> 5.4-alt3
- Removed ipf-mod.pl from utils subpackage (as it isnt needed anyway).

* Tue Jan 30 2007 Pavlov Konstantin <thresh@altlinux.ru> 5.4-alt2
- Added snmptrapd init-script (fixes #10672).
- Spec cleanup.
- Package tkmib into utils subpackage.

* Sun Dec 10 2006 Pavlov Konstantin <thresh@altlinux.ru> 5.4-alt1
- 5.4 release.
- Really fixed 7664.
- Patches merged into source tree.
- Some minor spec cleanup.
- Funnier default sys location.

* Thu Sep 28 2006 Pavlov Konstantin <thresh@altlinux.ru> 5.3.1-alt2
- Fixed #7664.
- Fixed #5757.

* Mon Jul 17 2006 Pavlov Konstantin <thresh@altlinux.ru> 5.3.1-alt1
- 5.3.1 release.
- Added a patch to deal with perl bindings version problem (thx at@).

* Tue Jun 06 2006 Pavlov Konstantin <thresh@altlinux.ru> 5.3.1-alt0.pre3
- 5.3.1.pre3.
- Reworked patch1, patch4, patch7 for current version.
- Synced with FC 5.3.1.pre3-1.
- Fix -ass-needed problem by damir@.

* Mon Mar 27 2006 Pavlov Konstantin <thresh@altlinux.ru> 5.2.2-alt2.EX
- Enabling mfd rewrites.

* Thu Feb 02 2006 Anton Farygin <rider@altlinux.ru> 5.2.2-alt1.1
- NMU: fix build for x86_64:
    - disabled patch2
    - fixed patch7 (snmptrapd.la added to libtool objects)

* Thu Dec 01 2005 Konstantin Timoshenko <kt@altlinux.ru> 5.2.2-alt1
- 5.2.2

* Mon May 30 2005 Konstantin Timoshenko <kt@altlinux.ru> 5.2.1-alt1
- 5.2.1

* Tue Dec 14 2004 Konstantin Timoshenko <kt@altlinux.ru> 5.2-alt1
- 5.2
- Moved mib files to net-snmp-mibs subpackage.
- fix #5518, #5534, #5617

* Fri Nov 12 2004 ALT QA Team Robot <qa-robot@altlinux.org> 5.1.2-alt2.1
- Removed libelf-devel from build dependencies.

* Wed Oct 20 2004 Konstantin Timoshenko <kt@altlinux.ru> 5.1.2-alt2
- fixed bug #0005367

* Thu Aug 26 2004 Konstantin Timoshenko <kt@altlinux.ru> 5.1.2-alt1
- 5.1.2
- Move %_bindir/net-snmp-config to lib%name-devel (closes: #5068) Sir Raorn <raorn@altlinux.ru>

* Mon May 10 2004 ALT QA Team Robot <qa-robot@altlinux.org> 5.1.1-alt1.1
- Rebuilt with openssl-0.9.7d.

* Wed Apr 21 2004 Konstantin Timoshenko <kt@altlinux.ru> 5.1.1-alt1
- 5.1.1

* Wed Mar 03 2004 Konstantin Timoshenko <kt@altlinux.ru> 5.1-alt3
- rebuild with libdb4.2

* Wed Feb 18 2004 Konstantin Timoshenko <kt@altlinux.ru> 5.1-alt2
- fix init script
- add in group proc

* Tue Dec 30 2003 Konstantin Timoshenko <kt@altlinux.ru> 5.1-alt1
- 5.1

* Tue Dec 16 2003 Alexey Tourbin <at@altlinux.ru> 5.0.9-alt2
- perl-SNMP package built
- lib{net,ucd}-snmp-devel-static not packaged by default
- additional spec conventions enforcement

* Wed Oct 22 2003 Konstantin Timoshenko <kt@altlinux.ru> 5.0.9-alt1
- 5.0.9

* Mon Jan 20 2003 Rider <rider@altlinux.ru> 4.2.3-alt8
- fixed bug #0001668 (snmpd MUST HAVE rw access to /var/lib/ucd-snmp)

* Wed Dec 04 2002 AEN <aen@altlinux.ru> 4.2.3-alt7
- rebuilt with gcc-3.2

* Wed Aug 21 2002 Alexander Bokovoy <ab@altlinux.ru> 4.2.3-alt6
- Fix disk option problem again

* Tue Jul 30 2002 Alexander Bokovoy <ab@altlinux.ru> 4.2.3-alt5
- Fix disk option problem (see below)
- http://sourceforge.net/tracker/?group_id=12694&atid=112694&func=detail&aid=498809

* Thu Apr 18 2002 Alexander Bokovoy <ab@altlinux.ru> 4.2.3-alt4
- Fix includes

* Wed Mar 27 2002 Dmitry V. Levin <ldv@alt-linux.org> 4.2.3-alt3
- Added librpm-4.0.4 build support.
- Built with librpm-4.0.4, updated buildrequires.

* Thu Mar 14 2002 Rider <rider@altlinux.ru> 4.2.3-alt2
- requires fix

* Sat Feb 09 2002 Rider <rider@altlinux.ru> 4.2.3-alt1
- 4.2.3
- add RH patches

* Fri Nov 09 2001 Dmitry V. Levin <ldv@alt-linux.org> 4.2.1-alt4
- Built without librpm support.

* Fri Aug 24 2001 Rider <rider@altlinux.ru> 4.2.1-alt3
- added security patches from Caldera

* Fri Aug 17 2001 Rider <rider@altlinux.ru> 4.2.1-alt2
- default config file changed
- ifdef path from SuSE
- snmpd new started over snmp user

* Mon Jun 04 2001 Alexander Bokovoy <ab@altlinux.ru> 4.2.1-alt1
- 4.2.1
- Installation fixed for broken libtool usage
- Null patch from RH applied
- BuildRequires cleaned

* Thu May 31 2001 Dmitry V. Levin <ldv@altlinux.ru> 4.2-ipl2mdk
- Added patch so that only four bytes are returned for IP addresses on ia64 (rh #32244).
- Added patch to correcly handle a NULL value (rh #35016).
- Moved static libraries to devel-static subpackage.
- Fixed libraries, binaries and manpages packaging.

* Mon Feb 05 2001 Dmitry V. Levin <ldv@fandra.org> 4.2-ipl1mdk
- 4.2
- Merged RH patches.
- Libification.
- RE adaptions.


