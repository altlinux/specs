%define _unpackaged_files_terminate_build 1

%def_with check

Name: rapidfuzz-cpp
Version: 2.2.3
Release: alt1

Summary: Rapid fuzzy string matching in C++ using the Levenshtein Distance
License: MIT
Group: Development/C++
Url: https://github.com/maxbachmann/rapidfuzz-cpp
Vcs: https://github.com/maxbachmann/rapidfuzz-cpp

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++

%if_with check
BuildRequires: ctest
BuildRequires: catch-devel
%endif

%description
%summary.

%package devel
Summary: Rapid fuzzy string matching in C++ using the Levenshtein Distance
Group: Development/C++

%description devel
%summary.

%prep
%setup

%build
%cmake \
  -DRAPIDFUZZ_INSTALL:BOOL=ON \
%if_with check
  -DRAPIDFUZZ_BUILD_TESTING:BOOL=ON \
%endif
  %nil
%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%doc LICENSE README.md CHANGELOG.md
%_includedir/rapidfuzz
%_libdir/cmake/rapidfuzz

%changelog
* Mon Nov 20 2023 Anton Zhukharev <ancieg@altlinux.org> 2.2.3-alt1
- Updated to 2.2.3.

* Mon Nov 20 2023 Anton Zhukharev <ancieg@altlinux.org> 2.1.1-alt2
- Renamed to rapidfuzz-cpp to match the project name.

* Fri Oct 13 2023 Anton Zhukharev <ancieg@altlinux.org> 2.1.1-alt1
- Built for ALT Sisyphus.

