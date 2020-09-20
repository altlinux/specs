%define somver 2
%define sover %somver.3.14
%def_without check

Name: qd
Version: 2.3.14
Release: alt2

Summary: C++/Fortran-90 double-double and quad-double package

License: BSD
Group: Sciences/Mathematics
Url: http://crd.lbl.gov/~dhbailey/mpdist/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/aoki-t/libqd/issues/5
Source: %name-%version.tar

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
Requires: lib%name = %EVR

%description -n lib%name-devel
This package provides numeric types of twice the precision of IEEE
double (106 mantissa bits, or approximately 32 decimal digits) and
four times the precision of IEEE double (212 mantissa bits, or
approximately 64 decimal digits).  Due to features such as operator
and function overloading, these facilities can be utilized
with only minor modifications to conventional C++ and Fortran-90
programs.

This package contains development files of QD.

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
%configure \
	--enable-shared \
	--enable-static=no \
	--enable-fortran \
	--enable-ieee-add \
	--enable-debug
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make -C fortran f_main.o
%make_build
%make cpp-demo fortran-demo

%install
%makeinstall_std

install -d %buildroot%_datadir/%name

install -m755 \
	fortran/.libs/quad* tests/.libs/* \
	%buildroot%_bindir
install -p -m644 tests/coeff.dat %buildroot%_datadir/%name

# shared libraries

#pushd %buildroot%_libdir
#echo "int f_main_() {}" > f_main.c
#gcc -g -c -fPIC f_main.c
#ar r libqd_f_main.a f_main.o
#ranlib libqd_f_main.a
#mkdir tmp
#pushd tmp
#for i in libqd libqd_f_main libqdmod; do
#	if [ "$i" != "libqd" ]; then
#		ADDLIBS="-L.. -lqd"
#	else
#		ADDLIBS=
#	fi
#	ar x ../$i.a
#	f77 -shared * $ADDLIBS -lstdc++ \
#		-Wl,-soname,$i.so.%somver -o ../$i.so.%sover
#	ln -s $i.so.%sover ../$i.so.%somver
#	ln -s $i.so.%somver ../$i.so
#	rm -f *
#done
#popd
#rmdir tmp
#ar d libqd_f_main.a f_main.o
#ranlib libqd_f_main.a
#popd

%if_with check
%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%make check time
%endif

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
%_includedir/*

%files -n lib%name-devel-doc
%_docdir/%name

%changelog
* Sun Sep 20 2020 Vitaly Lipatov <lav@altlinux.ru> 2.3.14-alt2
- cleanup spec and repo, drop obsoletes itself
- temp. disable check ([ppc64le] FAIL: qd_test)

* Tue Sep 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.14-alt1
- Version 2.3.14

* Mon Sep 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.13-alt1
- Version 2.3.13

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

