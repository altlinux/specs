%define _unpackaged_files_terminate_build 1

Name: any
Version: 0
Release: alt1.gite88b1bfc

Summary: Implementation of std::experimental::any
License: BSL-1.0
Group: Development/C++
Url: https://github.com/thelink2012/any.git

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake cmake
BuildRequires: gcc-c++

%description
Implementation of std::experimental::any, including small
object optimization, for C++11 compilers

%prep
%setup
%patch -p1

%build
%cmake

%cmake_build

%install
mkdir -p %buildroot%_includedir/any
install -m0644 ./any.hpp %buildroot%_includedir/any/
%cmake_install

%files
%_includedir/*
%_libdir/cmake/%name

%changelog
* Wed Sep 13 2023 Aleksei Kalinin <kaa@altlinux.org> 0-alt1.gite88b1bfc
- Added cmake instructions for detecting headers.
- Initial build for Alt.
