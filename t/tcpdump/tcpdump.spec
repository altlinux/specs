Name: tcpdump
Version: 4.1.1
Release: alt3
Epoch: 1

Summary: A network traffic monitoring tool
License: BSD
Group: Monitoring
Url: http://www.tcpdump.org

# git://git.altlinux.org/gears/t/tcpdump
Source: %name-%version-%release.tar

Requires: /var/resolv, libpcap0.8 >= 2:1.1.1

# for test suite
%{?!_without_check:%{?!_disable_check:BuildRequires: sharutils}}

BuildRequires: libpcap-devel >= 2:1.1.1, libssl-devel

%description
Tcpdump is a command-line tool for monitoring network traffic.  Tcpdump
can capture and display the packet headers on a particular network
interface or on all interfaces.  Tcpdump can display all of the packet
headers, or just the ones that match particular criteria.

%prep
%setup -n %name-%version-%release
bzip2 -9k CHANGES

%build
%add_optflags -fno-strict-aliasing
%autoreconf
%configure --without-smi --with-crypto --enable-ipv6 \
	--with-user=tcpdump --with-chroot=/var/resolv
%make_build

%install
mkdir -p %buildroot%_datadir/%name
%makeinstall_std
install -pm755 *.awk %buildroot%_datadir/%name/

%check
%make_build -k check

%post
/usr/sbin/groupadd -r -f tcpdump
/usr/sbin/useradd -r -g tcpdump -d /dev/null -s /dev/null -n tcpdump >/dev/null 2>&1 ||:

%files
%_sbindir/*
%_datadir/%name
%_mandir/man?/*
%doc CHANGES.bz2 CREDITS LICENSE README TODO

%changelog
* Fri Feb 25 2011 Dmitry V. Levin <ldv@altlinux.org> 1:4.1.1-alt3
- Rebuilt for debuginfo.

* Fri Oct 01 2010 Dmitry V. Levin <ldv@altlinux.org> 1:4.1.1-alt2
- Rebuilt with libcrypto.so.10.

* Thu Jun 17 2010 Dmitry V. Levin <ldv@altlinux.org> 1:4.1.1-alt1
- Updated to 4.1.1.
- Enabled test suite.

* Tue Dec 02 2008 Dmitry V. Levin <ldv@altlinux.org> 1:3.9.8-alt1
- Updated to 3.9.8.

* Thu Aug 02 2007 Dmitry V. Levin <ldv@altlinux.org> 1:3.9.7-alt1
- Updated to 3.9.7 (fixes CVE-2007-3798: BGP dissector integer overflow).

* Sat Mar 03 2007 Dmitry V. Levin <ldv@altlinux.org> 1:3.9.5-alt1
- Updated to 3.9.5.
- Disabled chroot in dump truncation mode (#5027).
- Applied upstream fix for a potential off-by-one buffer overflow
  in the ieee802.11 printer (CVE-2007-1218, #10983).

* Thu Nov 17 2005 Dmitry V. Levin <ldv@altlinux.org> 1:3.9.4-alt1
- Updated to 3.9.4.
- Updated patches.

* Wed May 11 2005 Dmitry V. Levin <ldv@altlinux.org> 1:3.8.2-alt3
- Applied fixes from Debian package, including fixes for
  CAN-2005-1278, CAN-2005-1279 and CAN-2005-1280.

* Mon Jan 17 2005 Dmitry V. Levin <ldv@altlinux.org> 1:3.8.2-alt2
- Fixed compilation issues detected by gcc-3.4.3.

* Mon May 10 2004 ALT QA Team Robot <qa-robot@altlinux.org> 1:3.8.2-alt1.1
- Rebuilt with openssl-0.9.7d.

* Tue Mar 30 2004 Dmitry V. Levin <ldv@altlinux.org> 1:3.8.2-alt1
- Updated to 3.8.2, updated patches.
- Fixed build with fresh autotools.

* Tue Jan 13 2004 Dmitry V. Levin <ldv@altlinux.org> 1:3.8.1-alt2
- Backported two fixes from CVS, thanks to Jonathan Heusser.

* Fri Jan 09 2004 Dmitry V. Levin <ldv@altlinux.org> 1:3.8.1-alt1
- Updated to 3.8.1, updated patches.

* Thu Feb 27 2003 Dmitry V. Levin <ldv@altlinux.org> 1:3.7.2-alt1
- Updated to 3.7.2
- Removed rh-alt-snaplen patch (merged upstream).
- Explicitly require autoconf = 2.13 for build.
- Explicitly disable libsmi support.

* Wed Sep 18 2002 Dmitry V. Levin <ldv@altlinux.org> 1:3.7.1-alt3
- Enhanced previous fix.

* Tue Sep 17 2002 Dmitry V. Levin <ldv@altlinux.org> 1:3.7.1-alt2
- Fixed error() redefine problem (reported by Alexey M. Tourbin).

* Tue Apr 09 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:3.7.1-alt1
- Updated code to 3.7.1
- Updated droppriv patch (chroot to /var/resolv).

* Mon Mar 04 2002 Stanislav Ievlev <inger@altlinux.ru> 1:3.6.2-ipl2mdk
- Rebuilt, added some patches from RH
- Added drop-root and chroot patch

* Wed Feb 07 2001 Dmitry V. Levin <ldv@fandra.org> 3.6.2-ipl1mdk
- 3.6.2

* Tue Jan 09 2001 Dmitry V. Levin <ldv@fandra.org> 3.6.1-ipl1mdk
- 3.6.1
- Enabled ipv6 support.

* Fri Sep 01 2000 Dmitry V. Levin <ldv@fandra.org> 3.5.2-ipl1mdk
- 3.5.2
- libpcap and arpwatch now in their own packages.
- RE adaptions.

* Wed Sep 11 1999 Dmitry V. Levin <ldv@fandra.org>
- Fandra adaptions

* Mon Aug 23 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- fix bogus includes directory that make iplog fail to compile (even pcap
  headers were bogus while seeking for other includes)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 10)

* Fri Mar 19 1999 Jeff Johnson <jbj@redhat.com>
- strip binaries.

* Wed Jan 13 1999 Bill Nottingham <notting@redhat.com>
- autoconf fixes for arm

* Tue Sep 29 1998 Jeff Johnson <jbj@redhat.com>
- libpcap description typo.

* Sat Sep 19 1998 Jeff Johnson <jbj@redhat.com>
- fix arpwatch summary line.

* Mon Aug 17 1998 Jeff Johnson <jbj@redhat.com>
- enable arpwatch

* Mon Aug  3 1998 Jeff Johnson <jbj@redhat.com>
- separate package for libpcap.
- update tcpdump to 3.4, libpcap to 0.4.
- added arpwatch (but disabled for now)

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sat May  2 1998 Alan Cox <alan@rehat.com>
- Added the SACK printing fix so you can dump Linux 2.1+.

* Tue Oct 21 1997 Erik Troan <ewt@redhat.com>
- updated to release 3.4a5
- uses a buildroot and %%attr

* Thu Jul 17 1997 Erik Troan <ewt@redhat.com>
- built against glibc
