%define _unpackaged_files_terminate_build 1 

Name: libminc
Version: 2.4.3
Release: alt2

Group: System/Libraries
Summary: The core library and API of the MINC toolkit 
License: MIT
Url: https://github.com/BIC-MNI/libminc

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires: gcc-c++ cmake 
BuildRequires: zlib-devel libhdf5-devel netcdf-cxx4-devel libniftilib-devel

%define _description \
The MINC file format is a highly flexible medical image file format \
built on the HDF5 generalized data format. The format is \
simple, self-describing, extensible, portable and N-dimensional, with \
programming interfaces for both low-level data access and high-level \
volume manipulation. On top of the libraries is a suite of generic \
image-file manipulation tools. The format, libraries and tools are \
designed for use in a medical-imaging research environment : they are \
simple and powerful and make no attempt to provide a pretty interface \
to users.

%description 
%_description

%package devel
Summary: Development files for libminc
Group: Development/C
%description devel 
This package contains development files for libminc.
%_description

%prep
%setup
%patch -p1

%build
%cmake \
    -DLIBMINC_BUILD_SHARED_LIBS=ON \
    -DLIBMINC_USE_SYSTEM_NIFTI=ON \
    -DLIBMINC_NIFTI_SUPPORT=OFF \
    -DLIBMINC_MINC1_SUPPORT=OFF \
    -DLIBMINC_BUILD_EZMINC_EXAMPLES=OFF \
    %nil
%cmake_build VERBOSE=1

%install
%cmakeinstall_std

%files
%doc README COPYING NEWS ChangeLog
%_libdir/lib*.so.*

%files devel
%_libdir/lib*.so
%_libdir/cmake/%name/*.cmake
%_includedir/*

%changelog
* Fri Apr 16 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.4.3-alt2
- Updated build dependencies.

* Mon Feb 18 2019 Slava Aseev <ptrnine@altlinux.org> 2.4.3-alt1
- Initial build for ALT

