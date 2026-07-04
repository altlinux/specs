# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: lib3mf
Version: 2.5.0
Release: alt1

Summary: lib3mf is an implementation of the 3D Manufacturing Format file standard
License: BSD-2-Clause
Group: Graphics
URL: https://github.com/3MFConsortium/lib3mf
VCS: https://github.com/3MFConsortium/lib3mf.git

# Source-url: https://github.com/3MFConsortium/lib3mf/archive/v%version/lib3mf-%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: act
BuildRequires: libzip-devel
BuildRequires: zlib-devel
BuildRequires: libssl-devel
BuildRequires: libfast_float-devel

BuildRequires: libgtest-devel

%description
lib3mf is a C++ implementation of the 3D Manufacturing Format standard.
This is a 3D printing standard for representing geometry as meshes.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %EVR

%description devel
lib3mf is a C++ implementation of the 3D Manufacturing Format standard.
This is a 3D printing standard for representing geometry as meshes.

%prep
%setup

# Set version
%__subst 's|@PROJECT_VERSION@|%version|' lib3mf.pc.in 

# The tests FTBFS with old gtest
# https://github.com/google/googletest/issues/2065
sed -i 's/INSTANTIATE_TEST_SUITE_P/INSTANTIATE_TEST_CASE_P/' Tests/CPP_Bindings/Source/*.cpp

%build
%cmake \
	-DLIB3MF_TESTS=ON \
	-DUSE_INCLUDED_ZLIB=OFF \
	-DUSE_INCLUDED_LIBZIP=OFF \
	-DUSE_INCLUDED_GTEST=OFF \
	-DUSE_INCLUDED_SSL=OFF \
	-DSTRIP_BINARIES=OFF \
	-DCMAKE_INSTALL_LIBDIR=%_libdir \
	-DCMAKE_INSTALL_INCLUDEDIR=%_includedir/%name
%cmake_build

%install
%cmake_install

# Also include the other headers
cp -a Include/* %buildroot%_includedir/lib3mf/

# Backward compatibility links (compatibility with 2.0.x)
ln -s Bindings/C/lib3mf.h \
      Bindings/Cpp/lib3mf_abi.hpp \
      Bindings/CDynamic/lib3mf_dynamic.h \
      Bindings/CppDynamic/lib3mf_dynamic.hpp \
      Bindings/Cpp/lib3mf_implicit.hpp \
      Bindings/NodeJS/lib3mf_nodewrapper.h \
      Bindings/C/lib3mf_types.h \
      Bindings/Cpp/lib3mf_types.hpp \
  %buildroot%_includedir/%name/
ln -s lib3mf.pc %buildroot%_libdir/pkgconfig/lib3MF.pc

%files
%doc README.md
%_libdir/lib3mf.so.2
%_libdir/lib3mf.so.%version.0

%files devel
%_libdir/lib3mf.so
%_libdir/cmake/lib3mf
%_includedir/lib3mf/
%_pkgconfigdir/lib3MF.pc
%_pkgconfigdir/lib3mf.pc

%changelog
* Sat Jul 04 2026 Anton Midyukov <antohami@altlinux.org> 2.5.0-alt1
- New version 2.5.0 (Closes: 59727).

* Thu Apr 23 2026 Anton Midyukov <antohami@altlinux.org> 2.2.0-alt6
- Fix build with gcc15.
- Fix debuginfo.

* Sat Mar 14 2026 Anton Midyukov <antohami@altlinux.org> 2.2.0-alt5
- Fix FTBFS.

* Fri Jul 11 2025 Anton Midyukov <antohami@altlinux.org> 2.2.0-alt4
- use system libzip

* Thu Apr 17 2025 Anton Midyukov <antohami@altlinux.org> 2.2.0-alt3
- disable tests for build with cmake >= 4.0
- spec: add Vcs tag

* Sat Jan 28 2023 Anton Midyukov <antohami@altlinux.org> 2.2.0-alt2
- Don't force C++11 to fix FTBFS with gtest 1.13+

* Sat May 21 2022 Anton Midyukov <antohami@altlinux.org> 2.2.0-alt1
- new version (2.2.0) with rpmgs script
- enable check
- ubundled libraries: libzip, zlib, libssl
- compatibility with 2.0.x

* Thu May 13 2021 Anton Midyukov <antohami@altlinux.org> 2.0.1-alt1
- Initial build
