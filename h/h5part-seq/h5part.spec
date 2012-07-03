%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define oname h5part
%define otype seq

%if %otype == "seq"
%define ldir %_libdir/hdf5-seq
%else
%define ldir %mpidir
%endif

%define somver 0
%define sover %somver.0.0

Name: h5part-%otype
Version: 1.6.6
Release: alt2
Summary: API that simplifies the reading/writing of the data to the HDF5 file format
License: BSD
Group: Sciences/Other
Url: https://codeforge.lbl.gov/projects/h5part/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: H5Part-%version.tar.gz

BuildPreReq: gcc-c++ gcc-fortran doxygen graphviz python-devel
BuildPreReq: zlib-devel libsz2-devel
%if %otype == "mpi"
BuildPreReq: %mpiimpl-devel libhdf5-mpi-devel libmpe2-devel chrpath
%else
BuildPreReq: libhdf5-devel
%endif

Requires: lib%name = %version-%release

%description
H5Part is a very simple data storage schema and provides an API that
simplifies the reading/writing of the data to the HDF5 file format. An
important foundation for a stable visualization and data analysis
environment is a stable and portable file storage format and its
associated APIs. The presence of a "common file storage format,"
including associated APIs, will help foster a fundamental level of
interoperability across the project's software infrastructure. It will
also help ensure that key data analysis capabilities are present during
the earliest phases of the software development effort.

%package -n lib%name
Summary: Shared libraries of H5Part
Group: System/Libraries

%description -n lib%name
H5Part is a very simple data storage schema and provides an API that
simplifies the reading/writing of the data to the HDF5 file format. An
important foundation for a stable visualization and data analysis
environment is a stable and portable file storage format and its
associated APIs. The presence of a "common file storage format,"
including associated APIs, will help foster a fundamental level of
interoperability across the project's software infrastructure. It will
also help ensure that key data analysis capabilities are present during
the earliest phases of the software development effort.

This package contains shared libraries of H5Part.

%package -n lib%name-devel
Summary: Development files of H5Part
Group: Development/Other
Requires: lib%name = %version-%release
%if %otype == "seq"
Requires: libhdf5-devel %mpiimpl-devel
%else
Requires: libhdf5-mpi-devel
%endif

%description -n lib%name-devel
H5Part is a very simple data storage schema and provides an API that
simplifies the reading/writing of the data to the HDF5 file format. An
important foundation for a stable visualization and data analysis
environment is a stable and portable file storage format and its
associated APIs. The presence of a "common file storage format,"
including associated APIs, will help foster a fundamental level of
interoperability across the project's software infrastructure. It will
also help ensure that key data analysis capabilities are present during
the earliest phases of the software development effort.

This package contains development files of H5Part.

%package -n lib%name-devel-doc
Summary: Documentation for H5Part
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
H5Part is a very simple data storage schema and provides an API that
simplifies the reading/writing of the data to the HDF5 file format. An
important foundation for a stable visualization and data analysis
environment is a stable and portable file storage format and its
associated APIs. The presence of a "common file storage format,"
including associated APIs, will help foster a fundamental level of
interoperability across the project's software infrastructure. It will
also help ensure that key data analysis capabilities are present during
the earliest phases of the software development effort.

This package contains development documentation for H5Part.

%prep
%setup
rm -f aclocal.m4

%build
%if %otype == "mpi"
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"
%endif

%autoreconf
%add_optflags %optflags_shared
%configure \
%if %otype == "mpi"
	--enable-parallel \
	--with-mpipath=%mpidir \
%endif
	--prefix=%ldir \
	--bindir=%ldir/bin \
	--libdir=%ldir/lib \
	--includedir=%ldir/include \
	--enable-shared \
	--enable-fortran \
	--enable-tools \
	--enable-python \
	--with-hdf5path=%ldir \
	--with-hdf5=%ldir
%make_build

pushd doc
doxygen
popd

%install
%if %otype == "mpi"
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"
%endif

%makeinstall_std

%if %otype == "seq"
install -d %buildroot%_bindir
pushd %buildroot%ldir/bin
for i in *; do
	ln -s %ldir/bin/$i %buildroot%_bindir/
done
popd
%else
for i in %buildroot%ldir/bin/*; do
	chrpath -r %mpidir/lib $i
done
%endif

%files
%doc AUTHORS COPYING ChangeLog NEWS README
%dir %ldir/bin
%ldir/bin/*
%if %otype == "seq"
%_bindir/*
%endif

%files -n lib%name
#_libdir/*.so.*
%ldir/lib/*.so.*

%files -n lib%name-devel
%ldir/lib/*.so
%ldir/include

%if %otype == "seq"
%files -n lib%name-devel-doc
%doc doc/ReferencePages/*
%endif

%changelog
* Tue Jun 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.6-alt2
- Rebuilt

* Fri Feb 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.6-alt1
- Version 1.6.6

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.5-alt2
- Rebuilt

* Thu Dec 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.5-alt1
- Version 1.6.5

* Tue Sep 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.4-alt2
- Rebuilt with libhdf5-7

* Mon Sep 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.4-alt1
- Version 1.6.4

* Fri Mar 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.2-alt4
- Rebuilt for debuginfo

* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.2-alt3
- Rebuilt for soname set-versions

* Thu Oct 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.2-alt2
- Fixed linking of libraries

* Thu Sep 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.2-alt1
- Initial build for Sisyphus

