%define oname oski
%define scalar_type real

%if "%scalar_type" == "real"
%define altname %oname-complex
%define value_binding double
%else
%define altname %oname-real
%define value_binding dcomplex
%endif

Name: %oname-%scalar_type
Version: 1.0.1h
Release: alt5
Summary: BeBOP Optimized Sparse Kernel Interface (OSKI) Library (%scalar_type scalars)
License: BSD
Group: Sciences/Mathematics
Url: http://bebop.cs.berkeley.edu/oski/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# cvs -z3 -d:pserver:anonymous@oski.cvs.sourceforge.net:/cvsroot/oski co -P oski
Source: %oname-%version.tar.gz

BuildPreReq: liblapack-goto-devel libfftw3-devel
BuildPreReq: libltdl-devel gcc-c++ gcc-fortran
BuildPreReq: doxygen graphviz texlive-latex-base texlive-lang-german

%description
The OSKI Library is a collection of low-level primitives
that provide automatically tuned sparse matrix kernels,
for use by solver libraries and applications.

%package -n lib%name
Summary: Shared libraries of OSKI (%scalar_type scalars)
Group: System/Libraries
Provides: lib%oname = %version-%release

%description -n lib%name
The OSKI Library is a collection of low-level primitives
that provide automatically tuned sparse matrix kernels,
for use by solver libraries and applications.

This package contains shared libraries of OSKI.

%package -n lib%name-devel
Summary: Development files of OSKI (%scalar_type scalars)
Group: Development/C
Requires: lib%name = %version-%release
Conflicts: lib%altname-devel

%description -n lib%name-devel
The OSKI Library is a collection of low-level primitives
that provide automatically tuned sparse matrix kernels,
for use by solver libraries and applications.

This package contains development files of OSKI.

%package -n lib%name-devel-static
Summary: Static libraries of OSKI (%scalar_type scalars)
Group: Development/C
Requires: lib%name-devel = %version-%release
Conflicts: lib%altname-devel-static

%description -n lib%name-devel-static
The OSKI Library is a collection of low-level primitives
that provide automatically tuned sparse matrix kernels,
for use by solver libraries and applications.

This package contains static libraries of OSKI.

%package -n lib%oname-devel-doc
Summary: Documentation for OSKI
Group: Development/Documentation
BuildArch: noarch

%description -n lib%oname-devel-doc
The OSKI Library is a collection of low-level primitives
that provide automatically tuned sparse matrix kernels,
for use by solver libraries and applications.

This package contains documentation for OSKI.

%prep
%setup
%if "%scalar_type" == "complex"
sed -i 's|@SCALAR_TYPE@|complex-|' src/Makefile.common
%else
sed -i 's|@SCALAR_TYPE@||' src/Makefile.common
%endif

%build
./bootstrap.bash

%configure \
	--enable-int-double \
	--disable-long-double \
	--enable-int-dcomplex \
	--disable-long-dcomplex \
	--enable-MBCSR-symm \
	--enable-MBCSR-ata \
	--enable-MBCSR-a_and_at \
	--without-papi \
	--with-blas="-llapack -lgoto2" \
	--with-index-binding=int \
	--with-value-binding=%value_binding

%make_build -C src/lt
%make_build
%make sitemods
%if "%scalar_type" == "real"
%make docs
%make -C doc libdep.ps
%endif

%install
%makeinstall_std -C src/lt
%makeinstall_std install-exec-hook

%files -n lib%name
%doc AUTHORS ChangeLog COPYING NEWS README
%dir %_libdir/%oname
%_libdir/%oname/*-1.so
%_libdir/%oname/*.lua
%_libdir/%oname/site-modules*.txt
%exclude %_libdir/%oname/site-modules-shared.txt
%exclude %_libdir/%oname/site-modules-static.txt

%files -n lib%name-devel
%_libdir/%oname/*.so
%exclude %_libdir/%oname/*-1.so
%_libdir/%oname/site-modules-shared.txt
%_includedir/%oname

%files -n lib%name-devel-static
%_libdir/%oname/*.a
%_libdir/%oname/site-modules-static.txt

%if "%scalar_type" == "real"
%files -n lib%oname-devel-doc
%doc CODING NOTES-devel TODO oski-ug.pdf example doc/html doc/*.ps
%endif

%changelog
* Fri Apr 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1h-alt5
- Rebuilt with GotoBLAS2 1.13-alt3

* Thu Apr 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1h-alt4
- Built with GotoBLAS2 instead of ATLAS

* Thu Mar 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1h-alt3
- Rebuilt for debuginfo

* Fri Oct 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1h-alt2
- Fixed underlinking

* Fri Nov 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1h-alt1
- Initial build for Sisyphus

