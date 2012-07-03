Name: traceroute
Version: 2.0.18
Release: alt1
Epoch: 1

Summary: Traces the route taken by packets over an IPv4/IPv6 network
License: GPLv2+
Group: Monitoring
Url: http://traceroute.sourceforge.net/

# http://downloads.sourceforge.net/traceroute/traceroute-%version.tar.gz
Source: traceroute-%version.tar
# git://git.altlinux.org/gears/t/traceroute.git
Patch: traceroute-%version-%release.patch

# due to traceroute6
Conflicts: iputils < 0:20020927-alt3

%description
traceroute tracks the route packets taken from an IP network on their way
to a given host.  It utilizes the IP protocol's time to live (TTL) field
and attempts to elicit an ICMP TIME_EXCEEDED response from each gateway
along the path to the host.

%prep
%setup
%patch -p1

%build
%make_build CFLAGS='%optflags -W' LDFLAGS=

%install
install -pD -m755 traceroute/traceroute %buildroot/bin/traceroute
install -pD -m644 traceroute/traceroute.8 %buildroot%_man1dir/traceroute.1
ln -s traceroute %buildroot/bin/traceroute6
ln -s traceroute.1 %buildroot%_man1dir/traceroute6.1

%files
/bin/*
%_man1dir/*

%changelog
* Wed Sep 07 2011 Dmitry V. Levin <ldv@altlinux.org> 1:2.0.18-alt1
- Updated to 2.0.18.

* Thu Apr 21 2011 Dmitry V. Levin <ldv@altlinux.org> 1:2.0.17-alt1
- Updated to 2.0.17.

* Fri Jun 05 2009 Dmitry V. Levin <ldv@altlinux.org> 1:2.0.12-alt1
- Packaged traceroute-2.0.12 from traceroute.sourceforge.net.

* Thu Oct 05 2006 Dmitry V. Levin <ldv@altlinux.org> 1:1.0.4-alt1
- Updated to 1.0.4.
- Make traceroute's output more like LBNL's traceroute (Owl).

* Thu Nov 24 2005 Dmitry V. Levin <ldv@altlinux.org> 1:1.0.3-alt4
- Relocated manual pages to 1st section.

* Mon Nov 14 2005 Dmitry V. Levin <ldv@altlinux.org> 1:1.0.3-alt3
- Packaged traceroute6 within this package.
- Fixed typos in traceroute(8) manual page.

* Thu Nov 10 2005 Dmitry V. Levin <ldv@altlinux.org> 1:1.0.3-alt2
- Removed backwards compatibillity symlink.
- Updated compatibility patch from Fedora.
- Fixed compilation warnings.
- Added -P option.

* Thu Nov 03 2005 Victor Forsyuk <force@altlinux.ru> 1:1.0.3-alt1
- Replaced with traceroute written by Olaf Kirch.

* Wed Aug 27 2003 Dmitry V. Levin <ldv@altlinux.org> 1.4a12-alt7
- Reworked drop privs patch, to make -i option work for root.
- Fixed build with -Werror.
- Relocated traceroute binary from %_sbindir to /bin;
  added backwards compatibillity symlink.
- Keep traceroute at mode 700 ("restricted") in the package,
  but default it to "public" in %post when the package is first
  installed.  This avoids a race and fail-open behavior (Owl).

* Mon Aug 25 2003 Dmitry V. Levin <ldv@altlinux.org> 1.4a12-alt6
- Explicitly use old autoconf for build.
- Merged RH patches:
  + fix for -i option;
  + enhanced -t option.

* Wed Oct 16 2002 Dmitry V. Levin <ldv@altlinux.org> 1.4a12-alt5
- Added control support for traceroute.

* Tue Apr 09 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.4a12-alt4
- Updated droppriv patch (chroot to /var/resolv).

* Thu Apr 04 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.4a12-alt3
- When drop root for root user, switch to "iputils" user
  (sync with iputils package).

* Wed Apr 03 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.4a12-alt2
- Redone error reporting.
- Drop root also for root.

* Wed Dec 05 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.4a12-alt1
- 1.4a12
- Integrated Mandrake & Redhat & Owl patches

* Wed Oct 04 2000 Dmitry V. Levin <ldv@fandra.org> 1.4a7-ipl1mdk
- 1.4a7
- Merge RH patches.
- Automatically added BuildRequires.

* Mon Jul 31 2000 Francis Galiegue <fg@mandrakesoft.com> 1.4a5-13mdk
- More macros
- let spec-helper do its job

* Fri Jul 21 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.4a5-12mdk
- BM, macros

* Wed Apr 05 2000 John Buswell <johnb@mandrakesoft.com> 1.4a5-11mdk
- fix vendor tag

* Thu Mar 30 2000 John Buswell <johnb@mandrakesoft.com> 1.4a5-10mdk
- fix groups
- spec-helper

* Wed Jan 12 2000 Pixel <pixel@mandrakesoft.com>
- fix build as non-root (removed call to make install, done by hand)

* Thu Nov  4 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Fix wrong patch :-\.

* Wed Jul 21 1999 Gregus <gregus@etudiant.net>
- Add fr

* Tue Jul 12 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- bzip2 manpage

* Thu Jul  8 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Merging with RH patchs :
    * avoid unaligned traps writing into the output data area.
    * fix segfault when host cannot be reached through if (#2819)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 14)

* Fri Mar 19 1999 Jeff Johnson <jbj@redhat.com>
- strip binaries.

* Sun Feb 07 1999 Preston Brown <pbrown@redhat.com>
- patch added to automatically determine interface to route through

* Fri Jan 22 1999 Jeff Johnson <jbj@redhat.com>
- use %configure
- fix 64 bit problem on alpha (#919)

* Wed Jan 13 1999 Bill Nottingham <notting@redhat.com>
- configure fix for arm

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Dec 16 1997 Cristian Gafton <gafton@redhat.com>
- updated the security patch (ouch!). Without the glibc fix, it could be
  worthless anyway

* Sat Dec 13 1997 Cristian Gafton <gafton@redhat.com>
- added a security patch fix

* Wed Oct 22 1997 Erik Troan <ewt@redhat.com>
- added fix from Christopher Seawood

* Mon Sep 22 1997 Erik Troan <ewt@redhat.com>
- updated to 1.4a5 for security fixes; release 1 is for RH 4.2, release 2
  is against glibc

* Fri Jul 18 1997 Erik Troan <ewt@redhat.com>
- built against glibc
