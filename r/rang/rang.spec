%define _unpackaged_files_terminate_build 1

Name: rang
Version: 3.2
Release: alt1

License: Unlicense
Summary: Provides colors for your Terminal
BuildArch: noarch
Group: Development/C++
Url: https://github.com/agauniyal/rang

Source: %name-%version.tar

BuildRequires(pre): cmake gcc-c++
BuildRequires(pre): meson cppcheck
BuildRequires(pre): doctest-devel

%description
Rang uses iostream objects - cout/clog/cerr to apply attributes
to output text. rang is a single header-only library. Put rang.hpp
in the include folder directly into the project source tree or
somewhere reachable from your project.

%package devel
Summary: Development files for rang
Group: Development/C++
%description devel
This package contains development files for rang.

%prep
%setup

sed -i 's|doctest.h|doctest/doctest.h|' test/test.cpp

%build
%meson
%meson_build

%install
mkdir -p %buildroot%_includedir

install -D -m644 %_builddir/%name-%version/include/rang.hpp %buildroot/%_includedir/rang.hpp

%check
%meson_test

%files devel
%doc README.md
%doc LICENSE
%_includedir/*


%changelog
* Thu Jun 01 2023 Elizaveta Morozova <morozovaes@altlinux.org> 3.2-alt1
- Initial build for ALT
