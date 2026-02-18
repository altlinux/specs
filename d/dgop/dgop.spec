%define _unpackaged_files_terminate_build 1
%global import_path github.com/AvengeMedia/dgop

Name: dgop
Version: 0.2.2
Release: alt1

Summary: System monitoring CLI and REST API
License: MIT
Group: Monitoring

Url: https://github.com/AvengeMedia/dgop
# Source-url: https://github.com/AvengeMedia/dgop/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
dgop is a go-based stateless system monitoring tool that provides both a CLI interface
and REST API for retrieving system metrics including CPU, memory, disk, network,
processes, and GPU information.

Features:
- Interactive TUI with real-time system monitoring
- REST API server with OpenAPI specification
- JSON output for all metrics
- GPU temperature monitoring (NVIDIA)
- Lightweight single-binary deployment

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

cd .build/src/%import_path
%golang_build cmd/dgop

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%files
%_bindir/dgop

%changelog
* Wed Feb 18 2026 Boris Yumankulov <boria138@altlinux.org> 0.2.2-alt1
- new version 0.2.2
- use go macros to build

* Sun Feb 08 2026 Boris Yumankulov <boria138@altlinux.org> 0.2.0-alt1
- new version 0.2.0

* Fri Jan 23 2026 Boris Yumankulov <boria138@altlinux.org> 0.1.13-alt1
- new version 0.1.13

* Mon Dec 22 2025 Boris Yumankulov <boria138@altlinux.org> 0.1.12-alt1
- new version 0.1.12

* Fri Nov 07 2025 Boris Yumankulov <boria138@altlinux.org> 0.1.11-alt1
- initial build for ALT Sisyphus

