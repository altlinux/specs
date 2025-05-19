%define        _unpackaged_files_terminate_build 1
%define        _stripped_files_terminate_build 1

%def_disable   check
%define        oname HDF5
%define        sname hdf5mpi

Name:          lib%sname
Version:       1.14.6
Release:       alt1.1
Summary:       Hierarchical Data Format 5 library
License:       BSD
Group:         System/Libraries
Url:           http://www.hdfgroup.org/HDF5/
Vcs:           https://github.com/HDFGroup/hdf5.git

Source: %name-%version.tar
BuildRequires: /proc
BuildRequires: gcc-c++
BuildRequires: cmake
%{?_enable_check:BuildRequires: ctest}
BuildRequires: libssl-devel
BuildRequires: zlib-devel
BuildRequires: openmpi-devel

%add_optflags -fno-strict-aliasing

%description
HDF5 is a completely new Hierarchical Data Format product consisting
of a data format specification and a supporting library
implementation. HDF5 is designed to address some of the limitations of
the older HDF product and to address current and anticipated
requirements of modern systems and applications.


%package       -n lib%sname-hl
Summary:       Hierarchical Data Format 5 library
Group:         System/Libraries
Requires:      lib%sname = %EVR

%description   -n lib%sname-hl
HDF5 is a completely new Hierarchical Data Format product consisting
of a data format specification and a supporting library
implementation. HDF5 is designed to address some of the limitations of
the older HDF product and to address current and anticipated
requirements of modern systems and applications.


%package       -n lib%sname-devel
Summary:       HDF5 library development package
Group:         Development/C
Requires:      %sname-utils = %EVR
Requires:      gcc-c++
Requires:      cmake
Requires:      libstdc++-devel
Requires:      zlib-devel
Requires:      openmpi-devel

%description   -n lib%sname-devel
Header files for HDF5 library.


%package       -n %sname-utils
Summary:       HDF5 tools and utils
Group:         Development/Tools
Conflicts:     hdf5-tools

%description   -n %sname-utils
HDF5 is a completely new Hierarchical Data Format product consisting
of a data format specification and a supporting library
implementation. HDF5 is designed to address some of the limitations of
the older HDF product and to address current and anticipated
requirements of modern systems and applications.

This package contains utils for work with HDF5.

%prep
%setup

%ifarch %e2k
# too many unsupported warning options
find config/gnu-warnings/ -type f ! -name '*general' \
	-exec rm -f {} \; -exec touch {} \;
%endif

%build
%cmake \
   -DCMAKE_BUILD_TYPE=RelWithDebInfo \
   -DHDF5_ENABLE_PARALLEL=ON \
   -DHDF5_BUILD_PARALLEL_TOOLS=OFF \
   -DHDF5_LIB_BASE=%sname \
   -DHDF5_INSTALL_LIB_DIR=%_lib \
   -DHDF5_INSTALL_INCLUDE_DIR=%_includedir/%sname \
   -DHDF5_INSTALL_CMAKE_DIR=%_cmakedir/%oname \
   -DHDF5_INSTALL_DATA_DIR=%_defaultdocdir/%name \
   -DHDF5_INSTALL_DOC_DIR=%_defaultdocdir/%name \
   -DHDF5_ENABLE_SZIP_SUPPORT=ON \
   -DCMAKE_SKIP_BUILD_RPATH=ON \
   -DCMAKE_BUILD_WITH_INSTALL_RPATH=OFF \
   -DCMAKE_SKIP_RPATH=ON \
   -DHDF5_BUILD_CPP_LIB=OFF \
   -DONLY_SHARED_LIBS=ON \
   %nil

%cmake_build

%install
# NOTE due to duplication bug in #configure_package_config_file method
find -name hdf5-config.cmake -exec sed 's,${PACKAGE_PREFIX_DIR}/${PACKAGE_PREFIX_DIR},${PACKAGE_PREFIX_DIR},' -i {} \;

%cmakeinstall_std

%check
%ctest

%files
%_defaultdocdir/%name
%_libdir/lib%{sname}.so.*
%_libdir/lib%{sname}_tools.so.*
%_libdir/lib%{sname}.settings

%files         -n lib%sname-hl
%_libdir/lib%{sname}_hl.so.*

%files         -n lib%sname-devel
%doc COPYING COPYING_LBNL_HDF5
%doc README.md release_docs/{HISTORY*,RELEASE.txt}
%_libdir/lib%{sname}.so
%_libdir/lib%{sname}_hl.so
%_libdir/lib%{sname}_tools.so
%_includedir/%{sname}
%_pkgconfigdir/*
%_cmakedir/*

%files         -n %sname-utils
%_bindir/*
# used to show configuration at runtime


%changelog
* Mon May 19 2025 Pavel Skrylev <majioa@altlinux.org> 1.14.6-alt1.1
- ! restored lost dep to utils because of its cmake's config requirement

* Tue May 13 2025 Pavel Skrylev <majioa@altlinux.org> 1.14.6-alt1
- initial build for ALT Linux Sisyphus
