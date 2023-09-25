Name: libXaw3d
Version: 1.6.5
Release: alt1

Summary: A version of the MIT Athena widget set for X
License: MIT
Group: System/Libraries
Url: http://cgit.freedesktop.org/xorg/lib/libXaw3d

Source: %name-%version.tar

Provides: Xaw3d
Obsoletes: Xaw3d

# Automatically added by buildreq on Wed Nov 03 2010
BuildRequires: flex imake libXmu-devel libXp-devel libXpm-devel
BuildRequires: xorg-cf-files

BuildPreReq: libXext-devel xorg-util-macros

%package devel
Summary: Header files for development using Xaw3d
Group: Development/C
Provides: Xaw3d-devel
Obsoletes: Xaw3d-devel
Requires: %name = %version-%release

%description
Xaw3d is an enhanced version of the MIT Athena Widget set for
the X Window System.  Xaw3d adds a three-dimensional look to applications
with minimal or no source code changes.

You should install this package if you are using applications which incorporate
the MIT Athena widget set and you'd like to incorporate a 3D look into
those applications.

%description devel
Xaw3d is an enhanced version of the MIT Athena widget set for
the X Window System.  Xaw3d adds a three-dimensional look to those
applications with minimal or no source code changes.

This package includes the header files and development libraries required
for building programs that take full advantage of Xaw3d's features.

%prep
%setup

%build
%autoreconf
%configure --disable-static
%make

%install
%make_install install DESTDIR=%buildroot

%files
%_libdir/*.so.*
#%doc README*

%files devel
%_libdir/*.so
%_includedir/X11/*
%dir %_docdir/libXaw3d
%_docdir/libXaw3d/*
%_libdir/pkgconfig/xaw3d.pc

%changelog
* Mon Sep 25 2023 Vladislav Zavjalov <slazav@altlinux.org> 1.6.5-alt1
- 1.6.5

* Sat Oct 22 2022 Vladislav Zavjalov <slazav@altlinux.org> 1.6.4-alt1
- 1.6.4

* Mon Sep 20 2021 Vladislav Zavjalov <slazav@altlinux.org> 1.6.3-alt2
- fix build with LTO by disabling static library

* Fri Aug 03 2018 Vladislav Zavjalov <slazav@altlinux.org> 1.6.3-alt1
- 1.6.3

* Sun May 19 2013 Vladislav Zavjalov <slazav@altlinux.org> 1.6.2-alt1
- 1.6.2

* Sun Mar 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5e-alt4
- Rebuilt for debuginfo

* Wed Nov 03 2010 Vladislav Zavjalov <slazav@altlinux.org> 1.5e-alt3
- rebuild for soname set-versions
- cleanup spec and git-repository

* Sat Dec  6 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5e-alt2
- obsolete by filetriggers macros removed

* Sat Feb  4 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5e-alt1
- Updated to recent upstream version

* Fri Sep 12 2003 Dmitry V. Levin <ldv@altlinux.org> 1.5-alt2
- Updated build dependencies.

* Sun Sep 29 2002 Dmitry V. Levin <ldv@altlinux.org> 1.5-alt1
- Libificated:
  + renamed to libXaw3d*;
  + moved static library to devel-static subpackage.
- Specfile cleanup.
- Fixed some compilation warnings.
- Added documentation.

* Mon Apr 15 2002 Rider <rider@altlinux.ru> 1.5-ipl8mdk
- rebuild

* Tue Nov 28 2000 AEN <aen@logic.ru>
- rebuild for RE

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.5-6mdk
- automatically added BuildRequires

* Mon Mar 27 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.5-5mdk
- fix group.

* Sat Dec 18 1999 Stefan van der Eijk <s.vandereijk@chello.nl>
- adopted spec file to build on alpha (ifarch statement in build)
(pixel's rebuild)

* Tue Nov 02 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- build for new environment

* Sat Jul 17 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- 1.5
- update download URL
- remove obsolete R6.3 patch

* Tue May 04 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions
- handle RPM_OPT_FLAGS
- add de locale

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 21)

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Fri Dec 18 1998 Preston Brown <pbrown@redhat.com>
- bumped spec number for initial rh 6.0 build

* Fri Nov 06 1998 Preston Brown <pbrown@redhat.com>
- added security/update patch from debian (the X11R6.3 patch). Thanks guys. :)

* Wed Oct 14 1998 Cristian Gafton <gafton@redhat.com>
- handle the symlink with triggers instead of getting rid of it

* Mon Oct  5 1998 Jeff Johnson <jbj@redhat.com>
- remove backward compatible symlink.

* Wed May 06 1998 Cristian Gafton <gafton@redhat.com>
- fixed the bad symlink
- BuildRoot

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Nov 04 1997 Erik Troan <ewt@redhat.com>
- don't lave an improper return code from %pre

* Mon Nov 03 1997 Cristian Gafton <gafton@redhat.com>
- take care of the old location of the Xaw3d includes in case that one exist
- updated Prereq: field

* Mon Oct 26 1997 Cristian Gafton <gafton@redhat.com
- fixed the -devel package for the right include files path

* Mon Oct 13 1997 Donnie Barnes <djb@redhat.com>
- minor spec file cleanups

* Wed Oct 01 1997 Erik Troan <ewt@redhat.com>
- i18n widec.h patch needs to be applied on all systems

* Sun Sep 14 1997 Erik Troan <ewt@redhat.com>
- changed axp check to alpha

* Mon Jun 16 1997 Erik Troan <ewt@redhat.com>
- built against glibc

