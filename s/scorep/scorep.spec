%set_verify_elf_method unresolved=relaxed

%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

Name: scorep
Version: 1.2.1
Release: alt1
Summary: Score-P (Scalable Performance Measurement Infrastructure for Parallel Codes)
License: BSD
Group: Development/Tools
Url: http://www.vi-hps.org/projects/score-p/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://www.vi-hps.org/upload/packages/scorep/scorep-1.2.1.tar.gz

BuildPreReq: %mpiimpl-devel libotf2-devel opari2-devel libcube-devel
BuildPreReq: libbfd-devel uncrustify doxygen libpapi-devel flex
BuildPreReq: libopenpdt-devel libcube-devel graphviz texlive-base-bin
BuildPreReq: chrpath

%description
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

%build
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

#autoreconf
%configure \
	--with-mpi=openmpi \
	--with-otf2 \
	--with-opari2 \
	--with-cube \
	--with-pdt=%_bindir

pushd build-backend
%make_build V=1 libscorep_adapter_utils.la
%make_build V=1 libscorep_mutex_mockup.la
%make_build V=1 libscorep_adapter_compiler_mgmt.la
%make_build V=1 libscorep_measurement.la
%make_build V=1 libscorep_adapter_pomp_omp_mgmt_mockup.la
%make_build V=1 libscorep_online_access_mockup.la
%make_build V=1 libscorep_mutex_mockup.la
popd
pushd build-mpi
%make_build V=1 libscorep_online_access_mpp_mpi.la
popd

%make V=1 TOPDIR=$PWD

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%makeinstall_std TOPDIR=$PWD

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%_bindir/*
%exclude %_bindir/scorep-config
%_datadir/%name

%files -n lib%name-devel
%_bindir/scorep-config
%_includedir/*
%_libdir/*.a

%files docs
%_docdir/%name

%changelog
* Wed Nov 20 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1
- Version 1.2.1

* Tue Sep 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1
- Initial build for Sisyphus

