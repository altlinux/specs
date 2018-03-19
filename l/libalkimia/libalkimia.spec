%define lib_name libalkimia5

Name:    libalkimia
Version: 7.0.1
Release: alt1

Summary: Financial library
License: LGPLv2+
Group:	 System/Libraries
URL:     http://community.kde.org/Alkimia/libalkimia

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: qt5-base-devel
BuildRequires: libgmp_cxx-devel

%description
libalkimia is a library with common classes and functionality used by
finance applications for the KDE SC. Currently it supports a common
class to represent monetary values with arbitrary precision.

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
Requires: %name = %version-%release

%description devel
Headers and other files for develop with %name.

%prep
%setup -q

%build
%cmake -Wno-dev
%cmake_build

%install
%cmakeinstall_std

%files
%doc README.md
%_libdir/%lib_name.so.*

%files devel
%dir %_includedir/alkimia
%_includedir/alkimia/*
%_libdir/%lib_name.so
%_pkgconfigdir/%lib_name.pc
%_libdir/cmake/LibAlkimia*

%changelog
* Mon Mar 19 2018 Andrey Cherepanov <cas@altlinux.org> 7.0.1-alt1
- New version.

* Fri Feb 16 2018 Andrey Cherepanov <cas@altlinux.org> 7.0-alt1
- New version.

* Tue Feb 09 2016 Andrey Cherepanov <cas@altlinux.org> 5.0.0-alt1
- New version

* Thu Aug 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.2-alt1.1
- Rebuilt with gmp 5.0.5

* Thu Feb 09 2012 Andrey Cherepanov <cas@altlinux.org> 4.3.2-alt1
- New version 4.3.2

* Tue Sep 06 2011 Andrey Cherepanov <cas@altlinux.org> 4.3.1-alt1
- Initial build in Sisyphus

