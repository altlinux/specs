Name: ncompress
Version: 4.2.4.2
Release: alt1

Summary: Fast compression and decompression utilities
License: Public domain
Group: Archiving/Compression
Url: http://ncompress.sourceforge.net/
Packager: Dmitry V. Levin <ldv@altlinux.org>

# ftp://ibiblio.org/pub/Linux/utils/compress/ncompress-%version.tar.bz2
Source: ncompress-%version.tar
Patch1: ncompress-4.2.4-rh-lfs.patch
Patch2: ncompress-4.2.4-rh-endians.patch

%description
This package contains the compress and uncompress file compression and
decompression utilities, which are compatible with the original UNIX
compress utility (.Z file extensions).  These utilities can't handle
gzipped (.gz file extensions) files, but gzip can handle compressed files.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
%add_optflags -DNOFUNCDEF -DDIRENT -DSYSDIR -DUTIME_H -DUSERMEM=800000 -DREGISTERS=20 -DIBUFSIZ=1024 -DOBUFSIZ=1024

%ifarch %ix86 x86_64
%add_optflags -DBYTEORDER=4321
%endif

%ifarch sparc m68k armv4l ppc
%add_optflags -DBYTEORDER=1234
%endif

%ifarch alpha
%add_optflags -DNOALLIGN=0 -DBYTEORDER=4321
%endif

%__cc %optflags `getconf LFS_CFLAGS` -DCOMPILE_DATE="\"`LC_TIME=C date +%%Y%%m%%d`\"" compress42.c -o compress

%install
install -pD -m755 compress %buildroot%_bindir/compress
install -pD -m644 compress.1 %buildroot%_man1dir/compress.1
ln -s compress %buildroot%_bindir/uncompress
ln -s compress.1 %buildroot%_man1dir/uncompress.1

%files
%_bindir/*
%_man1dir/*
%doc Acknowleds Changes LZW.INFO README

%changelog
* Wed Apr 23 2008 Dmitry V. Levin <ldv@altlinux.org> 4.2.4.2-alt1
- Updated to 4.2.4.2.

* Thu Oct 24 2002 Stanislav Ievlev <inger@altlinux.ru> 4.2.4-ipl23mdk
- rebuild with gcc3
- added LFS patch from RH.

* Mon Mar 18 2002 Stanislav Ievlev <inger@altlinux.ru> 4.2.4-ipl22mdk
- Rebuilt
- Added patch from RH.

* Thu Jan 18 2001 Dmitry V. Levin <ldv@fandra.org> 4.2.4-ipl21mdk
- RE adaptions.

* Sun Sep 24 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 4.2.4-21mdk
- rebuilt for macros.
- use of spec helper.
- the Big Move.

* Fri Apr 14 2000 Vincent Saugey <vince@mandrakesoft.com> 4.2.4-20mdk
- corrected group

* Sun Mar 19 2000 John Buswell <johnb@mandrakesoft.com> 4.2.4-19mdk
- Added PPC Support

* Wed Nov 10 1999 Jerome Martin <jerome@mandrakesoft.com>
- minor specfile cleanup
- rebuild for new environment

* Sun Oct 31 1999 David BAUDENS <baudens@mandrakesoft.com>
- Add i486 and i686 arch (forgotten by Lord DarkChmou ;)

* Mon Oct 25 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- fix build mutliple archichtechtures..

* Sat Apr 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- bzip2 man/info pages
- add de locale

* Tue Jan 12 1999 Cristian Gafton <gafton@redhat.com>
- build on armv4l too
- build for 6.0

* Thu Aug 13 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Oct 21 1997 Cristian Gafton <gafton@redhat.com>
- fixed the spec file

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc
