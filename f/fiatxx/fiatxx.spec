%define lname libfiat
%define sover 0
Name: fiatxx
Version: 3.14159
Release: alt9
Summary: FInite element Automatic Tabulator (C++ implementation)
License: LGPL
Group: Sciences/Mathematics
Url: http://www.fenics.org/wiki/FIAT
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone http://www.fenics.org/dev/fiat++
Source: %name-%version.tar.gz

BuildPreReq: gcc-fortran gcc-c++ liblapack-devel libblitz-devel

%description
FIAT++ is a FInite element Automatic Tabulator, written in C++.

%package -n lib%name
Summary: Shared library of FIAT++
Group: System/Libraries

%description -n lib%name
FIAT++ is a FInite element Automatic Tabulator, written in C++.

This package contains shared library of FIAT++.

%package -n lib%name-devel
Summary: Development files of FIAT++
Group: Development/C++
Requires: lib%name = %version-%release
Requires: libblitz-devel

%description -n lib%name-devel
FIAT++ is a FInite element Automatic Tabulator, written in C++.

This package contains development files of FIAT++.

%package -n lib%name-devel-static
Summary: Static development files of FIAT++
Group: Development/C++
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
FIAT++ is a FInite element Automatic Tabulator, written in C++.

This package contains static development files of FIAT++.

%prep
%setup
rm -fR autom4te.cache

%build
%add_optflags -pthread %optflags_shared
%configure --with-blas=goto2
%make_build

%install
%makeinstall_std
install -m644 Makefile.export.FIAT %buildroot/%_includedir

mkdir tmp
pushd tmp
ar x %buildroot%_libdir/%lname.a
g++ -shared -o %lname.so.%sover \
	-Wl,-soname,%lname.so.%sover \
	* -llapack -lgoto2

install -m644 %lname.so.%sover %buildroot%_libdir
ln -s %lname.so.%sover %buildroot%_libdir/%lname.so
popd

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

#files -n lib%name-devel-static
#_libdir/*.a

%changelog
* Wed Aug 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.14159-alt9
- Fixed build

* Wed Apr 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.14159-alt8
- Disabled devel-static package

* Fri Apr 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.14159-alt7
- Rebuilt with GotoBLAS2 1.13-alt3

* Thu Apr 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.14159-alt6
- Built with GotoBLAS2 instead of ATLAS

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.14159-alt5
- Rebuilt for debuginfo

* Fri Oct 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.14159-alt4
- Rebuilt with new ATLAS

* Tue Oct 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.14159-alt3
- Rebuilt for soname set-versions

* Mon Aug 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.14159-alt2
- Fixed Makefile.export.FIAT

* Sat Aug 08 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.14159-alt1
- Initial build for Sisyphus

