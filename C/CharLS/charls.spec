%define _unpackaged_files_terminate_build 1
%define abiversion 2

%{expand: %(sed 's,^%%,%%global ,' /usr/lib/rpm/macros.d/ubt)}
%define ubt_id %__ubt_branch_id

Name: CharLS
Version: 2.4.2
Release: alt2

Summary: C++ JPEG-LS library implementation
License: BSD-3-Clause
Group: System/Libraries
Url: https://github.com/team-charls/charls
VCS: https://github.com/team-charls/charls.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-cmake
BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-macros-ifver
BuildRequires: cmake
BuildRequires: ctest
BuildRequires: gcc-c++

%description
%summary.

%package -n libcharls%abiversion
Summary: %summary
Group: System/Libraries

Provides: charls = %EVR
Provides: CharLS = %EVR
%ifver_gteq %ubt_id M120
Provides: libCharLS2 = %EVR
Obsoletes: libCharLS2 < %EVR
%endif

%description -n libcharls%abiversion
CharLS is a C++ implementation of the JPEG-LS standard
for lossless and near-lossless image compression and decompression.
JPEG-LS is a low-complexity image compression standard
that matches JPEG 2000 compression ratios.

%package -n lib%name-devel
Summary: Development package for %name
Group: Development/C++

Provides: charls-devel = %EVR
Provides: CharLS-devel = %EVR

%description -n lib%name-devel
%summary.

%prep
%setup

%build
%cmake \
  -DBUILD_SHARED_LIBS:BOOL=ON \
  -DBUILD_TESTING:BOOL=ON \
  -DCHARLS_BUILD_SAMPLES:BOOL=ON \
  -DCHARLS_BUILD_TESTS:BOOL=ON \
  -DCHARLS_PEDANTIC_WARNINGS:BOOL=ON \
%nil

%cmake_build

%install
%cmake_install

%check
%ctest

%files -n libcharls%abiversion
%_libdir/libcharls.so.%abiversion
%_libdir/libcharls.so.%version

%files -n lib%name-devel
%doc README.md SECURITY.md
%_cmakedir/charls/charlsConfig.cmake
%_cmakedir/charls/charlsConfig-noconfig.cmake
%_cmakedir/charls/charlsConfigVersion.cmake
%_includedir/charls
%_libdir/libcharls.so
%_libdir/pkgconfig/charls.pc

%changelog
* Mon Jan 27 2025 Constantin Sunzow <protvin@altlinux.org> 2.4.2-alt2
- Changed binary package name for library.

* Thu Dec 26 2024 Constantin Sunzow <protvin@altlinux.org> 2.4.2-alt1
- Purge archive extracted source code.
- Build from git tag.
- New version.

* Mon Feb 24 2020 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_3
- new version

* Sun Jan 12 2014 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0-alt2
- fix build

* Wed Nov 09 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0-alt1
- first build for ALT Linux
