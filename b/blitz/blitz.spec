Name: blitz
Summary: C++ class library for scientific computing
Version: 0.10
Release: alt1.hg20120125
Group: Sciences/Mathematics
License: LGPL v2.1
URL: http://www.oonumerics.org/blitz/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone http://blitz.hg.sourceforge.net:8000/hgroot/blitz/blitz
Source: %name-%version.tar.gz

Requires: lib%name = %version-%release

BuildPreReq: gcc-c++ gcc-fortran liblapack-devel
BuildPreReq: doxygen graphviz

%description
Blitz++ is a C++ class library for scientific computing which provides
performance on par with Fortran 77/90. It uses template techniques to achieve
high performance. Blitz++ provides dense arrays and vectors, random number
generators, and small vectors.

%package -n lib%name
Summary: Shared libraries of Blitz++
Group: System/Libraries

%description -n lib%name
Blitz++ is a C++ class library for scientific computing which provides
performance on par with Fortran 77/90. It uses template techniques to achieve
high performance. Blitz++ provides dense arrays and vectors, random number
generators, and small vectors.

This package contains shared libraries of Blitz++.

%package -n lib%name-devel
Summary: Development files of Blitz++
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
Blitz++ is a C++ class library for scientific computing which provides
performance on par with Fortran 77/90. It uses template techniques to achieve
high performance. Blitz++ provides dense arrays and vectors, random number
generators, and small vectors.

This package contains development files of Blitz++.

%package -n lib%name-devel-doc
Summary: Documentation for Blitz++
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
Blitz++ is a C++ class library for scientific computing which provides
performance on par with Fortran 77/90. It uses template techniques to achieve
high performance. Blitz++ provides dense arrays and vectors, random number
generators, and small vectors.

This package contains development documentation for Blitz++.

%package examples
Summary: Examples for Blitz++
Group: Development/Documentation
BuildArch: noarch

%description examples
Blitz++ is a C++ class library for scientific computing which provides
performance on par with Fortran 77/90. It uses template techniques to achieve
high performance. Blitz++ provides dense arrays and vectors, random number
generators, and small vectors.

This package contains examples for Blitz++.

%prep
%setup

%build
%add_optflags
%autoreconf
%configure \
%ifarch x86_64
	--enable-64bit \
%endif
	--enable-shared \
	--enable-optimize \
	--enable-threadsafe \
	--enable-fortran \
	--with-blas=%prefix
%make_build
%make info

%install
%makeinstall_std install-info

mv %buildroot%_docdir/%name-%version %buildroot%_docdir/%name
cp -fR examples %buildroot%_docdir/%name/

bzip2 ChangeLog*

%files
%doc AUTHORS COPYING COPYRIGHT ChangeLog.* LEGAL LICENSE README TODO
%_infodir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*

%files -n lib%name-devel-doc
%doc %dir %_docdir/%name
%doc %_docdir/%name/*
%exclude %_docdir/%name/examples

%files examples
%doc %dir %_docdir/%name
%_docdir/%name/examples

%changelog
* Fri Jan 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10-alt1.hg20120125
- New snapshot

* Sat Aug 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10-alt1.cvs20110820
- New snapshot

* Mon Apr 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10-alt1.cvs20110418
- Version 0.10

* Tue Apr 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1.cvs20100803.4
- Built with GotoBLAS2 instead of ATLAS
- Disabled devel-static package

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1.cvs20100803.3
- Added -g into compiler flags

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1.cvs20100803.2
- Rebuilt for debuginfo

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1.cvs20100803.1
- Rebuilt for soname set-versions

* Tue Aug 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1.cvs20100803
- New snapshot

* Tue Jul 07 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1.cvs20090702
- Initial build for Sisyphus

