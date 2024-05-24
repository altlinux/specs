%def_disable snapshot
%define _name hyprlang

%def_enable check

Name: %_name
Version: 0.5.2
Release: alt1

Summary: Hyprland configuration library
License: GPL-3.0
Group: System/Libraries
Url: https://github.com/hyprwm/hyprlang

Vcs: https://github.com/hyprwm/hyprlang.git

%if_disabled snapshot
Source: %url/archive/v%version/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake
%{?_enable_check:BuildRequires: ctest}

%description
The hypr configuration language is an extremely efficient, yet easy to
work with, configuration language for linux applications.

It's user-friendly, easy to grasp, and easy to implement.

%package -n lib%name
Summary: Hyprlang shared library
Group: System/Libraries

%description -n lib%name
This packaage provides Hyprlang shared library.

%package -n lib%name-devel
Summary: Development files for Hyprlang
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
Development files for the Hyprlang library.

%prep
%setup -n %_name-%version

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%cmake_build -t test

%files -n lib%name
%_libdir/lib%_name.so.*

%files -n lib%name-devel
%_includedir/%_name.hpp
%_libdir/lib%_name.so
#%_libdir/cmake/%_name/
%_pkgconfigdir/%_name.pc

%changelog
* Fri May 24 2024 Yuri N. Sedunov <aris@altlinux.org> 0.5.2-alt1
- 0.5.2

* Mon Apr 15 2024 Yuri N. Sedunov <aris@altlinux.org> 0.5.1-alt1
- 0.5.1

* Sat Mar 09 2024 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- 0.5.0

* Thu Feb 29 2024 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- 0.4.1

* Sat Feb 17 2024 Yuri N. Sedunov <aris@altlinux.org> 0.3.2-alt1
- 0.3.2

* Tue Feb 13 2024 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt1
- 0.3.1

* Sun Jan 07 2024 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt1
- first build for Sisyphus (v0.2.1-5-gf1aaf52)



