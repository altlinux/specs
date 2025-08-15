%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%add_optflags -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64

%def_with check

%define abiversion 1
Name: libfido2
Version: 1.16.0
Release: alt2

Summary: Library functionality to communicate with a FIDO device over USB
License: BSD-2-Clause
Group: System/Libraries
Url: https://github.com/Yubico/libfido2
Vcs: https://github.com/Yubico/libfido2

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libssl-devel
BuildRequires: libudev-devel
BuildRequires: libcbor-devel
BuildRequires: zlib-devel
%if_with check
BuildRequires: ctest
%endif

%description
Provides library functionality to communicate with a FIDO device over USB,
and to verify attestation and assertion signatures.

Supports the FIDO U2F (CTAP 1) and FIDO2 (CTAP 2) protocols.

%package -n %{name}_%{abiversion}
Summary: %{summary %name}
Group: System/Libraries

%description -n %{name}_%{abiversion}
%{description %name}.

%package devel
Summary: Development header files for %name
Group: Development/C
Requires: %{name}_%{abiversion} = %EVR

%description devel
Provides development header files for %name.

%package tools
Summary: Command-line tools to communicate with a FIDO device over USB
Group: System/Configuration/Hardware
Requires: %{name}_%{abiversion} = %EVR

%description tools
Provides command-line tools for %name.

%prep
%setup
%autopatch -p1

%build
%ifarch %e2k
# hid.c has questionable code as for lcc 1.26.16
sed -i 's,-Werror,& -Wno-error=conversion,' CMakeLists.txt
%endif
%cmake \
    -DBUILD_STATIC_LIBS=OFF \
    -DUDEV_RULES_DIR=%_udevrulesdir \
%if_without check
    -DBUILD_TESTS=OFF \
%endif
    %nil
%cmake_build

%install
%cmake_install

%check
%ctest

%files -n %{name}_%{abiversion}
%doc LICENSE NEWS
%_libdir/%name.so.%abiversion
%_libdir/%name.so.%version
%_udevrulesdir/70-u2f.rules

%files tools
%_bindir/*
%_man1dir/*

%files devel
%_includedir/*
%_libdir/%name.so
%_pkgconfigdir/%name.pc
%_man3dir/*

%changelog
* Fri Aug 15 2025 Anton Zhukharev <ancieg@altlinux.org> 1.16.0-alt2
- Shipped udev-rules for FIDO devices.

* Thu May 29 2025 Anton Zhukharev <ancieg@altlinux.org> 1.16.0-alt1
- Updated to 1.16.0.
- Followed Shared Libs Policy.

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
