%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define somver 0
%define sover %somver.0.0
Name: trlan
Version: 20100901
Release: alt3
Summary: The thick-restart Lanczos method
License: BSD-like
Group: Sciences/Mathematics
Url: http://crd.lbl.gov/~kewu/trlan.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: https://codeforge.lbl.gov/frs/download.php/15/trlan.tar.gz
Source1: http://lbl.gov/~kwu/trlan-license.txt

BuildPreReq: liblapack-devel
BuildPreReq: %mpiimpl-devel

%description
This software package implements the thick-restart Lanczos method. It can be
used on either a single address space machine or a distributed parallel machine.
The user can choose to implement or use a matrix-vector multiplication routine
in any form convenient. Most of the arithmetic computations in the software are
done through calls to BLAS and LAPACK.

The software is written in Fortran 90. Because Fortran 90 offers many utility
functions such functions such as dynamic memory management, timing functions,
random number generator and so on, the program is easily portable to different
machines without modifying the source code. It can also be easily accessed from
other language such as C or C++. Since the software is highly modularized, it
relatively easy to adopt it for different type of situation. For example if the
eigenvalue problem may have some symmetry and only a portion of the physical
domain is discretized, then the dot-product routine needs to be modified. In
this software, this modification is limited to one subroutine. It also can be
instructed to write checkpoint files so that it can be restarted is a later time.

%package doc
Summary: Documentation for TRLan
Group: Documentation
BuildArch: noarch

%description doc
This software package implements the thick-restart Lanczos method. It can be
used on either a single address space machine or a distributed parallel machine.
The user can choose to implement or use a matrix-vector multiplication routine
in any form convenient. Most of the arithmetic computations in the software are
done through calls to BLAS and LAPACK.

This package contains documentation for TRLan.

%package info
Summary: Info files for TRLan
Group: Documentation
BuildArch: noarch

%description info
This software package implements the thick-restart Lanczos method. It can be
used on either a single address space machine or a distributed parallel machine.
The user can choose to implement or use a matrix-vector multiplication routine
in any form convenient. Most of the arithmetic computations in the software are
done through calls to BLAS and LAPACK.

This package contains info files for TRLan.

%package examples
Summary: Examples for TRLan
Group: Documentation
BuildArch: noarch

%description examples
This software package implements the thick-restart Lanczos method. It can be
used on either a single address space machine or a distributed parallel machine.
The user can choose to implement or use a matrix-vector multiplication routine
in any form convenient. Most of the arithmetic computations in the software are
done through calls to BLAS and LAPACK.

This package contains examples for TRLan.

%package -n lib%name
Summary: Shared libraries of TRLan
Group: System/Libraries

%description -n lib%name
This software package implements the thick-restart Lanczos method. It can be
used on either a single address space machine or a distributed parallel machine.
The user can choose to implement or use a matrix-vector multiplication routine
in any form convenient. Most of the arithmetic computations in the software are
done through calls to BLAS and LAPACK.

This package contains development files of TRLan.

%package -n lib%name-devel
Summary: Development files of TRLan
Group: Development/Other
Requires: lib%name = %version-%release
Conflicts: lib%name-devel < %version-%release
Obsoletes: lib%name-devel < %version-%release

%description -n lib%name-devel
This software package implements the thick-restart Lanczos method. It can be
used on either a single address space machine or a distributed parallel machine.
The user can choose to implement or use a matrix-vector multiplication routine
in any form convenient. Most of the arithmetic computations in the software are
done through calls to BLAS and LAPACK.

This package contains development files of TRLan.

%package -n lib%name-devel-static
Summary: Static libraries of TRLan
Group: Development/Other
Requires: lib%name-devel = %version-%release
Conflicts: lib%name-devel < %version-%release

%description -n lib%name-devel-static
This software package implements the thick-restart Lanczos method. It can be
used on either a single address space machine or a distributed parallel machine.
The user can choose to implement or use a matrix-vector multiplication routine
in any form convenient. Most of the arithmetic computations in the software are
done through calls to BLAS and LAPACK.

This package contains static libraries of TRLan.

%prep
%setup
install -p -m644 %SOURCE1 .

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

export MPIDIR=%mpidir
%make_build lib
%make_build plib
pushd dym
%make_build TOPDIR=$PWD/..
popd

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

install -d %buildroot%_bindir
install -d %buildroot%_libdir
install -d %buildroot%_includedir
install -d %buildroot%_infodir
install -d %buildroot%_docdir/%name-%version/dym

install -m644 *.a %buildroot%_libdir
install -m644 SRC/*.mod %buildroot%_includedir
pushd dym
install -m755 grep2 tease try ttrl %buildroot%_bindir
rm -f grep2 tease try ttrl *.o
install -p -m644 * %buildroot%_docdir/%name-%version/dym
popd
cp -fR examples README *.txt %buildroot%_docdir/%name-%version/
install -p -m644 doc/*.html doc/*.ps %buildroot%_docdir/%name-%version
install -p -m644 doc/*.info* %buildroot%_infodir

# shared libraries

pushd %buildroot%_libdir
LIBS="$(ls *.a|sed 's|\.a||')"
mkdir tmp
pushd tmp
for i in $LIBS; do
	ar x ../$i.a
	mpif77 -shared * -llapack -lgoto2 \
		-Wl,-R%mpidir/lib \
		-Wl,-soname,$i.so.%somver -o ../$i.so.%sover
	ln -s $i.so.%sover ../$i.so.%somver
	ln -s $i.so.%somver ../$i.so
	rm -f *
done
popd
rmdir tmp
popd

%files
%_bindir/*
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version/README
%doc %_docdir/%name-%version/*.txt

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

#files -n lib%name-devel-static
#_libdir/*.a

%files doc
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version/*.html
%doc %_docdir/%name-%version/*.ps
%doc %_docdir/%name-%version/dym

%files examples
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version/examples

%files info
%_infodir/*

%changelog
* Mon Jun 25 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100901-alt3
- Rebuilt with OpenMPI 1.6

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100901-alt2
- Fixed RPATH

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100901-alt1
- Version 201009

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20021121-alt7
- Rebuilt

* Sun Apr 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20021121-alt6
- Built with GotoBLAS2 instead of ATLAS
- Disabled devel-static package

* Tue Mar 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20021121-alt5
- Added -g into compiler flags

* Fri Feb 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20021121-alt4
- Rebuilt for debuginfo

* Tue Oct 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20021121-alt3
- Fixed linking of libraries

* Tue Sep 08 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20021121-alt2
- Added shared libraries

* Sun Jul 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20021121-alt1
- Initial build for Sisyphus

