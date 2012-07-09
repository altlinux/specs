Name: bind9.8
Version: 9.8.3
Release: alt1

%def_enable ipv6
%def_with openssl

Summary: ISC BIND - DNS server
License: BSD-style
Group: System/Servers

Url: http://www.isc.org/products/BIND/
%define vsuffix -P1
#define vsuffix %nil
%define srcname %name-%version%vsuffix
Source0: ftp://ftp.isc.org/isc/bind9/%version%vsuffix/bind-%version%vsuffix.tar.gz
Source3: bind.README.bind-devel
Source4: bind.README.ALT

Source11: bind.init
Source12: lwresd.init

Source21: rndc.conf
Source22: rndc.key

Source31: bind.named.conf
Source32: bind.options.conf
Source33: bind.rndc.conf
Source34: bind.local.conf
Source35: bind.rfc1912.conf
Source36: bind.rfc1918.conf

Source41: bind.localhost
Source42: bind.localdomain
Source43: bind.127.in-addr.arpa
Source44: bind.empty

Source50: ldap2zone.c
Source51: ldap2zone.1
Source52: zonetodb.1
Source53: zone2sqlite.1
Source54: bind-9.3.1rc1-sdb_tools-Makefile.in

Source100: bind9.8.watch

Patch1: bind-9.5-PIE.patch
Patch2: bind-9.5-overflow.patch
#Patch0: bind-9.3.6-owl-warnings.patch
#Patch1: bind-9.3.6-openbsd-owl-pidfile.patch
Patch101: bind-9.7.3-chroot-defaults.patch
#Patch3: bind-9.3.6-alt-owl-chroot.patch
#Patch4: bind-9.3.6-owl-checkconf-chroot.patch
#Patch5: bind-9.3.6-rh-h_errno.patch
Patch6: bind-9.3.6-alt-isc-config.patch
#Patch7: bind-9.3.6-alt-man.patch
Patch8: bind-9.3.6-alt-owl-rndc-confgen.patch
#Patch9: bind-9.3.6-owl-rfc-index.patch
Patch10: bind-9.3.6-alt-nofile.patch
#Patch11: bind-9.3.6-up-CVE-2009-0696.patch

Patch87: bind-9.5-parallel-build.patch
# IDN paches
Patch73: bind-9.5-libidn.patch
Patch83: bind-9.5-libidn2.patch
Patch85: bind-9.5-libidn3.patch
Patch94: bind95-rh461409.patch

Patch99: bind-96-libtool2.patch

Patch111: bind97-exportlib.patch
Patch112: bind-9.5-dlz-64bit.patch

Patch117: bind98-libdns-export.patch

Patch125: bind-dlzexternal-buildfix.patch

# >>> SDB patches
Patch200: bind-9.3.2b2-sdbsrc.patch

# Patch applied after cloning named source tree and facilitates building
# sdb-enabled bind in one directory and plain bind without them in other
Patch201: bind-9.5-sdb.patch
Patch202: bind-9.3.2b1-fix_sdb_ldap.patch
# Integrate sqlite sdb backend
Patch203: bind-9.5-sdb-sqlite-bld.patch

Patch300: bind-9.7.3-alt-owl-chroot.patch
Patch301: bind-9.7.3-openbsd-owl-pidfile.patch

# root directory for chrooted environment.
%define _chrootdir %_localstatedir/bind

# common directory for documentation.
%define docdir %_docdir/bind-%version

%ifndef timestamp
%define timestamp %(TZ=UTC LC_TIME=C date +%%Y%%m%%d)
%endif


Provides: bind-chroot(%_chrootdir)
Obsoletes: bind-chroot, bind-debug, bind-slave, caching-nameserver
# Because of /etc/syslog.d/ feature.
Conflicts: syslogd < 1.4.1-alt11
PreReq: bind-control chrooted syslogd-daemon
PreReq: lib%name = %version-%release

# due to %_chrootdir/dev/log
BuildPreReq: coreutils

# due to broken configure script
BuildPreReq: gcc-c++

%{?_with_openssl:BuildPreReq: libssl-devel}

# Automatically added by buildreq on Mon Feb 28 2011
BuildRequires: doxygen libidn-devel libldap-devel libsqlite3-devel libssl-devel libxml2-devel perl-IO-Socket-INET6 postgresql-devel texlive-latex-base tzdata xml-utils xsltproc

#BuildRequires: doxygen gcc-c++ libidn-devel libkrb5 libssl-devel libxml2-devel perl-IO-Socket-INET6 texlive-latex-base tzdata xml-utils xsltproc

%package sdb
Summary: BIND server with database backends and DLZ support
Group: System/Servers
Requires: %name

%package utils
Summary: Utilities provided by ISC BIND
Group: Networking/Other
Requires: lib%name = %version-%release
Conflicts: bind-utils

%package -n lib%name
Summary: Shared library used by ISC BIND
Group: System/Libraries
Provides: libdns = %version-%release
Provides: libisc = %version-%release
Provides: libisccc = %version-%release
Provides: libisccfg = %version-%release
Provides: liblwres = %version-%release
Obsoletes: libdns8, libdns9, libdns10, libdns11, libdns16
Obsoletes: libisc4, libisc7, libisccc0, libisccfg0, liblwres1

%package -n lib%name-lite
Summary:  Libraries for working with the DNS protocol
Group: System/Libraries

%package devel
Summary: ISC BIND development libraries and headers
Group: Development/C
Requires: lib%name = %version-%release

%package doc
Summary: Documentation for ISC BIND
Group: Development/Other
BuildArch: noarch
Prefix: %prefix

%package -n lwresd9.8
Summary: Lightweight resolver daemon
Group: System/Servers
PreReq: /var/resolv, chkconfig, shadow-utils
Requires: lib%name = %version-%release

%description
The Berkeley Internet Name Domain (BIND) implements an Internet domain
name server.  BIND is the most widely-used name server software on the
Internet, and is supported by the Internet Software Consortium (ISC).

This package provides the server and related configuration files.

%description sdb
BIND (Berkeley Internet Name Domain) is an implementation of the DNS (Domain
Name System) protocols. This package includes a DNS server (named-sdb) which
has compiled-in SDB (Simplified Database Backend) which includes support for
using alternative Zone Databases stored in an LDAP server (ldapdb), a
postgreSQL database (pgsqldb), an sqlite database (sqlitedb), or in the
filesystem (dirdb), in addition to the standard in-memory RBT (Red Black Tree)
zone database. It also includes support for DLZ (Dynamic Loadable Zones).

%description utils
This package contains various utilities related to DNS that are
derived from the BIND source tree, including dig, host, nslookup
and nsupdate.

%description -n lib%name
This package contains shared libraries used by BIND's daemons
and clients.

%description -n lib%name-lite
Contains lite version of BIND suite libraries which are used by various
programs to work with DNS protocol.

%description devel
This package contains development libraries, header files, and API man
pages for libdns, libisc, libisccc, libisccfg and liblwres.  These are
only needed if you want to compile packages that need more nameserver
API than the resolver code provided by glibc.

%description doc
This package provides various documents that are useful for maintaining a
working BIND installation.

%description -n lwresd9.8
This package contains lwresd, the daemon providing name lookup services
to clients that use the BIND 9 lightweight resolver library.  It is
essentially a stripped-down, caching-only name server that answers
queries using the BIND 9 lightweight resolver protocol rather than
the DNS protocol.

%prep
%setup -n bind-%version%vsuffix

%patch101 -p1

%patch1 -p1 -b .PIE
#patch2 -p1 -b .overflow
%patch8 -p1
###%patch3 -p1
###%patch4 -p1
###%patch5 -p1
###%patch6 -p1
###%patch7 -p1
###%patch8 -p1
###%patch9 -p1
%patch10 -p1
###%patch11 -p1

%patch73 -p1 -b .libidn
%patch83 -p1 -b .libidn2
%patch85 -p1 -b .libidn3
%patch87 -p1 -b .parallel
%patch94 -p1 -b .rh461409

%patch111 -p1 -b .exportlib
%patch112 -p1 -b .64bit
### %patch117 -p1 -b .libdns-export
%patch125 -p1 -b .dlzexternal

# make source tree for sdb-enables build:
mkdir bin/named-sdb
cp -r bin/named/* bin/named-sdb
%patch200 -p1 -b .sdbsrc

# SDB ldap
cp -fp contrib/sdb/ldap/ldapdb.[ch] bin/named-sdb
# SDB postgreSQL
cp -fp contrib/sdb/pgsql/pgsqldb.[ch] bin/named-sdb
# SDB sqlite
cp -fp contrib/sdb/sqlite/sqlitedb.[ch] bin/named-sdb
# SDB Berkeley DB - needs to be ported to DB4!
#cp -fp contrib/sdb/bdb/bdb.[ch] bin/named_sdb
# SDB dir
cp -fp contrib/sdb/dir/dirdb.[ch] bin/named-sdb
# SDB tools
mkdir -p bin/sdb_tools
cp -fp %_sourcedir/ldap2zone.c bin/sdb_tools/ldap2zone.c
cp -fp %_sourcedir/bind-9.3.1rc1-sdb_tools-Makefile.in bin/sdb_tools/Makefile.in
#cp -fp contrib/sdb/bdb/zone2bdb.c bin/sdb_tools
cp -fp contrib/sdb/ldap/{zone2ldap.1,zone2ldap.c} bin/sdb_tools
cp -fp contrib/sdb/pgsql/zonetodb.c bin/sdb_tools
cp -fp contrib/sdb/sqlite/zone2sqlite.c bin/sdb_tools

%patch201 -p1 -b .sdb
%patch202 -p1 -b .fix_sdb_ldap
%patch203 -p1 -b .sdbsqlite

%patch300 -p1
%patch301 -p1

# XXX due new libtool. Not sure about proper upstream approach yet.
mkdir m4
%patch99 -p1 -b .libtool2

install -pm644 %_sourcedir/bind.README.bind-devel README.bind-devel
install -pm644 %_sourcedir/bind.README.ALT README.ALT

mkdir addon
install -pm644 %_sourcedir/{bind,lwresd}.init addon/
install -pm644 %_sourcedir/bind.{named,options,rndc,local,rfc1912,rfc1918}.conf \
	addon/
install -pm644 %_sourcedir/bind.{localhost,localdomain,127.in-addr.arpa,empty} \
	addon/
install -pm644 %_sourcedir/rndc.{conf,key} addon/

find -type f -print0 |
	xargs -r0 grep -lZ '@[A-Z_]\+@' -- |
	xargs -r0 sed -i \
'
s,@ROOT@,%_chrootdir,g;
s,@LWRESD_ROOT@,/var/resolv,g;
s,@DOCDIR@,%docdir,g;
s,@SBINDIR@,%_sbindir,g;
' --

%build
libtoolize -c -f; aclocal -I m4 --force; autoconf -f

# Need this fixes due to unusual include path of our libkrb5-devel.
# TODO: fix krb5 build instead...
subst 's@gssapi/gssapi.h@krb5/gssapi.h@' configure
subst 's@use_gssapi/include@use_gssapi/include/krb5@' configure

CPP="%__cpp"; export CPP
CC="gcc"; export CC
%configure \
	--with-libtool \
	--localstatedir=/var \
	--with-libtool \
	--with-randomdev=/dev/urandom \
	--disable-threads \
	--disable-linux-caps \
	 %{subst_with openssl} \
	 %{subst_enable ipv6} \
	--disable-static \
	--with-gssapi=yes \
	--disable-isc-spnego \
	--enable-exportlib \
	--with-export-libdir=%_libdir \
	--with-export-includedir=%_includedir \
	--disable-openssl-version-check
# Patched to parallel build. Try it:
%make_build

# Build queryperf
pushd contrib/queryperf
	%configure
	%make_build
popd # contrib/queryperf

%install
rln()
{
	local target=$1 && shift
	local source=$1 && shift
	target=`relative "$target" "$source"`
	ln -snf "$target" "%buildroot$source"
}

%makeinstall_std

# Install queryperf.
install -pm755 contrib/queryperf/queryperf %buildroot%_sbindir/

# Install startup scripts.
install -pD -m755 addon/bind.init %buildroot%_initdir/bind
install -pD -m755 addon/lwresd.init %buildroot%_initdir/lwresd

# Install configurations files
install -pm600 addon/rndc.conf %buildroot%_sysconfdir/

# Create a chrooted environment...
mkdir -p %buildroot%_chrootdir/{dev,%_sysconfdir,var/{run,tmp},zone/slave}
for n in named options rndc local rfc1912 rfc1918; do
	install -pm640 "addon/bind.$n.conf" \
		"%buildroot%_chrootdir%_sysconfdir/$n.conf"
done
for n in localhost localdomain 127.in-addr.arpa empty; do
	install -pm640 "addon/bind.$n" \
		"%buildroot%_chrootdir/zone/$n"
	sed -i s/YYYYMMDDNN/%{timestamp}00/ \
		"%buildroot%_chrootdir/zone/$n"
done
install -pm640 addon/rndc.key %buildroot%_chrootdir%_sysconfdir/
rln %_chrootdir%_sysconfdir/named.conf %_sysconfdir/

# Make use of syslogd-1.4.1-alt11 /etc/syslog.d/ feature.
/usr/bin/mksock %buildroot%_chrootdir/dev/log
mkdir %buildroot%_sysconfdir/syslog.d
ln -s %_chrootdir/dev/log %buildroot%_sysconfdir/syslog.d/bind
#... end of the chroot configuration.

# Create ndc compatibility symlinks.
ln -s rndc %buildroot%_sbindir/ndc
ln -s rndc.8 %buildroot%_man8dir/ndc.8

# Create ghost files
touch %buildroot/var/run/{named,lwresd}.pid

# Package documentation files
mkdir -p %buildroot%docdir
cp -a CHANGES COPYRIGHT FAQ README* \
	doc/{arm,misc} \
	%buildroot%docdir/
install -pm644 contrib/queryperf/README %buildroot%docdir/README.queryperf

bzip2 -9q %buildroot%docdir/{*/*.txt,FAQ,CHANGES} ||:
rm -fv %buildroot%docdir/*/{Makefile*,README-SGML,*.dsl*,*.sh*,*.xml}

# SDB manpages
install -m644 %_sourcedir/ldap2zone.1 %buildroot%_man1dir/ldap2zone.1
install -m644 %_sourcedir/zonetodb.1 %buildroot%_man1dir/zonetodb.1
install -m644 %_sourcedir/zone2sqlite.1 %buildroot%_man1dir/zone2sqlite.1

%pre
/usr/sbin/groupadd -r -f named
/usr/sbin/useradd -r -g named -d %_chrootdir -s /dev/null -n -c "Domain Name Server" named >/dev/null 2>&1 ||:
[ -f %_initdir/named -a ! -L %_initdir/named ] && /sbin/chkconfig --del named ||:
%pre_control bind-debug bind-slave

%preun
%preun_service bind

%post
SYSLOGD_SCRIPT=/etc/init.d/syslogd
SYSLOGD_CONFIG=/etc/sysconfig/syslogd
if grep -qs '^SYSLOGD_OPTIONS=.*-a %_chrootdir/dev/log' "$SYSLOGD_CONFIG"; then
	# Remove artefacts of pre-syslog.d epoch.
	sed -i 's|^\(SYSLOGD_OPTIONS=.*\) \?-a %_chrootdir/dev/log|\1|' "$SYSLOGD_CONFIG"
	if [ -x "$SYSLOGD_SCRIPT" ]; then
		"$SYSLOGD_SCRIPT" condreload ||:
	fi
fi

%post_control -s disabled bind-debug bind-slave
%post_service bind

%pre -n lwresd9.8
/usr/sbin/groupadd -r -f lwresd
/usr/sbin/useradd -r -g lwresd -d / -s /dev/null -n -c "Lightweight Resolver Daemon" lwresd >/dev/null 2>&1 ||:

%post -n lwresd9.8
%post_service lwresd

%preun -n lwresd9.8
%preun_service lwresd

%files -n lib%name
%_libdir/lib*.so.*
%exclude %_libdir/*export.so.*

%files -n lib%name-lite
%_libdir/*export.so.*

%files -n lwresd9.8
%config %_initdir/lwresd
%_sbindir/lwresd
%_man8dir/lwresd.*
%ghost %attr(644,root,root) /var/run/lwresd.pid

%files devel
%_libdir/*.so
%_bindir/isc-config.sh
%_includedir/*
%_man3dir/*
%dir %docdir
%docdir/README.bind-devel

%files
%_sbindir/arpaname
%_sbindir/ddns-confgen
%_sbindir/dnssec-*
%_sbindir/genrandom
%_sbindir/isc-hmac-fixup
%_sbindir/named
%_sbindir/named-checkconf
%_sbindir/named-checkzone
%_sbindir/named-compilezone
%_sbindir/named-journalprint
%_sbindir/ndc
%_sbindir/nsec3hash
%_sbindir/queryperf
%_sbindir/rndc
%_sbindir/rndc-confgen

%_sysconfdir/named.conf
%config %_initdir/bind
%config(noreplace) %_sysconfdir/rndc.conf

%_man1dir/arpaname*
%_man1dir/isc-config.sh*

%_man5dir/named.conf.*
%_man5dir/rndc.conf.*

%_man8dir/ddns-confgen*
%_man8dir/dnssec*
%_man8dir/genrandom*
%_man8dir/isc-hmac-fixup*
%_man8dir/nsec3hash*
%_man8dir/named*
%_man8dir/*ndc*

%ghost %attr(644,root,root) /var/run/named.pid

#chroot
%_sysconfdir/syslog.d/*
%defattr(640,root,named,710)
%dir %_chrootdir
%dir %_chrootdir/dev
%dir %_chrootdir%_sysconfdir
%dir %_chrootdir/zone
%dir %attr(700,root,named) %verify(not mode) %_chrootdir/zone/slave
%dir %attr(700,root,named) %verify(not mode) %_chrootdir/var
%dir %attr(1770,root,named) %_chrootdir/var/run
%dir %attr(1770,root,named) %_chrootdir/var/tmp
%config(noreplace) %_chrootdir%_sysconfdir/*.conf
%config(noreplace) %verify(not md5 mtime size) %_chrootdir%_sysconfdir/rndc.key
%config %_chrootdir/zone/localhost
%config %_chrootdir/zone/localdomain
%config %_chrootdir/zone/127.in-addr.arpa
%config %_chrootdir/zone/empty

%ghost %attr(666,root,root) %_chrootdir/dev/*

%files sdb
%_sbindir/named-sdb
%_sbindir/ldap2zone
%_sbindir/zone2ldap
%_sbindir/zone2sqlite
%_sbindir/zonetodb
%_man1dir/zone2ldap*
%_man1dir/zonetodb*
%_man1dir/zone2sqlite*
%_man1dir/ldap2zone*

%files utils
%_bindir/dig
%_bindir/host
%_bindir/nslookup
%_bindir/nsupdate
%_man1dir/dig.*
%_man1dir/host.*
%_man1dir/nslookup.*
%_man1dir/nsupdate.*

%files doc
%docdir
%exclude %docdir/README.bind-devel

%changelog
* Mon Jul 09 2012 Michael Shigorin <mike@altlinux.org> 9.8.3-alt1
- new version (watch file uupdate)
  + 9.8.3-P1

* Wed May 09 2012 Michael Shigorin <mike@altlinux.org> 9.8.2-alt3
- added watch file

* Sat May 05 2012 Michael Shigorin <mike@altlinux.org> 9.8.2-alt2
- dropped patch2
- doc/{draft,rfc} are there no more

* Sat Apr 21 2012 Michael Shigorin <mike@altlinux.org> 9.8.2-alt1
- 9.8.2 (closes: #26588)

* Wed Dec 14 2011 Michael Shigorin <mike@altlinux.org> 9.8.1-alt0.2
- NMU: Conflicts: bind-utils rather that Obsoletes:

* Fri Nov 18 2011 Victor Forsiuk <force@altlinux.org> 9.8.1-alt0.1
- 9.8.1-P1 (security fix for CVE-2011-4313).
- Utils subpackage now obsoletes bind-utils.

* Sun Jun 12 2011 Victor Forsiuk <force@altlinux.org> 9.8.0-alt0.2
- 9.8.0-P2 (security fixes for CVE-2011-1907 and CVE-2011-1910).

* Thu Mar 31 2011 Victor Forsiuk <force@altlinux.org> 9.8.0-alt0.1
- Build 9.8.0 and package as bind9.8 to co-exist with ages old and lacking
  desperately needed features bind 9.3.6.
- Build with IPv6.
- Add PIE patch.
- Disable static libraries.
- Patch to fix https://bugzilla.redhat.com/show_bug.cgi?id=247856 (bind-9.5-overflow.patch).
- Build --with-gssapi (and use SPNEGO from GSSAPI library: --disable-isc-spnego).
- Build with /dev/urandom insted of /dev/random (better get not so perfect
  randomness than wait for it...).
- Build exportable library (--enable-exportlib) and package it separately.
- Build both SDB and DLZ enabled bind and lighter version without them.
- Add LSB section to named initscript, don't start daemon by default.
- Modify initscript to start SDB-enabled bind if installed.
- Remove rfc1912.txt, it is already located in doc/rfc directory.

* Fri Oct 01 2010 Dmitry V. Levin <ldv@altlinux.org> 9.3.6-alt6
- Rebuilt with libcrypto.so.10.

* Tue Jul 28 2009 Dmitry V. Levin <ldv@altlinux.org> 9.3.6-alt5
- Backported upstream fix for a remote DoS bug (CVE-2009-0696).

* Thu Apr 30 2009 Dmitry V. Levin <ldv@altlinux.org> 9.3.6-alt4
- Removed resolver(5) manual page (closes: #19784).

* Fri Mar 06 2009 Dmitry V. Levin <ldv@altlinux.org> 9.3.6-alt3
- options.conf:
  + Removed root-delegation-only directive.
  + Added interface-interval directive example.
- Made "max open files" limit by default as large as default "max sockets" limit.

* Wed Jan 07 2009 Dmitry V. Levin <ldv@altlinux.org> 9.3.6-alt2
- Updated to 9.3.6-P1 release.

* Mon Nov 24 2008 Dmitry V. Levin <ldv@altlinux.org> 9.3.6-alt1
- Updated to 9.3.6 release.

* Sun Aug 10 2008 Dmitry V. Levin <ldv@altlinux.org> 9.3.5-alt4
- Implemented automatic fdsets expansion to overcome FD_SETSIZE limit.

* Thu Aug 07 2008 Dmitry V. Levin <ldv@altlinux.org> 9.3.5-alt3
- Updated to 9.3.5-P2 release.

* Fri Jun 06 2008 Dmitry V. Levin <ldv@altlinux.org> 9.3.5-alt2
- Updated to 9.3.5-P1 release (fixes VU#800113/CVE-2008-1447).

* Wed Apr 16 2008 Dmitry V. Levin <ldv@altlinux.org> 9.3.5-alt1
- Updated to 9.3.5 release.

* Mon Nov 05 2007 Dmitry V. Levin <ldv@altlinux.org> 9.3.4-alt5
- options.conf: Added recursing-file directive.
- Updated L.ROOT-SERVERS.NET: 198.32.64.12 -> 199.7.83.42.

* Tue Jul 24 2007 Dmitry V. Levin <ldv@altlinux.org> 9.3.4-alt4
- Updated to 9.3.4-P1 release (fixes CVE-2007-2926).

* Fri Apr 06 2007 Dmitry V. Levin <ldv@altlinux.org> 9.3.4-alt3
- rndc-confgen: Revert previous change.
- Changed startup script to use /dev/urandom as a source
  of randomness during rndc key generation.

* Wed Apr 04 2007 Dmitry V. Levin <ldv@altlinux.org> 9.3.4-alt2
- rndc-confgen: Restore default key size (#11321).

* Thu Jan 25 2007 Dmitry V. Levin <ldv@altlinux.org> 9.3.4-alt1
- Updated to 9.3.4 release.

* Fri Dec 29 2006 Dmitry V. Levin <ldv@altlinux.org> 9.3.3-alt2
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Sat Dec 09 2006 Dmitry V. Levin <ldv@altlinux.org> 9.3.3-alt1
- Updated to 9.3.3 release.

* Fri Nov 03 2006 Dmitry V. Levin <ldv@altlinux.org> 9.3.3-alt0.2
- Updated to 9.3.3 RC3.

* Sat Sep 23 2006 Dmitry V. Levin <ldv@altlinux.org> 9.3.3-alt0.1
- Updated to 9.3.3 RC2.

* Wed Sep 06 2006 Dmitry V. Levin <ldv@altlinux.org> 9.3.2-alt2
- Updated to 9.3.2 P1.

* Thu Mar 30 2006 Dmitry V. Levin <ldv@altlinux.org> 9.3.2-alt1
- Updated to 9.3.2 release.

* Tue Sep 27 2005 Dmitry V. Levin <ldv@altlinux.org> 9.3.1-alt2
- Fixed /etc/syslog.d/bind bug introduced in previous release:
  /etc/syslog.d/* must be absolute symlinks.

* Wed Sep 21 2005 Dmitry V. Levin <ldv@altlinux.org> 9.3.1-alt1
- Updated to 9.3.1 release.
- Synced with Owl's bind-9.3.1-owl1 package.
- Applied few fixes from RH and SuSE bind packages.
- Merged all shared libraries into single package, libbind.
- Replaced -debug and -slave subpackages with control facilities.
- Converted absolute symlinks into relative.

* Sat Feb 12 2005 Dmitry V. Levin <ldv@altlinux.org> 9.2.4.rel-alt2
- Fixed build of queryperf utility on x86_64 platform (closes #6083).

* Fri Sep 24 2004 Dmitry V. Levin <ldv@altlinux.org> 9.2.4.rel-alt1
- Updated to 9.2.4 release (== 9.2.4rc8).

* Sun Sep 05 2004 Dmitry V. Levin <ldv@altlinux.org> 9.2.4.rc8-alt1
- Updated to 9.2.4rc8.
- Renamed subpackage according to soname change:
  libdns11 -> libdns16.
- Updated startup script to make use of new "status --lockfile" option.

* Wed Jun 30 2004 Dmitry V. Levin <ldv@altlinux.org> 9.2.4.rc5-alt1
- Updated to 9.2.4rc5.
- Updated patches.

* Mon May 10 2004 ALT QA Team Robot <qa-robot@altlinux.org> 9.2.3.rel-alt2.1
- Rebuilt with openssl-0.9.7d.

* Wed Mar 10 2004 Dmitry V. Levin <ldv@altlinux.org> 9.2.3.rel-alt2
- Updated build dependencies.
- Do not build static library by default.

* Mon Nov 24 2003 Dmitry V. Levin <ldv@altlinux.org> 9.2.3.rel-alt1
- Updated to 9.2.3 release.
- Rediffed patches.
- Do not package .la files.
- named.8: fixed reference to the BIND 9 Administrator Reference Manual.

* Mon Sep 22 2003 Dmitry V. Levin <ldv@altlinux.org> 9.2.3.rc4-alt1
- Updated to 9.2.3rc4.
- Renamed subpackage according to soname change:
  libdns10 -> libdns11.
- Replaced "delegation-only" defaults implemented in previous release
  with new option, root-delegation-only, and enabled it by default.

* Thu Sep 18 2003 Dmitry V. Levin <ldv@altlinux.org> 9.2.3.rc2-alt1
- Updated to 9.2.3rc2.
- Renamed subpackage according to soname change:
  libdns9 -> libdns10.
- Marked all known gTLDs and ccTLDs as delegation-only by default.

* Thu Sep 11 2003 Dmitry V. Levin <ldv@altlinux.org> 9.2.3.rc1-alt2
- Merged patches from OpenBSD, thanks to Jarno Huuskonen:
  + write pidfile before chroot (#2866);
  + use chroot jailing by default, no -u/-t options are necessary;
- Make named-checkconf use chroot jail by default (Jarno Huuskonen).
- options.conf: added few samples (#2968).

* Tue Aug 26 2003 Dmitry V. Levin <ldv@altlinux.org> 9.2.3.rc1-alt1
- Updated to 9.2.3rc1.
- Removed alt-lib_dns_rootns patch (merged upstream).
- Explicitly disable use of linux capabilities.
- Renamed subpackages according to soname changes:
  libdns8 -> libdns9, libisc4 -> libisc7.

* Tue Jul 29 2003 Dmitry V. Levin <ldv@altlinux.org> 9.2.2.rel-alt2
- Fixed message from 'service bind reload' (#0002411).
- Moved 'include "/etc/rfc1912.conf";' directive
  from bind.conf to local.conf (#0002791).
- Rewritten start/stop script to new rc scheme.

* Tue Mar 04 2003 Dmitry V. Levin <ldv@altlinux.org> 9.2.2.rel-alt1
- Updated to 9.2.2 release.

* Wed Feb 12 2003 Dmitry V. Levin <ldv@altlinux.org> 9.2.2.rc1-alt2
- Relocated initial rndc key generation from %%post to startup script.
- Added some information about ALT specific to named(8) and rndc(8).
- Added README.ALT.

* Thu Feb 06 2003 Dmitry V. Levin <ldv@altlinux.org> 9.2.2.rc1-alt1
- Migrated to 9.2.2rc1.
- Build --with-libtool --with-openssl --disable-ipv6 --disable-threads.
- Do not package contrib.
- Package queryperf utility.
- Package each shared library separately:
  libdns8 libisc4 libisccc0 libisccfg0 liblwres1.
- Package lwresd separately (chrooted to /var/resolv).
- Moved %_chrootdir/zone/slave to separate subpackage, %name-slave.
- Moved %_chrootdir/var/run to separate subpackage, %name-debug.
- Added nslookup(1) and resolver(5) manpages from bind8.
- Minor manpage corrections.
- isc-config.sh: fixed --cflags.
- libdns: updated root_ns list to 2002110501.
- rndc-confgen: added "-A" option support.
- Implemented default rndc settings.
- named: patched to get correct chroot jailing support.
- Updated chroot jail and relocated it to /var/lib/bind:
  default CE is now readonly.
- Renamed %_initdir/named to %_initdir/bind.
- Merged caching-nameserver into bind package.
- Split named.conf into several configurations files.
- Added more rfc1912 zones by default.
- Added rfc1918 zones (not enabled by default).

* Wed Nov 13 2002 Dmitry V. Levin <ldv@altlinux.org> 8.3.3-alt2
- Security fixes from ISC:
  + 1469. buffer length calculation for PX was wrong.
  + 1468. ns_name_ntol() could overwite a zero length buffer.
  + 1467. off by one bug in ns_makecannon().
  + 1466. large ENDS UDP buffer size could trigger a assertion.
  + 1465. possible NULL pointer dereference in db_sec.c
  + 1464. the buffer used to construct the -ve record was not
    	  big enough for all possible SOA records.  use pointer
    	  arithmetic to calculate the remaining size in this
    	  buffer.
  + 1463. use serial space arithmetic to determine if a SIG is
    	  too old, in the future or has internally constistant
    	  times.
  + 1462. write buffer overflow in make_rr().
- Changed named.init:
  + added condreload();
  + fixed argument for "-c" option.
- Changed bind chroot jail:
  + removed /var/lib;
  + removed /etc/{host,nsswitch}.conf;
  + added /etc/{protocols,services}.
- Use subst instead of perl in %%post script.
- Dont't calc perl dependencies for -contrib.

* Mon Jul 01 2002 Dmitry V. Levin <ldv@altlinux.org> 8.3.3-alt1
- Updated code to 8.3.3 release.
- Explicitly use mksock from fileutils.
- Fixed build when glibc-core-archopt is installed.
- Updated packager information.

* Tue Apr 16 2002 Dmitry V. Levin <ldv@alt-linux.org> 8.3.1-alt1
- Updated code to 8.3.1 release.
- Fixed bind to use /dev/null from core system.
- Make use of syslogd-1.4.1-alt9 /etc/syslog.d/ feature.
- Renamed /etc/chroot.d/named.* to /etc/chroot.d/bind.*
- Relaxed dependencies (conflicts instead of requires).

* Wed Oct 03 2001 Dmitry V. Levin <ldv@altlinux.ru> 8.2.5-alt1
- 8.2.5

* Tue Sep 04 2001 Dmitry V. Levin <ldv@altlinux.ru> 8.2.4-alt3
- Corrected manpages according to chrooted scheme.
- More manpages moved to man-pages package.

* Tue Jul 24 2001 Dmitry V. Levin <ldv@altlinux.ru> 8.2.4-alt2
- Moved chroot from /var/named to %_localstatedir/named (according to FHS).
- Merged bind-chroot into main package.
- Updated scripts to handle new syslogd.
- Removed restart support from named.

* Thu May 31 2001 Dmitry V. Levin <ldv@altlinux.ru> 8.2.4-alt1
- 8.2.4

* Mon Mar 19 2001 Dmitry V. Levin <ldv@altlinux.ru> 8.2.3-ipl4mdk
- Updated PreReqs.

* Mon Feb 05 2001 Dmitry V. Levin <ldv@fandra.org> 8.2.3-ipl3mdk
- Fixed %%devel subpackage.

* Wed Jan 31 2001 Dmitry V. Levin <ldv@fandra.org> 8.2.3-ipl2mdk
- Pacthed db_defs.h to ease finding errors.
- Added %%triggerpostun.
- Added call for chrooted environment adjustment before server start.

* Sun Jan 28 2001 Dmitry V. Levin <ldv@fandra.org> 8.2.3-ipl1mdk
- 8.2.3
- Ported to new chrooted scheme.

* Thu Nov 16 2000 Dmitry V. Levin <ldv@fandra.org> 8.2.2_P7-ipl1mdk
- 8.2.2_P7
- Moved chrooted environment to separate subpackage.
- Removed few manpages, obsoleted by new man-pages package.

* Sat May 13 2000 Dmitry V. Levin <ldv@fandra.org>
- xfer tmpdir patch
- chrooted environment fix

* Fri Mar 10 2000 Dmitry V. Levin <ldv@fandra.org>
- fixed startup script to exit with error if no configuration available
- updated to rpm-3.0.4

* Thu Nov 11 1999 Dmitry V. Levin <ldv@fandra.org>
- 8.2.2-P3

* Sun Oct 31 1999 Dmitry V. Levin <ldv@fandra.org>
- chrooted environment
- doc and contrib packages
- optimal manpage compression
- Fandra adaptions

* Sat Oct 09 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Add lame server patch

* Fri Jul 16 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- 8.2.1

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Wed Mar 31 1999 Bill Nottingham <notting@redhat.com>
- add ISC patch
- add quick hack to make host not crash
- add more docs

* Fri Mar 26 1999 Cristian Gafton <gafton@redhat.com>
- add probing information in the init file to keep linuxconf happy
- dont strip libbind

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 3)

* Wed Mar 17 1999 Preston Brown <pbrown@redhat.com>
- removed 'done' output at named shutdown.

* Tue Mar 16 1999 Cristian Gafton <gafton@redhat.com>
- version 8.2

* Wed Dec 30 1998 Cristian Gafton <gafton@redhat.com>
- patch to use the __FDS_BITS macro
- build for glibc 2.1

* Wed Sep 23 1998 Jeff Johnson <jbj@redhat.com>
- change named.restart to /usr/sbin/ndc restart

* Sat Sep 19 1998 Jeff Johnson <jbj@redhat.com>
- install man pages correctly.
- change K10named to K45named.

* Wed Aug 12 1998 Jeff Johnson <jbj@redhat.com>
- don't start if /etc/named.conf doesn't exist.

* Sat Aug  8 1998 Jeff Johnson <jbj@redhat.com>
- autmagically create /etc/named.conf from /etc/named.boot in %post
- remove echo in %post

* Wed Jun 10 1998 Jeff Johnson <jbj@redhat.com>
- merge in 5.1 mods

* Sun Apr 12 1998 Manuel J. Galan <manolow@step.es>
- Several essential modifications to build and install correctly.
- Modified 'ndc' to avoid deprecated use of '-'

* Mon Dec 22 1997 Scott Lampert <fortunato@heavymetal.org>
- Used buildroot
- patched bin/named/ns_udp.c to use <libelf/nlist.h> for include
  on Redhat 5.0 instead of <nlist.h>
