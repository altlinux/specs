%define _unpackaged_files_terminate_build 1

%define pkgname yaml-cpp
%define soversion 0.8

Name: %pkgname%soversion
Version: 0.8.0
Release: alt2

Summary: A YAML parser and emitter for C++
License: MIT
Group: System/Legacy libraries

Url: https://github.com/jbeder/%pkgname

# https://github.com/jbeder/%pkgname/archive/%version/%pkgname-%version.tar.gz
Source: %pkgname-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: boost-devel-headers cmake gcc-c++

%description
A YAML parser and emitter for C++

%package -n lib%name
Summary: A YAML parser and emitter for C++
Group: System/Legacy libraries

%description -n lib%name
A YAML parser and emitter for C++

%prep
%setup -n %pkgname-%version

%build
%cmake \
	-DCMAKE_INSTALL_DATADIR:PATH=%_libdir \
	-DYAML_BUILD_SHARED_LIBS:BOOL=ON \
	-DYAML_CPP_BUILD_TOOLS:BOOL=OFF \
	-DYAML_CPP_BUILD_TESTS:BOOL=OFF \
	%nil

%cmake_build

%install
%cmake_install

%__rm -rf %buildroot%_includedir/%pkgname
%__rm -rf %buildroot%_pkgconfigdir/*.pc
%__rm -rf %buildroot%_libdir/*.so
%__rm -rf %buildroot%_libdir/cmake/%pkgname

%files -n lib%name
%doc LICENSE *.md
%_libdir/*.so.*

%changelog
* Fri Feb 06 2026 Nazarov Denis <nenderus@altlinux.org> 0.8.0-alt2
- Build as legacy library

* Sun Nov 12 2023 Nazarov Denis <nenderus@altlinux.org> 0.8.0-alt1
- New version 0.8.0.

* Fri Nov 05 2021 Nazarov Denis <nenderus@altlinux.org> 0.7.0-alt1
- Updated to upstream version 0.7.0.

* Tue Apr 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.3-alt1
- Updated to upstream version 0.6.3.

* Mon Oct 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.2-alt2
- Applied patches from Fedora (Fixes: CVE-2017-5950)

* Tue Sep 11 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.2-alt1
- Updated to upstream version 0.6.2.

* Tue Dec 1 2015 Vladimir Didenko <cow@altlinux.ru> 0.5.1-alt4
- Rebuild with gcc5

* Tue Mar 24 2015 Vladimir Didenko <cow@altlinux.ru> 0.5.1-alt3
- spec cleanup
- add dependency on corresponding library to devel package

* Sat Jun 7 2014 Andrew Clark <andyc@altlinux.ru> 0.5.1-alt2
- spec file has been changed

* Thu May 29 2014 Andrew Clark <andyc@altlinux.ru> 0.5.1-alt1
- initial build for ALT Linux
