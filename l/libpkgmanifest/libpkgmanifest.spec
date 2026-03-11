Name: libpkgmanifest
Version: 0.5.9
Release: alt1

Summary: Library for working with RPM package manifests

License: LGPL-2.1-or-later
Group: System/Libraries
URL: https://github.com/rpm-software-management/libpkgmanifest
# Source-url: https://github.com/rpm-software-management/libpkgmanifest/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake rpm-build-python3
BuildRequires: cmake >= 3.13 gcc-c++ ctest
BuildRequires: libyaml-cpp-devel >= 0.7.0
BuildRequires: swig >= 4.2.0
BuildRequires: python3-devel
BuildRequires: libgtest-devel libgmock-devel

%description
libpkgmanifest is a C++ library for parsing and generating RPM package
manifests. It is used as a dependency of DNF5 and similar tools for
streamlining container image building workflows.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %EVR

%description devel
Development files for %name.

%package -n python3-module-%name
Summary: Python 3 bindings for %name
Group: Development/Python3
Requires: %name = %EVR

%description -n python3-module-%name
Python 3 bindings for the libpkgmanifest library.

%prep
%setup

%build
%cmake \
    -DWITH_DOCS=OFF \
    -DWITH_PYTHON=ON \
    -DWITH_TESTS=ON \
    -DWITH_CODE_COVERAGE=OFF \
    -DVERSION_MAJOR=0 \
    -DVERSION_MINOR=5 \
    -DVERSION_PATCH=9
%cmake_build

%check
%cmake_build -t test

%install
%cmake_install

%files
%_libdir/%name.so.0
%doc README.md
%doc LICENSE

%files devel
%_includedir/%name/
%_libdir/%name.so
%_libdir/pkgconfig/%name.pc

%files -n python3-module-%name
%python3_sitelibdir/%name/
%python3_sitelibdir/%name-*.dist-info/

%changelog
* Wed Mar 11 2026 Vitaly Lipatov <lav@altlinux.ru> 0.5.9-alt1
- initial build for ALT Sisyphus

