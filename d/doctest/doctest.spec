Name: doctest
Version: 2.4.11
Release: alt2

Summary: Feature-rich header-only C++ testing framework
License: MIT
Group: Development/C++

Url: https://github.com/doctest/doctest
Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: cmake ctest

%description
A fast (both in compile times and runtime) C++ testing framework, with the
ability to write tests directly along production source (or in their own
source, if you prefer).

%package devel
Group: Development/C++
Summary: Development files for %name
Requires: libstdc++-devel

%description devel
%summary.

%prep
%setup
%ifarch %e2k
# unsupported as of lcc 1.26.20; see also mcst#8397
sed -i '/-Werror/d;/-Wcast-align=strict/d' scripts/cmake/common.cmake
%endif

%build
%cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DDOCTEST_WITH_MAIN_IN_STATIC_LIB:BOOL=OFF \
  -DDOCTEST_WITH_TESTS:BOOL=ON \
  %nil
%cmake_build

%check
ctest --test-dir %_cmake__builddir

%install
%cmake_install

%files devel
%doc README.md CHANGELOG.md CONTRIBUTING.md
%doc LICENSE.txt
%_includedir/%name/
%_libdir/cmake/%name/

%changelog
* Tue Oct 31 2023 Michael Shigorin <mike@altlinux.org> 2.4.11-alt2
- E2K: ftbfs workaround for lcc
- minor spec cleanup

* Sun May 14 2023 Anton Farygin <rider@altlinux.ru> 2.4.11-alt1
- 2.4.11

* Sat Feb 04 2023 Anton Farygin <rider@altlinux.ru> 2.4.9-alt1
- first build for ALT

