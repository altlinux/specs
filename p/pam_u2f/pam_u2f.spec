%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%add_optflags -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64

Name: pam_u2f
Version: 1.3.0
Release: alt1

Summary: Pluggable Authentication Module (PAM) for U2F and FIDO2
License: BSD-2-Clause
Group: System/Base
Url: https://github.com/Yubico/pam-u2f

Source: %name-%version.tar

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: asciidoc
BuildRequires: asciidoc-a2x
BuildRequires: pkg-config
BuildRequires: libfido2-devel
BuildRequires: libssl-devel
BuildRequires: libpam-devel

%description
This module implements PAM over U2F and FIDO2, providing an easy way to
integrate the YubiKey (or other U2F/FIDO2 compliant authenticators) into
your existing infrastructure.

%prep
%setup

%build
%autoreconf
%configure --with-pam-dir=%_pam_modules_dir
%make_build

%install
%makeinstall_std

%files
%doc README AUTHORS COPYING NEWS
%_bindir/*
%_pam_modules_dir/*.so
%_man1dir/*
%_man8dir/*

%check
%make_build check

%changelog
* Tue Mar 28 2023 Anton Zhukharev <ancieg@altlinux.org> 1.3.0-alt1
- New version.
- Set strict ELF verification.

* Tue Aug 02 2022 Anton Zhukharev <ancieg@altlinux.org> 1.2.1-alt1
- initial build for Sisyphus

