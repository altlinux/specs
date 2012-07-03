%define api_version 2.4
%define rname gtkmm
%define major 2.24

Name: libgtkmm2
Version: %major.0
Release: alt2

Summary: A C++ interface for GTK2 (a GUI library for X)
License: LGPL
Group: System/Libraries
Url: http://gtkmm.sourceforge.net/
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: ftp://ftp.gnome.org/pub/gnome/sources/%rname/%major/%rname-%version.tar.bz2

Provides: %rname = %version

BuildRequires: mm-common gcc-c++ libgtk+2-devel >= 2.24.0 libpangomm-devel libatkmm-devel

%description
Gtkmm provides a C++ interface to the GTK+ GUI library. gtkmm2 wraps GTK+ 2.
Highlights include typesafe callbacks, widgets extensible via inheritance
and a comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.

%package devel
Summary: Headers for developing programs that will use %name
Group: Development/C++
Requires: %name = %version-%release
Provides: %rname-devel = %version

%description devel
This package contains the static libraries and header files needed for
developing gtkmm applications.

%package doc
Summary: Documentation for developing with %name
Group: Development/C++
BuildArch: noarch

%description doc
This package contains the documentation for
developing gtkmm applications.

%package demos
Summary: Demos for developing programs that will use %name
Group: Development/C++
BuildArch: noarch
Requires: %name-devel = %version-%release

%description demos
The %name-demos package contains source code of demo programs for %name.

%prep
%setup -q -n %rname-%version

%build
mm-common-prepare
%autoreconf
%configure \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot gtkmm_docdir=%_docdir/%rname-%api_version install

%files
%doc AUTHORS NEWS
%_libdir/*.so.*

%files devel
%_includedir/gdkmm-%api_version
%_includedir/%rname-%api_version
%_libdir/*.so
%_libdir/gdkmm-%api_version
%_libdir/%rname-%api_version
%_pkgconfigdir/*.pc

%files doc
%_docdir/%rname-%api_version
%_datadir/devhelp/books/%rname-%api_version

#%files demos
#%_datadir/%rname-%api_version

%changelog
* Thu Apr 21 2011 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt2
- rebuild using new mm-common

* Tue Feb 08 2011 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt1
- 2.24.0

* Sun Oct 03 2010 Yuri N. Sedunov <aris@altlinux.org> 2.22.0-alt1
- 2.22.0

* Wed Sep 15 2010 Yuri N. Sedunov <aris@altlinux.org> 2.21.8-alt1
- 2.21.8

* Tue May 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.20.3-alt2
- build -demos subpackage as noarch

* Tue May 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.20.3-alt1
- 2.20.3

* Fri Apr 16 2010 Yuri N. Sedunov <aris@altlinux.org> 2.20.2-alt1
- 2.20.2

* Wed Apr 07 2010 Yuri N. Sedunov <aris@altlinux.org> 2.20.1-alt1
- 2.20.1

* Wed Apr 07 2010 Yuri N. Sedunov <aris@altlinux.org> 2.20.0-alt1
- 2.20.0

* Sat Oct 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.18.2-alt1
- 2.18.2

* Mon Sep 21 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.16.0-alt1
- 2.16.0

* Tue Nov 04 2008 Vitaly Lipatov <lav@altlinux.ru> 2.14.1-alt1
- new version 2.14.1 (with rpmrb script)
- pangomm moved to standalone package libpangomm
- update buildreqs
- disable package with examples

* Mon Apr 14 2008 Vitaly Lipatov <lav@altlinux.ru> 2.12.7-alt1
- new version 2.12.7 (with rpmrb script)

* Sat Mar 08 2008 Vitaly Lipatov <lav@altlinux.ru> 2.12.5-alt1
- new version 2.12.5 (with rpmrb script)
- fix devhelp doc dir

* Sun Jan 13 2008 Vitaly Lipatov <lav@altlinux.ru> 2.12.3-alt1
- new version 2.12.3 (with rpmrb script)
- cleanup spec, update requires

* Thu May 10 2007 Igor Zubkov <icesik@altlinux.org> 2.10.10-alt1
- 2.10.9 -> 2.10.10

* Sat Apr 28 2007 Vitaly Lipatov <lav@altlinux.ru> 2.10.9-alt1
- new version 2.10.9 (with rpmrb script)

* Sun Dec 24 2006 Vitaly Lipatov <lav@altlinux.ru> 2.10.6-alt0.1
- new version 2.10.6 (with rpmrb script)
- fix packager

* Sun Nov 12 2006 Vitaly Lipatov <lav@altlinux.ru> 2.10.3-alt0.1
- new version 2.10.3 (with rpmrb script)

* Sat Sep 02 2006 Vitaly Lipatov <lav@altlinux.ru> 2.10.1-alt0.1
- new version 2.10.1 (with rpmrb script)

* Tue Feb 21 2006 Vitaly Lipatov <lav@altlinux.ru> 2.8.3-alt0.1
- new version 2.8.3 (with rpmrb script)
- update buildreq

* Mon Oct 24 2005 Vitaly Lipatov <lav@altlinux.ru> 2.8.1-alt0.1
- new version
- fix unexpanded macros in descriptions

* Sun Sep 11 2005 Vitaly Lipatov <lav@altlinux.ru> 2.8.0-alt1
- new version

* Thu Mar 17 2005 Vitaly Lipatov <lav@altlinux.ru> 2.6.1-alt1
- new version

* Thu Jan 20 2005 Vitaly Lipatov <lav@altlinux.ru> 2.5.5-alt1
- new version
- build with gcc3.4

* Sat Dec 18 2004 Vitaly Lipatov <lav@altlinux.ru> 2.5.2-alt1
- new version from unstable
- add demos package

* Sat Nov 27 2004 Vitaly Lipatov <lav@altlinux.ru> 2.4.7-alt2
- fix library dependences

* Tue Nov 09 2004 Vitaly Lipatov <lav@altlinux.ru> 2.4.7-alt1
- new version
- add in -devel requiring libglibmm2-devel package (thanks pv@)

* Sat Sep 04 2004 Vitaly Lipatov <lav@altlinux.ru> 2.4.5-alt1
- new version

* Thu Jul 15 2004 Vitaly Lipatov <lav@altlinux.ru> 2.4.4-alt1
- new version
- add req for gtk+2 >2.4

* Sat Jun 19 2004 Vitaly Lipatov <lav@altlinux.ru> 2.4.2-alt2
- fix require libsigc++
- change doc placing for devhelp

* Wed Jun 09 2004 Vitaly Lipatov <lav@altlinux.ru> 2.4.2-alt1
- new version

* Mon May 24 2004 Vitaly Lipatov <lav@altlinux.ru> 2.4.1-alt1
- new version

* Sun Feb 15 2004 Vitaly Lipatov <lav@altlinux.ru> 2.2.8-alt2
- move examples to doc dir
- update buildreq
- Patch0: Make libtool 1.5 always search for staging libraries first
  during relinking (thanks Mandrake)

* Wed Dec 31 2003 Vitaly Lipatov <lav@altlinux.ru> 2.2.8-alt1
- new version
- remove duplicates from doc package
- build with gcc3.3

* Sat Dec 13 2003 Vitaly Lipatov <lav@altlinux.ru> 2.1.3-alt2
- rebuild without .la files

* Mon Jan 06 2003 Vitaly Lipatov <lav@altlinux.ru> 2.1.3-alt1
- new version

* Mon Nov 25 2002 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt1.1
- fix error in copying FAQ.html from doc
- summary and description were translated into russian
- cleanup spec
- add pkgconfig directory to the files section

* Mon Nov 25 2002 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt1
- new version for gtk+2
- new subpacket doc

* Wed Sep 18 2002 Stanislav Ievlev <inger@altlinux.ru> 1:1.2.10-alt1.1
- rebuild with new XFree86

* Tue Sep 10 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.2.10-alt1
- 1.2.10
- Bumped soname for g++ >= 3.2
- Updated %%post/%%postun scripts.

* Wed Apr 10 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.2.9-alt1
- 1.2.9

* Wed Nov 07 2001 Dmitry V. Levin <ldv@alt-linux.org> 1:1.2.8-alt2
- Corrected requires for devel subpackage.

* Tue Nov 06 2001 Dmitry V. Levin <ldv@alt-linux.org> 1:1.2.8-alt1
- 1.2.8

* Tue Aug 14 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.2.7-alt1
- 1.2.7
- Libification.

* Wed Apr 04 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.2.5-ipl2mdk
- Rebuilt with gtk+-1.2.10.

* Sat Feb 17 2001 Dmitry V. Levin <ldv@fandra.org> 1.2.5-ipl1mdk
- 1.2.5

* Sun Nov 19 2000 Dmitry V. Levin <ldv@fandra.org> 1.2.4-ipl1mdk
- 1.2.4
- Split into three packages: %name, %name-devel and %name-examples.
- Fixed Makefiles in %name-exmaples to allow build after installation.

* Sun Oct 01 2000 Dmitry V. Levin <ldv@fandra.org> 1.2.3-ipl1mdk
- 1.2.3
- Patched to build with glibc-2.1.94 & gcc-2.96.
- Automatically added build requires.

* Sun Apr 16 2000 Dmitry V. Levin <ldv@fandra.org>
- Fandra adaptions

* Sat Apr  1 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.2.0pre1-1mdk
- can actually be used now!
- new url

* Mon Mar 27 2000 DindinX <odin@mandrakesoft.com> 1.1.8-2mdk
- Fix group and other specs subtilities

* Mon Mar 06 2000 Lenny Cartier <lenny@mandrakesoft.com>
- back in contribs
- mandrake build

* Sun Jan  2 2000 Herbert Valerio Riedel <hvr@gnu.org>
- examples should be makeable now

* Sun Dec 26 1999 Herbert Valerio Riedel <hvr@gnu.org>
- commented out manpages for now...

* Sat Dec 25 1999 Herbert Valerio Riedel <hvr@gnu.org>
- added dependancies on libsigc++

* Sat Nov  6 1999 Herbert Valerio Riedel <hvr@gnu.org>
- cleanup for 1.1.x
- changed rpm package name from Gtk-- to gtkmm
- removed that static hack

* Sat Oct 21 1999 Karl Einar Nelson <kenelson@ece.ucdavis.edu>
- Changed dist from Gtk--- to gtkmm-

* Sat Sep 11 1999 Herbert Valerio Riedel <hvr@gnu.org>
- added SMP support
- added custom release feature

* Sun Aug  1 1999 Herbert Valerio Riedel <hvr@gnu.org>
- Updated to gtk---1.1.x

* Thu Jul 29 1999 Herbert Valerio Riedel <hvr@gnu.org>
- Updated to gtk---1.0.x
- Merged in changes from redhat's gtk--.spec
- conditional build of static libraries by define 'STATIC'

* Thu May 10 1998 Bibek Sahu <scorpio@dodds.net>
- Upgraded to gtk---0.9.3

* Thu Apr 30 1998 Bibek Sahu <scorpio@dodds.net>
- Fixed problem with gtk---devel requiring libgtk-- (not gtk--).  Oops.

* Thu Apr 30 1998 Bibek Sahu <scorpio@dodds.net>
- Fixed problem with most of the headers not being included.

* Thu Apr 30 1998 Bibek Sahu <scorpio@dodds.net>
- Upgraded to gtk---0.9.1

* Tue Apr 28 1998 Bibek Sahu <scorpio@dodds.net>
- Fixed to build gtk-- and gtk---devel packages.

* Tue Apr 28 1998 Bibek Sahu <scorpio@dodds.net>
- First (s)rpm build.

