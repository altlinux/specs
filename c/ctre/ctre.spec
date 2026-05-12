# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1
%def_with check

Name: ctre
Version: 3.11.0
Release: alt1
Summary: Compile Time Regular Expression in C++
License: Apache-2.0
Group: Development/C++
URL: https://compile-time.re
VCS: https://github.com/hanickadot/compile-time-regular-expressions

# Source-url: %vcs/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

Patch: ctre-3.11.0-noarch.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake %_bindir/python3
BuildRequires: python3-module-sphinx python3-module-sphinx_rtd_theme
# Tests
%if_with check
BuildRequires: gcc-c++
%endif

%description
Fast compile-time regular expressions with support
for matching/searching/capturing during compile-time or runtime.

%package devel
Group: Development/C++
Summary: Compile Time Regular Expression in C++
BuildArch: noarch
Provides: %name = %EVR

%description devel
Fast compile-time regular expressions with support
for matching/searching/capturing during compile-time or runtime.

%package doc
Group: Documentation
Summary: Documentation files for %name
BuildArch: noarch

%description doc
Documentation files for %name.

%prep
%setup
%autopatch -p1

%build
%cmake \
    -DCTRE_BUILD_PACKAGE_DEB:BOOL=FALSE \
    -DCTRE_BUILD_PACKAGE_RPM:BOOL=FALSE
sphinx-build docs doc

%install
%cmake_install

%check
%if_with check
%make_build
%endif

%files devel
%doc README.md LICENSE NOTES.md
%_includedir/ctre.hpp
%_includedir/ctre/
%_includedir/ctll.hpp
%_includedir/ctll/
%_includedir/unicode-db.hpp
%_includedir/unicode-db/
%_includedir/ctre-unicode.hpp
%_datadir/cmake/ctre
%_datadir/pkgconfig/ctre.pc

%files doc
%doc doc/*

%changelog
* Tue May 12 2026 Valery Zabrovsky <brow@altlinux.org> 3.11.0-alt1
- New version 3.11.0.
- Minor spec cleanup.

* Wed Apr 22 2026 Valery Zabrovsky <brow@altlinux.org> 3.10.0-alt2
- Fix noarch-ness issue when other modules try to find ctre.

* Mon Apr 20 2026 Valery Zabrovsky <brow@altlinux.org> 3.10.0-alt1
- Initial build for ALT Sisyphus.
