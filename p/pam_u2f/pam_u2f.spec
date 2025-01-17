%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%add_optflags -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64

Name: pam_u2f
Version: 1.3.2
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

%description
This module implements PAM over U2F and FIDO2, providing an easy way to
integrate the YubiKey (or other U2F/FIDO2 compliant authenticators) into
your existing infrastructure.

%prep
%setup
%autopatch -p1

%build
%autoreconf
%configure --with-pam-dir=%_pam_modules_dir
%make_build

%install
%makeinstall_std

%check
%make_build check

%files
%doc README AUTHORS COPYING NEWS
%_bindir/*
%_pam_modules_dir/*.so
%_man1dir/*
%_man8dir/*

%changelog
* Fri Jan 17 2025 Anton Zhukharev <ancieg@altlinux.org> 1.3.2-alt1
- Updated to 1.3.2 (closes CVE-2025-23013).

* Tue Mar 28 2023 Anton Zhukharev <ancieg@altlinux.org> 1.3.0-alt1
- New version.
- Set strict ELF verification.

* Tue Aug 02 2022 Anton Zhukharev <ancieg@altlinux.org> 1.2.1-alt1
- initial build for Sisyphus

