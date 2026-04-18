# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed

Name: bin-github
Version: 0.25.3
Release: alt1
Summary: Binaries manager for GitHub (and Docker) releases
License: MIT
Group: System/Configuration/Packaging
Url: https://github.com/marcosnils/bin
Obsoletes: bin-marcosnils < %EVR
Provides: bin-marcosnils = %EVR

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
	 -X 'main.builtBy=%distribution'" .
# Needs writable dir in PATH
( export PATH=$TMPDIR:$PATH
  ./bin completion bash > bin.bash
  ./bin completion fish > bin.fish
  ./bin completion zsh  > bin.zsh )

%install
install -Dp bin -t %buildroot%_bindir
install -Dpm644 bin.bash %buildroot%_datadir/bash-completion/completions/bin
install -Dpm644 bin.fish %buildroot%_datadir/fish/vendor_completions.d/bin.fish
install -Dpm644 bin.zsh  %buildroot%_datadir/zsh/site-functions/_bin

%check
./bin --help
./bin --version
./bin --version |& grep -Fx 'bin version %version-%release'
go test -v ./...

%files
%doc LICENSE README.md
%_bindir/bin
%_datadir/bash-completion/completions/bin
%_datadir/fish/vendor_completions.d/bin.fish
%_datadir/zsh/site-functions/_bin

%changelog
* Sat Apr 18 2026 Vitaly Chikunov <vt@altlinux.org> 0.25.3-alt1
- Update to v0.25.3 (2026-04-17).

* Sat Mar 21 2026 Vitaly Chikunov <vt@altlinux.org> 0.24.3-alt1
- Update to v0.24.3 (2026-03-19).

* Tue Nov 18 2025 Vitaly Chikunov <vt@altlinux.org> 0.24.2-alt1
- Update to v0.24.2 (2025-11-06).

* Fri Oct 31 2025 Vitaly Chikunov <vt@altlinux.org> 0.24.1-alt1
- Update to v0.24.1 (2025-10-27).

* Fri Aug 01 2025 Vitaly Chikunov <vt@altlinux.org> 0.23.1-alt1
- Update to v0.23.1 (2025-07-24).

* Thu May 29 2025 Vitaly Chikunov <vt@altlinux.org> 0.21.2-alt1
- Update to v0.21.2 (2025-05-17).

* Thu May 01 2025 Vitaly Chikunov <vt@altlinux.org> 0.21.1-alt1
- Update to v0.21.1 (2025-04-26).

* Sat Feb 22 2025 Vitaly Chikunov <vt@altlinux.org> 0.20.0-alt1
- Update to v0.20.0 (2025-01-29).
- The package is renamed from bin-marcosnils to bin-github.

* Sat Oct 26 2024 Vitaly Chikunov <vt@altlinux.org> 0.19.0-alt1
- Update to v0.19.0 (2024-10-20).

* Tue Jul 30 2024 Vitaly Chikunov <vt@altlinux.org> 0.18.0-alt1
- Update to v0.18.0 (2024-07-15).

* Tue Jun 18 2024 Vitaly Chikunov <vt@altlinux.org> 0.17.6-alt1
- Update to v0.17.6 (2024-06-17).

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
