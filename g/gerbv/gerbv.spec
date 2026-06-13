%define sover 1

Name: gerbv
Version: 2.13.0
Release: alt1

Summary: Gerber file viewer
URL: https://github.com/gerbv/gerbv
VCS: https://github.com/gerbv/gerbv
License: GPL-2.0
Group: Graphics

# Source-url: https://github.com/gerbv/gerbv/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Patch: gerbv-2.13.0-Fix-Fails-GCC15.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: ImageMagick-tools
BuildRequires: gcc-c++ 
BuildRequires: libdxflib-devel
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: libpng-devel

# needed for p10/c10/c9
BuildRequires: desktop-file-utils

%description
Gerber Viewer (gerbv) is a viewer for Gerber files. Gerber files
are generated from PCB CAD system and sent to PCB manufacturers
as basis for the manufacturing process. The standard supported
by gerbv is RS-274X.

gerbv also supports drill files. The format supported are known
under names as NC-drill or Excellon. The format is a bit undefined
and different EDA-vendors implement it different.

%package examples
Summary: Gerber file examples for gerbv
Requires: gerbv
Group: Graphics
BuildArch: noarch

%description examples
Example files for gerbv.

%package -n lib%name
Summary: %name library files
Group: Development/Other

%description -n lib%name
lib%name library.

%package -n lib%name-devel
Summary: Header files for lib%name
Group: Development/Other
Requires: lib%name = %EVR

%description -n lib%name-devel
Header files for lib%name library.

%prep
%setup
%autopatch -p1
subst 's|set -e||' utils/git-version-gen.sh

%build
%cmake
%cmake_build

%install
%cmake_install

#rm %buildroot%_libdir/libgerbv.la
rm %buildroot%_libdir/libgerbv.a
rm -r %buildroot%_docdir/%name

mkdir -p %buildroot%_datadir/gerbv
cp -r example %buildroot%_datadir/gerbv
cp -r doc %buildroot%_datadir/gerbv

%find_lang %name

%files -f %name.lang
%dir %_datadir/gerbv
%dir %_datadir/gerbv/doc
%dir %_datadir/gerbv/scheme
%doc AUTHORS COPYING README.md
%_bindir/gerbv
%_man1dir/gerbv.*
%_datadir/gerbv/doc/*
%_datadir/gerbv/scheme/*.scm
%_datadir/glib-2.0/schemas/org.geda-user.gerbv.gschema.xml
%_datadir/gerbv/gerbv_icon.ico
%_desktopdir/*.desktop
%_iconsdir/*/*/*/*

%files -n lib%name
%_libdir/libgerbv.so.%sover
%_libdir/libgerbv.so.%sover.*

%files -n lib%name-devel
%_pkgconfigdir/*.pc
%_includedir/%name/
%_libdir/libgerbv.so

%files examples
%dir %_datadir/gerbv/example
%_datadir/gerbv/example/*

%changelog
* Sat Jun 13 2026 Anton Midyukov <antohami@altlinux.org> 2.13.0-alt1
- New version 2.13.0.
- switch to build with cmake.

* Tue Dec 17 2024 Vitaly Lipatov <lav@altlinux.ru> 2.10.0-alt2
- restored missed BR: desktop-file-utils

* Tue Dec 17 2024 Vitaly Lipatov <lav@altlinux.ru> 2.10.0-alt1
- new version 2.10.0 (with rpmrb script)
- fixed:
 + CVE-2023-4508: Out-of-bounds memory access of filename
 + CVE-2021-40400: Gerbv RS-274X aperture macro outline primitive out-of-bounds read vulnerability
 + CVE-2021-40403: Gerbv pick-and-place rotation parsing use of uninitialized variable vulnerability
 + CVE-2021-40401: Gerbv RS-274X aperture definition tokenization use-after-free vulnerability
 + CVE-2021-40393: RS-274X format aperture macro variables out-of-bounds write vulnerability
 + CVE-2021-40394: Gerbv RS-274X aperture macro outline primitive integer overflow vulnerability
 + CVE-2021-40391: Gerbv drill format T-code tool number out-of-bounds write vulnerability
- enable build with libdxf

* Mon Mar 01 2021 Vitaly Lipatov <lav@altlinux.ru> 2.7.0-alt1
- new version 2.7.0 (with rpmrb script)

* Sun Dec 10 2017 Vitaly Lipatov <lav@altlinux.ru> 2.6.2-alt2
- make examples subpackage noarch

* Sat Dec 09 2017 Vitaly Lipatov <lav@altlinux.ru> 2.6.2-alt1
- new version

* Fri Dec 12 2014 Vitaly Lipatov <lav@altlinux.ru> 2.6.1-alt1
- new version 2.6.1 (ALT bug #30537)

* Sat Aug 03 2013 Vitaly Lipatov <lav@altlinux.ru> 2.6.0-alt1
- new version 2.6.0 (with rpmrb script)

* Thu Jun 14 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt2.2
- Fixed build

* Thu Feb 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt2.1
- Removed bad RPATH

* Fri Apr 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1.0-alt2
- fix build

* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 2.1.0-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libgerbv
  * postun_ldconfig for libgerbv
  * update_menus for gerbv
  * postclean-05-filetriggers for spec file

* Wed Nov 12 2008 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt1
- new version 2.1.0 (with rpmrb script)

* Wed Nov 12 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt2
- fix build with gcc 4.3
- cleanup spec

* Mon May 29 2006 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1.1
- fixes for GCC4
- remove LICENSE file

* Thu Feb 24 2005 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- first build for ALT Linux Sisyphus

* Thu Dec 16 2004 Stew Benedict <sbenedict@mandrakelinux.com>> 0.16-1mdk
- 1st Mandrakelinux release
- adapted from FC2 package by Wojciech Kazubski
