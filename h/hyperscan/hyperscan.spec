%define major 5.4
%define libname libhyperscan%major
%define develname libhyperscan-devel

# objcopy: redefining symbols does not work on LTO-compiled object files
%define optflags_lto %nil

Name: hyperscan
Version: %major.2
Release: alt1

Summary: High-performance regular expression matching library

Group: System/Libraries
License: BSD
Url: https://www.hyperscan.io/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/01org/%name/archive/v%version.tar.gz
Source: %name-%version.tar


BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++
BuildRequires: cmake ctest
BuildRequires: boost-devel
BuildRequires: pkgconfig(libpcre)
BuildRequires: ragel
BuildRequires: pkgconfig(sqlite3) >= 3.0
BuildRequires: libpcap-devel
BuildRequires: %_bindir/doxygen %_bindir/sphinx-build

Requires: pcretest

#package requires SSE support and fails to build on non x86_64 archs
ExclusiveArch: x86_64

%description
Hyperscan is a high-performance multiple regex matching library. It
follows the regular expression syntax of the commonly-used libpcre
library, but is a standalone library with its own C API.

Hyperscan uses hybrid automata techniques to allow simultaneous
matching of large numbers (up to tens of thousands) of regular
expressions and for the matching of regular expressions across streams
of data.

Hyperscan is typically used in a DPI library stack.

%package -n %libname
Group: System/Libraries
Summary: Dynamic libraries for the hyperscan library

%description -n %libname
This package provides the dynamic libraries needed for developing Hyperscan
applications.

%package -n %develname
Group: Development/C
Summary: Libraries and header files for the hyperscan library
Requires: %libname = %version

%description -n %develname
This package provides the libraries, include files and other resources
needed for developing Hyperscan applications.

%prep
%setup

%build
%cmake -DBUILD_SHARED_LIBS:BOOL=ON \
       -DBUILD_STATIC_AND_SHARED:BOOL=OFF
%cmake_build

%install
%cmakeinstall_std

%files -n %libname
%doc %_docdir/%name
%doc COPYING
%doc LICENSE
%_libdir/*.so.5
%_libdir/*.so.%version

%files -n %develname
%_libdir/*.so
%_pkgconfigdir/libhs.pc
%_includedir/hs/

%changelog
* Tue Aug 01 2023 Vitaly Lipatov <lav@altlinux.ru> 5.4.2-alt1
- new version 5.4.2 (with rpmrb script)

* Wed Sep 08 2021 Vitaly Lipatov <lav@altlinux.ru> 5.4.0-alt2
- disable LTO for now

* Mon Mar 29 2021 Vitaly Lipatov <lav@altlinux.ru> 5.4.0-alt1
- new version 5.4.0 (with rpmrb script)

* Fri Jun 19 2020 Vitaly Lipatov <lav@altlinux.ru> 5.3.0-alt1
- new version 5.3.0 (with rpmrb script)

* Sun Jan 26 2020 Vitaly Lipatov <lav@altlinux.ru> 5.2.1-alt1
- new version 5.2.1 (with rpmrb script)

* Mon May 06 2019 Vitaly Lipatov <lav@altlinux.ru> 5.1.1-alt1
- new version 5.1.1 (with rpmrb script)

* Fri Feb 22 2019 Vitaly Lipatov <lav@altlinux.ru> 5.1.0-alt2
- real build

* Wed Feb 20 2019 Igor Vlasenko <viy@altlinux.ru> 5.1.0-alt1_1
- update by mgaimport

* Thu Jan 31 2019 Igor Vlasenko <viy@altlinux.ru> 5.0.0-alt1_3
- update by mgaimport

* Thu Oct 04 2018 Igor Vlasenko <viy@altlinux.ru> 5.0.0-alt1_2
- update by mgaimport

* Mon Aug 27 2018 Igor Vlasenko <viy@altlinux.ru> 5.0.0-alt1_1
- update by mgaimport

* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 4.7.0-alt1_1
- new version

