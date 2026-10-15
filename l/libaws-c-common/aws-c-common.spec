%def_disable   check
%def_enable    devel
%{?!_disable_check:%define _unpackaged_files_terminate_build 1}
%define        nomen aws-c-common

Name:          lib%nomen
Version:       1.0.3
Release:       alt1
Group:         Development/C
Summary:       Core c99 package for AWS SDK for C
License:       Apache-2.0
Url:           https://github.com/awslabs/aws-c-common
Vcs:           https://github.com/awslabs/aws-c-common.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-cmake
%{?!_disable_check:BuildRequires: ctest}
BuildRequires: cmake
BuildRequires: clang-tools

%description
Core c99 package for AWS SDK for C. Includes cross-platform primitives,
configuration, data structures, and error handling.


%if_enabled    devel
%package       devel
Group:         Development/C
Summary:       Core c99 package for AWS SDK for C development files
Requires:      cmake
Requires:      ctest
Requires:      clang-tools

%description   devel
Development headers and libraries for %nomen.

Core c99 package for AWS SDK for C. Includes cross-platform primitives,
configuration, data structures, and error handling.
%endif


%prep
%setup
%autopatch
%ifarch %e2k
sed -i 's/has_avx2(void);/has_avx2(void){return 1;}/' source/encoding.c
%endif

%build
%cmake \
   -DCMAKE_C_COMPILER=clang \
   -DBUILD_SHARED_LIBS=ON \
   %nil
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%doc README*
%_libdir/%name.so.*

%if_enabled    devel
%files         devel
%doc README*
%_libdir/%name.so
%_libdir/cmake/%nomen
%_includedir/aws/common
%_includedir/aws/testing
%endif


%changelog
* Tue Oct 15 2026 Pavel Skrylev <majioa@altlinux.org> 1.0.3-alt1
- ^ 0.9.12 -> 1.0.3

* Thu May 16 2024 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 0.9.12-alt2
- Fixed build for Elbrus

* Tue Jan 02 2024 Pavel Skrylev <majioa@altlinux.org> 0.9.12-alt1
- Initial build for Sisyphus
