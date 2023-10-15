%define _unpackaged_files_terminate_build 1

Name: libcoeurl
Version: 0.1.1
Release: alt2.1

Summary: A simple async wrapper around CURL for C++

Group: Development/Other
License: MIT
Url: https://nheko.im/nheko-reborn/coeurl.git

Source: %name-%version.tar
Patch0: %name-%version-add-pkgconfig.patch
Patch1: coeurl-fmt10-fix.patch

BuildRequires: cmake gcc-c++ libspdlog-devel
BuildRequires: libevent-devel libcurl-devel

%description
Simple library to do http requests asynchronously via CURL in C++.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
Simple library to do http requests asynchronously via CURL in C++.

This package contains C++ header files for developing and the static
library.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
# Undefined references from_json/to_json:
%define optflags_lto %nil

%cmake -DUSE_BUNDLED_SPDLOG=OFF   \
       -DUSE_BUNDLED_LIBEVENT=OFF \
       -DUSE_BUNDLED_LIBCURL=OFF  \
       -DBUILD_SHARED_LIBS=ON     \
       -DCMAKE_BUILD_TYPE=Release

%cmake_build

%install
%cmakeinstall_std

# Testing needs a local Synapse server instance
#%check
#%make_build test

%files
%doc README.md
%doc LICENSE
%_libdir/*.so

%files devel
%doc examples
%_includedir/coeurl
%_libdir/cmake/coeurl/*.cmake
%_libdir/pkgconfig/coeurl.pc

%changelog
* Sat Oct 14 2023 Nazarov Denis <nenderus@altlinux.org> 0.1.1-alt2.1
- NMU: Fix build with fmt 10

* Mon Jan 10 2022 Paul Wolneykien <manowar@altlinux.org> 0.1.1-alt2
- Add missing pkgconfig (patch).

* Mon Jan 10 2022 Paul Wolneykien <manowar@altlinux.org> 0.1.1-alt1
- Initial version for Sisyphus.
