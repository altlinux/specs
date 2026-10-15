%def_disable   check
%def_enable    devel
%{?!_disable_devel:%define _unpackaged_files_terminate_build 1}
%define        nomen aws-c-sdkutils

Name:          lib%nomen
Version:       1.0.0
Release:       alt1
Group:         Development/C
Summary:       C99 library implementing AWS SDK specific utilities
License:       Apache-2.0
Url:           https://github.com/aws/aws-sdk-cpp
Vcs:           https://github.com/aws/aws-sdk-cpp.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-cmake
%{?!_disable_check:BuildRequires: ctest}
BuildRequires: /proc
BuildRequires: cmake
BuildRequires: clang-tools
BuildRequires: pkgconfig(libssl)
BuildRequires: cmake(aws-c-common)

%description
C99 library implementing AWS SDK specific utilities. Includes utilities for ARN
parsing, reading AWS profiles, etc...


%if_enabled    devel
%package       devel
Group:         Development/Other
Summary:       Development headers and libraries for %nomen
Requires:      ctest
Requires:      cmake
Requires:      clang-tools
Requires:      pkgconfig(libssl)
Requires:      cmake(aws-c-common)

%description   devel
Development headers and libraries for %nomen.

C99 library implementing AWS SDK specific utilities. Includes utilities for ARN
parsing, reading AWS profiles, etc...
%endif


%prep
%setup

%build
%cmake \
   -DCMAKE_MODULE_PATH=%_libdir/cmake \
   -DCMAKE_PREFIX_PATH=%_usr \
   -DCMAKE_C_COMPILER=clang \
   -DBUILD_SHARED_LIBS=ON \
   %nil
%cmake_build

%install
%cmakeinstall_std

%check
%ctest

%files
%doc README*
%_libdir/%name.so.*

%if_enabled    devel
%files         devel
%_libdir/%name.so
%_libdir/cmake/%nomen
%_includedir/aws/sdkutils
%endif


%changelog
* Tue Oct 06 2026 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- ^ 0.1.13 -> 1.0.0

* Tue Jan 02 2024 Pavel Skrylev <majioa@altlinux.org> 0.1.13-alt1
- Initial build for Sisyphus
