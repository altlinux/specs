Name:    valijson
Version: 1.0.4
Release: alt1

Summary: Valijson is a header-only JSON Schema validation library for C++11
License: BSD-2-Clause
Group:   System/Libraries
Url:     https://github.com/tristanpenman/valijson

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++

%description
%summary

%package devel
Summary: Valijson is a header-only JSON Schema validation library for C++11
Group: Development/C++

%description devel
%summary

%prep
%setup

%build
%cmake -GNinja -Wno-dev
%ninja_build -C "%_cmake__builddir"

%install
%ninja_install -C "%_cmake__builddir"

%files devel
%doc Authors README.md LICENSE
%_includedir/%name
%_includedir/compat/optional.hpp
%_libdir/cmake/%name

%changelog
* Sun Feb 16 2025 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt1
- New version.

* Thu Feb 06 2025 Andrey Cherepanov <cas@altlinux.org> 1.0.3-alt1
- Initial build for Sisyphus.
