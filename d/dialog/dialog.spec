# -*- rpm-spec -*-
# $Id: dialog,v 1.5 2003/09/05 10:17:48 grigory Exp $

Name: dialog
Version: 1.1
Release: alt6.1
%define snapshot 20110302

Packager: Stanislav Ievlev <inger@altlinux.org>

Summary: A utility for creating TTY dialog boxes
License: LGPL
Group: Development/Other

Url: http://invisible-island.net/dialog/
Source: ftp://invisible-island.net/dialog/%name-%version.tar
Patch0: %name-link.patch
Provides: cdialog lib%name-devel
Obsoletes: cdialog

Requires: terminfo

BuildPreReq: libncursesw-devel libtinfo-devel

%description
Dialog is a utility that allows you to show dialog boxes (containing
questions or messages) in TTY (text mode) interfaces.  Dialog is called
from within a shell script.  The following dialog boxes are implemented:
yes/no, menu, input, message, text, info, checklist, radiolist, and
gauge.

Install dialog if you would like to create TTY dialog boxes.

%package -n lib%name
Summary: Libraries for dialog
Group: System/Libraries

%description -n lib%name
Libraries for dialog.

%package -n lib%name-devel
Summary: Libraries and headers files for dialog
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Libraries and header files for dialog.

%package -n lib%name-devel-static
Summary: Static dialog library
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
Static dialog library.

%prep
%setup
%patch0 -p1

%build
%configure \
	--with-libtool \
	--enable-nls \
	--with-ncursesw \
	--disable-rpath-hack
%make_build

%install
%makeinstall_std install-full
find samples -type f -print0 |xargs -r0 chmod a-x

%find_lang %name

%files -f %name.lang
%doc README samples
%_bindir/dialog
%_man1dir/dialog.*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_bindir/dialog-config
%_libdir/*.so
%_includedir/*.h
%_man3dir/dialog.*

%files -n lib%name-devel-static
%_libdir/*.a

%changelog
* Thu Feb 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt6.1
- Removed bad RPATH

* Sun Mar 20 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1-alt6
- new version

* Wed Oct 21 2009 Boris Savelev <boris@altlinux.org> 1.1-alt5
- new version

* Thu Oct 15 2009 Boris Savelev <boris@altlinux.org> 1.1-alt4
- build with libtool
- add shared library

* Sun Sep 27 2009 Boris Savelev <boris@altlinux.org> 1.1-alt3
- add static library

* Tue Nov 13 2007 Stanislav Ievlev <inger@altlinux.org> 1.1-alt2
- new snapshot, fix license tag

* Fri Apr 13 2007 Stanislav Ievlev <inger@altlinux.org> 1.1-alt1
- 1.1
- build with ncursesw

* Thu Dec 30 2004 Stanislav Ievlev <inger@altlinux.org> 1.0-alt2
- new snapshot

* Thu Aug 12 2004 Stanislav Ievlev <inger@altlinux.org> 1.0-alt1
- 1.0

* Fri Apr 02 2004 Stanislav Ievlev <inger@altlinux.org> 0.9b-alt8
- 20040316

* Thu Dec 04 2003 Stanislav Ievlev <inger@altlinux.org> 0.9b-alt7
- latest snapshot

* Fri Sep  5 2003 Grigory Milev <week@altlinux.ru> 0.9b-alt6
- latest snapshot

* Mon Sep  1 2003 Grigory Milev <week@altlinux.ru> 0.9b-alt5
- added 2 gauges patch

* Fri Aug 29 2003 Stanislav Ievlev <inger@altlinux.ru> 0.9b-alt4
- new snapshot, patch for gauge temporary removed

* Tue Mar 25 2003 Stanislav Ievlev <inger@altlinux.ru> 0.9b-alt3
- latest snapshot

* Wed Sep 04 2002 Stanislav Ievlev <inger@altlinux.ru> 0.9b-alt2
- rebuild with gcc3

* Tue Jun 25 2002 Stanislav Ievlev <inger@altlinux.ru> 0.9b-alt1
- 0.9b

* Wed Apr 03 2002 Stanislav Ievlev <inger@altlinux.ru> 0.9a-alt9
- new snapshot
- changes by Amon Ott (ao@rsbac.org) added to upstream
- dropped patch to man-page

* Tue Feb 12 2002 Grigory Milev <week@altlinux.ru> 0.9a-alt8
- added requires to ncurses, with out it dilog can't work
- added patch for gauge, now may create 2 lines

* Thu Jan 24 2002 Stanislav Ievlev <inger@altlinux.ru> 0.9a-alt7
- latest snapshot
- added patch to fselect from Owl

* Fri Nov 16 2001 Stanislav Ievlev <inger@altlinux.ru> 0.9a-alt6
- 20011111
- fix charsets

* Thu Sep 06 2001 Stanislav Ievlev <inger@altlinux.ru> 0.9a-alt5
- 20010811

* Mon Jul 09 2001 Stanislav Ievlev <inger@altlinux.ru> 0.9a-alt4
- Up to 0.9-20010527

* Wed May 16 2001 Stanislav Ievlev <inger@altlinux.ru> 0.9a-alt3
- Up to 0.9-20010429

* Fri May 04 2001 Stanislav Ievlev <inger@altlinux.ru> 0.9a-alt2
- Up to 0.9-20010415.

* Tue Apr 03 2001 Stanislav Ievlev <inger@altlinux.ru> 0.9a-alt1
- Up to 0.9-20010115. Some adopt bugfixes

* Mon Dec  4 2000 AEN <aen@logic.ru>
- build for RE

* Mon Aug  7 2000 Bill Nottingham <notting@redhat.com>
- fix one of the examples (#14073)

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Wed Apr  5 2000 Bill Nottingham <notting@redhat.com>
- rebuild against current ncurses/readline

* Thu Feb  3 2000 Bill Nottingham <notting@redhat.com>
- handle compressed man pages

* Thu Jan 20 2000 Bill Nottingham <notting@redhat.com>
- fix loop patch for reading from pipe

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 14)

* Fri Dec 18 1998 Bill Nottingham <notting@redhat.com>
- build for 6.0

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Thu May 7 1998 Michael Maher <mike@redhat.com>
- Added Sean Reifschneider <jafo@tummy.com> patches for
  infinite loop problems.

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 15 1998 Erik Troan <ewt@redhat.com>
- built against new ncurses

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc

