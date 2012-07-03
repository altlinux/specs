Name: gnuplotfortran
Version: 0.2.2
Release: alt1
Summary: Provides an interface between Fortran 90/95 and GNUPlot
License: LGPLv2.1+
Group: Development/Tools
Url: http://sourceforge.net/projects/gnuplotfortran/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: libfortranposix gcc-fortran

%description
This library is a Fortran 95 gnuplot interface for some Unix like OS'es.
This provides some routines that enables direct access of a child
gnuplot session from a Fortran 95 program. You will need a copy of
fortranposix to make this work.

%package -n lib%name
Summary: Shared library of gnuplotfortran
Group: System/Libraries

%description -n lib%name
This library is a Fortran 95 gnuplot interface for some Unix like OS'es.
This provides some routines that enables direct access of a child
gnuplot session from a Fortran 95 program. You will need a copy of
fortranposix to make this work.

%package devel
Summary: Development files of gnuplotfortran
Group: Development/Other
Requires: lib%name = %version-%release

%description devel
This library is a Fortran 95 gnuplot interface for some Unix like OS'es.
This provides some routines that enables direct access of a child
gnuplot session from a Fortran 95 program. You will need a copy of
fortranposix to make this work.

This package contains development files of gnuplotfortran.

%package -n lib%name-devel-doc
Summary: Documentation for gnuplotfortran
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
This library is a Fortran 95 gnuplot interface for some Unix like OS'es.
This provides some routines that enables direct access of a child
gnuplot session from a Fortran 95 program. You will need a copy of
fortranposix to make this work.

This package contains development documentation for gnuplotfortran.


%prep
%setup

%build
%make_build

%install
install -d %buildroot%_libdir
install -m644 *.so %buildroot%_libdir

install -d %buildroot%_includedir
install -m644 *.mod %buildroot%_includedir

install -d %buildroot%_infodir
install -p -m644 *.info %buildroot%_infodir

install -d %buildroot%_docdir
TOP=$PWD
pushd %buildroot%_docdir
tar -xf $TOP/gnuplotfortran-htmldoc.tar.bz2
popd

%files -n lib%name
%doc CHANGES CREDITS LICENSE README TODO
%_libdir/*.so

%files devel
%doc Makefile *.f90
%_includedir/*.mod
%_infodir/*

%files -n lib%name-devel-doc
%_docdir/%name
%doc *.pdf

%changelog
* Wed Mar 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1
- Initial build for Sisyphus

