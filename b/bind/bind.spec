Name: bind
Version: 9.3.6
Release: alt7

Summary: ISC BIND - DNS server
License: BSD-style
Group: System/Servers
Url: http://www.isc.org/products/BIND/

%define vsuffix %nil
%define srcname %name-%version%vsuffix
# ftp://ftp.isc.org/isc/bind9/%version%vsuffix/bind-%version%vsuffix.tar.gz
Source0: %srcname.tar
Source2: rfc1912.txt
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

Patch0: bind-9.3.6-owl-warnings.patch
Patch1: bind-9.3.6-openbsd-owl-pidfile.patch
Patch2: bind-9.3.6-openbsd-owl-chroot-defaults.patch
Patch3: bind-9.3.6-alt-owl-chroot.patch
Patch4: bind-9.3.6-owl-checkconf-chroot.patch
Patch5: bind-9.3.6-rh-h_errno.patch
Patch6: bind-9.3.6-alt-isc-config.patch
Patch7: bind-9.3.6-alt-man.patch
Patch8: bind-9.3.6-alt-owl-rndc-confgen.patch
Patch9: bind-9.3.6-owl-rfc-index.patch
Patch10: bind-9.3.6-alt-nofile.patch
Patch11: bind-9.3.6-up-CVE-2009-0696.patch
Patch12: bind-9.3.6-up-rt22270-isc_print_vsnprintf.patch
Patch13: bind-9.3.6-rh538744-CVE-2009-4022.patch
Patch14: bind-9.3.6-rh554851-CVE-2010-0097.patch
Patch15: bind-9.3.6-rh640730-CVE-2010-3762.patch
Patch16: bind-9.3.6-rh754398-CVE-2011-4313.patch

# root directory for chrooted environment.
%define _chrootdir %_localstatedir/bind

# common directory for documentation.
%define docdir %_docdir/bind-%version

%ifndef timestamp
%define timestamp %(TZ=UTC LC_TIME=C date +%%Y%%m%%d)
%endif

%def_disable static
%def_enable ipv6
%def_with openssl

Provides: bind-chroot(%_chrootdir)
Obsoletes: bind-chroot, bind-debug, bind-slave, caching-nameserver
# Because of /etc/syslog.d/ feature.
Conflicts: syslogd < 1.4.1-alt11
PreReq: bind-control chrooted syslogd-daemon
PreReq: libbind = %version-%release

# due to %_chrootdir/dev/log
BuildPreReq: coreutils

# due to broken configure script
BuildPreReq: gcc-c++

%{?_with_openssl:BuildPreReq: libssl-devel}

%package utils
Summary: Utilities provided by ISC BIND
Group: Networking/Other
Requires: libbind = %version-%release

%package -n libbind
Summary: Shared library used by ISC BIND
Group: System/Libraries
Provides: libdns = %version-%release
Provides: libisc = %version-%release
Provides: libisccc = %version-%release
Provides: libisccfg = %version-%release
Provides: liblwres = %version-%release
Obsoletes: libdns8, libdns9, libdns10, libdns11, libdns16
Obsoletes: libisc4, libisc7, libisccc0, libisccfg0, liblwres1

%package devel
Summary: ISC BIND development libraries and headers
Group: Development/C
Requires: libbind = %version-%release

%package devel-static
Summary: ISC BIND static development libraries
Group: Development/C
Requires: %name-devel = %version-%release

%package doc
Summary: Documentation for ISC BIND
Group: Development/Other
BuildArch: noarch
Prefix: %prefix

%package -n lwresd
Summary: Lightweight resolver daemon
Group: System/Servers
PreReq: /var/resolv, chkconfig, shadow-utils
Requires: libbind = %version-%release

%description
The Berkeley Internet Name Domain (BIND) implements an Internet domain
name server.  BIND is the most widely-used name server software on the
Internet, and is supported by the Internet Software Consortium (ISC).

This package provides the server and related configuration files.

%description utils
This package contains various utilities related to DNS that are
derived from the BIND source tree, including dig, host, nslookup
and nsupdate.

%description -n libbind
This package contains shared libraries used by BIND's daemons
and clients.

%description devel
This package contains development libraries, header files, and API man
pages for libdns, libisc, libisccc, libisccfg and liblwres.  These are
only needed if you want to compile packages that need more nameserver
API than the resolver code provided by glibc.

%description devel-static
This package contains development static libraries, header files, and
API man pages for libdns, libisc, libisccc, libisccfg and liblwres.
These are only needed if you want to compile statically linked packages
that need more nameserver API than the resolver code provided by glibc.

%description doc
This package provides various documents that are useful for maintaining a
working BIND installation.

%description -n lwresd
This package contains lwresd, the daemon providing name lookup services
to clients that use the BIND 9 lightweight resolver library.  It is
essentially a stripped-down, caching-only name server that answers
queries using the BIND 9 lightweight resolver protocol rather than
the DNS protocol.

%prep
%setup -n %srcname
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1

install -pm644 %_sourcedir/rfc1912.txt doc/rfc/
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
CPP="%__cpp"; export CPP
%configure \
	--localstatedir=/var \
	--with-libtool \
	--with-randomdev=/dev/random \
	--disable-threads \
	--disable-linux-caps \
	 %{subst_with openssl} \
	 %{subst_enable ipv6} \
	 %{subst_enable static} \
	 --disable-openssl-version-check
# Get rid of RPATH.
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
# SMP-incompatible build.
%__make

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
	doc/{arm,draft,misc,rfc} \
	%buildroot%docdir/
install -pm644 contrib/queryperf/README %buildroot%docdir/README.queryperf

bzip2 -9q %buildroot%docdir/{*/*.txt,FAQ,CHANGES}
rm -fv %buildroot%docdir/*/{Makefile*,README-SGML,*.dsl*,*.sh*,*.xml}

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

%pre -n lwresd
/usr/sbin/groupadd -r -f lwresd
/usr/sbin/useradd -r -g lwresd -d / -s /dev/null -n -c "Lightweight Resolver Daemon" lwresd >/dev/null 2>&1 ||:

%post -n lwresd
%post_service lwresd

%preun -n lwresd
%preun_service lwresd

%files -n libbind
%_libdir/lib*.so.*
%dir %docdir
%docdir/COPYRIGHT

%files -n lwresd
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

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%files
%exclude %_sbindir/lwresd
%_sbindir/*

%_sysconfdir/named.conf
%config %_initdir/bind
%config(noreplace) %_sysconfdir/rndc.conf

%_man5dir/named.conf.*
%_man5dir/rndc.conf.*
%_man8dir/dnssec*
%_man8dir/named*
%_man8dir/*ndc*

%dir %docdir
%docdir/README*
%docdir/FAQ*
%docdir/misc
%exclude %docdir/README.bind-devel

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
* Fri Dec 16 2011 Dmitry V. Levin <ldv@altlinux.org> 9.3.6-alt7
- Imported fixes for several DNSSEC vulnerabilities from RH bind
  (CVE-2009-4022, CVE-2010-0097, CVE-2010-3762, CVE-2011-4313);
  note that DNSSEC is not enabled by default.
- Enabled IPv6 support.
- Fixed RPATH issue.

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
