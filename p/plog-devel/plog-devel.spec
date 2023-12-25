# This is a header only library
%global debug_package %nil

Name: plog-devel
Version: 1.1.10
Release: alt1
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
* Mon Nov 13 2023 Anton Midyukov <antohami@altlinux.org> 1.1.10-alt1
- initial build
