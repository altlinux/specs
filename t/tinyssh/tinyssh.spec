# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: tinyssh
Version: 20230101
Release: alt1
Summary: TinySSH is small server
License: ALT-Public-Domain or CC0-1.0
Group: Security/Networking
Url: https://tinyssh.org/
Vcs: https://github.com/janmojzis/tinyssh

Source: %name-%version.tar
BuildRequires: libsodium-devel
BuildRequires: rpm-build-python3

%description
TinySSH is a minimalistic SSH server which implements only a subset of SSHv2
features.

%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS)
unset MAKEFLAGS
export LIBS="-lsodium"
export CFLAGS="%optflags -I/usr/include/sodium -I${PWD}/crypto"
%make_build

%install
%makeinstall_std
mkdir -p %buildroot/etc/tinyssh/sshkeydir
install -Dp tools/tinyssh-convert %buildroot%_bindir/tinyssh-convert

%check
LD_DEBUG=bindings %buildroot%_sbindir/tinysshd 2> bindings.txt ||:
cat <<-EOF | xargs -i -n1 grep -e "tinysshd .* to .*libsodium\.so.*symbol \`{}'" bindings.txt
	crypto_hash_sha256
	crypto_hash_sha512
	crypto_onetimeauth_poly1305
	crypto_scalarmult_curve25519
	crypto_scalarmult_curve25519_base
	crypto_sign_ed25519
	crypto_sign_ed25519_keypair
	crypto_sign_ed25519_open
	crypto_stream_chacha20_xor
	crypto_verify_16
EOF

%files
%define _customdocdir %_docdir/%name
%doc LICENCE README.md
%_sysconfdir/%name
%_bindir/tinyssh*
%_sbindir/tinysshd*
%_man8dir/tiny*.8*

%changelog
* Sun Jan 01 2023 Vitaly Chikunov <vt@altlinux.org> 20230101-alt1
- First import 20230101 (2022-12-31).
