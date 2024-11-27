# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed

Name: pup
Epoch: 1
Version: 0.4.0
Release: alt1
Summary: Parsing HTML at the command line
License: MIT
Group: Text tools
Url: https://github.com/ericchiang/pup

Source: %name-%version.tar
BuildRequires: golang
%{?!_without_check:%{?!_disable_check:
BuildRequires: python3
}}

%description
pup is a command line tool for processing HTML. It reads from stdin,
prints to stdout, and allows the user to filter parts of the page using
CSS selectors.

Inspired by jq, pup aims to be a fast and flexible way of exploring HTML
from the terminal.

%prep
%setup

%build
%ifnarch armh %ix86 loongarch64 riscv64
export CGO_ENABLED=0
%endif
go build -v -mod=vendor -buildmode=pie

%install
install -Dp pup %buildroot%_bindir/pup

%check
%buildroot%_bindir/pup --version | grep -Fx '%version'
go test -mod=vendor -v ./...
PATH=%buildroot%_bindir:$PATH
cd tests
bash -x test

%files
%doc LICENSE README.md
%_bindir/pup

%changelog
* Wed Nov 27 2024 Vitaly Chikunov <vt@altlinux.org> 1:0.4.0-alt1
- First import v0.4.0-11-g5a57cf1 (2022-03-06).
