%define abiversion 52
%define main_version 0.%abiversion.14
%define _name newt

Name: %_name%abiversion
Version: %main_version
Release: alt1

%def_enable tk
 
Summary: A development library for text mode user interfaces.
License: LGPL
Group: System/Libraries
Url: https://fedorahosted.org/releases/n/e/newt/
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

Source: %url/%name-%version.tar
Patch: %name-%version-%release.patch

Requires: slang, lib%name = %version-%release
Provides: snack = %version-%release

# Automatically added by buildreq on Tue Oct 22 2002
BuildRequires: libpopt-devel libslang2-devel python-devel docbook-utils
%if_enabled tk
BuildRequires: tkinter
%endif

%package -n lib%name
Summary: Newt windowing toolkit development files library.
Group: System/Libraries
Provides: lib%_name = %version-%release

%package -n python-module-%name
Summary: Python files for the %name.
Version: %{main_version}_%_python_version
Group: System/Libraries
Requires: python = %_python_version, lib%name = %{main_version}-%release
Provides: python-module-%_name = %version-%release

%package -n lib%_name-devel
Summary: Newt windowing toolkit development files.
Group: Development/C
Version: %main_version
Requires: lib%name = %version-%release, libslang2-devel
Provides: lib%_name-devel = %version-%release lib%name-devel = %version-%release
Obsoletes: %_name-devel

%package -n lib%_name-devel-static
Summary: Newt windowing toolkit development files.
Group: Development/C
Requires: lib%name-devel = %version-%release
Provides: lib%_name-devel-static = %version-%release lib%name-devel-static = %version-%release

%description
Newt is a programming library for color text mode, widget based user
interfaces.  Newt can be used to add stacked windows, entry widgets,
checkboxes, radio buttons, labels, plain text fields, scrollbars,
etc., to text mode user interfaces.  This package contains a
/usr/bin/dialog replacement called whiptail.
Newt is based on the slang library.

%description -n lib%name
Newt is a programming library for color text mode, widget based user
interfaces.  Newt can be used to add stacked windows, entry widgets,
checkboxes, radio buttons, labels, plain text fields, scrollbars,
etc., to text mode user interfaces.  This package contains the
shared library needed by programs built with %name.
Newt is based on the slang library.

%description -n python-module-%name
python stuff for the %name

%description -n lib%_name-devel
The lib%name-devel package contains the header files and libraries
necessary for developing applications which use %name. Newt is
a development library for text mode user interfaces.
Newt is based on the slang library.

Install lib%name-devel if you want to develop applications which will
use %name.

%description -n lib%_name-devel-static
Static libraries for  lib%name-devel 

%prep
%setup
%patch -p1

subst s/^PYTHONVERS.*/PYTHONVERS=python%_python_version/ Makefile.in

%build
./autogen.sh
%configure --with-gpm-support 
# NO SMP
%make PYTHON_LIBS="-lpython%_python_version"
docbook2html -u tutorial.sgml

%install
%makeinstall 

%find_lang --with-gnome %_name

%files -n lib%name -f %_name.lang
%_libdir/*.so.*

%files 
%_bindir/*
%doc CHANGES
%_man1dir/*

%files -n python-module-%name
%_libdir/python%_python_version/*/*.py*
%_libdir/python%_python_version/*/*.so

%files -n lib%_name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*
%doc tutorial.html

%files -n lib%_name-devel-static
%_libdir/*.*a

%changelog
* Fri Dec 09 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 0.52.14-alt1
- 0.52.14

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.52.13-alt1.1
- Rebuild with Python-2.7

* Mon Aug 01 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 0.52.13-alt1
- 0.52.13

* Sun Mar 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.52.12-alt1.1
- Rebuilt for debuginfo

* Wed Jan 12 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 0.52.12-alt1
- 0.52.12

* Wed Dec 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.52.11-alt4.2
- Rebuilt for soname set-versions

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.52.11-alt4.1
- Rebuilt with python 2.6

* Sun Nov 08 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 0.52.11-alt4
- Fix (#ALT 22029)

* Wed Sep 30 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 0.52.11-alt3
- Remove BuildPreReq: python-devel = %__python_version and add python-devel
  to BuildRequires

* Mon Sep 28 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 0.52.11-alt2
- Add BuildPreReq: python-devel = %__python_version (fix repocop test)

* Fri Sep 25 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 0.52.11-alt1
- 0.52.11
- Update URL
- fix buffer overflow in textbox when reflowing (CVE-2009-2905)

* Tue Apr 28 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 0.52.10-alt1
- 0.52.10 (ALT #19825)
- Rebuild with libslang2-devel
- Rename lib%name-python -> python-module-%name
- Add %_man1dir/*
- Add Packager
- Update spec
- Add %abiversion

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 0.50.39-alt3.1
- Rebuilt with python-2.5.

* Wed Apr 13 2005 Anton D. Kachalov <mouse@altlinux.org> 0.50.39-alt3
- rebuild with python2.4
- added missed _snackmodule.so

* Tue Oct 22 2002 Stanislav Ievlev <inger@altlinux.ru> 0.50.39-alt2
- rebuild with gcc3.
  New version has new soname, so still waiting for next distro release (ALM3?)
- don't build example static

* Wed Apr 24 2002 Stanislav Ievlev <inger@altlinux.ru> 0.50.35-alt1
- 0.50.35

* Mon Oct 08 2001 Stanislav Ievlev <inger@altlinux.ru> 0.50.34-alt2
- 0.50.34. 
- code cleanup patch

* Thu Aug 09 2001 Stanislav Ievlev <inger@altlinux.ru> 0.50.30-alt1
- 0.50.30

* Wed Jun 27 2001 Stanislav Ievlev <inger@altlinux.ru> 0.50.26-alt2
- Rebuilt with python-2.1

* Fri Jun 22 2001 Stanislav Ievlev <inger@altlinux.ru> 0.50.26-alt1
- 0.50.26.

* Thu May 10 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.50.20-alt3
- Enhanced recent fix for Gpm_Open() function.

* Mon May 07 2001 Stanislav Ievlev <inger@altlinux.ru> 0.50.20-alt2
- tmp dir cleaning bugfix.

* Mon May 07 2001 Stanislav Ievlev <inger@altlinux.ru> 0.50.20-alt1
- 0.50.20. tmpdir correction, tty variable bugfix, statification
 
* Tue Jan 09 2001 Dmitry V. Levin <ldv@fandra.org> 0.50.19-ipl1mdk
- 0.50.19.

* Sun Dec 10 2000 Dmitry V. Levin <ldv@fandra.org> 0.50.17-ipl1mdk
- 0.50.17.
- RE adaptions.
- Fixed building with python version != 1.5.
- Automatically added BuildRequires.

* Wed Nov 29 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.50.8-8mdk
- Add missing Provides: (thx stefan, warlyscks).

* Fri Nov 24 2000 Warly <warly@mandrakesoft.com> 0.50.8-7mdk
- split libnewt0 packages

* Thu Nov 23 2000 Vincent Saugey <vince@mandrakesoft.com> 0.50.8-6mdk
- add dependencie on newt from newt-devel
- Patch for python 2.0
- Add build requires on tcl

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.50.8-5mdk
- automatically added BuildRequires

* Sun Jul 23 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.50.8-4mdk
- macro-ization
- BM

* Fri May 19 2000 Pixel <pixel@mandrakesoft.com> 0.50.8-3mdk
- add soname

* Wed Apr 5 2000 Warly <warly@mandrakesoft.com> 0.50.8-2mdk
- readd the mandrake colors patch

* Wed Apr 5 2000 Warly <warly@mandrakesoft.com> 0.50.8-1mdk
- new groups: System/Librairies and Development/C for devel

* Sat Mar 11 2000 Pixel <pixel@mandrakesoft.com> 0.50-15mdk
- really default to mandrake colors (applying the patch works better :)

* Tue Jan 11 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.50-14mdk
- By default mandrake colors.

* Tue Dec 14 1999 Frederic Lepied <flepied@mandrakesoft.com>
- fix bug when gpm isn't running

* Wed Oct 27 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Build release.

* Fri Oct  1 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 0.50.

* Wed Jun 23 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Patch from H.J. Lu <hjl@varesearch.com> :
- fixed tab expansion.

* Sat Apr 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- add de locale

* Mon Mar 15 1999 Matt Wilson <msw@redhat.com>
- fix from Jakub Jelinek for listbox keypresses

* Fri Feb 27 1999 Matt Wilson <msw@redhat.com>
- fixed support for navigating listboxes with alphabetical keypresses

* Thu Feb 25 1999 Matt Wilson <msw@redhat.com>
- updated descriptions
- added support for navigating listboxes with alphabetical keypresses

* Mon Feb  8 1999 Matt Wilson <msw@redhat.com>
- made grid wrapped windows at least the size of their title bars

* Fri Feb  5 1999 Matt Wilson <msw@redhat.com>
- Function to set checkbox flags.  This will go away later when I have
  a generic flag setting function and signals to comps to go insensitive.

* Tue Jan 19 1999 Matt Wilson <msw@redhat.com>
- Stopped using libgpm, internalized all gpm calls.  Still need some cleanups.

* Thu Jan  7 1999 Matt Wilson <msw@redhat.com>
- Added GPM mouse support
- Moved to autoconf to allow compiling without GPM support
- Changed revision to 0.40

* Wed Oct 21 1998 Bill Nottingham <notting@redhat.com>
- built against slang-1.2.2

* Wed Aug 19 1998 Bill Nottingham <notting@redhat.com>
- bugfixes for text reflow
- added docs

* Fri May 01 1998 Cristian Gafton <gafton@redhat.com>
- devel package moved to Development/Libraries

* Thu Apr 30 1998 Erik Troan <ewt@redhat.com>
- removed whiptcl.so -- it should be in a separate package

* Mon Feb 16 1998 Erik Troan <ewt@redhat.com>
- added newtWinMenu()
- many bug fixes in grid code

* Wed Jan 21 1998 Erik Troan <ewt@redhat.com>
- removed newtWinTernary()
- made newtWinChoice() return codes consistent with newtWinTernary()

* Fri Jan 16 1998 Erik Troan <ewt@redhat.com>
- added changes from Bruce Perens
    - small cleanups
    - lets whiptail automatically resize windows
- the order of placing a grid and adding components to a form no longer
  matters
- added newtGridAddComponentsToForm()

* Wed Oct 08 1997 Erik Troan <ewt@redhat.com>
- added newtWinTernary()

* Tue Oct 07 1997 Erik Troan <ewt@redhat.com>
- made Make/spec files use a buildroot
- added grid support (for newt 0.11 actually)

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- Added patched from Clarence Smith for setting the size of a listbox
- Version 0.9

* Tue May 28 1997 Elliot Lee <sopwith@redhat.com> 0.8-2
- Touchups on Makefile
- Cleaned up NEWT_FLAGS_*

* Tue Mar 18 1997 Erik Troan <ewt@redhat.com>
- Cleaned up listbox
- Added whiptail
- Added newtButtonCompact button type and associated colors
- Added newtTextboxGetNumLines() and newtTextboxSetHeight()

* Tue Feb 25 1997 Erik Troan <ewt@redhat.com>
- Added changes from sopwith for C++ cleanliness and some listbox fixes.
