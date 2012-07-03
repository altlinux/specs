# vim: set ft=spec: -*- spec -*-

# Please, RPM, do not remove documentation after installing...
%define _customdocdir %_docdir/%name-%version

%define oname gle

Name: lib%oname
Version: 3.1.0
Release: alt7
Summary: The GLE Tubing and Extrusion Library for OpenGL
License: GPL
Group: System/Libraries
Url: http://www.linas.org/gle/
Packager: Sir Raorn <raorn@altlinux.ru>

Source: %url/pub/%oname-%version.tar.gz

Patch: %name-3.1.0-alt-link.patch

# Automatically added by buildreq on Sat Jan 28 2006 and filtered by raorn
BuildRequires: libGL-devel libXext-devel libXi-devel libXmu-devel libfreeglut-devel

%description
The GLE Tubing and Extrusion Library consists of a number of "C"
language subroutines for drawing tubing and extrusions. It is a very
fast implementation of these shapes, outperforming all other
implementations, most by orders of magnitude. It uses the
OpenGL (TM) programming API to perform the actual drawing of the tubing
and extrusions.

%package devel
Summary: Dedelopment headers for the GLE Tubing and Extrusion Library
Group: Development/C
Requires: %name = %version-%release
# Due to %_includedir/GL directory...
Requires: xorg-x11-proto-devel

%description devel
The GLE Tubing and Extrusion Library consists of a number of "C"
language subroutines for drawing tubing and extrusions. It is a very
fast implementation of these shapes, outperforming all other
implementations, most by orders of magnitude. It uses the
OpenGL (TM) programming API to perform the actual drawing of the tubing
and extrusions.

This package contain development headers and libraries.

%package doc
Summary: Documentation for the GLE Tubing and Extrusion Library
Group: Books/Computer books
Conflicts: %name > %version-%release
Conflicts: %name < %version-%release
Obsoletes: gle-doc <= 3.1.0-alt3

%description doc
The GLE Tubing and Extrusion Library consists of a number of "C"
language subroutines for drawing tubing and extrusions. It is a very
fast implementation of these shapes, outperforming all other
implementations, most by orders of magnitude. It uses the
OpenGL (TM) programming API to perform the actual drawing of the tubing
and extrusions.

This package contains documentation.

%prep
%setup -q -n %oname-%version
#patch -p1

%build
export lt_cv_prog_cc_static_works=no
%configure \
	--disable-static
%make_build libgle_la_LIBADD="-lGL -lGLU"

%install
%makeinstall_std libgle_la_LIBADD="-lGL -lGLU"
mv %buildroot%_docdir/%oname %buildroot%_docdir/%name-%version

%files
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version/*
%exclude %_docdir/%name-%version/examples
%exclude %_docdir/%name-%version/html
%_libdir/lib%oname.so.*

%files devel
%_libdir/lib%oname.so
%_includedir/GL/*
%_man3dir/*

%files doc
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version/examples
%doc %_docdir/%name-%version/html

%changelog
* Mon Nov 09 2009 Alexey I. Froloff <raorn@altlinux.org> 3.1.0-alt7
- spec cleanup

* Sun Mar 19 2006 Sir Raorn <raorn@altlinux.ru> 3.1.0-alt6
- libgle should be linked with libGL and libGLU

* Sat Jan 28 2006 Sir Raorn <raorn@altlinux.ru> 3.1.0-alt5
- Rebuilt with new Xorg, buildreqs updated

* Thu Jun 16 2005 Sir Raorn <raorn@altlinux.ru> 3.1.0-alt4
- Renamed sourcerpm to libgle due to conflict with http://glx.sf.net/ (closes: #7115)

* Fri Dec 12 2003 Sir Raorn <raorn@altlinux.ru> 3.1.0-alt3
- devel-static and *.la fixes

* Sun Apr 13 2003 Sir Raorn <raorn@altlinux.ru> 3.1.0-alt2
- Oops. Added %%post/%%postun scripts for lib%name

* Mon Apr 07 2003 Sir Raorn <raorn@altlinux.ru> 3.1.0-alt1
- Built for Sisyphus



