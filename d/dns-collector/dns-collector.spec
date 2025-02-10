%global import_path github.com/dmachard/dns-collector
Name:    dns-collector
Version: 1.4.0
Release: alt1

Summary: Ingesting, pipelining, and enhancing your DNS logs with usage indicators, security analysis, and additional metadata
License: MIT
Group:   Other
Url:     https://github.com/dmachard/DNS-collector

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
DNS-collector acts as a passive high speed ingestor with pipelining support for
your DNS logs, written in Golang. It allows enhancing your DNS logs by adding
metadata, extracting usage patterns, and facilitating security analysis.

Additionally, DNS-collector also supports:
- Extended DNStap with TLS encryption, compression, and more metadata
  capabilities DNS protocol conversions to Plain text, Key/Value JSON, Jinja
  and more
- DNS parser with Extension Mechanisms for DNS (EDNS) support
- Live capture on a network interface
- IPv4/v6 defragmentation and TCP reassembly
- Nanoseconds in timestamps

%prep
%setup
tar xf %SOURCE1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc *.md
%_bindir/*

%changelog
* Mon Feb 10 2025 Andrey Cherepanov <cas@altlinux.org> 1.4.0-alt1
- New version.

* Thu Jan 16 2025 Andrey Cherepanov <cas@altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus.
