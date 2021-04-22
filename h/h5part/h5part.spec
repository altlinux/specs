%define _unpackaged_files_terminate_build 1

%define sover 0

Name: h5part
Version: 1.6.6
Release: alt4
Summary: API that simplifies the reading/writing of the data to the HDF5 file format
License: BSD
Group: Sciences/Other
Url: https://codeforge.lbl.gov/projects/h5part/

Source: H5Part-%version.tar

BuildPreReq: gcc-c++ gcc-fortran doxygen graphviz python-devel
BuildPreReq: zlib-devel libsz2-devel
BuildPreReq: libhdf5-devel

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

%package -n lib%name%sover
Summary: Shared libraries of H5Part
Group: System/Libraries
# TODO: remove obsolete on sover change
Obsoletes: lib%name-seq < %EVR

%description -n lib%name%sover
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
Requires: libhdf5-devel

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
%autoreconf
%add_optflags %optflags_shared
%configure \
	--enable-shared \
	--disable-static \
	--enable-fortran \
	--enable-tools \
	--enable-python \
	%nil

%make_build

pushd doc
doxygen
popd

%install
%makeinstall_std

%files
%doc AUTHORS COPYING ChangeLog NEWS README
%_bindir/*

%files -n lib%name%sover
%_libdir/*.so.%{sover}
%_libdir/*.so.%{sover}.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%files -n lib%name-devel-doc
%doc doc/ReferencePages/*

%changelog
* Fri Apr 16 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.6.6-alt4
- Rebuilt with new libhdf5.
- Updated packaging scheme.

* Wed Jun 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.6-alt3
- Rebuilt with new libhdf5

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

