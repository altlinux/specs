%def_enable snapshot
%define _name cxxopts

%def_disable unicode_help
%def_enable check

Name: %_name
Version: 3.2.1
Release: alt2

Summary: Lightweight C++ option parser library
License: MIT
Group: System/Libraries
Url: https://github.com/jarro2783/cxxopts

%if_disabled snapshot
Source: %url/archive/v%version/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif

%{?_disable_unicode_help:BuildArch: noarch}

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake
%{?_enable_unicode_help:BuildRequires: pkgconfig(icu-cu)}
%{?_enable_check:BuildRequires: ctest}

%description
This is a lightweight C++ option parser library, supporting the standard
GNU style syntax for options.

%package devel
Summary: Development files for %name
Group: Development/C++

%description devel
Development files for %name.

%prep
%setup -n %_name-%version

%ifarch %e2k
sed -i 's/-Werror/-Wno-error/' cmake/cxxopts.cmake
%endif

%build
%cmake -DCMAKE_BUILD_TYPE=Release \
    %{?_enable_unicode_help:-DCXXOPTS_USE_UNICODE_HELP=ON}
%nil
%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%_includedir/%_name.hpp
%if_enabled unicode_help
%_libdir/cmake/%_name/
%_pkgconfigdir/%_name.pc
%else
%_datadir/cmake/%_name/
%_datadir/pkgconfig/%_name.pc
%endif

%changelog
* Mon Apr 28 2025 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt2
- updated to v3.2.1-12-gdbf4c6a (fixed for CMake-4/gcc-15)
- made unicode support optional (disabled by default)

* Tue Nov 19 2024 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1.1
- fixed build for E2K (ilyakurdyukov@)

* Tue Feb 20 2024 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Thu Feb 15 2024 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Sun Nov 26 2023 Yuri N. Sedunov <aris@altlinux.org> 3.1.1-alt1
- first build for Sisyphus



