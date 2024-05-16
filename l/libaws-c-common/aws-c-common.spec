%define        _unpackaged_files_terminate_build 1
%define        oname aws-c-common

Name:          lib%oname
Version:       0.9.12
Release:       alt2
Group:         Development/C
Summary:       Core c99 package for AWS SDK for C
License:       Apache-2.0
Url:           https://github.com/awslabs/aws-c-common
Vcs:           https://github.com/awslabs/aws-c-common.git

Source:        %name-%version.tar
Patch:         path.patch
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-ninja-build
BuildRequires: cmake
BuildRequires: ctest
BuildRequires: clang-tools
BuildRequires: ninja-build

%description
Core c99 package for AWS SDK for C. Includes cross-platform primitives,
configuration, data structures, and error handling.


%package       devel
Group:         Development/C
Summary:       Core c99 package for AWS SDK for C development files
Requires:      %name = %EVR
Requires:      cmake
Requires:      ctest
Requires:      clang-tools
Requires:      ninja-build

%description   devel
Development headers and libraries for %oname.

Core c99 package for AWS SDK for C. Includes cross-platform primitives,
configuration, data structures, and error handling.


%prep
%setup
%autopatch
%ifarch %e2k
sed -i 's/has_avx2(void);/has_avx2(void){return 1;}/' source/encoding.c
%endif

%build
%cmake \
   -GNinja \
   -DBUILD_SHARED_LIBS=ON

cd %_cmake__builddir
%ninja_build

%install
cd %_cmake__builddir
%ninja_install

%check
cd %_cmake__builddir
# %ninja_test

%files
%doc README*
%_libdir/%name.so.*

%files         devel
%doc README*
%_libdir/%name.so
%_libdir/cmake/*
%_includedir/aws/common
%_includedir/aws/testing


%changelog
* Thu May 16 2024 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 0.9.12-alt2
- Fixed build for Elbrus

* Tue Jan 02 2024 Pavel Skrylev <majioa@altlinux.org> 0.9.12-alt1
- Initial build for Sisyphus
