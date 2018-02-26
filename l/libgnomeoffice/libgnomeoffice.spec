%define ver_major 0.8
%define abiversion 0.8
%define _name goffice

Name: libgnomeoffice
Version: 0.8.17
Release: alt2

Summary: Library for writing gnome office programs
Group: Graphical desktop/GNOME
License: GPL
Url: http://projects.gnome.org/gnumeric/

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
# not included in the tarball
Source1: go-conf-gsettings.c
Patch: libgnomeoffice-0.8.17-alt-build.patch

Obsoletes: libgnomeoffice%abiversion
Provides: libgnomeoffice%abiversion = %version-%release

BuildRequires: flex libXext-devel libgsf-devel libgio-devel libxml2-devel
BuildRequires: libgtk+2-devel libpcre-devel intltool gtk-doc

%description
GOffice is a library that eases the task of writing gnome office
programs.

%package devel
Summary: Development libraries and header files for %name
Group: Development/C
Requires: %name = %version-%release
Obsoletes: libgnomeoffice%abiversion-devel
Provides: libgnomeoffice%abiversion-devel = %version-%release

%description devel
This package contains the header files and libraries needed to write and
compile programs that use %name.

%package devel-doc
Summary: Development documentation for Goffice
Group: Development/Documentation
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
This package contains development documentation for Goffice library.

%define _libexecdir %_libdir/%name

%prep
%setup -n %_name-%version
%patch -p1

cp %SOURCE1 %_name/app/

%build
%autoreconf
%configure \
	--with-config-backend=gsettings

%make_build

%install
%makeinstall

%find_lang --output=%_name.lang %_name-%version

%files -f %_name.lang
%_libdir/*.so.*
%_libdir/goffice/
%_datadir/goffice/
%_datadir/pixmaps/goffice/*
%doc AUTHORS NEWS README

%exclude %_libdir/%_name/%version/plugins/*/*.la

%files devel
%_includedir/libgoffice-%abiversion/
%_libdir/*.so
%_libdir/pkgconfig/*

%files devel-doc
%_datadir/gtk-doc/html/%_name-%abiversion/

%changelog
* Tue Jun 19 2012 Yuri N. Sedunov <aris@altlinux.org> 0.8.17-alt2
- used GSettings as a configuration backend
- updated buildreqs
- obsoletes/provides libgnomeoffice0.8
- new devel-doc subpackage
- fixed find_lang usage

* Mon Sep 12 2011 Alexey Morsov <swi@altlinux.ru> 0.8.17-alt1
- new version

* Sun Mar 20 2011 Alexey Morsov <swi@altlinux.ru> 0.8.13-alt1
- new version

* Sun Dec 19 2010 Alexey Morsov <swi@altlinux.ru> 0.8.12-alt1
- new version

* Tue Oct 12 2010 Alexey Morsov <swi@altlinux.ru> 0.8.11-alt1
- new version

* Sat Jul 03 2010 Alexey Morsov <swi@altlinux.ru> 0.8.7-alt1
- new version

* Tue Jun 01 2010 Alexey Morsov <swi@altlinux.ru> 0.8.5-alt1
- new version

* Wed Apr 21 2010 Alexey Morsov <swi@altlinux.ru> 0.8.2-alt1
- new version

* Tue Apr 20 2010 Alexey Morsov <swi@altlinux.ru> 0.8.0-alt2
-  fix build (add intltool)

* Wed Feb 17 2010 Alexey Morsov <swi@altlinux.ru> 0.8.0-alt1
- new version

* Sat Dec 19 2009 Alexey Morsov <swi@altlinux.ru> 0.7.17-alt1
- new version

* Tue Nov 03 2009 Alexey Morsov <swi@altlinux.ru> 0.7.15-alt1
- new version

* Sun Aug 30 2009 Alexey Morsov <swi@altlinux.ru> 0.7.9-alt1
- new version
- fix #20655

* Thu Jul 23 2009 Alexey Morsov <swi@altlinux.ru> 0.7.8-alt1
- new version

* Wed Jun 17 2009 Alexey Morsov <swi@altlinux.ru> 0.7.7-alt1
- new version

* Thu Mar 19 2009 Alexey Morsov <swi@altlinux.ru> 0.7.3-alt1
- new version
- remove post/postun (repocop)

* Wed Nov 26 2008 Alexey Morsov <swi@altlinux.ru> 0.7.2-alt1
- version 0.7.2

* Wed Sep 10 2008 Alexey Morsov <swi@altlinux.org> 0.7.1-alt1
- new version (development)
- fix bug #16482 (remove abi version from devel package name)
- fix bug #16962

* Sat Jul 19 2008 Alexey Morsov <swi@altlinux.ru> 0.7.0-alt1
- new version (development)
  + abi version changed to 0.8
- clean spec
  + remove static

* Fri Jul 18 2008 Alexey Morsov <swi@altlinux.ru> 0.6.4-alt1
- new version
- pursue ChangeLog policy

* Sat Mar 15 2008 Alexey Morsov <swi@altlinux.ru> 0.6.2-alt1
- version 0.6.2

* Tue Jan 01 2008 Alexey Morsov <swi@altlinux.ru> 0.6.1-alt1
- version 0.6.1

* Thu Nov 08 2007 Alexey Morsov <swi@altlinux.ru> 0.5.2-alt1
- 0.5.2

* Fri Sep 14 2007 Alexey Morsov <swi@altlinux.ru> 0.5.0-alt1
- version 0.5.0
- so-name changed

* Tue Jul 31 2007 Alexey Morsov <swi@altlinux.ru> 0.4.2-alt1
- Avoid crash if libxml2 returns ERROR or NONE when guessing encoding.
- do not leak the mime type
- fixed signedness issue spotted with help of sparse
- needed for gnumeric 1.7.11


* Sat Jun 02 2007 Alexey Morsov <swi@altlinux.ru> 0.4.0-alt1
- new version for Gnumeric 1.7.10
- added new cubic spline support
- new convenience function
- fixes

* Wed Apr 25 2007 Alexey Morsov <swi@altlinux.ru> 0.3.8-alt1
- new version
- clean spec from cvs bounds (port to git)
- add docs for -devel

* Tue Mar 06 2007 Alexey Morsov <swi@altlinux.ru> 0.3.7-alt1
- new version (bug fixes)
- add libpcre-devel req (patch for pcre)

* Mon Feb 19 2007 Alexey Morsov <swi@altlinux.ru> 0.3.6-alt1
- new version (for gnumeric 1.7.7)

* Mon Dec 25 2006 Alexey Morsov <swi@altlinux.ru> 0.3.5-alt2
- fix spec (bug 10496)

* Tue Dec 19 2006 Alexey Morsov <swi@altlinux.ru> 0.3.5-alt1
- new version (for gnumeric 1.7.6)

* Tue Dec 05 2006 Alexey Morsov <swi@altlinux.ru> 0.3.4-alt1
- build new version (for gnumeric 1.7.5)

* Fri Mar 31 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.1.2-alt1.1
- Rebuild with libgsf-1.so.114 .

* Thu Nov 17 2005 Vital Khilko <vk@altlinux.ru> 0.1.2-alt1
- first release

