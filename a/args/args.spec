Name: args
Version: 6.4.15
Release: alt1

Summary: A simple header-only C++ argument parser library
License: MIT
Group: Development/C++

Url: https://github.com/Taywee/args
VCS: https://github.com/Taywee/args

Source:  %name-%version.tar

BuildRequires: gcc-c++ cmake ctest

%package -n lib%name-devel
Summary: Development ARGS files
Group: Development/C++
%description -n lib%name-devel
Development ARGS files.

%description
A simple header-only C++ argument parser library. Supposed to be
flexible and powerful, and attempts to be compatible with the
functionality of the Python standard argparse library (though not
necessarily the API). 

%prep
%setup
subst 's|DESTINATION lib/|DESTINATION %_libdir/|' CMakeLists.txt

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files -n lib%name-devel
%doc *.md CHANGELOG LICENSE
%_includedir/%name.hxx
%_libdir/cmake/%name
%_datadir/pkgconfig/%name.pc
%_datadir/cmake/%name

%changelog
* Wed Apr 29 2026 Aleksandr Shamaraev <shad@altlinux.org> 6.4.15-alt1
- 6.4.13 -> 6.4.15

* Tue Apr 28 2026 Aleksandr Shamaraev <shad@altlinux.org> 6.4.13-alt1
- 6.4.12 -> 6.4.13

* Sat Apr 25 2026 Aleksandr Shamaraev <shad@altlinux.org> 6.4.12-alt1
- 6.4.11 -> 6.4.12

* Fri Apr 24 2026 Aleksandr Shamaraev <shad@altlinux.org> 6.4.11-alt1
- 6.4.10 -> 6.4.11

* Wed Apr 22 2026 Aleksandr Shamaraev <shad@altlinux.org> 6.4.10-alt1
- 6.4.9 -> 6.4.10

* Tue Apr 21 2026 Aleksandr Shamaraev <shad@altlinux.org> 6.4.9-alt1
- 6.4.8 -> 6.4.9

* Thu Feb 12 2026 Aleksandr Shamaraev <shad@altlinux.org> 6.4.8-alt1
- 6.4.7 -> 6.4.8

* Sat Feb 07 2026 Aleksandr Shamaraev <shad@altlinux.org> 6.4.7-alt1
- Initial build for ALT Linux.

