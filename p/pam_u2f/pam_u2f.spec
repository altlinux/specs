%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%add_optflags -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64

%def_with check

Name: pam_u2f
Version: 1.4.0
Release: alt1

Summary: Pluggable Authentication Module (PAM) for U2F and FIDO2
License: BSD-2-Clause
Group: System/Base
Url: https://github.com/Yubico/pam-u2f
Vcs: https://github.com/Yubico/pam-u2f

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires: asciidoc-a2x
BuildRequires: libfido2-devel
BuildRequires: libssl-devel
BuildRequires: libpam-devel
%if_with check
BuildRequires: ctest
%endif

%description
This module implements PAM over U2F and FIDO2, providing an easy way to
integrate the YubiKey (or other U2F/FIDO2 compliant authenticators) into
your existing infrastructure.

%prep
%setup
%autopatch -p1

%build
%cmake -DPAM_INCLUDE_DIRS=%_includedir/security
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%doc README AUTHORS COPYING NEWS
%_bindir/pamu2fcfg
%_pam_modules_dir/pam_u2f.so
%_man1dir/pamu2fcfg.1*
%_man8dir/pam_u2f.8*

%changelog
* Thu Mar 27 2025 Anton Zhukharev <ancieg@altlinux.org> 1.4.0-alt1
- Updated to 1.4.0.

* Fri Jan 17 2025 Anton Zhukharev <ancieg@altlinux.org> 1.3.2-alt1
- Updated to 1.3.2 (closes CVE-2025-23013).

* Tue Mar 28 2023 Anton Zhukharev <ancieg@altlinux.org> 1.3.0-alt1
- New version.
- Set strict ELF verification.

* Tue Aug 02 2022 Anton Zhukharev <ancieg@altlinux.org> 1.2.1-alt1
- initial build for Sisyphus

