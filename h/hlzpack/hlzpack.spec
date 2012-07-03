%define somver 0
%define sover %somver.4.0
Name: hlzpack
Version: 04.00
Release: alt7
Summary: Hermitian LancZos PACKage
License: BSD
Group: Sciences/Mathematics
Url: http://crd.lbl.gov/~osni/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://crd.lbl.gov/~osni/Codes/hlzpack.zip

BuildPreReq: liblapack-goto-devel libparmetis-devel
BuildPreReq: gcc-fortran unzip

%description
The HLZPACK package corresponds to a set of subprograms written in
standard Fortran 77 intended for the computation of scalars eig
and vectors (x) for the problem (H)*(x)-eig*(x)=0, where (H) is
a complex Hermitian matrix of dimension N.

%package -n lib%name
Summary: Shared library of HLZPACK
Group: System/Libraries

%description -n lib%name
The HLZPACK package corresponds to a set of subprograms written in
standard Fortran 77 intended for the computation of scalars eig
and vectors (x) for the problem (H)*(x)-eig*(x)=0, where (H) is
a complex Hermitian matrix of dimension N.

This package contains shared library of HLZPACK.

%package -n lib%name-devel
Summary: Development library of HLZPACK
Group: Development/Other
Requires: lib%name = %version-%release

%description -n lib%name-devel
The HLZPACK package corresponds to a set of subprograms written in
standard Fortran 77 intended for the computation of scalars eig
and vectors (x) for the problem (H)*(x)-eig*(x)=0, where (H) is
a complex Hermitian matrix of dimension N.

This package contains development library of HLZPACK.

%package -n lib%name-devel-static
Summary: Static library of HLZPACK
Group: Development/Other
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
The HLZPACK package corresponds to a set of subprograms written in
standard Fortran 77 intended for the computation of scalars eig
and vectors (x) for the problem (H)*(x)-eig*(x)=0, where (H) is
a complex Hermitian matrix of dimension N.

This package contains static library of HLZPACK.

%package examples
Summary: Examples for HLZPACK
Group: Development/Documentation
Requires: lib%name = %version-%release

%description examples
The HLZPACK package corresponds to a set of subprograms written in
standard Fortran 77 intended for the computation of scalars eig
and vectors (x) for the problem (H)*(x)-eig*(x)=0, where (H) is
a complex Hermitian matrix of dimension N.

This package contains examples for HLZPACK.

%package -n lib%name-devel-doc
Summary: Documentation for HLZPACK
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
The HLZPACK package corresponds to a set of subprograms written in
standard Fortran 77 intended for the computation of scalars eig
and vectors (x) for the problem (H)*(x)-eig*(x)=0, where (H) is
a complex Hermitian matrix of dimension N.

This package contains development documentation for HLZPACK.

%prep
%setup
touch Makefile sys/Makefile src/double/Makefile

%build
sed -i 's|@BUILDLIBS@|%buildroot%_libdir|g' \
	Makefile drv/Makefile
sed -i 's|@SOMVER@|%somver|g' Makefile
sed -i 's|@SOVER@|%sover|g' Makefile

%install
%make_build g77.lib

sed -i 's|%buildroot||' drv/Makefile
install -d %buildroot%_libdir/%name/examples
cp -f drv/* %buildroot%_libdir/%name/examples/
rm -f %buildroot%_libdir/%name/examples/*.o

install -d %buildroot%_docdir/lib%name-devel/sources
install -p -m644 doc/* \
	%buildroot%_docdir/lib%name-devel
install -p -m644 src/double/*.f \
	%buildroot%_docdir/lib%name-devel/sources

%files -n lib%name
%doc license.txt README
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so

#files -n lib%name-devel-static
#_libdir/*.a

%files -n lib%name-devel-doc
%_docdir/lib%name-devel

%files examples
%dir %_libdir/%name
%_libdir/%name/examples

%changelog
* Wed Apr 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 04.00-alt7
- Built with GotoBLAS2 instead of ATLAS
- Disabled devel-static package

* Fri Mar 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 04.00-alt6
- Added -g into compiler flags

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 04.00-alt5
- Rebuilt for debuginfo

* Wed Oct 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 04.00-alt4
- Rebuilt for soname set-versions

* Thu Aug 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 04.00-alt3
- Removed path to buildroot

* Wed Oct 07 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 04.00-alt2
- Fixed package summary

* Sun Oct 04 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 04.00-alt1
- Initial build for Sisyphus

