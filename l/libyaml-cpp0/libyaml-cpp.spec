%define _unpackaged_files_terminate_build 1

%define origname yaml-cpp
%define soversion 0

Name: lib%origname%soversion
Version: 0.6.3
Release: alt1

Summary: A YAML parser and emitter for C++
License: MIT
Group: Development/Other

Url: https://github.com/jbeder/yaml-cpp

# https://github.com/jbeder/yaml-cpp.git
Source: %name-%version.tar

Patch1: CVE-2017-5950.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: boost-devel-headers cmake gcc-c++

Provides: %name = %EVR

%description
A YAML parser and emitter for C++

%package -n lib%origname-devel
Summary: YAML Development libraries
Group: Development/Other
Requires: lib%origname%soversion = %EVR
Provides: %name-devel = %EVR
Obsoletes: %name-devel < %EVR

%description -n lib%origname-devel
Development libraries for YAML.
This package contains static development files for YAML.

%prep
%setup
%patch1 -p1

%build
%cmake \
	-DYAML_BUILD_SHARED_LIBS:BOOL=ON \
	-DYAML_CPP_BUILD_TOOLS:BOOL=OFF \
	-DYAML_CPP_BUILD_TESTS:BOOL=OFF \
	%nil

%cmake_build

%install
%cmakeinstall_std

%files
%doc LICENSE *.md
%_libdir/*.so.*

%files -n lib%origname-devel
%_includedir/%origname
%_pkgconfigdir/*.pc
%_libdir/*.so
%_libdir/cmake/%origname

%changelog
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
