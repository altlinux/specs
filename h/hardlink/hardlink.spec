Name: hardlink
Version: 1.0
Release: alt6

Summary: Consolidate duplicate files via hardlinks
License: GPLv2+
Group: System/Base
Url: http://cvs.fedora.redhat.com/viewcvs/devel/hardlink/

Source0: hardlink.c
Source1: hardlink.1

%description
This package contains hardlink, an utility which consolidates duplicate
files in one or more directories using hardlinks.

hardlink traverses one or more directories searching for duplicate files.
When it finds duplicate files, it uses one of them as the master.  It then
removes all other duplicates and places a hardlink for each one pointing
to the master file.  This allows for conservation of disk space where
multiple directories on a single filesystem contain many duplicate files.

Since hard links can only span a single filesystem, hardlink is only
useful when all directories specified are on the same filesystem.

%prep
%setup -cT

%build
%__cc %optflags $(getconf LFS_CFLAGS) %_sourcedir/hardlink.c -o hardlink

%install
install -pDm755 hardlink %buildroot%_bindir/hardlink
install -pDm644 %_sourcedir/hardlink.1 %buildroot%_man1dir/hardlink.1

%files
%_bindir/hardlink
%_man1dir/hardlink.*

%changelog
* Tue Dec 27 2011 Dmitry V. Levin <ldv@altlinux.org> 1.0-alt6
- Merged with hardlink-1.0-owl2.

* Sat Nov 26 2011 Dmitry V. Levin <ldv@altlinux.org> 1.0-alt5
- Merged with hardlink-1.0-owl1 (closes: #26632).

* Tue Feb 15 2011 Dmitry V. Levin <ldv@altlinux.org> 1.0-alt4
- Rebuilt.

* Thu Aug 30 2007 Dmitry V. Levin <ldv@altlinux.org> 1.0-alt3
- Fixed help/usage output and return values.

* Thu Aug 30 2007 Dmitry V. Levin <ldv@altlinux.org> 1.0-alt2
- Relocated hardlink(1) utility from %_sbindir to %_bindir.
- Cleaned up specfile.

* Mon Aug 27 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.0-alt1
- Built for ALT Linux.

* Thu Aug 23 2007 Jindrich Novy <jnovy@redhat.com> - 1:1.0-5
- update License
- rebuild for BuildID

* Mon Apr 23 2007 Jindrich Novy <jnovy@redhat.com> - 1:1.0-4
- include sources in debuginfo package (#230833)

* Mon Feb  5 2007 Jindrich Novy <jnovy@redhat.com> - 1:1.0-3
- merge review related spec fixes (#225881)

* Sun Oct 29 2006 Jindrich Novy <jnovy@redhat.com> - 1:1.0-2
- update docs to describe highest verbosity -vv option (#210816)
- use dist

* Wed Jul 12 2006 Jindrich Novy <jnovy@redhat.com> - 1:1.0-1.23
- remove ugly suffixes added by rebuild script

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1:1.0-1.21.2.1
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1:1.0-1.20.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1:1.0-1.19.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Nov 14 2005 Jindrich Novy <jnovy@redhat.com>
- more spec cleanup - thanks to Matthias Saou (#172968)
- use UTF-8 encoding in the source

* Mon Nov  7 2005 Jindrich Novy <jnovy@redhat.com>
- add hardlink man page
- add -h option
- use _sbindir instead of /usr/sbin directly
- don't warn because of uninitialized variable
- spec cleanup

* Fri Aug 26 2005 Dave Jones <davej@redhat.com>
- Document hardlink command line options. (Ville Skytta) (#161738)

* Wed Apr 27 2005 Jeremy Katz <katzj@redhat.com>
- don't try to hardlink 0 byte files (#154404)

* Fri Apr 15 2005 Florian La Roche <laroche@redhat.com>
- remove empty scripts

* Tue Mar  1 2005 Dave Jones <davej@redhat.com>
- rebuild for gcc4

* Tue Feb  8 2005 Dave Jones <davej@redhat.com>
- rebuild with -D_FORTIFY_SOURCE=2

* Tue Jan 11 2005 Dave Jones <davej@redhat.com>
- Add missing Obsoletes: kernel-utils

* Sat Dec 18 2004 Dave Jones <davej@redhat.com>
- Initial packaging, based upon kernel-utils.
