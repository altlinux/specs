Name: flex
Version: 2.5.35
Release: alt5

Summary: A fast lexical analyzer generator
License: BSD-style
Group: Development/Other
Url: http://flex.sourceforge.net/

# http://sf.net/flex/%name-%version.tar.bz2
Source0: flex-%version.tar
Source1: flex-NEWS.ALT
Patch0: flex-2.5.35-cvs-20081228.patch
Patch1: flex-2.5.35-deb-6.patch
Patch2: flex-2.5.35-alt-YY_STATE_BUF_SIZE.patch
Patch3: flex-2.5.35-alt-texinfo.patch
Patch4: flex-2.5.35-alt-yy_fatal_error-noreturn.patch
Patch5: flex-2.5.35-alt-gcc44.patch
Patch6: flex-2.5.35-alt-isatty.patch
Patch7: flex-2.5.35-suse-pic.patch
Patch8: flex-2.5.35-suse-doc.patch

Requires: m4 >= 0:1.4
Conflicts: flex-old

BuildRequires: flex, help2man
%{?!_without_check:%{?!_disable_check:BuildRequires: gcc-c++}}

%description
flex is a tool for generating scanners: programs which recognized lexical
patterns in text.  flex reads the given input files for a description of a
scanner to generate.  The description is in the form of pairs of regular
expressions and C code, called rules.  flex generates as output a C source
file, lex.yy.c, which defines a routine yylex().  This file is compiled
and linked with the -lfl library to produce an executable.  When the
executable is run, it analyzes its input for occurrences of the regular
expressions.  Whenever it finds one, it executes the corresponding C code.

The behaviour of Flex has undergone a major change since version
2.5.4a.  Flex scanners are now reentrant, you may have multiple
scanners in the same program with differing sets of defaults, and
they play nicer with modern C and C++ compilers.  The Flip side is
that Flex no longer conforms to the POSIX lex behaviour, and the
scanners require conforming implementations when flex is used in ANSI
C mode.  The package flex-old provides the older behaviour.

%prep
%setup -q
rm parse.[hc] scan.c skel.c
%patch0 -p0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

install -pm644 %_sourcedir/flex-NEWS.ALT NEWS.ALT
bzip2 -9k NEWS

%build
%autoreconf
%configure
%make_build CFLAGS='%optflags -D_REENTRANT' MAKEINFOFLAGS=--no-split dist_doc_DATA=

%check
%make_build -k check dist_doc_DATA=

%install
%makeinstall dist_doc_DATA=

ln -s flex %buildroot%_bindir/lex
ln -s flex %buildroot%_bindir/flex++
ln -s libfl.a %buildroot%_libdir/libl.a
ln -s libfl.a %buildroot%_libdir/libfl_pic.a
ln -s flex.1 %buildroot%_man1dir/lex.1
ln -s flex.1 %buildroot%_man1dir/flex++.1

%find_lang %name

%files -f %name.lang
%doc AUTHORS COPYING NEWS.* README examples
%_bindir/*
%_libdir/lib*.a
%_includedir/*
%_mandir/man?/*
%_infodir/*.info*

%changelog
* Mon Feb 07 2011 Dmitry V. Levin <ldv@altlinux.org> 2.5.35-alt5
- Minor specfile cleanup.

* Thu Sep 10 2009 Dmitry V. Levin <ldv@altlinux.org> 2.5.35-alt4
- Moved "make check" to %%check section.

* Tue Jun 02 2009 Dmitry V. Levin <ldv@altlinux.org> 2.5.35-alt3
- Removed obsolete %%install_info/%%uninstall_info calls.
- Updated backport for doc/flex.texi.

* Wed Mar 04 2009 Dmitry V. Levin <ldv@altlinux.org> 2.5.35-alt2
- Backported fixes from flex cvs snapshot 20081228.
- Fixed isatty(3) declaration (closes: SF#1984987).
- Fixed gcc-4.4 testsuite failures (closes: SF#2178663).
- Updated patches from debian and opensuse flex packages.
- Enabled flex test suite during build by default.

* Wed Mar 04 2009 Alexey Gladkov <legion@altlinux.ru> 2.5.35-alt1
- Updated to 2.5.35 (closes: ALT#19055).
- Added compiler-specific optimization: yy_fatal_error should be
  declared noreturn (closes: ALT#19053).
- Disabled flex-2.5.31-11 patch.
- Added Debian and Mandriva patches.

* Sat Apr 14 2007 Dmitry V. Levin <ldv@altlinux.org> 2.5.33-alt3
- Synced with Debian's flex-2.5.31-11.

* Sun Jul 30 2006 Dmitry V. Levin <ldv@altlinux.org> 2.5.33-alt2
- The sourceforge project name was changed from lex to flex,
  updated URLs (closes #9813).
- Synced with Debian's flex-2.5.31-4.

* Wed Mar 01 2006 Dmitry V. Levin <ldv@altlinux.org> 2.5.33-alt1
- Updated to 2.5.33.
- Synced with Debian's flex-2.5.31-1.

* Sat Oct 22 2005 Dmitry V. Levin <ldv@altlinux.org> 2.5.31-alt2
- Applied patch from Debian's flex-2.5.31-34.
- Build with -D_REENTRANT option added.
- Additional specfile convention enforcement.

* Fri Oct 14 2005 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.5.31-alt1
- 2.5.31

* Tue Oct 29 2002 Stanislav Ievlev <inger@altlinux.ru> 2.5.4a-ipl16mdk
- rebuild

* Tue Jul 23 2002 Dmitry V. Levin <ldv@altlinux.org> 2.5.4a-ipl15mdk
- Applied gcc31 C++ compilation fixes (mdk).

* Thu Oct 25 2001 Dmitry V. Levin <ldv@alt-linux.org> 2.5.4a-ipl14mdk
- Fixed generation of glibc22-incompatible code.
- Fixed license, url.

* Tue Jan 16 2001 Dmitry V. Levin <ldv@fandra.org> 2.5.4a-ipl13mdk
- Added and fixed texinfo documentation.
- RE adaptions.

* Tue Sep 12 2000 David BAUDENS <baudens@mandrakesoft.com> 2.5.4a-13mdk
- Allow to build (aka don't use %%configure macro)
- Macrozification for other parts of spec

* Wed May 24 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.5.4a-12mdk
- Use %%{_tmppath}
- Really use spec-helper.

* Sun Apr 02 2000 Jerome Martin <jerome@mandrakesoft.com> 2.5.4a-11mdk
- Fix rpm group
- specfile cleanup for spec-helper

* Wed Nov 10 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- avoid uninitialized variable warning.

* Mon May 17 1999 Axalon Bloodstone <axalon@jumpstart.netpirate.org>
- incorrect symlinks

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 6)

* Fri Dec 18 1998 Bill Nottingham <notting@redhat.com>
- build for 6.0 tree

* Mon Aug 10 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Oct 23 1997 Donnie Barnes <djb@redhat.com>
- updated from 2.5.4 to 2.5.4a

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Thu Mar 20 1997 Michael Fulbright <msf@redhat.com>
- Updated to v. 2.5.4
