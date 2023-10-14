%define _unpackaged_files_terminate_build 1

%def_with check

Name: rapidfuzz-devel
Version: 2.1.1
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

%files
%doc LICENSE README.md CHANGELOG.md
%_includedir/rapidfuzz
%_libdir/cmake/rapidfuzz

%changelog
* Fri Oct 13 2023 Anton Zhukharev <ancieg@altlinux.org> 2.1.1-alt1
- Built for ALT Sisyphus.

