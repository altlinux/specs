%define _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=relaxed

%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define over 2.3.1
%define cubever 3.4.2.%over
%define somver 0
%define sover %somver.%over

Name: scalasca
Version: %over
Release: alt3
Summary: Scalable performance Analysis of Large-Scale parallel Applications
License: MIT
Group: Development/Tools
Url: http://www.scalasca.org/

Source: %name-%version.tar
Source1: Makefile.shared
Source2: status.m4
Patch1: %name-%version-alt-linking.patch

Requires: papi
Requires: scorep libscorep-devel
Requires: cube
Conflicts: linuxtv-dvb-apps
Provides: kojak = 2.2p1_%over-%release
Conflicts: kojak < 2.2p1_%over-%release
Obsoletes: kojak < 2.2p1_%over-%release

BuildRequires(pre): %mpiimpl-devel
BuildRequires: libgomp-devel libpapi-devel
BuildRequires: doxygen binutils-devel
BuildRequires: texlive-latex-base ghostscript-utils chrpath
BuildRequires: libotf2-devel opari2-devel libcube-devel
BuildRequires: graphviz flex libgomp-devel

%description
The KOJAK project (Kit for Objective Judgement And Knowledge-based
detection of performance bottlenecks) was part of the European IST
working group APART, and has been complemented by the SCALASCA project
(Scalable performance Analysis of Large-Scale parallel Applications).

The projects aim to develop a generic automatic performance analysis
environment for parallel applications.  Performance problems are specified
in terms of execution patterns that represent situations of inefficient
behavior.  These patterns are input for an analysis process that recognizes
and quantifies the inefficient behavior in event traces.  Mechanisms that
hide the complex relationships within event pattern specifications allow a
simple description of inefficient behavior on a high level of abstraction.

%package doc
Summary: Documentation for SCALASCA
Group: Documentation
BuildArch: noarch

%description doc
The KOJAK project (Kit for Objective Judgement And Knowledge-based
detection of performance bottlenecks) was part of the European IST
working group APART, and has been complemented by the SCALASCA project
(Scalable performance Analysis of Large-Scale parallel Applications).

The projects aim to develop a generic automatic performance analysis
environment for parallel applications.  Performance problems are specified
in terms of execution patterns that represent situations of inefficient
behavior.  These patterns are input for an analysis process that recognizes
and quantifies the inefficient behavior in event traces.  Mechanisms that
hide the complex relationships within event pattern specifications allow a
simple description of inefficient behavior on a high level of abstraction.

This package contains documentation for SCALASCA.

%package -n lib%name
Summary: Shared libraries of SCALASCA
Group: System/Libraries

%description -n lib%name
The KOJAK project (Kit for Objective Judgement And Knowledge-based
detection of performance bottlenecks) was part of the European IST
working group APART, and has been complemented by the SCALASCA project
(Scalable performance Analysis of Large-Scale parallel Applications).

The projects aim to develop a generic automatic performance analysis
environment for parallel applications.  Performance problems are specified
in terms of execution patterns that represent situations of inefficient
behavior.  These patterns are input for an analysis process that recognizes
and quantifies the inefficient behavior in event traces.  Mechanisms that
hide the complex relationships within event pattern specifications allow a
simple description of inefficient behavior on a high level of abstraction.

This package contains shared libraries of SCALASCA.

%package -n lib%name-devel
Summary: development files of SCALASCA
Group: Development/Other
Requires: libpapi-devel libotf-devel
Requires: libiberty-devel %mpiimpl-devel binutils-devel
Provides: libkojak-devel = 2.2p1_%over-%release
Conflicts: libkojak-devel < 2.2p1_%over-%release
Obsoletes: libkojak-devel < 2.2p1_%over-%release
Conflicts: kojak < 2.2p1_%over-%release
Obsoletes: kojak < 2.2p1_%over-%release
Requires: lib%name = %EVR

%description -n lib%name-devel
The KOJAK project (Kit for Objective Judgement And Knowledge-based
detection of performance bottlenecks) was part of the European IST
working group APART, and has been complemented by the SCALASCA project
(Scalable performance Analysis of Large-Scale parallel Applications).

The projects aim to develop a generic automatic performance analysis
environment for parallel applications.  Performance problems are specified
in terms of execution patterns that represent situations of inefficient
behavior.  These patterns are input for an analysis process that recognizes
and quantifies the inefficient behavior in event traces.  Mechanisms that
hide the complex relationships within event pattern specifications allow a
simple description of inefficient behavior on a high level of abstraction.

This package contains development files of SCALASCA.

%prep
%setup
%patch1 -p2
# configure.ac uses some macros not provided by autoconf, just copy file with them from previous scalasca version
cp %SOURCE2 vendor/common/build-config/m4/status.m4

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"
export MPIDIR=%mpidir

export CC="mpicc -g"
export CXX="mpicxx -g"
%autoreconf
%configure \
	--prefix=%prefix \
	--with-papi=%prefix \
	--with-otf2 \
	--with-cube \
	--with-mpi=openmpi \
	--with-pdt=%prefix \
	--enable-all-mpi-wrappers \
	--with-binutils=%prefix \
	--enable-shared \
	--enable-static=no \
	%nil

export TOPDIR=$PWD
%make

pushd doc

pushd doxygen-common
doxygen doxygen-common.cfg
mkdir -p pearl/html
doxygen doxygen-pearl.cfg
popd

tar -xvf manual-html.tar.gz

popd

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

export TOPDIR=$PWD
%makeinstall_std

install -d %buildroot%_includedir
install -m644 src/epik/*.h %buildroot%_includedir/

for i in %buildroot%_libdir/*.so %buildroot%_bindir/*; do
	chrpath -r %mpidir/lib $i ||\
		chrpath -d $i ||:
done

%files
%doc ChangeLog COPYING OPEN_ISSUES README
%_bindir/*
%_datadir/%name

%files doc
%doc doc/*.pdf
%doc doc/doxygen-common/html
%doc doc/doxygen-common/pearl
%doc doc/manual
%_docdir/%name

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%changelog
* Fri Sep 18 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.1-alt3
- Updated conflicts and obsoletes.

* Fri Jul 27 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.1-alt2
- Updated build dependencies.

* Fri Sep 22 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.1-alt1
- Updated to upstream version 2.3.1.

* Wed Sep 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1-alt2.rc2
- Fixed build with gcc-6.

* Thu Jul 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1-alt1.rc2
- Version 2.1-rc2

* Mon Sep 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1
- Version 2.0

* Mon Jul 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.3-alt1
- Version 1.4.3

* Sat Feb 23 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.2-alt3
- Rebuilt with openpdt instead of pdtoolkit

* Fri Sep 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.2-alt2
- Fixed kinst-pomp for work with shared libraries

* Thu Sep 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.2-alt1
- Version 1.4.2
- Disabled static libraries

* Wed Sep 19 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt15
- Rebuilt with papi 5.0.0

* Mon Jun 25 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt14
- Rebuilt with OpenMPI 1.6

* Wed Jun 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt13
- Fixed build

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt12
- Fixed RPATH

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt11
- Rebuilt with papi 4.2.0
- Disabled using of perfctr

* Wed Nov 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt10
- Rebuilt

* Tue Mar 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt9
- Added -g into compiler flags

* Thu Feb 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt8
- Rebuilt for debuginfo

* Tue Dec 14 2010 Kirill A. Shutemov <kas@altlinux.org> 1.3.1-alt7
- Rebuilt with binutils-devel

* Mon Oct 25 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt6
- Rebuilt for soname set-versions

* Fri Oct 15 2010 Kirill A. Shutemov <kas@altlinux.org> 1.3.1-alt5
- Rebuilt wit new binutils

* Tue Oct 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt4
- Fixed linking

* Tue Aug 31 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt3
- Fixed for checkbashisms

* Fri Jul 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt2
- Rebuilt with papi 4.1.0

* Fri Jul 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1
- Version 1.3.1

* Tue Jun 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt7
- Rebuilt with binutils 2.20.51.0.9

* Sat Mar 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt6
- Rebuilt wit new binutils

* Sat Jan 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt5
- Rebuilt wit new binutils

* Tue Dec 15 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt4
- Release up

* Tue Nov 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt3
- Rebuilt with texlive instead of tetex

* Mon Nov 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2
- Rebuilt with binutils 2.20.51.0.2

* Tue Sep 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1
- Version 1.2
- Added shared libraries

* Wed Aug 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt6
- Rebuilt

* Wed Jul 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt5
- Created alternatives for CUBE

* Mon Jun 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt4.1
- Minimize requirements for devel package
- Extract Qt4/wxGTK+ CUBE's GUI and example into separate packages

* Mon Jun 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt4
- Nothing news

* Thu Jun 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt3
- Changed requirements: *-devel-static -> *-devel

* Sun Jun 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt2
- Moved szlib headers into separate package

* Wed Jun 10 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus

