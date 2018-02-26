%define somver 2
%define sover %somver.3.12
Name: qd
Version: 2.3.12
Release: alt2
Summary: C++/Fortran-90 double-double and quad-double package
License: BSD
Group: Sciences/Mathematics
Url: http://crd.lbl.gov/~dhbailey/mpdist/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar.gz

Requires: lib%name = %version-%release

BuildPreReq: gcc-fortran libgfortran-devel gcc-c++

%description
This package provides numeric types of twice the precision of IEEE
double (106 mantissa bits, or approximately 32 decimal digits) and
four times the precision of IEEE double (212 mantissa bits, or
approximately 64 decimal digits).  Due to features such as operator
and function overloading, these facilities can be utilized
with only minor modifications to conventional C++ and Fortran-90
programs.

In addition to the basic arithmetic operations (add, subtract,
multiply, divide, square root), common transcendental functions such
as the exponential, logarithm, trigonometric and hyperbolic functions
are also included.

%package -n lib%name
Summary: Shared libraries  of QD
Group: System/Libraries

%description -n lib%name
This package provides numeric types of twice the precision of IEEE
double (106 mantissa bits, or approximately 32 decimal digits) and
four times the precision of IEEE double (212 mantissa bits, or
approximately 64 decimal digits).  Due to features such as operator
and function overloading, these facilities can be utilized
with only minor modifications to conventional C++ and Fortran-90
programs.

This package contains shared libraries of QD.

%package -n lib%name-devel
Summary: Development files of QD
Group: Development/Other
Requires: lib%name = %version-%release
Conflicts: lib%name-devel < %version-%release
Obsoletes: lib%name-devel < %version-%release

%description -n lib%name-devel
This package provides numeric types of twice the precision of IEEE
double (106 mantissa bits, or approximately 32 decimal digits) and
four times the precision of IEEE double (212 mantissa bits, or
approximately 64 decimal digits).  Due to features such as operator
and function overloading, these facilities can be utilized
with only minor modifications to conventional C++ and Fortran-90
programs.

This package contains development files of QD.

%package -n lib%name-devel-static
Summary: Static libraries of QD
Group: Development/Other
Requires: lib%name-devel = %version-%release
Conflicts: lib%name-devel < %version-%release

%description -n lib%name-devel-static
This package provides numeric types of twice the precision of IEEE
double (106 mantissa bits, or approximately 32 decimal digits) and
four times the precision of IEEE double (212 mantissa bits, or
approximately 64 decimal digits).  Due to features such as operator
and function overloading, these facilities can be utilized
with only minor modifications to conventional C++ and Fortran-90
programs.

This package contains static libraries of QD.

%package -n lib%name-devel-doc
Summary: Documentation for QD
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
This package provides numeric types of twice the precision of IEEE
double (106 mantissa bits, or approximately 32 decimal digits) and
four times the precision of IEEE double (212 mantissa bits, or
approximately 64 decimal digits).  Due to features such as operator
and function overloading, these facilities can be utilized
with only minor modifications to conventional C++ and Fortran-90
programs.

This package contains documentation for QD.

%prep
%setup

%build
%add_optflags %optflags_shared
%autoreconf
%configure --enable-fortran --enable-ieee-add --enable-debug
%make_build
%make check time
%make cpp-demo fortran-demo

%install
%makeinstall_std

install -d %buildroot%_datadir/%name

install -m755 \
	fortran/quad??q fortran/quad??q2d \
	tests/*_test tests/huge tests/qd_timer \
	%buildroot%_bindir
install -p -m644 tests/coeff.dat %buildroot%_datadir/%name

# shared libraries

pushd %buildroot%_libdir
echo "int f_main_() {}" > f_main.c
gcc -g -c -fPIC f_main.c
ar r libqd_f_main.a f_main.o
ranlib libqd_f_main.a
mkdir tmp
pushd tmp
for i in libqd libqd_f_main libqdmod; do
	if [ "$i" != "libqd" ]; then
		ADDLIBS="-L.. -lqd"
	else
		ADDLIBS=
	fi
	ar x ../$i.a
	f77 -shared * $ADDLIBS -lstdc++ \
		-Wl,-soname,$i.so.%somver -o ../$i.so.%sover
	ln -s $i.so.%sover ../$i.so.%somver
	ln -s $i.so.%somver ../$i.so
	rm -f *
done
popd
rmdir tmp
ar d libqd_f_main.a f_main.o
ranlib libqd_f_main.a
popd

%files
%doc *.doc AUTHORS ChangeLog COPYING NEWS README* TODO
%_bindir/*
%exclude %_bindir/qd-config
%_datadir/%name

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_bindir/qd-config
%_libdir/*.so
%_libdir/%name
%_includedir/*

#files -n lib%name-devel-static
#_libdir/*.a

%files -n lib%name-devel-doc
%_docdir/%name

%changelog
* Fri Apr 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.12-alt2
- Fixed build with new automake

* Wed Dec 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.12-alt1
- Version 2.3.12
- Disabled devel-static package

* Fri Mar 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.11-alt4
- Added -g for gfortran flags

* Wed Feb 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.11-alt3
- Rebuilt for debuginfo

* Thu Oct 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.11-alt2
- Rebuilt for soname set-versions

* Fri Jul 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.11-alt1
- Version 2.3.11

* Sat Aug 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.8-alt3
- Added shared libraries

* Fri Jun 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.8-alt2
- Rebuild with PIC

* Mon May 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.8-alt1
- Version 2.3.8

* Thu May 07 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.7-alt1
- Initial build for Sisyphus

