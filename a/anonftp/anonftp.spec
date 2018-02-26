Name: anonftp
Version: 3.2
Release: alt1
Prefix: /var/ftp

Summary: The %prefix area for anonymous FTP access
License: public domain
Group: System/Servers
BuildArch: noarch

PreReq: setup >= 2.1.9-ipl15mdk
Conflicts: wu-ftpd

%description
This package contains %prefix area for anonymous FTP access.

%install
%__mkdir_p $RPM_BUILD_ROOT%prefix

%files
%attr(2775,root,ftpadmin) %prefix

%changelog
* Sun Oct 27 2002 Dmitry V. Levin <ldv@altlinux.org> 3.2-alt1
- Removed requirement on ftpserver.

* Wed Mar 20 2002 Dmitry V. Levin <ldv@alt-linux.org> 3.1-alt1
- Dropped all but %prefix directory.

* Fri Mar  2 2001 Ivan Zakharyaschev <vanyaz@mccme.ru> 3.0-ipl18mdk
- Fixed typo in %%post script.

* Mon Feb 26 2001 Dmitry V. Levin <ldv@fandra.org> 3.0-ipl17mdk
- Fixed typo in %%preun script.

* Tue Jan 30 2001 Dmitry V. Levin <ldv@fandra.org> 3.0-ipl16mdk
- Ported to new chrooted scheme.

* Sun Dec 17 2000 Dmitry V. Levin <ldv@fandra.org> 3.0-ipl15mdk
- Completely rewritten using new chroot scheme.

* Mon Dec  4 2000 Renaud Chaillat <rchaillat@mandrakesoft.com> 3.0-15mdk
- updated for glibc-2.2

* Thu Sep 21 2000 Renaud Chaillat <rchaillat@mandrakesoft.com> 3.0-14mdk
- changed ftpserver to wu-ftpd in requirements to avoid conflict
  with proftpd

* Wed Sep  6 2000 Renaud Chaillat <rchaillat@mandrakesoft.com> 3.0-13mdk
- added requires on setup (for /etc/passwd), including release
  number

* Wed Sep  6 2000 Renaud Chaillat <rchaillat@mandrakesoft.com> 3.0-12mdk
- BM /home/ftp => %prefix, needs update in /etc/passwd
  (admin needs move its public files manually)
- noreplace for passwd and group

* Thu Aug 24 2000 Renaud Chaillat <rchaillat@pc-1229.mandrakesoft.com> 3.0-11mdk
- compressed source

* Thu Jun  8 2000 Frederic Lepied <flepied@mandrakesoft.com> 3.0-10mdk
- added prereq on ftpserver to let the %post do its job
right.

* Mon May 29 2000 Adam Lebsack <adam@mandrakesoft.com> 3.0-9mdk
- change ppc LIBCSOVER and LIBNSLOVER to 6 and 1, respectively
- remove ld-linux.so from ppc

* Tue May 16 2000 Daouda LO <daouda@mandrakesoft.com> 3.0-8mdk
- who forget to put libtermcap* to %files ??

* Mon May 15 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.0-7mdk
- Remove ldconfig (let me know where it's needed)
- Fix build on alpha.

* Sun May 14 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 3.0-6mdk
- Fixed Yet Another Problem in Post Scripts (FYAPIPS).

* Sat May 13 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 3.0-5mdk
- Fix another problem in post scripts. (%preun)
- added ldconfig

* Fri May 12 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.0-4mdk
- Fix post scripts again.
- Add libtermcap.so.2 for ls :\

* Mon May 08 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 3.0-3mdk
- removed reference to $RPM_BUILD_ROOT in post scripts (DOH!)

* Sat Apr 22 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.0-2mdk
- %preun not %postun.

* Fri Apr  7 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 3.0-1mdk
- merged with Rawhide:
  Add BuildPrereqs
  add recompress from BeroFTPD - it's useful for ftpconversions
  remove sh. Having a shell in the chroot ftp-structure is a security
  problem, not a feature.
- our recompress is actually in the file, not redhat ;-)

* Thu Apr  6 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 2.8-9mdk
- fix group
- new libc

* Sun Mar 19 2000 John Buswell <johnb@mandrakesoft.com>
- Fixed support for PPC

* Mon Jan 17 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.8-6mdk

- ||: when fail on strip.

* Fri Jan 07 2000 Yoann Vandoorselaere <yoann@mandrakesoft.com>
- Removed conflict with /etc/ftpaccess from wu-ftpd package :
  use %post && %postun to modify it and don't include this file
  as one of ours to avoid this problem.

* Tue Jan 04 2000 John Buswell <johnb@mandrakesoft.com> 2.2-8mdk
- Added ppc arch
- fixed anonymous access

* Sun Oct 31 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Add a k6 arch
- glibc version 2.1.2

* Tue May 11 1999 Bernhard Rosenkränzer <bero@mandrakesoft.com>
- Some fixes (libc.so.6, not 6.1)
- fix build with arch=i[456789]86

* Tue May 11 1999 Bernhard Rosenkränzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 5)
- glibc version 2.1.1

* Tue Jan 12 1999 Cristian Gafton <gafton@redhat.com>
- add sparc

* Tue Jan 12 1999 Jeff Johnson <jbj@redhat.com>
- fix defattr typo (#784)
- newer libc

* Wed Jan 06 1999 Cristian Gafton <gafton@redhat.com>
- abuse the %attr settings instead of massive chown
- avoid cp-av because it breaks on symlinks (the wonders of lchown/chown
- rebuild for glibc 2.1

* Thu Sep 10 1998 Cristian Gafton <gafton@redhat.com>
- newer libc

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- updated for the newer glibc libs

* Thu Nov 06 1997 Donnie Barnes <djb@redhat.com>
- Built with glibc for the first time
- moved BuildRoot to /var/tmp
- mega-reworking of the spec file

* Mon Mar 03 1997 Erik Troan <ewt@redhat.com>
- Requires ftpserver virtual package now (which wu-ftpd provides).

