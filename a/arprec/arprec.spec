%define somver 2
%define sover %somver.2.6
Name: arprec
Version: 2.2.8
Release: alt4
Summary: C++/Fortran-90 arbitrary precision package
License: BSD
Group: Sciences/Mathematics
Url: http://crd.lbl.gov/~dhbailey/mpdist/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar.gz

BuildPreReq: gcc-fortran libgfortran-devel gcc-c++ libqd-devel

Conflicts: Io-language

%description
This package supports a flexible, arbitrarily high level of numeric precision --
the equivalent of hundreds or even thousands of decimal digits (up to
approximately ten million digits if needed). Special routines are provided for
extra-high precision (above 1000 digits). The entire library is written in C++.
High-precision real, integer and complex datatypes are supported. Both C++ and
Fortran-90 translation modules modules are also provided that permit one to
convert an existing C++ or Fortran-90 program to use the library with only minor
changes to the source code. In most cases only the type statements and (in the
case of Fortran-90 programs) read/write statements need be changed. Six
implementations of PSLQ (one-, two- and three-level, regular and multi-pair) are
included, as well as three high-precision quadrature programs. New users are
encouraged to use this package, rather than MPFUN90 or MPFUN77 (see below).

%package -n lib%name
Summary: Shared libraries of ARPREC
Group: System/Libraries

%description -n lib%name
This package supports a flexible, arbitrarily high level of numeric precision --
the equivalent of hundreds or even thousands of decimal digits (up to
approximately ten million digits if needed). Special routines are provided for
extra-high precision (above 1000 digits). The entire library is written in C++.
High-precision real, integer and complex datatypes are supported. Both C++ and
Fortran-90 translation modules modules are also provided that permit one to
convert an existing C++ or Fortran-90 program to use the library with only minor
changes to the source code. In most cases only the type statements and (in the
case of Fortran-90 programs) read/write statements need be changed. Six
implementations of PSLQ (one-, two- and three-level, regular and multi-pair) are
included, as well as three high-precision quadrature programs. New users are
encouraged to use this package, rather than MPFUN90 or MPFUN77 (see below).

This package contains static libraries and headers of ARPREC.

%package -n lib%name-devel
Summary: Development files of ARPREC
Group: Development/Other
Requires: libqd-devel
Requires: lib%name = %version-%release
Conflicts: lib%name-devel < %version-%release
Obsoletes: lib%name-devel < %version-%release

%description -n lib%name-devel
This package supports a flexible, arbitrarily high level of numeric precision --
the equivalent of hundreds or even thousands of decimal digits (up to
approximately ten million digits if needed). Special routines are provided for
extra-high precision (above 1000 digits). The entire library is written in C++.
High-precision real, integer and complex datatypes are supported. Both C++ and
Fortran-90 translation modules modules are also provided that permit one to
convert an existing C++ or Fortran-90 program to use the library with only minor
changes to the source code. In most cases only the type statements and (in the
case of Fortran-90 programs) read/write statements need be changed. Six
implementations of PSLQ (one-, two- and three-level, regular and multi-pair) are
included, as well as three high-precision quadrature programs. New users are
encouraged to use this package, rather than MPFUN90 or MPFUN77 (see below).

This package contains development files of ARPREC.

%package -n lib%name-devel-static
Summary: Static libraries of ARPREC
Group: Development/Other
Requires: lib%name-devel = %version-%release
Conflicts: lib%name-devel < %version-%release

%description -n lib%name-devel-static
This package supports a flexible, arbitrarily high level of numeric precision --
the equivalent of hundreds or even thousands of decimal digits (up to
approximately ten million digits if needed). Special routines are provided for
extra-high precision (above 1000 digits). The entire library is written in C++.
High-precision real, integer and complex datatypes are supported. Both C++ and
Fortran-90 translation modules modules are also provided that permit one to
convert an existing C++ or Fortran-90 program to use the library with only minor
changes to the source code. In most cases only the type statements and (in the
case of Fortran-90 programs) read/write statements need be changed. Six
implementations of PSLQ (one-, two- and three-level, regular and multi-pair) are
included, as well as three high-precision quadrature programs. New users are
encouraged to use this package, rather than MPFUN90 or MPFUN77 (see below).

This package contains static libraries of ARPREC.

%package -n lib%name-devel-doc
Summary: Documentation for ARPREC
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
This package supports a flexible, arbitrarily high level of numeric precision --
the equivalent of hundreds or even thousands of decimal digits (up to
approximately ten million digits if needed). Special routines are provided for
extra-high precision (above 1000 digits). The entire library is written in C++.
High-precision real, integer and complex datatypes are supported. Both C++ and
Fortran-90 translation modules modules are also provided that permit one to
convert an existing C++ or Fortran-90 program to use the library with only minor
changes to the source code. In most cases only the type statements and (in the
case of Fortran-90 programs) read/write statements need be changed. Six
implementations of PSLQ (one-, two- and three-level, regular and multi-pair) are
included, as well as three high-precision quadrature programs. New users are
encouraged to use this package, rather than MPFUN90 or MPFUN77 (see below).

This package contains documentation for ARPREC.

%package toolkit
Summary: ARPREC's Experimental Mathematician's Toolkit
Group: Development/Other

%description toolkit
This package supports a flexible, arbitrarily high level of numeric precision --
the equivalent of hundreds or even thousands of decimal digits (up to
approximately ten million digits if needed). Special routines are provided for
extra-high precision (above 1000 digits). The entire library is written in C++.
High-precision real, integer and complex datatypes are supported. Both C++ and
Fortran-90 translation modules modules are also provided that permit one to
convert an existing C++ or Fortran-90 program to use the library with only minor
changes to the source code. In most cases only the type statements and (in the
case of Fortran-90 programs) read/write statements need be changed. Six
implementations of PSLQ (one-, two- and three-level, regular and multi-pair) are
included, as well as three high-precision quadrature programs. New users are
encouraged to use this package, rather than MPFUN90 or MPFUN77 (see below).

This verion of the ARPREC package now includes "The Experimental Mathematician's
Toolkit". This is a complete interactive high-precision arithmetic computing
environment. One enters expressions in a Mathematica-style syntax, and the
operations are performed using the ARPREC package, with a level of precision
that can be set from 100 to 1000 decimal digit accuracy. Variables and vector
arrays can be defined and referenced. This program supports all basic arithmetic
operations, common transcendental and combinatorial functions, multi-pair PSLQ
(one-, two- or three-level versions), high-precision quadrature, i.e. numeric
integration (Gaussian, error function or tanh-sinh), and summation of series.

%prep
%setup

%build
%add_optflags %optflags_shared
%autoreconf
%configure --enable-qd --enable-fortran --enable-debug
%make_build
#make check
%make cpp-demo fortran-demo toolkit

%install
%makeinstall_std

pushd tests
for i in $(ls pslq?); do
	mv $i cpp$i
done
popd
install -m755 \
	fortran/pslq? fortran/pslqm? fortran/quaderf fortran/quad?s fortran/roots \
	tests/mp_ex tests/mp_timer tests/mpslq?  tests/quads \
	tests/cpppslq? toolkit/math???? \
	%buildroot%_bindir

# shared libraries

pushd %buildroot%_libdir
mkdir tmp
pushd tmp
for i in libarprec libarprec_f_main libarprecmod; do
	if [ "$i" != "libarprec" ]; then
		ADDLIB="-L.. -larprec"
	else
		ADDLIB=
	fi
	ar x ../$i.a
	f77 -shared *.o $ADDLIB -lqd_f_main -lstdc++ -lc \
		-Wl,-soname,$i.so.%somver -o ../$i.so.%sover
	ln -s $i.so.%sover ../$i.so.%somver
	ln -s $i.so.%somver ../$i.so
	rm -f *
done
popd
rmdir tmp
popd

# There is a file in the package with a name starting with <tt>._</tt>, 
# the file name pattern used by Mac OS X to store resource forks in non-native 
# file systems. Such files are generally useless in packages and were usually 
# accidentally included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT -name '._*' -size 1 -print0 | xargs -0 grep -lZ 'Mac OS X' -- | xargs -0 rm -f
# for ones installed as %%doc
find . -name '._*' -size 1 -print0 | xargs -0 grep -lZ 'Mac OS X' -- | xargs -0 rm -f


%files
%doc *.doc AUTHORS ChangeLog COPYING NEWS README* TODO
%_bindir/*
%exclude %_bindir/%name-config
%exclude %_bindir/math*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_bindir/%name-config
%_libdir/*.so
%_libdir/%name
%_includedir/*

#files -n lib%name-devel-static
#_libdir/*.a

%files -n lib%name-devel-doc
%_docdir/%name

%files toolkit
%_bindir/math*

%changelog
* Wed Jun 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.8-alt4
- Fixed build

* Fri Apr 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.8-alt3
- Restored previous location of *.mod

* Fri Apr 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.8-alt2
- Fixed build with new automake

* Thu Dec 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.8-alt1
- Version 2.2.8
- Disabled devel-static package

* Thu Nov 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.7-alt6
- Rebuilt

* Sun Jul 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.7-alt5
- Added explicit conflict with Io-language

* Fri Mar 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.7-alt4
- Added -g for gfortran flags

* Wed Feb 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.7-alt3
- Rebuilt for debuginfo

* Wed Oct 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.7-alt2
- Rebuilt for soname set-versions

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.7-alt1
- Version 2.2.7

* Mon Jul 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.6-alt2
- Repocop fix for macos-resource-fork-file-in-package

* Fri Jul 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.6-alt1
- Version 2.2.6

* Fri Jun 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.5-alt1
- Version 2.2.5

* Sat Aug 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.3-alt3
- Added shared libraries

* Fri Jun 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.3-alt2
- Rebuild with PIC

* Mon May 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.3-alt1
- Version 2.2.3

* Thu May 07 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.2-alt1
- Initial build for Sisyphus

