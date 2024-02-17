# This is a header only library
%global debug_package %nil

Name: plog-devel
Version: 1.1.10
Release: alt2
Summary: Portable, simple and extensible C++ logging library
Group: Development/Other
License: MIT
Url: https://github.com/SergiusTheBest/plog
# Source-url: %url/archive/%version/plog-%version.tar.gz
Source: plog-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++

%description
Plog is a C++ logging library that is designed to be as simple,
small and flexible as possible. It is created as an alternative
to existing large libraries and provides some unique features
as CSV log format and wide string support.

%prep
%setup -n plog-%version
%ifarch %e2k
sed -i 's/-Werror/-Wno-error/' samples/CMakeLists.txt
%endif

%build
%cmake -DPLOG_BUILD_TESTS=ON
%cmake_build

%install
%cmake_install

# Delete wrongly installed doc content, we'll docify later
rm -rv %buildroot%_docdir/plog

%files
%doc LICENSE README.md doc
%_includedir/plog/
%_libdir/cmake/plog/

%changelog
* Sat Feb 17 2024 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.1.10-alt2
- Fixed build for Elbrus

* Mon Nov 13 2023 Anton Midyukov <antohami@altlinux.org> 1.1.10-alt1
- initial build
