# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed

Name: bin-marcosnils
Version: 0.17.5
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
%ifnarch %ix86 armh riscv64 loongarch64
export CGO_ENABLED=0
%endif
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
* Fri Apr 26 2024 Vitaly Chikunov <vt@altlinux.org> 0.17.5-alt1
- Update to v0.17.5 (2024-04-25).

* Wed Mar 13 2024 Vitaly Chikunov <vt@altlinux.org> 0.17.4-alt1
- Update to v0.17.4 (2024-03-10).

* Wed Feb 28 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.17.3-alt1.1
- NMU: fixed FTBFS on LoongArch:
  + -buildmode=pie requires cgo here
  + use golang.org/x/sys@v0.0.0-20220712014510-0a85c31ab51e

* Sat Feb 24 2024 Vitaly Chikunov <vt@altlinux.org> 0.17.3-alt1
- Update to v0.17.3 (2024-01-31).

* Sat Jan 20 2024 Vitaly Chikunov <vt@altlinux.org> 0.17.2-alt1
- First import v0.17.2 (2023-10-03).
