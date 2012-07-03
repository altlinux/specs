Name: flex-old
Version: 2.5.4a
Release: alt2

Summary: The old version of the fast lexical analyzer generator
License: BSD
Group: Development/Other
Url: ftp://ftp.gnu.org/non-gnu/flex/

# ftp://ftp.gnu.org/non-gnu/flex/flex-%version.tar.bz2
Source: flex-%version.tar
Patch1: flex-2.5.4-rh-glibc22.patch
Patch2: flex-2.5.4a-rh-skel.patch
Patch3: flex-2.5.4a-alt-texinfo.patch
Patch4: flex-2.5.4-mdk-gcc31.patch

#Provides: flex = 2.5.4a-ipl16mdk
Conflicts: flex

%description
flex is a tool for generating scanners: programs which recognize lexical
patterns in text.  This is the old 2.5.4a version, which is no longer
being developed.  You should normally choose flex, unless you have
legacy lexer files that do not work with a modern flex.

%prep
%setup -q -n flex-2.5.4
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
# Force regeneration of skel.c
rm skel.c

autoconf
%configure

%make_build
cd MISC/texinfo
makeinfo --no-split flex

%install
%makeinstall mandir="%buildroot%_man1dir"
install -pD -m644 MISC/texinfo/flex.info %buildroot%_infodir/flex.info
ln -s flex %buildroot%_bindir/lex
ln -s libfl.a %buildroot%_libdir/libl.a
ln -s flex.1 %buildroot%_man1dir/lex.1
ln -s flex.1 %buildroot%_man1dir/flex++.1

%files
%_bindir/*
%_libdir/*.*a
%_includedir/*
%_mandir/man?/*
%_infodir/*.info*
%doc COPYING NEWS README MISC/testxxLexer.l

%changelog
* Tue Sep 08 2009 Dmitry V. Levin <ldv@altlinux.org> 2.5.4a-alt2
- Removed obsolete %%install_info/%%uninstall_info calls.

* Sat Oct 22 2005 Dmitry V. Levin <ldv@altlinux.org> 2.5.4a-alt1
- Created a new package called flex-old so that people who
  have not yet changed their lex files (or can't change them)
  and thus can't build with the new flex have an option.
  This is a dead-end package, and shall be removed at some
  point in the future.

* Tue Oct 29 2002 Stanislav Ievlev <inger@altlinux.ru> 2.5.4a-ipl16mdk
- rebuild

* Tue Jul 23 2002 Dmitry V. Levin <ldv@altlinux.org> 2.5.4a-ipl15mdk
- gcc31 C++ compilation fixes (mdk).

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
