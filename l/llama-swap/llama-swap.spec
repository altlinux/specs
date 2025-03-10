# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed

Name: llama-swap
Version: 92
Release: alt1
Summary: A proxy for llama.cpp-server to provide automatic model switching
License: MIT
Group: System/Servers
Url: https://github.com/mostlygeek/llama-swap

Source: %name-%version.tar
BuildRequires: golang

%description
llama-swap is a light weight, transparent proxy server that provides automatic
model swapping to llama.cpp's server.

%prep
%setup

%build
go build -v -buildmode=pie -ldflags "-X main.commit=%release -X main.version=%version -X main.date=$(date -uI)"

%install
install -Dp llama-swap -t %buildroot%_bindir

%check
%buildroot%_bindir/llama-swap --version | grep -F 'version: %version (%release), built at'
go build -o "build/simple-responder_linux_$(go env GOARCH)" misc/simple-responder/simple-responder.go
go test -v ./...

%files
%define _customdocdir %_docdir/%name
%doc LICENSE.md README.md examples
%_bindir/llama-swap

%changelog
* Mon Mar 10 2025 Vitaly Chikunov <vt@altlinux.org> 92-alt1
- First import v92 (2025-03-09).
