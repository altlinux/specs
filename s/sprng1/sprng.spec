%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define somver 0
%define sover %somver.1.0
Name: sprng1
Version: 1.0
Release: alt7
Summary: The Scalable Parallel Random Number Generators Library
License: GPL v2
Group: Sciences/Mathematics
Url: http://sprng.cs.fsu.edu/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://sprng.cs.fsu.edu/Version1.0/sprng.tar.Z
Source: %name-%version.tar.gz

Requires: lib%name = %version-%release

BuildPreReq: gcc-fortran gcc-c++ %mpiimpl-devel
BuildPreReq: libgmp-devel /usr/bin/compress

%description
Computational stochastic approaches (Monte Carlo methods) based on the random
sampling are becoming extremely important research tools not only in their
"traditional" fields such as physics, chemistry or applied mathematics but also
in social sciences and, recently, in various branches of industry. An indication
of importance is, for example, the fact that Monte Carlo calculations consume
about one half of the supercomputer cycles. One of the indispensable and
important ingredients for reliable and statistically sound calculations is the
source of pseudo random numbers. The goal of our project is to develop,
implement and test a scalable package for parallel pseudo random number
generation.

%package -n lib%name
Summary: Shared library of SPRNG
Group: System/Libraries
Requires: %name = %version-%release

%description -n lib%name
Computational stochastic approaches (Monte Carlo methods) based on the random
sampling are becoming extremely important research tools not only in their
"traditional" fields such as physics, chemistry or applied mathematics but also
in social sciences and, recently, in various branches of industry. An indication
of importance is, for example, the fact that Monte Carlo calculations consume
about one half of the supercomputer cycles. One of the indispensable and
important ingredients for reliable and statistically sound calculations is the
source of pseudo random numbers. The goal of our project is to develop,
implement and test a scalable package for parallel pseudo random number
generation.

This package contains shared library of SPRNG.

%package -n lib%name-devel
Summary: Development files of SPRNG
Group: Development/Other
Requires: %mpiimpl-devel
Requires: lib%name = %version-%release

%description -n lib%name-devel
Computational stochastic approaches (Monte Carlo methods) based on the random
sampling are becoming extremely important research tools not only in their
"traditional" fields such as physics, chemistry or applied mathematics but also
in social sciences and, recently, in various branches of industry. An indication
of importance is, for example, the fact that Monte Carlo calculations consume
about one half of the supercomputer cycles. One of the indispensable and
important ingredients for reliable and statistically sound calculations is the
source of pseudo random numbers. The goal of our project is to develop,
implement and test a scalable package for parallel pseudo random number
generation.

This package contains development files of SPRNG.

%package -n lib%name-devel-static
Summary: Static library of SPRNG
Group: Development/Other
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
Computational stochastic approaches (Monte Carlo methods) based on the random
sampling are becoming extremely important research tools not only in their
"traditional" fields such as physics, chemistry or applied mathematics but also
in social sciences and, recently, in various branches of industry. An indication
of importance is, for example, the fact that Monte Carlo calculations consume
about one half of the supercomputer cycles. One of the indispensable and
important ingredients for reliable and statistically sound calculations is the
source of pseudo random numbers. The goal of our project is to develop,
implement and test a scalable package for parallel pseudo random number
generation.

This package contains static library of SPRNG.

%package -n lib%name-devel-doc
Summary: Documentation for SPRNG
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
Computational stochastic approaches (Monte Carlo methods) based on the random
sampling are becoming extremely important research tools not only in their
"traditional" fields such as physics, chemistry or applied mathematics but also
in social sciences and, recently, in various branches of industry. An indication
of importance is, for example, the fact that Monte Carlo calculations consume
about one half of the supercomputer cycles. One of the indispensable and
important ingredients for reliable and statistically sound calculations is the
source of pseudo random numbers. The goal of our project is to develop,
implement and test a scalable package for parallel pseudo random number
generation.

This package contains development documentation for SPRNG.

%package examples
Summary: Examples for SPRNG
Group: Development/Documentation
Requires: lib%name = %version-%release

%description examples
Computational stochastic approaches (Monte Carlo methods) based on the random
sampling are becoming extremely important research tools not only in their
"traditional" fields such as physics, chemistry or applied mathematics but also
in social sciences and, recently, in various branches of industry. An indication
of importance is, for example, the fact that Monte Carlo calculations consume
about one half of the supercomputer cycles. One of the indispensable and
important ingredients for reliable and statistically sound calculations is the
source of pseudo random numbers. The goal of our project is to develop,
implement and test a scalable package for parallel pseudo random number
generation.

This package contains examples for SPRNG.

%prep
%setup

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-R,%mpidir/lib -L%mpidir/lib"

sed -i 's|@MPIDIR@|%mpidir|g' SRC/make.LINUX
%make

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-R,%mpidir/lib -L%mpidir/lib"

# libraries

install -d %buildroot%_libdir
rm -f lib/libsprngtest.a
install -m644 lib/*.a %buildroot%_libdir
pushd %buildroot%_libdir
LIBS="$(ls *.a|sed 's|\.a||')"
mkdir tmp
pushd tmp
for i in $LIBS; do
	ar x ../$i.a
	mpicc -shared * \
		-Wl,-R%mpidir/lib \
		-Wl,-soname,$i.so.%somver -o ../$i.so.%sover
	ln -s $i.so.%sover ../$i.so.%somver
	ln -s $i.so.%somver ../$i.so
	rm -f *
done
popd
rmdir tmp
popd

# includes

install -d %buildroot%_includedir/%name
install -p -m644 include/*.h %buildroot%_includedir/%name

# examples

install -d %buildroot%_libdir/%name/examples
cp EXAMPLES/* %buildroot%_libdir/%name/examples/

# docs

install -d %buildroot%_docdir/%name
pushd DOCS
tar -xf sprng.html.tar.Z
cp -fR README www %buildroot%_docdir/%name/
popd

%files
%doc CHANGES.TEXT README VERSION

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%files -n lib%name-devel-static
%_libdir/*.a

%files -n lib%name-devel-doc
%_docdir/%name

%files examples
%dir %_libdir/%name
%_libdir/%name/examples

%changelog
* Mon Jun 25 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt7
- Rebuilt with OpenMPI 1.6

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt6
- Fixed RPATH

* Tue Mar 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt5
- Added -g into compiler flags

* Fri Feb 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt4
- Rebuilt for debuginfo

* Tue Oct 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt3
- Rebuilt for soname set-versions

* Wed Oct 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Fixed overlinking of libraries

* Tue Sep 08 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

