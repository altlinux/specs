# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed

Name: bin-marcosnils
Version: 0.17.2
Release: alt1
Summary: Effortless binary manager
License: MIT
Group: System/Configuration/Packaging
Url: https://github.com/marcosnils/bin

Source: %name-%version.tar
BuildRequires: golang

%description
Install and manage upstream static binary executables downloaded from
different sources (mostly from GitHub or Docker registry).

%prep
%setup

%build
export CGO_ENABLED=0
go build -v -buildmode=pie -ldflags \
	"-X main.version=%version-%release
	 -X main.date=$(date -I)
	 -X main.builtBy=ALT" .

%install
install -Dp bin -t %buildroot%_bindir

%check
./bin --help
./bin --version
./bin --version |& grep -Fx 'bin version %version-%release'
go test -v ./...

%files
%_bindir/bin

%changelog
* Sat Jan 20 2024 Vitaly Chikunov <vt@altlinux.org> 0.17.2-alt1
- First import v0.17.2 (2023-10-03).
