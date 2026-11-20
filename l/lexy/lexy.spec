%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%define _unpackaged_files_terminate_build 1

%def_with check

Name: lexy
Version: 2025.05.0
Release: alt1

Summary: C++ parsing DSL
License: BSL-1.0
Group: Development/C++
URL: https://lexy.foonathan.net
VCS: https://github.com/foonathan/lexy

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++
BuildRequires: cmake
%if_with check
BuildRequires: ctest
BuildRequires: doctest-devel
%endif

%description
lexy is a parser combinator library for C++17 and onwards. It allows you
to write a parser by specifying it in a convenient C++ DSL,
which gives you all the flexibility and control of a handwritten parser
without any of the manual work.

%package devel
Summary: C++ parsing DSL
Group: Development/C++
Provides: %name = %EVR

%description devel
lexy is a parser combinator library for C++17 and onwards. It allows you
to write a parser by specifying it in a convenient C++ DSL,
which gives you all the flexibility and control of a handwritten parser
without any of the manual work.

%prep
%setup
%autopatch -p1

%build
%cmake \
    -DLEXY_BUILD_TESTS=%{?_with_check:ON}%{!?_with_check:OFF} \
    -DLEXY_BUILD_EXAMPLES=OFF \
    -DLEXY_BUILD_PACKAGE=OFF \
    -DLEXY_BUILD_DOCS=OFF
%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%doc LICENSE README.adoc CHANGELOG.adoc
%_includedir/%name
%_includedir/%{name}_ext
%_libdir/lib%{name}_file.a
%_cmakedir/%name

%changelog
* Mon Nov 02 2026 Valery Zabrovsky <brow@altlinux.org> 2025.05.0-alt1
- Initial build for ALT Sisyphus.
