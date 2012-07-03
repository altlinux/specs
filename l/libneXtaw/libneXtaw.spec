# vim: set ft=spec: -*- spec -*-

%define lname neXtaw

Name: lib%lname
Version: 0.15.1
Release: alt8

Summary: Modified version of the Athena Widgets with N*XTSTEP appearance
Group: System/Libraries
License: MIT
URL: http://siag.nu/neXtaw/

Source: %lname-%version.tar
Patch1: 0001-Dropped-buggy-keyboard-traversal-support.patch
Patch2: nextaw-alt-linkage.patch

# Automatically added by buildreq on Thu Feb 09 2006
BuildRequires: libXext-devel libXmu-devel

%description
This is %lname, a modified version of the Athena Widgets with N*XTSTEP
appearance. It is based on the Xaw3d 1.5 library by Kaleb S. Keithley.

This is not a magic library which will beautify all your apps instantly.
But with some .Xdefaults fiddling you can make Athena applications look
and, sometimes, behave much better.

%package devel
Summary: Header files for %lname library
Group: Development/C
Requires: %name = %version-%release

%description devel
This is %lname, a modified version of the Athena Widgets with N*XTSTEP
appearance. It is based on the Xaw3d 1.5 library by Kaleb S. Keithley.

This is not a magic library which will beautify all your apps instantly.
But with some .Xdefaults fiddling you can make Athena applications look
and, sometimes, behave much better.

This package contains the include files needed to develop programs
that use the %lname library.

%prep
%setup -n %lname-%version
%patch1 -p2
%patch2 -p1

%build
%autoreconf
%configure \
	--disable-static
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog README
%doc doc/app-defaults doc/CHANGES doc/FAQ doc/README.XAW3D doc/TODO
%_libdir/*.so.*

%files devel
%_includedir/X11/%lname/
%_libdir/*.so

%changelog
* Sun Apr 03 2011 Dmitry V. Levin <ldv@altlinux.org> 0.15.1-alt8
- Link libneXtaw.so with all required libraries.

* Sat Apr 10 2010 Alexey I. Froloff <raorn@altlinux.org> 0.15.1-alt7
- Dropped buggy keyboard traversal support (closes: #23027)

* Mon Dec 28 2009 Alexey I. Froloff <raorn@altlinux.org> 0.15.1-alt6
- Minor spec cleanup

* Thu Feb 09 2006 Sir Raorn <raorn@altlinux.ru> 0.15.1-alt5
- %%__autoreconf'ed, should fix x86_64 builds

* Sat Jan 28 2006 Sir Raorn <raorn@altlinux.ru> 0.15.1-alt4
- Rebuilt with new Xorg, buildreqs updated
- Removed summary/description translations

* Thu Feb 10 2005 Anton D. Kachalov <mouse@altlinux.org> 0.15.1-alt3
- lib64 fix

* Mon Dec 15 2003 Sir Raorn <raorn@altlinux.ru> 0.15.1-alt2
- devel-static and *.la fixes

* Mon Sep 22 2003 Sir Raorn <raorn@altlinux.ru> 0.15.1-alt1
- [0.15.1]

* Sat Sep 06 2003 Sir Raorn <raorn@altlinux.ru> 0.15.0-alt1
- [0.15.0]
- Some summary/description translation fixes
- Removed patches:
  + alt-SimpleMenu-fixes (merged upstream in 0.14.1 AKA 0.14.0-alt2)

* Sat Apr 26 2003 Sir Raorn <raorn@altlinux.ru> 0.14.0-alt2
- Some cosmetic fixes in SimpleMenu and SmeBSB code

* Fri Feb 28 2003 Sir Raorn <raorn@altlinux.ru> 0.14.0-alt1
- [0.14.0]

* Thu Jan 16 2003 Sir Raorn <raorn@altlinux.ru> 0.13.0-alt1
- [0.13.0]

* Mon Oct 21 2002 Stanislav Ievlev <inger@altlinux.ru> 0.12-alt4
- rebuild with gcc3
- added packager Tag

* Thu Jul 18 2002 Sir Raorn <raorn@altlinux.ru> 0.12-alt3
- Scroll scrollbars with mouse wheel (idea shamelessly stolen
  from vim's gui_at_sb.c)

* Thu Jul 11 2002 Sir Raorn <raorn@altlinux.ru> 0.12-alt2
- Fixed horisontal scroll click near thumb (was shifted
  right for size of two scroll buttons)

* Tue May 28 2002 Sir Raorn <raorn@altlinux.ru> 0.12-alt1
- [0.12]

* Fri Jan 11 2002 Sir Raorn <raorn@altlinux.ru> 0.10-alt2
- dotlib patch removed

* Tue Jan 08 2002 Sir Raorn <raorn@altlinux.ru> 0.10-alt1
- [0.2.10]
- Ghostdance around default prefix

* Sat Dec 22 2001 Sir Raorn <raorn@altlinux.ru> 0.8-alt1
- Built for Sisyphus
