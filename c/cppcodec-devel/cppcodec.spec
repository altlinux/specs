%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%if %{expand:%%{?!_without_test:%%{?!_disable_test:%%{?!_without_check:%%{?!_disable_check:1}}}}0}
%define tests yes
%else
%define tests no
%endif

Name: cppcodec-devel
Version: 0.2
Release: alt2
Buildarch: noarch

Summary: C++11 library codec for base64, base64url, base32, base32hex and hex

Group: System/Libraries
License: MIT
Url: https://github.com/tplgy/cppcodec
Vcs: https://github.com/tplgy/cppcodec.git

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake
%if "%tests" == "yes"
BuildRequires: catch2-devel ctest
%endif

%global desc \
Header-only C++11 library to encode/decode base64, base64url, base32, base32hex\
and hex (a.k.a. base16) as specified in RFC 4648, plus Crockford's base32.\
\
MIT licensed with consistent, flexible API. Supports raw pointers,\
`std::string` and (templated) character vectors without unnecessary allocations.\
Cross-platform with measured decent performance and without compiler warnings.

%description
%desc

%package examples
Group: System/Libraries
Summary: The cppcodec examples

%description examples
%desc

This package contains cppcodec usage examples.

%prep
%setup
%patch -p1
# upstream forgot to bump the library version
sed 's/PROJECT_VERSION 0.1/PROJECT_VERSION 0.2/' -i CMakeLists.txt

%build
%cmake -DBUILD_TESTING=%tests

%cmake_build

%check
%ctest

%install
%cmakeinstall_std

%files
%_includedir/cppcodec
%_datadir/pkgconfig/*.pc
%doc *.md

%files examples
%doc example/*.cpp

%changelog
* Fri Nov 22 2024 Andrew Savchenko <bircoph@altlinux.org> 0.2-alt2
- Fix url/cvs.

* Sun Nov 10 2024 Andrew Savchenko <bircoph@altlinux.org> 0.2-alt1
- Initial version.
