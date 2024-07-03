%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%def_with check

Name: libfido2
Version: 1.15.0
Release: alt1

Summary: Library functionality to communicate with a FIDO device over USB
License: BSD-2-Clause
Group: System/Libraries
Url: https://github.com/Yubico/libfido2
Vcs: https://github.com/Yubico/libfido2

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libssl-devel
BuildRequires: libudev-devel
BuildRequires: libcbor-devel
BuildRequires: zlib-devel
%{?_with_check:BuildRequires: ctest}

%add_optflags -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64

%description
Provides library functionality to communicate with a FIDO device over USB,
and to verify attestation and assertion signatures.

Supports the FIDO U2F (CTAP 1) and FIDO2 (CTAP 2) protocols.

%package devel
Summary: Development header files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
Provides development header files for %name.

%package tools
Summary: Command-line tools to communicate with a FIDO device over USB
Group: System/Configuration/Hardware
Requires: %name = %EVR

%description tools
Provides command-line tools for %name.

%prep
%setup

%build
%ifarch %e2k
# hid.c has questionable code as for lcc 1.26.16
sed -i 's,-Werror,& -Wno-error=conversion,' CMakeLists.txt
%endif
%cmake \
    -DBUILD_STATIC_LIBS=OFF \
    %{?_without_check:-DBUILD_TESTS=OFF} \
    %nil
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%doc LICENSE NEWS
%_libdir/%name.so.*

%files tools
%_bindir/*
%_man1dir/*

%files devel
%_includedir/*
%_libdir/%name.so
%_pkgconfigdir/%name.pc
%_man3dir/*

%changelog
* Wed Jul 03 2024 Anton Zhukharev <ancieg@altlinux.org> 1.15.0-alt1
- Updated to 1.15.0.

* Fri Dec 29 2023 Anton Zhukharev <ancieg@altlinux.org> 1.14.0-alt1
- Updated to 1.14.0.
- Renamed SRPM to libfido2 to match the project name.

* Sat Apr 08 2023 Michael Shigorin <mike@altlinux.org> 1.13.0-alt2
- E2K: ftbfs workaround

* Tue Mar 28 2023 Anton Zhukharev <ancieg@altlinux.org> 1.13.0-alt1
- New version.

* Sun Jan 08 2023 Anton Zhukharev <ancieg@altlinux.org> 1.12.0-alt1
- 1.12.0
- follow sharedlib policy
- add strict ELF verification

* Sat Jul 23 2022 Anton Zhukharev <ancieg@altlinux.org> 1.10.0-alt1
- initial build for Sisyphus
