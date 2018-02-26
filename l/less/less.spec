# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: less
Version: 444
Release: alt1

Summary: A text file browser similar to more, but better
License: GPLv3+
Group: File tools
Url: http://www.greenwoodsoftware.com/less/
Packager: Alexey Gladkov <legion@altlinux.ru>

# http://www.greenwoodsoftware.com/less/less-%version.tar.gz
Source:   less-%version.tar
Source1:  http://www.greenwoodsoftware.com/less/faq.html
Source2:  lesspipe
Source3:  lessfile
Source4:  lesspipe.sh
Source5:  lessfile.sh
Source6:  lessclose.sh
Source7:  zless
Source8:  zless.1
Source9:  lzless
Source10: lzless.1
Source11: lesspipe.1
Source12: less.sh
Source13: less.csh
Source14: lesspipe-color.sh

Patch1: less-394-alt-configure.patch
Patch3: less-394-rh-Foption.patch
Patch4: less-394-rh-search.patch
Patch6: less-394-suse-strict-aliasing.patch
Patch7: less-alt-old-bot-at-start.patch
Patch8: less-alt-pcre_include_path.patch
Patch9:	less-alt-colorenv.patch

Requires: file >= 4.26-alt3, mktemp >= 1:1.3.1

# due to bzless
Conflicts: bzip2 < 0:1.0.1-ipl6mdk
# due to zmore
Conflicts: gzip-utils < 0:1.3.5-alt1
# due to lzless
Conflicts: lzma-utils < 4.32.7-alt3

BuildRequires: libtinfo-devel libpcre-devel

%description
The less utility is a text file browser that resembles more, but has
more capabilities. less allows you to move backwards in the file as
well as forwards. Since less doesn't have to read the entire input file
before it starts, less starts up more quickly than text editors (for
example, vi).

%prep
%setup
%patch1 -p1
%patch3 -p1
%patch4 -p1
%patch6 -p1
%patch7 -p2
%patch8 -p1
%patch9 -p1

install -pm644 %_sourcedir/faq.html .
bzip2 -9k NEWS

%build
autoconf
%configure --with-regex=pcre
%make_build

%install
mkdir -p %buildroot{%_sysconfdir/profile.d,%_datadir/less}
%makeinstall
install -pm755 %_sourcedir/{lesspipe,lessfile,zless,lzless} \
	%buildroot%_bindir/
install -pm755 %_sourcedir/{lesspipe,lesspipe-color,lessfile,lessclose}.sh \
	%buildroot%_datadir/less/
install -pm644 %_sourcedir/{lesspipe,zless,lzless}.1 \
	%buildroot%_man1dir/
install -pm755 %_sourcedir/less.{sh,csh} \
	%buildroot%_sysconfdir/profile.d/
ln -s zless %buildroot%_bindir/zmore
ln -s zless %buildroot%_bindir/bzmore
ln -s zless %buildroot%_bindir/bzless
ln -s zless %buildroot%_bindir/xzmore
ln -s zless %buildroot%_bindir/xzless
ln -s lzless %buildroot%_bindir/lzmore
ln -s zless.1 %buildroot%_man1dir/zmore.1
ln -s zless.1 %buildroot%_man1dir/bzmore.1
ln -s zless.1 %buildroot%_man1dir/bzless.1
ln -s zless.1 %buildroot%_man1dir/xzmore.1
ln -s zless.1 %buildroot%_man1dir/xzless.1
ln -s lzless.1 %buildroot%_man1dir/lzmore.1
ln -s lesspipe.1 %buildroot%_man1dir/lessfile.1

%files
%config(noreplace) %_sysconfdir/profile.d/less.*
%_bindir/*
%_datadir/less
%_man1dir/*
%doc NEWS.bz2 *.html

%changelog
* Thu Aug 11 2011 Alexey Gladkov <legion@altlinux.ru> 444-alt1
- New version 444.

* Wed Apr 20 2011 Alexey Gladkov <legion@altlinux.ru> 443-alt1
- New version 443.
- Add LESSPIPE_DISABLED variable to turn off lesspipe.sh.

* Thu Oct 01 2009 Alexey Gladkov <legion@altlinux.ru> 436-alt2
- Move lzless here from lzma-utils package.
- Add xzless.

* Sat Aug 01 2009 Alexey Gladkov <legion@altlinux.ru> 436-alt1
- New version 436.

* Fri Jul 03 2009 Alexey Gladkov <legion@altlinux.ru> 434-alt1
- New version 434.
- Fix regex-off search (ALT#20585).

* Sat May 02 2009 Alexey Gladkov <legion@altlinux.ru> 431-alt1
- New version 431.
- Fix bug ALT#19397.

* Sun Apr 19 2009 Alexey Gladkov <legion@altlinux.ru> 429-alt3
- Show compressed files (ALT#19682).

* Fri Apr 17 2009 Alexey Gladkov <legion@altlinux.ru> 429-alt2
- lesspipe.sh: Add support of ~/.less directory.

* Sat Apr 11 2009 Alexey Gladkov <legion@altlinux.ru> 429-alt1
- New version 429.
- Set LESSCOLOR variable when -R option specified.
- Rewrite lesspipe.sh.

* Sat Nov 08 2008 Slava Semushin <php-coder@altlinux.ru> 424-alt3
- Build with PCRE (requested by at@)
- lesspipe.sh, lessfile.sh: added --lastchange to rpm options (at@)
- Changed Packager tag

* Wed Aug 06 2008 Slava Semushin <php-coder@altlinux.ru> 424-alt2
- Fixed --old-bot option (raorn@, closes: #14114)

* Sun Jul 20 2008 Slava Semushin <php-coder@altlinux.ru> 424-alt1
- Updated to 424

* Sat Jan 05 2008 Slava Semushin <php-coder@altlinux.ru> 418-alt1
- Updated to 418 (which also fixes #13942)
- Changed License tag to GPLv3+

* Wed Jan 02 2008 Slava Semushin <php-coder@altlinux.ru> 416-alt1
- Bump release and move package to Sisyphus

* Thu Nov 29 2007 Slava Semushin <php-coder@altlinux.ru> 416-alt0
- Updated to 416 (deb #453074)
- Enable _unpackaged_files_terminate_build

* Sun Oct 28 2007 Slava Semushin <php-coder@altlinux.ru> 409-alt0
- Updated to 409

* Mon Aug 27 2007 Slava Semushin <php-coder@altlinux.ru> 406-alt0
- Updated to 406
- Minor spec cleanup

* Sat Mar 31 2007 Dmitry V. Levin <ldv@altlinux.org> 394-alt1
- Updated to 394 (#10004).
- Reviewed patches.
- Updated alt-tinfo patch (php-coder@).
- Imported patches from FC and OpenSuSE.
- Updated manpage references.
- Reduced rpm macros abuse.

* Sat May 21 2005 Dmitry V. Levin <ldv@altlinux.org> 382-alt2
- Corrected utf8 detection.
- Packaged zmore and bzmore utilities.

* Tue Feb 17 2004 Dmitry V. Levin <ldv@altlinux.org> 382-alt1
- Updated to 382.
- lesspipe.sh, lessfile.sh: updated.

* Thu Aug 28 2003 Dmitry V. Levin <ldv@altlinux.org> 381-alt2
- lesspipe.sh, lessfile.sh: updated.

* Sun Feb 16 2003 Dmitry V. Levin <ldv@altlinux.org> 381-alt1
- Updated to 381.

* Wed Oct 02 2002 Dmitry V. Levin <ldv@altlinux.org> 378-alt1
- Updated to 378.

* Thu Sep 05 2002 Dmitry V. Levin <ldv@altlinux.org> 376-alt2
- Fixed zless (#0001249).

* Wed Aug 14 2002 Stanislav Ievlev <inger@altlinux.ru> 376-alt1
- 376
- turn off patch 1 (author change logic but there are two last hunks he didn't fix)

* Mon Jun 24 2002 Dmitry V. Levin <ldv@altlinux.org> 374-alt3
- Patched to link with libtinfo.

* Wed Jun 05 2002 Dmitry V. Levin <ldv@altlinux.org> 374-alt2
- Dropped obsolete patches.
- Implemented lessfile/lessclose method.
- Added lessecho(1) and lesspipe(1) manpages (deb).
- Added %_bindir/{lesspipe,lessfile} to fit documentation.
- Added profile scripts for sh(1) and csh(1) to use
  lesspipe method by default.
- Updated dependencies.

* Wed Mar 06 2002 Dmitry V. Levin <ldv@alt-linux.org> 374-alt1
- 374.

* Fri Oct 26 2001 Dmitry V. Levin <ldv@alt-linux.org> 358-ipl7mdk
- Corrected dependecies.

* Sat Jan 27 2001 Dmitry V. Levin <ldv@fandra.org> 358-ipl6mdk
- Merge RH patches.
- lesspipe.sh: use only absolute pathnames for program calls.
- lesspipe.sh: Added support for troff text (manpages).

* Tue Jan 09 2001 Dmitry V. Levin <ldv@fandra.org> 358-ipl5mdk
- Improved lesspipe.sh

* Tue Aug 29 2000 Dmitry V. Levin <ldv@fandra.org> 358-ipl4mdk
- RE adaptions.
- Moved lesspipe.sh and zless here from gzip package.
- Moved bzless here from bzip2 package.

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 358-3mdk
- automatically added BuildRequires

* Thu Jul 27 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 358-2mdk
- rebuild for BM

* Wed Jul 12 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 358-1mdk
- new release
- use more macros

* Thu Jun 29 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 346-2mdk
- added UTF-8 patch from Alastair.McKinstry@compaq.com
- modularized path names

* Mon Jun 26 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 346-1mdk
- new release

* Fri Mar 31 2000 Jerome Dumonteil <jd@mandrakesoft.com>
- use of _tmppath _prefix
- change copyright

* Mon Nov 01 1999 Vincent Saugey <vincent@mandrakesoft.com>
- add faq page to /usr/doc

* Wed Oct 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 340.

* Sat Apr 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Update to 337
- Fix up URL
- Mandrake adaptions
- bzip2 man/info pages
- add de locale
- relocatable

* Tue Mar 16 1999 Preston Brown <pbrown@redhat.com>
- removed ifarch axp stuff for /bin/more, more now works on alpha properly.

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Fri Dec 18 1998 Preston Brown <pbrown@redhat.com>
- bumped spec number for initial rh 6.0 build

* Thu May 07 1998 Prospector System <bugs@redhat.com>

- translations modified for de, fr, tr

* Wed Apr 08 1998 Cristian Gafton <gafton@redhat.com>
- updated to 332 and built for Manhattan
- added buildroot

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc
