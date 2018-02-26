Name: gawk
Version: 3.1.8
Release: alt1

%def_with profile
%define _libexecdir %_prefix/libexec

Summary: The GNU version of the awk text processing utility
License: GPLv3+
Group: Text tools
Url: http://www.gnu.org/software/gawk/
Packager: Stanislav Ievlev <inger@altlinux.org>

# ftp://ftp.gnu.org/gnu/gawk/gawk-%version.tar.bz2
Source: gawk-%version.tar

Provides: awk = %version
BuildRequires: groff-ps texlive-base-bin texlive-generic-recommended

%description
This packages contains the GNU version of awk, a text processing utility.
Awk interprets a special-purpose programming language to do quick
and easy text pattern matching and reformatting jobs.  Gawk should be
upwardly compatible with the Bell Labs research version of awk and is
almost completely compliant with the 1993 POSIX 1003.2 standard for awk.

%package profile
Summary: The version of gawk with profiling support.
Group: Development/Other
Requires: %name = %version-%release

%description profile
This package includes pgawk (profiling gawk).  pgawk is identical in
every way to gawk, except that when it has finished running, it creates
a profile of your program with line execution counts.

%package doc
Summary: Documentation about the GNU version of the awk text processing utility
Group: Text tools
BuildArch: noarch
Requires: %name = %version-%release

%description doc
This packages contains documentation about the GNU version of the awk
text processing utility.

%prep
%setup
rm awkgram.c doc/*.info awklib/eg/prog/igawk.sh awklib/stamp-eg
bzip2 -9k ChangeLog NEWS

%build
%configure --bindir=/bin --enable-switch
sed -i 's/#define HAVE_SOCKETS 1/#undef HAVE_SOCKETS/' config.h
%make_build
%make_build -C doc gawk.ps awkcard.ps
bzip2 -9 doc/{gawk,awkcard}.ps

%install
%makeinstall_std
rm %buildroot/bin/*-%{version}*
mkdir -p %buildroot%_bindir
mv %buildroot/bin/?gawk %buildroot%_bindir/
ln -s ../../bin/gawk %buildroot%_bindir/
ln -s gawk %buildroot%_bindir/awk
ln -s gawk.1 %buildroot%_man1dir/awk.1

%define docdir %_docdir/%name-%version
mkdir -p %buildroot%docdir
install -pm644 AUTHORS ChangeLog.bz2 FUTURES LIMITATIONS NEWS.bz2 POSIX.STD PROBLEMS README \
	doc/{gawk,awkcard}.ps.bz2 %buildroot%docdir/

%find_lang %name

%check
%make_build -k check diffout

%files -f %name.lang
/bin/*
%_bindir/*

%if_with profile
%exclude %_bindir/pgawk*
%endif #with profile

%_libexecdir/awk
%_datadir/awk
%_infodir/*.info*
%_mandir/man?/*

%dir %docdir
%docdir/[A-Z]*

%if_with profile
%files profile
%_bindir/pgawk*
%endif #with profile

%files doc
%dir %docdir
%docdir/*.ps.bz2

%changelog
* Thu Jun 03 2010 Dmitry V. Levin <ldv@altlinux.org> 3.1.8-alt1
- Updated to 3.1.8 (closes: #4911, #16359).

* Wed Sep 09 2009 Dmitry V. Levin <ldv@altlinux.org> 3.1.6-alt3
- Moved "make check" to %%check section.

* Sun May 17 2009 Dmitry V. Levin <ldv@altlinux.org> 3.1.6-alt2
- Removed obsolete %%install_info/%%uninstall_info calls.
- gawk-doc: Packaged as noarch.

* Sun Mar 29 2009 Slava Semushin <php-coder@altlinux.ru> 3.1.6-alt1
- 3.1.6
- License changed to GPLv3+
- Provide symlink for man awk (Closes: #11365)

* Sun Dec 17 2006 Dmitry V. Levin <ldv@altlinux.org> 3.1.5-alt3
- Updated to gawk-stable CVS snapshot 20061130, fixes multiple bugs.
- Applied suse fix for dfa generation of interval expressions
  in multibyte locales (suse#148453).
- Applied fix for length() return in multibyte locales (Paul Eggert),
  http://lists.gnu.org/archive/html/bug-gnu-utils/2005-11/msg00115.html
- Applied fix for memory leak in do_match (Sven Wegener),
  http://lists.gnu.org/archive/html/bug-gnu-utils/2006-11/msg00166.html
- Applied fix for invalid read and write bugs (Ralf Wildenhues),
  http://lists.gnu.org/archive/html/bug-gnu-utils/2006-12/msg00027.html
- Fixed str2wstr() invalid free in multibyte locales (#9785).
- Fixed do_match() invalid read in multibyte locales (#9785).
- Removed rh-wconcat patch, looks like obsoleted by applied multibyte fixes.

* Fri Jul 14 2006 Dmitry V. Levin <ldv@altlinux.org> 3.1.5-alt2
- Applied upstream fix for numeric conversion problem.
- Packaged translations.
- Updated texinfo patch.
- Relocated libexecdir.
- Relocated documentation.
- Enabled test suite.

* Wed Jul 05 2006 Stanislav Ievlev <inger@altlinux.org> 3.1.5-alt1
- 3.1.5
  with patches from RH

* Thu Apr 28 2005 Stanislav Ievlev <inger@altlinux.org> 3.1.4-alt2
- enable switch

* Thu Dec 30 2004 Stanislav Ievlev <inger@altlinux.org> 3.1.4-alt1
- 3.1.4

* Wed Jun 09 2004 Stanislav Ievlev <inger@altlinux.org> 3.1.3-alt3
- fixed #4310 (ignorecase doesn't work on non-ascii symbols)

* Fri Feb 27 2004 Stanislav Ievlev <inger@altlinux.org> 3.1.3-alt2
- fix build with automake-1.8

* Mon Sep 29 2003 Stanislav Ievlev <inger@altlinux.ru> 3.1.3-alt1
- 3.1.3

* Fri Apr 04 2003 Stanislav Ievlev <inger@altlinux.ru> 3.1.2-alt2.1
- added experimental patch to solve grow_buffer problem

* Thu Apr 03 2003 Stanislav Ievlev <inger@altlinux.ru> 3.1.2-alt2
- turn off network features

* Tue Mar 25 2003 Stanislav Ievlev <inger@altlinux.ru> 3.1.2-alt1
- 3.1.2
- removed patch for tmpfiles (author don't use it now)
- removed cleanups patch (was problems with regexp)

* Tue Sep 17 2002 Stanislav Ievlev <inger@altlinux.ru> 3.1.1-alt4
- fixed typo in the URL
- rebuild with gcc3

* Thu Aug 08 2002 Stanislav Ievlev <inger@altlinux.ru> 3.1.1-alt3
- fixed group tag

* Wed Aug 07 2002 Stanislav Ievlev <inger@altlinux.ru> 3.1.1-alt2
- update patch for igawk
- added profile subpackage
- removed regex from cleanup. Internal regex is too different from glibc's regexp

* Sat May 18 2002 Stanislav Ievlev <inger@altlinux.ru> 3.1.1-alt1
- 3.1.1

* Wed Oct 17 2001 Stanislav Ievlev <inger@altlinux.ru> 3.1.0-alt1
- 3.1.0

* Fri Jun 01 2001 Dmitry V. Levin <ldv@altlinux.ru> 3.0.6-ipl2mdk
- Fixed temporary file handling in igawk (owl).
- fixed texinfo dircategory.

* Wed Aug  8 2000 Dmitry V. Levin <ldv@fandra.org> 3.0.6-ipl1mdk
- new release 3.0.6.

* Wed Jul 26 2000 Dmitry V. Levin <ldv@fandra.org> 3.0.5-ipl1mdk
- RE and Fandra adaptions.

* Sat Jul 22 2000 Geoffrey Lee <snailtalk@linux-mandrake.com> 3.0.5-1mdk
- new version
- macros
- provides: awk

* Fri Jun 09 2000 Etienne Faure <etienne@mandrakesoft.com> 3.0.4-3mdk
-rebuild on kenobi

* Sat Apr 08 2000 John Buswell <johnb@mandrakesoft.com> 3.0.4-2mdk
- fixed distribution tag

* Thu Mar 30 2000 John Buswell <johnb@mandrakesoft.com> 3.0.4-1mdk
- 3.0.4
- fixed groups
- spec helper

* Mon Nov 22 1999 Pixel <pixel@linux-mandrake.com>
- moved the doc to gawk-doc

* Wed Oct 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Add defattr.

* Sat Apr 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- bzip2 man/info pages
- add de locale

* Fri Feb 19 1999 Jeff Johnson <jbj@redhat.com>
- Install info pages (#1242).

* Fri Dec 18 1998 Cristian Gafton <gafton@redhat.com>
- build for glibc 2.1
- don't package /usr/info/dir

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 08 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 3.0.3
- added documentation and buildroot

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc
