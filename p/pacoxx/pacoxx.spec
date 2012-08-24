%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define ldir %_libdir/PaCO++

Name: pacoxx
Version: 0.2.beta
Release: alt2
Summary: PaCO++: Portable Parallel CORBA Object
License: GPLv2+ / LGPLv2+
Group: Networking/Remote access
Url: http://www.irisa.fr/myriads/Paco++/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-c++ %mpiimpl-devel libomniORB-devel python-devel
BuildPreReq: java-devel-default xerces-j2
BuildPreReq: doxygen graphviz latex2html texlive-latex-recommended

Requires: lib%name = %version-%release
Requires: xerces-j2 %mpiimpl

%description
Parallel CORBA objects are defined as a collection of identical CORBA
objects. They aim at providing parallelism support to CORBA. CORBA
objects of a collection are assumed to work together. They are expected
to communicate thanks to an external mechanism, like for example via
MPI. We call such objects portable parallel CORBA objects.

PaCO++ provides portable parallel CORBA objects on top of compliant ORB
without involving whatsoever modification of the CORBA specifications.

%package -n lib%name
Summary: Shared libraries of PaCO++
Group: System/Libraries

%description -n lib%name
Parallel CORBA objects are defined as a collection of identical CORBA
objects. They aim at providing parallelism support to CORBA. CORBA
objects of a collection are assumed to work together. They are expected
to communicate thanks to an external mechanism, like for example via
MPI. We call such objects portable parallel CORBA objects.

PaCO++ provides portable parallel CORBA objects on top of compliant ORB
without involving whatsoever modification of the CORBA specifications.

This package contains shared libraries of PaCO++.

%package devel
Summary: Development files of PaCO++
Group: Development/C++
Requires: lib%name = %version-%release
Requires: libomniORB-devel %mpiimpl-devel
BuildArch: noarch

%description devel
Parallel CORBA objects are defined as a collection of identical CORBA
objects. They aim at providing parallelism support to CORBA. CORBA
objects of a collection are assumed to work together. They are expected
to communicate thanks to an external mechanism, like for example via
MPI. We call such objects portable parallel CORBA objects.

PaCO++ provides portable parallel CORBA objects on top of compliant ORB
without involving whatsoever modification of the CORBA specifications.

This package contains development files of PaCO++.

%package docs
Summary: Documentation for PaCO++
Group: Documentation
BuildArch: noarch

%description docs
Parallel CORBA objects are defined as a collection of identical CORBA
objects. They aim at providing parallelism support to CORBA. CORBA
objects of a collection are assumed to work together. They are expected
to communicate thanks to an external mechanism, like for example via
MPI. We call such objects portable parallel CORBA objects.

PaCO++ provides portable parallel CORBA objects on top of compliant ORB
without involving whatsoever modification of the CORBA specifications.

This package contains documentation for PaCO++.

%package examples
Summary: Examples for PaCO++
Group: Development/Documentation

%description examples
Parallel CORBA objects are defined as a collection of identical CORBA
objects. They aim at providing parallelism support to CORBA. CORBA
objects of a collection are assumed to work together. They are expected
to communicate thanks to an external mechanism, like for example via
MPI. We call such objects portable parallel CORBA objects.

PaCO++ provides portable parallel CORBA objects on top of compliant ORB
without involving whatsoever modification of the CORBA specifications.

This package contains examples for PaCO++.

%prep
%setup

%build
source %mpidir/bin/mpivars.sh                                                                     
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"
export PACOORB=%prefix
export CLASSPATH=%_javadir/xerces-j.jar

%add_optflags %optflags_shared $(pkg-config omniORB4 --cflags)
omniORB_4_0=$(rpm -q --queryformat '%{VERSION}' libomniORB)
%add_optflags -I$PWD/.lib/orb -DomniORB_4_0=\\\"$omniORB_4_0\\\"
%configure \
	--prefix=%ldir \
	--with-orb-dir=%prefix \
	--with-orb-flags="%optflags" \
	--with-mpi \
	--with-mpi-dir=%mpidir \
	--with-lib-mpi="-lmpi_cxx -lmpi"
# --with-extra-libs=""
%make MPIDIR=%mpidir

doxygen PaCO.doxygen
pushd Doc
latex2html PaCO++-manual.tex
popd

%install
source %mpidir/bin/mpivars.sh                                                                     
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"
export PACOORB=%prefix

%ifarch x86_64
export LIB_SUFFIX=64
%endif
%makeinstall_std

install -d %buildroot%_javadir %buildroot%_bindir %buildroot%_libdir

mv %buildroot%ldir/%_lib/PaCO.jar %buildroot%_javadir/
mv %buildroot%ldir/%_lib/*.so* %buildroot%_libdir/
mv %buildroot%ldir/bin/* %buildroot%_bindir/
mv %buildroot%ldir/include %buildroot%prefix/

cat <<EOF >%buildroot%_bindir/pacoenv.sh
#!/bin/bash

export PACOORB=%prefix
export PACOPATH=%ldir
if [ "$CLASSPATH" = "" ]; then
	export CLASSPATH=%_javadir/xerces-j.jar
else
	export CLASSPATH=$CLASSPATH:%_javadir/xerces-j.jar
fi

EOF
chmod +x %buildroot%_bindir/pacoenv.sh

%files
%doc COPYRIGHT CREDITS
%_bindir/*
%_javadir/*
%ldir/IDL2Tool
%ldir/GenFiles
%ldir/DistributionLibraries
%ldir/ORB

%files -n lib%name
%_libdir/*.so
%dir %ldir

%files devel
%_includedir/*

%files docs
%doc doc/html Doc/PaCO++-manual

%files examples
%dir %ldir
%ldir/Examples

%changelog
* Fri Aug 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.beta-alt2
- Fixed bin-permissions repocop warning

* Thu Aug 23 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.beta-alt1
- Initial build for Sisyphus

