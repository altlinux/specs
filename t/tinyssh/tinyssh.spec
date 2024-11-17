# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: tinyssh
Version: 20241111
Release: alt1
Summary: A minimalistic SSH server which implements only a subset of SSHv2 features
License: ALT-Public-Domain or CC0-1.0
Group: Security/Networking
Url: https://tinyssh.org/
Vcs: https://github.com/janmojzis/tinyssh

Source: %name-%version.tar
BuildRequires: gcc-c++
BuildRequires: lib25519-devel
BuildRequires: libntruprime-devel
BuildRequires: librandombytes-devel
BuildRequires: rpm-build-python3

%description
TinySSH is a minimalistic SSH server which implements only a subset of SSHv2
features.

%prep
%setup

%build
%add_optflags -fwrapv %(getconf LFS_CFLAGS)
%make_build CFLAGS="%optflags"

%install
%makeinstall_std PREFIX=%_prefix
mkdir -p %buildroot/etc/tinyssh/sshkeydir
install -Dp tools/tinyssh-convert %buildroot%_bindir/tinyssh-convert
%define _customdocdir %_docdir/%name

%check
ldd %buildroot%_sbindir/tinysshd
LD_DEBUG=bindings %buildroot%_sbindir/tinysshd 2> bindings.txt ||:
grep -Pe 'tinysshd .* to .*/librandombytes-kernel\.so' bindings.txt
grep -Pe 'tinysshd .* to .*/lib25519\.so' bindings.txt
grep -Pe 'tinysshd .* to .*/libntruprime\.so' bindings.txt

%files
%doc LICENCE README.md
%_sysconfdir/%name
%_bindir/tinyssh-convert
%_sbindir/tinysshd
%_sbindir/tinysshd-makekey
%_sbindir/tinysshd-printkey
%_sbindir/tinysshnoneauthd
%_man8dir/tiny*.8*

%changelog
* Thu Nov 14 2024 Vitaly Chikunov <vt@altlinux.org> 20241111-alt1
- Update to 20241111 (2024-11-11).
- libsodium is no longer used (abandoned by upstream) switching to djb's
  microlibraries and internal libraries.

* Mon Jan 01 2024 Vitaly Chikunov <vt@altlinux.org> 20240101-alt1
- Update to 20240101 (2024-01-01). (Fixes: CVE-2023-48795).

* Sun Jan 01 2023 Vitaly Chikunov <vt@altlinux.org> 20230101-alt1
- First import 20230101 (2022-12-31).
