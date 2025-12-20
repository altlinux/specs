# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed

Name: landrun
Version: 0.1.15
Release: alt1
Summary: Landlock sandbox
License:  MIT
Group: Security/Networking
Url: https://github.com/zouuup/landrun

Source: %name-%version.tar
BuildRequires: golang

%description
A lightweight, secure sandbox for running Linux processes using
Landlock. Think firejail, but with kernel-level security and minimal
overhead.

Linux Landlock is a kernel-native security module that lets unprivileged
processes sandbox themselves.

Landrun is designed to make it practical to sandbox any command with
fine-grained filesystem and network access controls. No root. No
containers. No SELinux/AppArmor configs.

It's lightweight, auditable, and wraps Landlock v5 features (file access +
TCP restrictions).

%prep
%setup
%ifarch %ix86
sed -i 's!/lib64!/lib!g' test.sh
%endif

%build
go build -v -buildmode=pie -ldflags "-X main.version=%version" cmd/landrun/main.go

%install
install -Dp main -T %buildroot%_bindir/%name

%check
PATH=%buildroot%_bindir:$PATH
landrun --version | grep -Fx 'landrun version %version'
# Cannot run at HOME becasue it's under /usr
cd /tmp
$OLDPWD/test.sh --use-system --offline

%files
%doc LICENSE README.md
%_bindir/landrun

%changelog
* Sat Dec 20 2025 Vitaly Chikunov <vt@altlinux.org> 0.1.15-alt1
- First import v0.1.15-15-g5ed4a3d (2025-10-01).
