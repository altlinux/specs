%define somver 0
%define sover %somver.4.0
Name: skypack
Version: 04.00
Release: alt5
Summary: SKYline PACKage - computations with matrices stored in a skyline form
License: BSD
Group: Sciences/Mathematics
Url: http://crd.lbl.gov/~osni/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://crd.lbl.gov/~osni/Codes/skypack.zip

BuildPreReq: gcc-fortran liblapack-goto-devel
BuildPreReq: unzip tcsh

%description
The SKYPACK package corresponds to a set of subprograms written in
standard Fortran 77 intended for linear algebra operations with
real symmetric matrices stored in skyline form.

%package -n lib%name
Summary: Shared library of SKYPACK
Group: System/Libraries

%description -n lib%name
The SKYPACK package corresponds to a set of subprograms written in
standard Fortran 77 intended for linear algebra operations with
real symmetric matrices stored in skyline form.

This package contains shared library of SKYPACK.

%package -n lib%name-devel
Summary: Development library of SKYPACK
Group: Development/Other
Requires: lib%name = %version-%release

%description -n lib%name-devel
The SKYPACK package corresponds to a set of subprograms written in
standard Fortran 77 intended for linear algebra operations with
real symmetric matrices stored in skyline form.

This package contains development library of SKYPACK.

%package -n lib%name-devel-static
Summary: Static library of SKYPACK
Group: Development/Other
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
The SKYPACK package corresponds to a set of subprograms written in
standard Fortran 77 intended for linear algebra operations with
real symmetric matrices stored in skyline form.

This package contains static library of SKYPACK.

%package examples
Summary: Examples for SKYPACK
Group: Development/Documentation
Requires: lib%name = %version-%release

%description examples
The SKYPACK package corresponds to a set of subprograms written in
standard Fortran 77 intended for linear algebra operations with
real symmetric matrices stored in skyline form.

This package contains examples for SKYPACK.

%package -n lib%name-devel-doc
Summary: Documentation for SKYPACK
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
The SKYPACK package corresponds to a set of subprograms written in
standard Fortran 77 intended for linear algebra operations with
real symmetric matrices stored in skyline form.

This package contains development documentation for SKYPACK.

%prep
%setup
chmod +x creator
sed -i 's|@SOMVER@|%somver|g' src/double/Makefile
sed -i 's|@SOVER@|%sover|g' src/double/Makefile

%build
mkdir -p lib
./creator -k

%install
install -d %buildroot%_libdir/%name/examples

cp -P lib/* %buildroot%_libdir/
cp -f drv/* %buildroot%_libdir/%name/examples/
rm -f buildroot%_libdir/%name/examples/*.o

mkdir sources
cp src/double/* sources/
rm -f sources/*.o


%files -n lib%name
%doc license.txt README
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so

#files -n lib%name-devel-static
#_libdir/*.a

%files -n lib%name-devel-doc
%doc doc/* sources

%files examples
%dir %_libdir/%name
%_libdir/%name/examples

%changelog
* Mon Apr 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 04.00-alt5
- Built with GotoBLAS instead of ATLAS
- Disabled devel-static package

* Tue Mar 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 04.00-alt4
- Added -g into compiler flags

* Fri Feb 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 04.00-alt3
- Rebuilt for debuginfo

* Wed Nov 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 04.00-alt2
- Rebuilt for soname set-versions

* Mon Oct 05 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 04.00-alt1
- Initial build for Sisyphus

