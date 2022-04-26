Name: m4
Version: 1.4.19.0.15.bb35
Release: alt1

Summary: The GNU macro processor
License: GPLv3+
Group: Development/Other
Url: https://www.gnu.org/software/m4/

# git://git.altlinux.org/gears/m/m4.git
Source: %name-%version-%release.tar

BuildRequires: gnulib >= 0.1.4645.3639c
BuildRequires: gperf
BuildRequires: help2man
BuildRequires: makeinfo

%description
A GNU implementation of the traditional UNIX macro processor.  m4 is
useful for writing text files which can be logically parsed, and is
used by many programs as part of their build process.  m4 has built-in
functions for including files, running shell commands, doing arithmetic,
etc.  The autoconf program needs m4 for generating configure scripts,
but not for running configure scripts.

%prep
%setup -n %name-%version-%release

# Build scripts expect to find m4 version in this file.
echo -n %version > .tarball-version

rmdir gnulib
ln -s %_datadir/gnulib .

%build
./bootstrap --skip-po --force
%configure
%make_build MAKEINFOFLAGS=--no-split

%install
%makeinstall_std
install -pD -m644 m4/m4.m4 %buildroot%_aclocaldir/m4.m4

%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%check
%make_build -k check VERBOSE=1

%files
%_bindir/*
%_infodir/*.info*
%_man1dir/*
%_aclocaldir/*
%doc AUTHORS BACKLOG NEWS README THANKS TODO

%changelog
* Wed Jan 26 2022 Dmitry V. Levin <ldv@altlinux.org> 1.4.19.0.15.bb35-alt1
- m4: v1.4.19-4-gcd7f4d15 -> v1.4.19-15-gbb35e808.

* Tue Jun 01 2021 Dmitry V. Levin <ldv@altlinux.org> 1.4.19.0.4.gcd7f-alt1
- v1.4.18-15-g4e5c2c01 -> v1.4.19-4-gcd7f4d15.
- gnulib BR: v0.1-3618-g4cfff6810 -> v0.1-4645-g3639c57a9.

* Tue Apr 06 2021 Dmitry V. Levin <ldv@altlinux.org> 1.4.18.0.15.4e5c-alt1
- v1.4.18 -> v1.4.18-15-g4e5c2c01 (fixes build with makeinfo >= 6.7).
- gnulib BR: v0.1-2305-g95c96b6dd -> v0.1-3618-g4cfff6810.

* Wed Dec 26 2018 Dmitry V. Levin <ldv@altlinux.org> 1.4.18-alt2
- gnulib: v0.1-1209-g24b3216 -> v0.1-2305-g95c96b6dd.

* Tue Mar 21 2017 Dmitry V. Levin <ldv@altlinux.org> 1.4.18-alt1
- m4: v1.4.17-11-gf258 -> v1.4.18.
- gnulib: v0.1-585-g2fda85e -> v0.1-1209-g24b3216.

* Fri Dec 04 2015 Dmitry V. Levin <ldv@altlinux.org> 1.4.17.0.11.f258-alt2
- Added makeinfo to BuildRequires.

* Wed Nov 19 2014 Dmitry V. Levin <ldv@altlinux.org> 1.4.17.0.11.f258-alt1
- Updated to v1.4.17-11-gf258.
- Built with gnulib v0.1-585-g2fda85e.

* Mon Oct 28 2013 Dmitry V. Levin <ldv@altlinux.org> 1.4.17-alt1
- Updated to v1.4.17-3-g4567a76.
- Built with gnulib v0.0-8061-g5191b35.

* Sun Apr 07 2013 Dmitry V. Levin <ldv@altlinux.org> 1.4.16-alt5
- Updated to v1.4.16-36-g197bca5.
- Built with gnulib v0.0-7901-g076ac82.

* Mon Sep 10 2012 Dmitry V. Levin <ldv@altlinux.org> 1.4.16-alt4
- Packaged proper m4 manpage.

* Fri Aug 24 2012 Dmitry V. Levin <ldv@altlinux.org> 1.4.16-alt3
- Updated to v1.4.16-9-ga0496f2.
- Updated m4.m4 from autoconf-v2.68-110-gb69f4c2.
- Built with system gnulib v0.0-7591-g898f143.

* Tue Jun 28 2011 Dmitry V. Levin <ldv@altlinux.org> 1.4.16-alt2
- Fixed build on linux kernel >= 2.6.39.

* Wed Mar 02 2011 Dmitry V. Levin <ldv@altlinux.org> 1.4.16-alt1
- Updated to 1.4.16.

* Thu Sep 02 2010 Dmitry V. Levin <ldv@altlinux.org> 1.4.15-alt1
- Updated to 1.4.15.

* Sat Feb 27 2010 Dmitry V. Levin <ldv@altlinux.org> 1.4.14-alt1
- Updated to 1.4.14.
- Updated m4.m4 from autoconf-v2.65-6-g4a814e4.

* Wed Sep 09 2009 Dmitry V. Levin <ldv@altlinux.org> 1.4.13-alt2
- Moved "make check" to %%check section.

* Sun Jun 07 2009 Dmitry V. Levin <ldv@altlinux.org> 1.4.13-alt1
- Updated to 1.4.13.
- Removed obsolete %%install_info/%%uninstall_info calls.

* Wed Oct 04 2006 Dmitry V. Levin <ldv@altlinux.org> 1.4.7-alt1
- Updated to 1.4.7.

* Sat Sep 23 2006 Dmitry V. Levin <ldv@altlinux.org> 1.4.6-alt1
- Updated to 1.4.6.
- Removed obsolete patches.

* Fri Oct 21 2005 Dmitry V. Levin <ldv@altlinux.org> 1.4.4-alt1
- Updated to 1.4.4.

* Fri Apr 01 2005 Dmitry V. Levin <ldv@altlinux.org> 1.4.3-alt1
- Updated to 1.4.3.
- Updated patches.

* Mon Jan 03 2005 Dmitry V. Levin <ldv@altlinux.org> 1.4.2-alt1
- Updated to 1.4.2.

* Tue Aug 10 2004 Dmitry V. Levin <ldv@altlinux.org> 1.4.1-alt3
- Updated to released tarball.
- Merged upstream patches: alt-format.
- Updated patches: alt-glibc.

* Fri Oct 04 2002 Dmitry V. Levin <ldv@altlinux.org> 1.4.1-alt2
- Explicitly use autoconf-2.13 for build.
- Use getopt, error, libintl, obstack implementations from
  glibc rather then build them statically here
- Added m4.m4 from autoconf-2.54 (Alexey Morozov).
- Additional convention enforcement on patch file names.

* Thu Oct 25 2001 Dmitry V. Levin <ldv@altlinux.org> 1.4.1-alt1
- 1.4.1

* Wed Feb 07 2001 Dmitry V. Levin <ldv@fandra.org> 1.4-ipl20mdk
- Fixed format string bug.

* Tue Jan 16 2001 Dmitry V. Levin <ldv@fandra.org> 1.4-ipl19mdk
- RE adaptions.
- Patched siginfo stuff.
- Fixed texinfo documentation.

* Thu Dec  7 2000 Jeff Garzik <jgarzik@mandrakesoft.com> 1.4-19mdk
- Run automated tests at build time
- Use RPM_OPT_FLAGS.  Damn, who forgot that one.

* Fri Nov 10 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.4-18mdk
- build for gcc-2.96

* Tue Aug 29 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.4-17mdk
- BM

* Wed Mar 22 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.4-16mdk
- spechelper fixes
- group fix

* Wed Nov  3 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Build release.
- Fix building as user.

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 12)

* Thu Dec 17 1998 Cristian Gafton <gafton@redhat.com>
- build against glibc 2.1

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Apr 10 1998 Cristian Gafton <gafton@redhat.com>
- Manhattan build

* Tue Oct 21 1997 Cristian Gafton <gafton@redhat.com>
- added info file handling and BuildRoot

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc
