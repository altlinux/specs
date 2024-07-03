%define _unpackaged_files_terminate_build 1

%def_with check

Name: rapidfuzz-cpp
Version: 3.0.5
Release: alt1

Summary: Rapid fuzzy string matching in C++ using the Levenshtein Distance
License: MIT
Group: Development/C++
Url: https://github.com/rapidfuzz/rapidfuzz-cpp
Vcs: https://github.com/rapidfuzz/rapidfuzz-cpp

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

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
%autopatch -p1

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
%_cmakedir/rapidfuzz

%changelog
* Wed Jul 03 2024 Anton Zhukharev <ancieg@altlinux.org> 3.0.5-alt1
- Updated to 3.0.5.

* Mon Apr 08 2024 Anton Zhukharev <ancieg@altlinux.org> 3.0.4-alt1
- Updated to 3.0.4.

* Mon Mar 25 2024 Anton Zhukharev <ancieg@altlinux.org> 3.0.2-alt1
- Updated to 3.0.2.

* Wed Dec 27 2023 Anton Zhukharev <ancieg@altlinux.org> 3.0.0-alt1
- Updated to 3.0.0.

* Mon Nov 20 2023 Anton Zhukharev <ancieg@altlinux.org> 2.2.3-alt1
- Updated to 2.2.3.

* Mon Nov 20 2023 Anton Zhukharev <ancieg@altlinux.org> 2.1.1-alt2
- Renamed to rapidfuzz-cpp to match the project name.

* Fri Oct 13 2023 Anton Zhukharev <ancieg@altlinux.org> 2.1.1-alt1
- Built for ALT Sisyphus.

