Name: gerbv
Version: 2.6.2
Release: alt1

Summary: Gerber file viewer

Packager: Vitaly Lipatov <lav@altlinux.ru>

Url: http://gerbv.sourceforge.net
License: GPL
Group: Graphics

# Source-git: http://git.geda-project.org/gerbv/
Source: %name-%version.tar
Patch2: %name-2.1.0-alt-DSO.patch

# Automatically added by buildreq on Wed Nov 12 2008
BuildRequires: ImageMagick desktop-file-utils gcc-c++ libgtk+2-devel libpng-devel


%description
Gerbv is a viewer for Gerber files. Gerber files are generated from PCB CAD
system and sent to PCB manufacturers as basis for the manufacturing process.

%package examples
Summary: Gerber file examples for gerbv
Requires: gerbv
Group: Graphics

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
Requires: lib%name = %version-%release

%description -n lib%name-devel
Header files for lib%name library.

%prep
%setup
#patch2 -p2

%build
%autoreconf
%configure --enable-exportpng --enable-gtk2 --disable-static
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_datadir/gerbv
cp -r example %buildroot%_datadir/gerbv
cp -r doc %buildroot%_datadir/gerbv

rm -f %buildroot%_desktopdir/*.cache

%find_lang %name

%files -f %name.lang
%dir %_datadir/gerbv
%dir %_datadir/gerbv/doc
%dir %_datadir/gerbv/scheme
%doc AUTHORS ChangeLog NEWS README TODO
%_bindir/gerbv
%_man1dir/gerbv.*
%_datadir/gerbv/doc/*
%_datadir/gerbv/scheme/*.scm
%_datadir/gerbv/gerbv_icon.ico
%_desktopdir/*.desktop
%_iconsdir/*/*/*/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_pkgconfigdir/*.pc
%_includedir/%name-*/
%_libdir/*.so

%files examples
%dir %_datadir/gerbv/example
%_datadir/gerbv/example/*

%changelog
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
