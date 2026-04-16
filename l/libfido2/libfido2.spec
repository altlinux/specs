%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%add_optflags -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64

%def_with check

%define abiversion 1
%define libname libfido2

Name: libfido2
Version: 1.17.0
Release: alt1

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

%package -n %{libname}_%{abiversion}
Summary: Library functionality to communicate with FIDO device over USB
Group: System/Libraries
%if "%{libname}_%{abiversion}" == "libfido2_1"
Provides: %libname = %EVR
Obsoletes: %libname < %EVR
%endif

%description -n %{libname}_%{abiversion}
Provides library functionality to communicate with a FIDO device over USB,
and to verify attestation and assertion signatures.

Supports the FIDO U2F (CTAP 1) and FIDO2 (CTAP 2) protocols.

%package devel
Summary: Development header files for libfido2
Group: Development/C
Requires: %{libname}_%{abiversion} = %EVR

%description devel
Provides development header files for libfido2.

%package tools
Summary: Command-line tools to communicate with a FIDO device over USB
Group: System/Configuration/Hardware
Requires: %{libname}_%{abiversion} = %EVR

%description tools
Provides command-line tools for libfido2.

%prep
%setup
%autopatch -p1
# uaccess tag is better than plugdev group
sed -i 's/, GROUP="plugdev", MODE="0660"//' udev/70-u2f.rules

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

%files -n %{libname}_%{abiversion}
%doc LICENSE NEWS
%_libdir/%libname.so.%abiversion
%_libdir/%libname.so.%version
%_udevrulesdir/70-u2f.rules

%files tools
%_bindir/fido2-*
%_man1dir/fido2-*.1*

%files devel
%_includedir/fido.h
%_includedir/fido/
%_libdir/%libname.so
%_pkgconfigdir/%libname.pc
%_man3dir/*.3*

%changelog
* Thu Apr 16 2026 Anton Zhukharev <ancieg@altlinux.org> 1.17.0-alt1
- Updated to 1.17.0.

* Thu Feb 12 2026 Anton Zhukharev <ancieg@altlinux.org> 1.16.0-alt6
- Removed 'plugdev' from 70-u2f.rules to use 'uaccess' only (ALT#57844).

* Thu Jan 22 2026 Anton Zhukharev <ancieg@altlinux.org> 1.16.0-alt5
- Removed libfido2 obsoletion for future ABI version change (ALT#56956).

* Wed Jan 21 2026 Anton Zhukharev <ancieg@altlinux.org> 1.16.0-alt4
- Unbound library name and source package name (ALT#56956).

* Tue Jan 20 2026 Anton Zhukharev <ancieg@altlinux.org> 1.16.0-alt3
- Fixed upgrading after 1.16.0-alt1 (ALT#56956).

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
