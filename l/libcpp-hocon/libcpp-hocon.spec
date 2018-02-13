Name:    libcpp-hocon
Version: 0.1.6
Release: alt1.2
Summary: A C++ port of the Typesafe Config library
 
Group:   System/Libraries
License: Apache 2.0
Url:     https://github.com/puppetlabs/cpp-hocon
Packager: Andrey Cherepanov <cas@altlinux.org>
 
Source: cpp-hocon-%version.tar
Patch1: libcpp-hocon-shared-library.patch
 
BuildRequires(pre): cmake
BuildRequires: gcc-c++
BuildRequires: boost-devel
BuildRequires: boost-filesystem-devel
BuildRequires: boost-log-devel
BuildRequires: boost-program_options-devel
BuildRequires: libleatherman-devel

%description
This is a port of the TypesafeConfig library to C++.

The library provides C++ support for the HOCON configuration file
format.

%package devel
Summary: cpp-hocon development libraries
Group: Development/Other
Provides: cpp-hocon-devel = %version-%release
Obsoletes: cpp-hocon-devel < %version-%release

%description devel
Development libraries for cpp-hocon.

%prep
%setup -n cpp-hocon-%version
%patch1 -p1

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%doc *.md
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/hocon

%changelog
* Tue Feb 13 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.6-alt1.2
- Rebuild with libleatherman 1.4.0.

* Mon Nov 06 2017 Andrey Cherepanov <cas@altlinux.org> 0.1.6-alt1.1
- Rebuild with leatherman 1.3.0

* Sat Sep 16 2017 Andrey Cherepanov <cas@altlinux.org> 0.1.6-alt1
- New version

* Sat Feb 18 2017 Andrey Cherepanov <cas@altlinux.org> 0.1.5-alt1
- new version 0.1.5

* Tue Jan 17 2017 Andrey Cherepanov <cas@altlinux.org> 0.1.4-alt1
- Initial build in Sisyphus

