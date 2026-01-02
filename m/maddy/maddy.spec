%define _unpackaged_files_terminate_build 1

Name: maddy
Version: 1.6.0
Release: alt1

Summary: C++ Markdown to HTML header-only parser library
License: MIT
Group: Development/C++

URL: https://github.com/progsource/maddy
VCS: https://github.com/progsource/maddy

Source: %name-%version.tar

BuildRequires: rpm-build-cmake
BuildRequires: gcc-c++

%description
%summary.

%package -n lib%name-devel
Summary: Headers for %name
Group: Development/C++

%description -n lib%name-devel
%summary.

%package doc
Summary: Documentation for %name
Group: Development/Documentation

%description doc
%summary.

%prep
%setup
%define _cmake__builddir build

%build
%cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -Wno-dev
%cmake_build

%install
%cmake_install

%files -n lib%name-devel
%_includedir/%name
%_cmakedir/%name/maddy*.cmake

%files doc
%doc docs/*

%changelog
* Tue Dec 09 2025 David Sultaniiazov <x1z53@altlinux.org> 1.6.0-alt1
- Initial build.
