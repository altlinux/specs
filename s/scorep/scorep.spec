%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%global optflags_lto %optflags_lto -ffat-lto-objects

%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

Name: scorep
Version: 6.0
Release: alt3
Summary: Score-P (Scalable Performance Measurement Infrastructure for Parallel Codes)
License: BSD
Group: Development/Tools
Url: http://www.vi-hps.org/projects/score-p/

Source: %name-%version.tar

BuildRequires(pre): %mpiimpl-devel
BuildRequires: libotf2-devel opari2-devel libcube-devel libcubegui-devel
BuildRequires: libbfd-devel uncrustify doxygen libpapi-devel flex
BuildRequires: libcube-devel graphviz texlive-base-bin
BuildRequires: lockfile-progs binutils-devel otf2 libgomp-devel
BuildRequires: chrpath

%description
The Score-P (Scalable Performance Measurement Infrastructure for
Parallel Codes) measurement infrastructure is a highly scalable and
easy-to-use tool suite for profiling, event trace recording, and
online analysis of HPC applications.

%package -n lib%name
Summary: Development files of Score-P
Group: System/Libraries

%description -n lib%name
The Score-P (Scalable Performance Measurement Infrastructure for
Parallel Codes) measurement infrastructure is a highly scalable and
easy-to-use tool suite for profiling, event trace recording, and
online analysis of HPC applications.

%package -n lib%name-devel
Summary: Development files of Score-P
Group: Development/C++
Requires: %name = %EVR

%description -n lib%name-devel
The Score-P (Scalable Performance Measurement Infrastructure for
Parallel Codes) measurement infrastructure is a highly scalable and
easy-to-use tool suite for profiling, event trace recording, and
online analysis of HPC applications.

This package contains development files of Score-P.

%package -n lib%name-devel-static
Summary: Static libraries of Score-P
Group: Development/C++
Requires: lib%name-devel = %EVR

%description -n lib%name-devel-static
The Score-P (Scalable Performance Measurement Infrastructure for
Parallel Codes) measurement infrastructure is a highly scalable and
easy-to-use tool suite for profiling, event trace recording, and
online analysis of HPC applications.

This package contains static libraries of Score-P.

%package docs
Summary: Documentation for Score-P
Group: Documentation
BuildArch: noarch

%description docs
The Score-P (Scalable Performance Measurement Infrastructure for
Parallel Codes) measurement infrastructure is a highly scalable and
easy-to-use tool suite for profiling, event trace recording, and
online analysis of HPC applications.

This package contains documentation for Score-P.

%prep
%setup

# remove some vendored sources
rm -rf vendor/{cubelib,cubew,opari2,otf2}

%build
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%autoreconf
%configure \
	--with-mpi=openmpi \
	--with-otf2 \
	--with-opari2 \
	--with-cubew \
	--with-cubelib \
	%nil

%make_build V=1

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%makeinstall_std

chrpath -d %buildroot%_bindir/scorep-score

# remove unneeded stuff
find %buildroot -type f -name libtool -print -delete

%files
%doc COPYING
%doc AUTHORS ChangeLog THANKS README OPEN_ISSUES
%_bindir/*
%exclude %_bindir/scorep-config
%_datadir/%name

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_bindir/scorep-config
%_includedir/*
%_libdir/*.so
%_libdir/scorep/*.o

%files -n lib%name-devel-static
%_libdir/*.a

%files docs
%_docdir/%name

%changelog
* Thu Sep 02 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 6.0-alt3
- Fixed build with LTO.

* Mon Dec 07 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 6.0-alt2
- Moved static libraries from lib%name-devel into lib%name-devel-static.

* Mon Sep 21 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 6.0-alt1
- Updated to upstream version 6.0.

* Wed Aug 01 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.1-alt2
- Updated build dependencies.

* Thu Sep 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.1-alt1
- Updated to upstream version 3.1.

* Thu Jul 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.rc2
- Version 1.3-rc2

* Tue Jun 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt1
- Version 1.2.3


* Wed Nov 20 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1
- Version 1.2.1

* Tue Sep 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1
- Initial build for Sisyphus

