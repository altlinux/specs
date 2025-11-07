%define _unpackaged_files_terminate_build 1

Name: dgop
Version: 0.1.11
Release: alt1

Summary: System monitoring CLI and REST API
License: MIT
Group: Monitoring

Url: https://github.com/AvengeMedia/dgop
# Source-url: https://github.com/AvengeMedia/dgop/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar

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
# %golang_build cmd/cli builds %_bindir/cli; replaced with go build -o %name
go build -o %name ./cmd/cli

%install
install -Dm 755 %name -t %buildroot%_bindir

%files
%_bindir/dgop

%changelog
* Fri Nov 07 2025 Boris Yumankulov <boria138@altlinux.org> 0.1.11-alt1
- initial build for ALT Sisyphus

