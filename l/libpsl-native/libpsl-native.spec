
%define targetdir %_libdir/powershell/runtimes/%_dotnet_rid/native

Name: libpsl-native
Version: 7.2.0
Release: alt1

Summary: PowerShell Native library

License: MIT
Group: Other
Url: https://github.com/PowerShell/PowerShell-Native

Packager: Vitaly Lipatov <lav@altlinux.ru>

ExclusiveArch: %_dotnet_archlist

# Source-url: https://github.com/PowerShell/PowerShell-Native/archive/v%version.tar.gz
Source: %name-%version.tar

Patch: libpsl-native-gtest.patch

BuildRequires(pre): rpm-macros-cmake rpm-macros-dotnet
BuildRequires: cmake gcc-c++
BuildRequires: libgtest-devel ctest

%add_optflags %optflags_shared

%description
This library provides functionality missing from .NET Core via system calls,
that are called from from the CorePsPlatform.cs file of PowerShell.
The method to do this is a Platform Invoke,
which is C#'s Foreign Function Interface to C code (and C++ by way of extern C).

%prep
%setup
%patch -p2
# use only optflags from rpm
subst 's|.*CMAKE_CXX_FLAGS.*||' src/libpsl-native/CMakeLists.txt

%build
pushd src/libpsl-native/
%cmake_insource -DCMAKE_BUILD_TYPE=Debug -D CMAKE_CXX_FLAGS="%optflags %optflags_shared"
%make_build VERBOSE=1

%install
mkdir -p %buildroot%targetdir/
cp src/powershell-unix/libpsl-native.so %buildroot%targetdir/

%check
pushd src/libpsl-native/
LANG=en_US.utf8 LD_LIBRARY_PATH=$(pwd)/../powershell-unix/ ctest --verbose || true
# TODO:
# failed in hasher:
#   GetFileOwner("/")
#     Which is: "caller"
#   "root"
#
#   GetUserFromPid(getpid())
#     Which is: NULL
#   expected
#     Which is: "builder"


%files
%targetdir/libpsl-native.so

%changelog
* Sun Feb 13 2022 Vitaly Lipatov <lav@altlinux.ru> 7.2.0-alt1
- new version 7.2.0 (with rpmrb script)
- fix build with GTest

* Sun Feb 13 2022 Vitaly Lipatov <lav@altlinux.ru> 7.1.0-alt2
- more compatibility with old GTest

* Wed Sep 01 2021 Vitaly Lipatov <lav@altlinux.ru> 7.1.0-alt2
- use optflags+optflags_shared instead of embedded cflags

* Mon Feb 22 2021 Vitaly Lipatov <lav@altlinux.ru> 7.1.0-alt1
- initial build for ALT Sisyphus
