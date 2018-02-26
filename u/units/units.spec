Name: units
Version: 1.88
Release: alt1

Summary: A utility for converting amounts from one unit to another
License: GPLv3+
Group: Office
Url: http://www.gnu.org/software/units/units.html
# ftp://ftp.gnu.org/pub/gnu/%name/%name-%version.tar.gz
Source: %name-%version.tar
Patch: units-1.88-alt-texinfo.patch
BuildRequires: libreadline-devel

%description
Units converts an amount from one unit to another, or tells you what
mathematical operation you need to perform to convert from one unit to
another.  The units program can handle multiplicative scale changes as
well as conversions such as Fahrenheit to Celsius.

%prep
%setup -q
%patch -p1
# remove generated files
rm parse.tab.c *.info*
find -type f -print0 |
	xargs -r0 fgrep -lZ /usr/local -- |
	xargs -r0 sed -i 's,/usr/local,%prefix,g' --

%build
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_datadir/%name.dat
%_infodir/*.info*
%_man1dir/*
%doc NEWS README

%changelog
* Sun Mar 07 2010 Dmitry V. Levin <ldv@altlinux.org> 1.88-alt1
- Updated to 1.88.
- Cleaned up specfile.

* Tue Oct 02 2007 Stanislav Ievlev <inger@altlinux.org> 1.87-alt1
- 1.87

* Fri Apr 13 2007 Stanislav Ievlev <inger@altlinux.org> 1.86-alt1
- 1.86
- fix License tag value

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.80-alt2.1
- Rebuilt with libreadline.so.5.

* Mon Jan 05 2004 Stanislav Ievlev <inger@altlinux.org> 1.80-alt2
- fix building with gcc 3.3

* Wed Sep 25 2002 Stanislav Ievlev <inger@altlinux.ru> 1.80-alt1
- 1.80

* Fri Jul 06 2001 Sergie Pugachev <fd_rag@altlinux.ru> 1.74-alt1
- new version

* Wed Jan 17 2001 Dmitry V. Levin <ldv@fandra.org> 1.55-ipl9mdk
- RE adaptions.
- Fixed texinfo documentation.

* Mon Dec 25 2000 Stefan van der Eijk <s.vandereijk@chello.nl> 1.55-9mdk
- fix BuildRequires

* Thu Dec 14 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.55-8mdk
- Recompile with full optimisations.

* Tue Nov 28 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.55-7mdk
- Compile as -O2.
- Change BuildRequires: to the new lib policy.

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.55-6mdk
- automatically added BuildRequires

* Fri Jul 21 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.55-5mdk
- macros, BM

* Tue Jun 20 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.55-4mdk
- Clean up specs.
- Use makeinstall macros.

* Sat Mar 25 2000 Daouda Lo	<daouda@mandrakesoft.com> 1.55-3mdk
- fix group

* Sat Nov 06 1999 John Buswell <johnb@mandrakesoft.com>
- Build Release

* Tue Aug 17 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- 1.55
- update source URL
- bzip2 man page
- FHS compliance
- install info page to info dir

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 12)

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- built package for 6.0

* Sun Aug 23 1998 Jeff Johnson <jbj@redhat.com>
- units.lib corrections (problem #685)

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Oct 21 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc

