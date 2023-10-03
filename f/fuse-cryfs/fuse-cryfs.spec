%define oname cryfs
Name: fuse-cryfs
Version: 0.11.4
Release: alt1

Summary: Cryptographic filesystem for the cloud

License: LGPLv2
Group: System/Kernel and hardware
Url: https://www.cryfs.org/

Requires: fuse

# Source-url: https://github.com/cryfs/cryfs/archive/%version.tar.gz
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

ExcludeArch: armh

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake >= 3.10
BuildRequires: boost-devel boost-devel-headers boost-filesystem-devel boost-program_options-devel boost-asio-devel
#BuildRequires: boost-devel-static
BuildRequires: libcryptopp-devel
BuildRequires: libcurl-devel
BuildRequires: libfuse-devel >= 2.8.6
BuildRequires: libssl-devel
BuildRequires: librange-v3-devel >= 0.11.0
BuildRequires: libspdlog-devel >= 1.8.5

BuildRequires: gcc-c++
BuildRequires: libgomp-devel
BuildRequires: python3

%description
CryFS encrypts your files, so you can safely store them anywhere.
It works well together with cloud services
like Dropbox, iCloud, OneDrive and others.
See https://www.cryfs.org.

%prep
%setup

%build
%cmake -DBUILD_TESTING=off -DBoost_INCLUDE_DIRS=%_includedir/boost -DBoost_USE_STATIC_LIBS=off \
       -DCMAKE_BUILD_TYPE=RELEASE \
       -DDEPENDENCY_CONFIG=cmake-utils/DependenciesFromLocalSystem.cmake
%cmake_build

%install
%cmake_install

%files
%_bindir/cryfs
%_bindir/cryfs-unmount
%_man1dir/*

%changelog
* Tue Oct 03 2023 Vitaly Lipatov <lav@altlinux.ru> 0.11.4-alt1
- new version (0.11.4) with rpmgs script
- update BR, build with system spdlog
- ExcludeArch: armh

* Tue Apr 27 2021 Arseny Maslennikov <arseny@altlinux.org> 0.9.11-alt2.1
- NMU: spec: adapted to new cmake macros.

* Thu Mar 11 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.11-alt2
- Rebuilt with boost-1.75.0.

* Wed Jun 03 2020 Vitaly Lipatov <lav@altlinux.ru> 0.9.11-alt1
- new version 0.9.11 (with rpmrb script)

* Mon Dec 16 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.10-alt2
- Rebuilt with boost-1.71.0.

* Tue Feb 12 2019 Vitaly Lipatov <lav@altlinux.ru> 0.9.10-alt1
- new version 0.9.10 (with rpmrb script)

* Sun Nov 04 2018 Vitaly Lipatov <lav@altlinux.ru> 0.9.9-alt2.1
- NMU: autorebuild with libcryptopp.so.7

* Mon Sep 03 2018 Vitaly Lipatov <lav@altlinux.ru> 0.9.9-alt2
- disable build with external stdlog

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 0.9.9-alt1
- new version 0.9.9 (with rpmrb script), rebuild with libcryptopp-6.1.0
- enable dynamic boost build

* Sat Dec 09 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.7-alt2.1
- NMU: autorebuild with libcryptopp-5.6.5

* Sun Jul 23 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.7-alt2
- fix build, build with external spdlog

* Wed Mar 08 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.7-alt1
- initial build for ALT Linux Sisyphus
