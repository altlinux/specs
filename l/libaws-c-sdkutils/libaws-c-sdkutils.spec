%define        _unpackaged_files_terminate_build 1
%define        oname aws-c-sdkutils

Name:          lib%oname
Version:       0.1.13
Release:       alt1
Group:         Development/C
Summary:       C99 library implementing AWS SDK specific utilities
License:       Apache-2.0
Url:           https://github.com/aws/aws-sdk-cpp
Vcs:           https://github.com/aws/aws-sdk-cpp.git

Source:        %name-%version.tar
Patch:         path.patch
BuildRequires(pre): rpm-macros-cmake
BuildRequires: /proc
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libssl-devel
BuildRequires: libaws-c-common-devel

%description
C99 library implementing AWS SDK specific utilities. Includes utilities for ARN
parsing, reading AWS profiles, etc...


%package       devel
Group:         Development/Other
Summary:       Development headers and libraries for %oname
Requires:      %name = %EVR
Requires:      cmake
Requires:      gcc-c++
Requires:      libssl-devel
Requires:      libaws-c-common-devel


%description   devel
Development headers and libraries for %oname.

C99 library implementing AWS SDK specific utilities. Includes utilities for ARN
parsing, reading AWS profiles, etc...


%prep
%setup
%autopatch

%build
%cmake_insource \
   -DCMAKE_MODULE_PATH=%_libdir/cmake \
   -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmakeinstall_std

%check
make test

%files
%doc README*
%_libdir/%name.so.*

%files         devel
%_libdir/%name.so
%_libdir/cmake/%oname
%_includedir/aws/sdkutils


%changelog
* Tue Jan 02 2024 Pavel Skrylev <majioa@altlinux.org> 0.1.13-alt1
- Initial build for Sisyphus
