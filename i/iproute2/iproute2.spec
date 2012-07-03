Name: iproute2
Version: 3.4.0
Release: alt1

Summary: Advanced IP routing and network devices configuration tools
License: GPLv2+
Group: Networking/Other

URL: http://git.kernel.org/?p=linux/kernel/git/shemminger/iproute2.git;a=summary
Source0: http://kernel.org/pub/linux/utils/net/iproute2/iproute2-%version.tar.xz

Source11: tcio7.ps.bz2
Source12: guaranteed.ps.bz2
Source13: http://www.aciri.org/floyd/papers/link.ps.bz2

# Apply only one of two patches below depending of target arch (32 or 64 bit)
Patch1: iproute2-iptables.patch
Patch2: iproute2-iptables64.patch

Patch5: iproute2-2.6.18-alt-ifcfg.patch

Patch20: iproute2-2.6.9-alt-libnetlink.patch
Patch21: http://rad.peet.spb.ru/files/related/iproute2-2.4.7-alt-rtacct_daemon.patch

Patch30: iproute2-2.6.35-fixrouteget.patch

# Fedora and Mandriva patches
Patch108: iproute2-2.6.29-IPPROTO_IP_for_SA.patch
Patch109: iproute2-2.6.39-lnstat-dump-to-stdout.patch

Provides: iproute = %version-%release
Obsoletes: iproute

# Upstream provides libnetlink without soname versioning, so we manually set versioned
# package dependency to ensure correct updates.
Requires: libnetlink = %version-%release

# Automatically added by buildreq on Fri Jan 06 2012
# optimized out: fontconfig ghostscript-classic ghostscript-common groff-base iptables pkg-config tex-common texlive-base texlive-base-bin texlive-common texlive-generic-recommended texlive-latex-base texlive-latex-recommended texlive-xetex xz
BuildRequires: OpenSP flex ghostscript-utils libatm-devel libdb4-devel libiptables-devel libnl-devel linuxdoc-tools sgml-common
# !!! buildreq overoptimized these:
BuildRequires: texlive-generic-recommended texlive-xetex

%description
The iproute package contains networking utilities (ip and rtmon, for example)
which are designed to use the advanced networking capabilities of the Linux
2.4.x and 2.6.x kernel.

%package doc
Summary: Documentation for Advanced IP routing and network device configuration tools
Group: Networking/Other
BuildArch: noarch

%description doc
Documentation for iproute2.

%package -n arpd
Summary: The arpd daemon
Group: Networking/Other
Requires: %name = %version-%release

%description -n arpd
arpd is a daemon collecting gratuitous ARP information, saving it on local disk
and feeding it to kernel on demand to avoid redundant broadcasting due to
limited size of kernel ARP cache.

%package -n libnetlink
Summary: Netlink socket library
Group: System/Libraries

%description -n libnetlink
This package contains libnetlink dynamic library.

%package -n libnetlink-devel
Summary: Netlink socket library headers
Group: System/Libraries
Requires: libnetlink = %version-%release

%description -n libnetlink-devel
This package contains libnetlink dynamic library headers.

%prep
%setup

%patch5 -p1

%if "%_lib" == "lib64"
%patch2 -p1
%else
%patch1 -p1
%endif

%patch20 -p1
%patch21 -p1

%patch30 -p1

%patch108 -p1
%patch109 -p1

%build
# Fix ALT#15409:
subst 's/TCSO :=/TCSO := q_prio.so/' tc/Makefile

%make_build \
	DBM_INCLUDE=%_includedir/db4 \
	LIBDIR=%_libdir \
	CCOPTS="-D_GNU_SOURCE %optflags"

%make_build -C doc all pdf
bzip2 -9f doc/*.ps ||:

subst 's,/sbin/arping,/usr/sbin/arping,g' examples/dhcp-client-script

%install
mkdir -p %buildroot{/sbin,%_sbindir,%_bindir,%_man8dir,%_sysconfdir/iproute2,%_initdir,%_localstatedir/arpd}

install -p -m755 ip/{ip,ifcfg,rtmon} tc/tc %buildroot/sbin/
install -p -m755 misc/{arpd,ifstat,lnstat,nstat,rtacct,ss} ip/{routel,routef} %buildroot%_sbindir/
install -p -m644 etc/iproute2/* %buildroot%_sysconfdir/iproute2/
install -p -m644 man/man8/*.8 %buildroot%_man8dir/

mkdir -p %buildroot%_libdir/tc
install -m 755 tc/q_atm.so tc/q_prio.so tc/m_xt.so %buildroot%_libdir/tc
install -m 644 netem/normal.dist netem/pareto.dist netem/paretonormal.dist %buildroot%_libdir/tc

install -p -m644 %SOURCE11 %SOURCE12 %SOURCE13 doc/

### libnetlink
mkdir -p %buildroot{%_includedir,%_libdir,%_man3dir,/%_lib}
install -p -m644 lib/libnetlink.so %buildroot/%_lib
install -p -m644 include/{libnetlink.h,ll_map.h} %buildroot%_includedir
install -p -m644 man/man3/libnetlink.3 %buildroot%_man3dir/
ln -s ../../%_lib/libnetlink.so %buildroot%_libdir/libnetlink.so

pushd %buildroot%_sbindir
    ln -s lnstat ctstat
    ln -s lnstat rtstat
popd

ln -s m_xt.so %buildroot%_libdir/tc/m_ipt.so

# Symlinks for unpriviledge users
for prg in ip rtmon tc; do ln -s ../../sbin/$prg %buildroot%_bindir; done
for prg in lnstat nstat routel ss; do ln -s ../sbin/$prg %buildroot%_bindir; done

%files
/sbin/*
%_sbindir/*
%_bindir/*
%_libdir/tc/
%exclude %_sbindir/arpd
%config(noreplace) %_sysconfdir/%name
%_man8dir/*

%files doc
%doc doc/*.bz2 doc/*.pdf doc/actions
%doc README* examples

%files -n arpd
%_sbindir/arpd
%attr(700,root,root) %dir %_localstatedir/arpd

%files -n libnetlink
/%_lib/libnetlink.so

%files -n libnetlink-devel
%_includedir/*
%_libdir/libnetlink.so
%_man3dir/*

%changelog
* Fri May 25 2012 Dmitry V. Levin <ldv@altlinux.org> 3.4.0-alt1
- Updated to 3.4.0.
- Built with libxtables.so.7.

* Sun Apr 01 2012 Victor Forsiuk <force@altlinux.org> 3.3.0-alt1
- 3.3.0
- Update source URL.

* Fri Jan 06 2012 Victor Forsiuk <force@altlinux.org> 3.2.0-alt1
- 3.2.0

* Sun Nov 27 2011 Victor Forsiuk <force@altlinux.org> 3.1.0-alt1
- 3.1.0
- lnstat fix: dump to stdout instead of stderr.

* Fri Jul 01 2011 Victor Forsiuk <force@altlinux.org> 2.6.39-alt1
- 2.6.39

* Fri Apr 08 2011 Victor Forsiuk <force@altlinux.org> 2.6.38-alt2
- Fix FTBFS by refreshing BuildRequires.

* Fri Mar 25 2011 Victor Forsiuk <force@altlinux.org> 2.6.38-alt1
- 2.6.38

* Mon Jan 10 2011 Victor Forsiuk <force@altlinux.org> 2.6.37-alt1
- 2.6.37

* Thu Dec 16 2010 Dmitry V. Levin <ldv@altlinux.org> 2.6.35-alt2.1
- Rebuilt for soname set-versions.

* Thu Aug 12 2010 Victor Forsiuk <force@altlinux.org> 2.6.35-alt2
- Fix bug with 'ip route get' (Closes: #23872).

* Thu Aug 05 2010 Victor Forsiuk <force@altlinux.org> 2.6.35-alt1
- 2.6.35

* Mon May 31 2010 Victor Forsiuk <force@altlinux.org> 2.6.34-alt1
- 2.6.34

* Tue Mar 02 2010 Victor Forsiuk <force@altlinux.org> 2.6.33-alt1
- 2.6.33

* Thu Feb 18 2010 Victor Forsiuk <force@altlinux.org> 2.6.31-alt2
- Provide symlinks in /usr/bin to all utilities usable by unpriviledge users (closes: #22887).
- Rebuild against libxtables.so.4.

* Fri Jan 15 2010 Victor Forsyuk <force@altlinux.org> 2.6.31-alt1
- 2.6.31

* Tue Sep 08 2009 Victor Forsyuk <force@altlinux.org> 2.6.29-alt1
- 2.6.29

* Fri Jan 16 2009 Victor Forsyuk <force@altlinux.org> 2.6.28-alt1
- 2.6.28

* Mon Dec 01 2008 Victor Forsyuk <force@altlinux.org> 2.6.26-alt1
- 2.6.26

* Sat Jun 14 2008 ALT QA Team Robot <qa-robot@altlinux.org> 2.6.25-alt1.1
- Automated rebuild with libdb-4.7.so.

* Thu May 22 2008 Victor Forsyuk <force@altlinux.org> 2.6.25-alt1
- 2.6.25
- Fix #15409 (segfault with tc qdisc).

* Fri Mar 14 2008 Victor Forsyuk <force@altlinux.org> 2.6.23-alt2
- Fix to restore backward compatibility with pre 2.6.22 kernels.

* Thu Mar 13 2008 Victor Forsyuk <force@altlinux.org> 2.6.23-alt1
- 2.6.23

* Mon Apr 02 2007 Victor Forsyuk <force@altlinux.org> 2.6.20.20070313-alt1
- 20070313 snapshot.
- Add versioned dependency on libnetlink package (fix ALT#10845). Thanks to ldv@.

* Tue Feb 06 2007 Victor Forsyuk <force@altlinux.org> 2.6.19.20061214-alt1
- 20061214 snapshot.
- Fix ALT#6277.

* Thu Oct 12 2006 Victor Forsyuk <force@altlinux.org> 2.6.18.20061002-alt1
- Updated to 20061002 snapshot.
- Really fixed path to iptables libdir (also for 64-bit arch build).
- Package shared libnetlink library.
- Add LOWER_UP and DORMANT flags (RH#202199).
- Fix ip.8 man page: add initcwnd option description (RH).

* Wed Apr 26 2006 Victor Forsyuk <force@altlinux.ru> 2.6.16.20060323-alt1
- Updated to 20060323 snapshot.
- Don't hardcode /usr/lib in tc (important for 64-bit arch).
- Own %%_libdir/tc.
- Manpages now included into the original package.

* Sat Mar 25 2006 ALT QA Team Robot <qa-robot@altlinux.org> 2.6.15.20060110-alt1.1
- Rebuilt with libdb4.4.

* Thu Jan 19 2006 Victor Forsyuk <force@altlinux.ru> 2.6.15.20060110-alt1
- Updated to 20060110 snapshot.
- Package routel and routef scripts.
- Add Fedora patches.
- Move big postsript docs to separate package.
- Correct path to iptables libdir (fixes iptables based targets support).

* Thu Feb 10 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.4.7.20020116-alt5.1
- Rebuilt with libdb4.3.

* Sat May 01 2004 Dmitry V. Levin <ldv@altlinux.org> 2.4.7.20020116-alt5
- Fixed the potential buffer overflow in nstat discovered by Steve Grubb,
  and a number of other related potential issues in nstat (Owl).
- Fixed default rtnetlink table (patch from pilot@, #3707).
- Implemented ipsectun support (patch from pilot@, #3708).
- Fixed "ss -f" mode.
- Added tc-cbq-details(8) manpage.

* Fri Feb 13 2004 Dmitry V. Levin <ldv@altlinux.org> 2.4.7.20020116-alt4
- Packaged arpd to separate subpackage.
- Rebuilt with libdb-4.2.so.

* Wed Nov 12 2003 Dmitry V. Levin <ldv@altlinux.org> 2.4.7.20020116-alt3
- Fixed netlink issue (CAN-2003-0856).
- Moved CBQ and HTB init scripts to separate packages (#3095).

* Thu Oct 16 2003 Dmitry V. Levin <ldv@altlinux.org> 2.4.7.20020116-alt2
- /sbin/ifcfg: fixed potential syntax errors (#2422).

* Wed Oct 15 2003 Dmitry V. Levin <ldv@altlinux.org> 2.4.7.20020116-alt1
- Build with TC_CONFIG_DIFFSERV enabled.

* Mon Oct 13 2003 Dmitry V. Levin <ldv@altlinux.org> 2.4.7-alt6.ss020116
- Updated to ss020116.
- Packaged new tools: arpd, ifstat, nstat, rtstat, ss.
- Removed obsolete patches:
  rh-config
  pld-owl-ll_types_proto
- Patched to use system headers - included ones seem to be broken.
- cbq.init: ignore config files with dots in their names (#3095).
- Added htb startup script.
- Moved Wondershaper to separate package.

* Wed Aug 27 2003 Dmitry V. Levin <ldv@altlinux.org> 2.4.7-alt5.ss010824
- Updated build dependencies, fixed build.

* Wed Feb 05 2003 Andy Gorev <horror@altlinux.ru> 2.4.7-alt4.ss010824
- Script cbq.init updated from v0.6.2 to v0.7.2
- Patch tc for HTB3 support
- Wondershaper scripts added to doc (lartc.org)
- README-cbq-use fix (added to doc)

* Wed Oct 30 2002 Dmitry V. Levin <ldv@altlinux.org> 2.4.7-alt3.ss010824
- Rebuilt in new environment.

* Tue Apr 02 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.4.7-alt2.ss010824
- Updated code to ss010824.
- Fixed build without kernel-source installed.
- Merged in RH patches:
  + %name-2.4.7-rh-config.patch
  + %name-2.4.7-rh-promisc-allmulti.patch
- Merged in Owl patches:
  + %name-2.4.7-pld-owl-ll_types_proto.patch
  + %name-2.4.7-owl-warnings.patch
- Added manpages from Owl.

* Tue Aug 14 2001 Alexander Bokovoy <ab@altlinux.ru> 2.4.7-alt1
- 2.4.7, cbq.init 0.6.2

* Thu Jan 04 2001 Dmitry V. Levin <ldv@fandra.org> 2.2.4-ipl10mdk
- Removed README.cbq-init, it is %_initdir/cbq now.
- Recompressed postscript documentation with bzip2 since
  our postscript viewer (gv) can show bzipped documents.

* Tue Dec 27 2000 Alexander Bokovoy <ab@avilink.net> 2.2.4-ipl9mdk
- Wrong dependency caused by wrong path (/sbin/arping) in example
  script dhcp-client-script fixed.

* Tue Dec 26 2000 Alexander Bokovoy <ab@avilink.net> 2.2.4-ipl8mdk
- Sally Floyd's papers added as well additional docs about CBQ
- cbq.init script integrated (it really should be in this package)

* Thu Oct 19 2000 Dmitry V. Levin <ldv@fandra.org> 2.2.4-ipl7mdk
- ss001007.
- Merge RH patches.

* Mon Aug 14 2000 Dmitry V. Levin <ldv@fandra.org> 2.2.4-ipl6mdk
- RE adaptions.

* Thu Aug 10 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.2.4-6mdk
- fix config files

* Wed Jul 19 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.2.4-5mdk
- BM

* Wed Jul 12 2000 Christian Zoffoli <czoffoli@linux-mandrake.com> 2.2.4-4mdk
- removed _sysconfdir 
- added %clean

* Wed Jul 12 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.2.4-3mdk
- fix a few typo (chrs scks :-) ) and make this spec short-circuit aware :
  *  _sysconfig/_sysconfdir
  *  creation of subdirs while installing
- Christian Zoffoli <czoffoli@linux-mandrake.com> : macroszifications

* Fri Apr 28 2000 Lenny Cartier <lenny@mandrakesoft.com> 2.2.4-2mdk
- fix group and files section

* Wed Mar 01 2000 Lenny Cartier <lenny@mandrakesoft.com> 2.2.4-1mdk
- mandrake build
- used latest release of 2.2.4 series / 000225
 
* Mon Apr 26 1999 Jan "Yenya" Kasprzak <kas@fi.muni.cz>
- Added $RPM_OPT_FLAGS
 
* Fri Apr 23 1999 Damien Miller <damien@ibs.com.au>
- Built RPM  
