%define _unpackaged_files_terminate_build 1

%define soversion 0.7

Name: yaml-cpp
Version: 0.7.0
Release: alt1

Summary: A YAML parser and emitter for C++
License: MIT
Group: System/Libraries

Url: https://github.com/jbeder/%name

# https://github.com/jbeder/%name/archive/%name-%version/%name-%name-%version.tar.gz
Source: %name-%name-%version.tar

Patch1: https://patch-diff.githubusercontent.com/raw/jbeder/yaml-cpp/pull/1037.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: boost-devel-headers cmake gcc-c++

%description
A YAML parser and emitter for C++

%package -n lib%name%soversion
Summary: A YAML parser and emitter for C++
Group: System/Libraries

%description -n lib%name%soversion
A YAML parser and emitter for C++

%package -n lib%name-devel
Summary: YAML Development libraries
Group: Development/C++
Provides: %name-devel = %EVR
Obsoletes: %name-devel < %EVR

%description -n lib%name-devel
Development libraries for YAML.
This package contains static development files for YAML.

%prep
%setup -n %name-%name-%version
%patch1 -p1

%build
%cmake \
	-DCMAKE_INSTALL_DATADIR:PATH=%_libdir \
	-DYAML_BUILD_SHARED_LIBS:BOOL=ON \
	-DYAML_CPP_BUILD_TOOLS:BOOL=OFF \
	-DYAML_CPP_BUILD_TESTS:BOOL=OFF \
	%nil

%cmake_build

%install
%cmakeinstall_std

%files -n lib%name%soversion
%doc LICENSE *.md
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/%name
%_pkgconfigdir/*.pc
%_libdir/*.so
%_libdir/cmake/%name

%changelog
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
