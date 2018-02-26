Name: ntp
Version: 4.2.4
%define vers_rc p7
Release: alt5%{?vers_rc:.%vers_rc}
%define srcname %name-%version%{?vers_rc:-%vers_rc}

Summary: The Network Time Protocol (NTP)
License: BSD-Style
Group: System/Configuration/Other
Url: http://www.ntp.org/

Packager: Dmitry Lebkov <dlebkov@altlinux.ru>

Source0: ftp://ftp.udel.edu/pub/ntp/ntp4/%srcname.tar.bz2
Source1: ntpd.init
Source2: ntpd.sysconfig
Source3: %name.conf
Source4: %name.keys

Source11: ntp.1
Source12: ntpd.8
Source13: ntpdate.8
Source14: ntpsweep.8

Patch1: %name-4.2.4-p7-alt-compile-dirty-hack-NANO.patch

Requires: ntp-doc = %version-%release
Requires: ntp-utils = %version-%release
Requires: ntpdate = %version-%release
Requires: ntpd = %version-%release

# due to readline library linked with tinfo.
BuildPreReq: libreadline-devel >= 4.3-alt5

# due to ntp_drop_priv.
BuildRequires: libcap-devel

# Root directory for chrooted environment, must not be same as real system root.
%define ROOT /var/lib/ntpd

%package aux
Summary: The Network Time Protocol (NTP) auxiliary package
Group: System/Configuration/Other
Conflicts: ntp < 4.1.1b

%package doc
Summary: The Network Time Protocol (NTP) documentation
Group: Development/Other
Requires: ntp-aux = %version-%release

%package utils
Summary: The Network Time Protocol (NTP) utilities
Group: System/Base
Requires: ntpdate = %version-%release

%package -n ntpdate
Summary: Set the date and time via NTP
Group: System/Base
Requires: ntp-aux = %version-%release
Requires(pre): shadow-utils
Requires: /var/empty

%package -n ntpd
Summary: The Network Time Protocol daemon
Group: System/Servers
Requires: ntpdate = %version-%release
Obsoletes: xntp3
Requires(pre): shadow-utils
PreReq: service, coreutils
# due to ntp_intres.
Requires: /var/resolv
Provides: ntp-server

%description
The Network Time Protocol (NTP) is used to synchronize the time
of a computer client or server to another server or reference time source,
such as a radio or satellite receiver or modem.  It provides client
accuracies typically within a millisecond on LANs and up to a few tens of
milliseconds on WANs.

%description aux
The Network Time Protocol (NTP) is used to synchronize the time
of a computer client or server to another server or reference time source,
such as a radio or satellite receiver or modem.  It provides client
accuracies typically within a millisecond on LANs and up to a few tens of
milliseconds on WANs.

This is an auxiliary package.

%description doc
The Network Time Protocol (NTP) is used to synchronize the time
of a computer client or server to another server or reference time source,
such as a radio or satellite receiver or modem.  It provides client
accuracies typically within a millisecond on LANs and up to a few tens of
milliseconds on WANs.

This package contains NTP documentation.

%description utils
The Network Time Protocol (NTP) is used to synchronize the time
of a computer client or server to another server or reference time source,
such as a radio or satellite receiver or modem.  It provides client
accuracies typically within a millisecond on LANs and up to a few tens of
milliseconds on WANs.

This package contains various NTP utilities.

%description -n ntpd
The Network Time Protocol (NTP) is used to synchronize the time
of a computer client or server to another server or reference time source,
such as a radio or satellite receiver or modem.  It provides client
accuracies typically within a millisecond on LANs and up to a few tens of
milliseconds on WANs.

This package contains Network Time Protocol daemon.

%description -n ntpdate
The Network Time Protocol (NTP) is used to synchronize the time
of a computer client or server to another server or reference time source,
such as a radio or satellite receiver or modem.  It provides client
accuracies typically within a millisecond on LANs and up to a few tens of
milliseconds on WANs.

This package contains ntpdate program for retrieving the date and time
from remote machines via a network.

%prep
%setup -q -n %srcname

%patch1 -p1

# Fix progname initialization when argc==0.
fgrep -rl 'progname = argv[0];' . |
	xargs grep -l 'main *(' |
	while read f; do
		n="${f##*/}"
		n="${n%%.c}"
		subst 's/progname = argv\[0\];/progname = argc ? argv[0] : "PROGNAME";/' "$f"
		subst "s/PROGNAME/$n/" "$f"
	done

%__install -p -m644 %SOURCE2 ntpd.sysconfig
%__install -p -m644 $RPM_SOURCE_DIR/{ntp.1,{ntpd,ntpdate,ntpsweep}.8} .

find -type f -print0 |
	xargs -r0 %__grep -FZl '@ROOT@' -- |
	xargs -r0 %__subst -p 's,@ROOT@,%ROOT,g' --

%build
%add_optflags -D_GNU_SOURCE
%define _bindir %_sbindir
#autoreconf --force --verbose
%configure --without-openssl-libdir --without-openssl-incdir --without-crypto --without-readline \
		--enable-linuxcaps
echo '#define HAVE_LIBREADLINE 1' >>config.h

%make_build

%install
%makeinstall transform=
%__install -p -m755 scripts/ntpsweep $RPM_BUILD_ROOT%_sbindir/

# Manpages.
%__mkdir_p $RPM_BUILD_ROOT{%_man1dir,%_man8dir}
%__install -p -m644 ntp.1 $RPM_BUILD_ROOT%_man1dir/
%__install -p -m644 {ntpd,ntpdate,ntpsweep}.8 $RPM_BUILD_ROOT%_man8dir/
for f in $RPM_BUILD_ROOT%_sbindir/*; do
	t="$RPM_BUILD_ROOT%_man8dir/${f##*/}.8"
	[ -f "$t" ] || %__ln_s ../man1/ntp.1 "$t"
done

# Docs.
%define docdir %_docdir/%name-%version
%__mkdir_p $RPM_BUILD_ROOT%docdir
%__cp -a COPYRIGHT NEWS TODO WHERE-TO-START README.bk README.hackers README.refclocks README.versions html \
	$RPM_BUILD_ROOT%docdir/

%__install -pD -m755 %SOURCE1 $RPM_BUILD_ROOT%_initdir/ntpd
%__install -pD -m644 ntpd.sysconfig $RPM_BUILD_ROOT%_sysconfdir/sysconfig/ntpd
%__install -pD -m600 %SOURCE3 $RPM_BUILD_ROOT%_sysconfdir/%name.conf

%__mkdir_p $RPM_BUILD_ROOT%ROOT/tmp
%__install -pD -m600 %SOURCE4 $RPM_BUILD_ROOT%ROOT%_sysconfdir/%name/keys
touch $RPM_BUILD_ROOT%ROOT%_sysconfdir/%name/{drift,step-tickers}
%__ln_s ..%ROOT%_sysconfdir/%name $RPM_BUILD_ROOT%_sysconfdir/

%define r_dir %ROOT%_sysconfdir/%name
%define r_link %_sysconfdir/%name

%pre -n ntpdate
/usr/sbin/groupadd -r -f ntpd
/usr/sbin/useradd -r -g ntpd -d /dev/null -s /dev/null -n ntpd >/dev/null 2>&1 ||:

%pre -n ntpd
/usr/sbin/groupadd -r -f ntpd
/usr/sbin/useradd -r -g ntpd -d /dev/null -s /dev/null -n ntpd >/dev/null 2>&1 ||:
f=%r_link
if [ -d "$f" -a ! -L "$f" ]; then
	%__rm -rf "$f"
	/bin/touch "$f.RPMLOCK"
fi

%post -n ntpd
if [ $1 = 1 ]; then
        /sbin/chkconfig --add ntpd
fi
d=%r_dir
f=%r_link
if [ -f "$f.RPMLOCK" -a -d "$f" -a ! -d "$d.RPMSAVE" ]; then
	%__mv "$d" "$d.RPMSAVE"
	%__rm -f "$f.RPMLOCK"
else
	/sbin/service ntpd condrestart ||:
fi

%preun -n ntpd
%preun_service ntpd

%triggerpostun -n ntpd -- %name < 4.1.1b
d=%r_dir
if [ -d "$d.RPMSAVE" -a ! -d "$d" ]; then
	%__mv "$d.RPMSAVE" "$d"
	/sbin/service ntpd condrestart ||:
fi

%files

%files aux

%files doc
%dir %docdir
%docdir/html

%files utils
%_sbindir/*
%_mandir/man?/*
%exclude %_sbindir/ntpd
%exclude %_sbindir/ntpdate
%exclude %_man8dir/ntpd.*
%exclude %_man8dir/ntpdate.*

%files -n ntpdate
%_sbindir/ntpdate
%_man8dir/ntpdate.*
%dir %docdir
%docdir/[A-Z]*

%files -n ntpd
%config %_initdir/ntpd
%config(noreplace) %_sysconfdir/sysconfig/ntpd
%config(noreplace) %_sysconfdir/%name.conf
%_sysconfdir/%name
%_sbindir/ntpd
%_man8dir/ntpd.*

%defattr(640,root,ntpd,710)
%dir %ROOT
%dir %ROOT%_sysconfdir
%attr(1770,root,ntpd) %dir %ROOT/tmp
%attr(1770,root,ntpd) %dir %ROOT%_sysconfdir/%name
%config(noreplace) %ROOT%_sysconfdir/%name/keys
%config(noreplace) %verify(not md5 size mtime) %ROOT%_sysconfdir/%name/step-tickers
%attr(640,ntpd,ntpd) %ghost %ROOT%_sysconfdir/%name/drift

%changelog
* Wed May 20 2009 Dmitry Lebkov <dlebkov@altlinux.ru> 4.2.4-alt5.p7
- 4.2.4p7
- fix for CVE-2009-1252 (closes: #20099)
- fix for CVE-2009-0159 (closes: #19779)

* Sun Apr 05 2009 Stanislav Ievlev <inger@altlinux.org> 4.2.4-alt4.p6.1
- Provides ntp-server

* Sat Jan 10 2009 Dmitry Lebkov <dlebkov@altlinux.ru> 4.2.4-alt4.p6
- 4.2.4p6 ( fix for http://www.ocert.org/advisories/ocert-2008-016.html )
- LSB header for init-script

* Sat Apr 05 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 4.2.4-alt3.p4
- add NTPD_GROUP to /etc/sysconfig/ntpd and init-script

* Tue Apr 01 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 4.2.4-alt2.p4
- add ntptrace output to service ntp status (#8411)
  + fix from Denis Smirnov <mithraen@altlinux.ru> in 4.2.2-alt2.p4.3
- add pid-file creation to init-script (#3825)

* Sun Mar 30 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 4.2.4-alt1.p4
- 4.2.4p4
- fix for #11139 and #13233

* Mon Mar 12 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 4.2.4-alt1.p0
- 4.2.4p0

* Fri Nov 24 2006 Denis Smirnov <mithraen@altlinux.ru> 4.2.2-alt1.p4.3
- fix buffer overflow in WWV Audio driver (#216309 from fedora)

* Sun Nov 19 2006 Denis Smirnov <mithraen@altlinux.ru> 4.2.2-alt1.p4.2
- Chroot and change user to ntpd by default
- Ignore -T in ntpdate (for compatibility with old /etc/sysconfig/ntp)

* Fri Nov 17 2006 Denis Smirnov <mithraen@altlinux.ru> 4.2.2-alt1.p4.1
- Version update

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 4.1.2-alt3.1
- Rebuilt with libreadline.so.5.

* Tue Apr 20 2004 Dmitry V. Levin <ldv@altlinux.org> 4.1.2-alt3
- ntpd, ntpdate:
  Do not try to drop privileges when run by unprivileged user.
- ntpd: Create pid file by default.
- Fix progname initialization when argc==0.
- Updated alt-tinfo patch (now called alt-readline patch).

* Sun Feb 15 2004 Dmitry V. Levin <ldv@altlinux.org> 4.1.2-alt2
- Fixed chroot jailing and droppriv code (#3461).
- Changed default settings:
  ntpd: switch to ntpd:ntpd, chroot to %ROOT;
  ntp_intres: switch to ntpd:ntpd, chroot to /var/resolv;
  ntpdate: switch to ntpd:ntpd, chroot to /var/empty.
- Added auxiliary subpackage for better interpackage dependencies.

* Sun Aug 17 2003 Dmitry V. Levin <ldv@altlinux.org> 4.1.2-alt1
- Updated to 4.1.2.
- Rewritten start/stop script to new rc scheme.

* Tue Feb 25 2003 Dmitry V. Levin <ldv@altlinux.org> 4.1.1c-alt1.rc1
- Updated to 4.1.1c-rc1.
- More new RH patches to be considered:
  4.1.73-limit, 4.1.1c-loopfilter.

* Tue Nov 19 2002 Dmitry V. Levin <ldv@altlinux.org> 4.1.1b-alt1
- Updated to 4.1.1b.
- Merged in RH patches:
  + ntp-4.1.0b-rc1-genkey
  + ntp-4.1.1a-genkey2
  - ntp-4.1.1a-mfp (not needed in 4.1.1b)
- Updated droproot patch.
- Removed ntp-4.0.99j-rh-vsnprintf patch (merged upstream).
- Enabled (fixed) readline support.
- Packaged ntpsweep.
- Added manpages from Debian
  (and mentioned our chroot support options there).
- Split into several subpackages.

* Tue Apr 16 2002 Dmitry V. Levin <ldv@altlinux.org> 4.1.1-alt3
- Updated startup script.
- Updated dependencies.

* Mon Apr 01 2002 Dmitry V. Levin <ldv@altlinux.org> 4.1.1-alt2
- 4.1.1
- Chrooted by default to %ROOT.
- Updated default config (cornet).

* Wed Oct 03 2001 Dmitry V. Levin <ldv@altlinux.ru> 4.1.0-alt1
- 4.1.0 (not chrooted yet).

* Thu May 17 2001 Dmitry V. Levin <ldv@altlinux.ru> 4.0.99k-ipl4mdk
- Conflicts: xntp3
- Use service macros.

* Mon Apr 09 2001 Dmitry V. Levin <ldv@altlinux.ru> 4.0.99k-ipl3mdk
- Fixed buffer overrun.
- Fixed glibc-2.2.2 compilation.

* Sat Jan 20 2001 Dmitry V. Levin <ldv@fandra.org> 4.0.99k-ipl2mdk
- RE adaptions.

* Thu Aug 31 2000 Warly <warly@mandrakesoft.com> 4.0.99k-2mdk
- add condrestart

* Mon Jul 24 2000 Warly <warly@mandrakesoft.com> 4.0.99k-1mdk
- new release
- BM

* Wed Apr 05 2000 Daouda Lo <daouda@mandrakesoft.com> 4.0.99g-3mdk
- fix the conf files permissions
- bunzip'ed conf files

* Fri Mar 31 2000 Warly <warly@mandrakesoft.com> 4.0.99g-2mdk
- New group: System/Configuration/Other

* Tue Mar 07 2000 Daouda LO <daouda@mandrakesoft.com>
- Mandrakised (relocatable + %%define )

* Sun May 23 1999 David E. Myers <dem@skyline.rtp.nc.us>
- Changes for submission to Red Hat Contrib|Net.

* Wed Apr 14 1999 Cristian Gafton <gafton@redhat.com>
- disallow remote updates by default in ntp.conf (#2170)

* Fri Mar 26 1999 Cristian Gafton <gafton@redhat.com>
- use %configure
- fix initscript not to sit out the output of ntpdate (use syslog instead)
- eliminate subshell from the install stage

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 9)

* Sun Nov 22 1998 Jeff Johnson <jbj@redhat.com>
- ntp.conf: default local clock stratum to 10.

* Wed Oct 21 1998 Jeff Johnson <jbj@redhat.com>
- update to 5.93e.

* Mon Oct 12 1998 Cristian Gafton <gafton@redhat.com>
- strip binaries

* Thu Aug  6 1998 Jeff Johnson <jbj@redhat.com>
- update to 5.93c.
- implement suggestions from James Youngman <JYoungman@vggas.com>:
-   correct default /etc/ntp/keys
-   use /etc/ntp/step-tickers for ntpdate hosts

* Sun May 10 1998 Cristian Gafton <gafton@redhat.com>
- start it after named

* Mon May 04 1998 Jeff Johnson <jbj@redhat.com>
- Update to 5.93.

* Mon Feb  2 1998 Jeff Johnson <jbj@jbj.org>
- Fiddles for RH-5.0. Update to xntp3-5.92.

* Mon Feb  2 1998 Jeff Johnson <jbj@jbj.org>
- Fiddles for RH-5.0. Update to xntp3-5.92.

* Sat Oct 18 1997 Manoj Kasichainula <manojk@io.com>
- Initial release for 5.91
