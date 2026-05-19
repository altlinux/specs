%global import_path github.com/Zxilly/go-size-analyzer
%global _unpackaged_files_terminate_build 1

Name:    go-size-analyzer
Version: 1.13.0
Release: alt1

Summary: A tool for analyzing the size of compiled Go binaries, offering cross-platform support, detailed breakdowns, and multiple output formats
License: AGPL-3.0-only
Group:   Development/Tools
Url:     https://gsa.zxilly.dev
Vcs:     https://github.com/Zxilly/go-size-analyzer.git

Source: %name-%version.tar
Source1: %name-%version-vendor.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: golang >= 1.25
BuildRequires: /proc

%description
A simple tool to analyze the size of a Go compiled binary.
- Cross-platform support for analyzing `ELF`, `Mach-O`, and `PE` binary formats
- Detailed size breakdown by packages and sections
- Support multiple output formats: `text`, `json`, `html`, `svg`
- Interactive exploration via web interface and terminal UI
- Binary comparison with diff mode (supports `json` and `text` output)

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-X %import_path.version=%version"
export GOEXPERIMENT=jsonv2

%golang_prepare

%golang_build cmd/gsa

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc *.md
%_bindir/*

%changelog
* Tue May 19 2026 Maxim Slipenko <maks1ms@altlinux.org> 1.13.0-alt1
- New version 1.13.0.

* Sun May 10 2026 Maxim Slipenko <maks1ms@altlinux.org> 1.12.6-alt1
- New version 1.12.6.

* Wed Mar 25 2026 Maxim Slipenko <maks1ms@altlinux.org> 1.11.0-alt1
- New version 1.11.0.

* Wed Dec 10 2025 Maxim Slipenko <maks1ms@altlinux.org> 1.10.2-alt1
- New version 1.10.2.

* Wed Oct 15 2025 Maxim Slipenko <maks1ms@altlinux.org> 1.10.0-alt1
- New version 1.10.0.

* Mon Jul 21 2025 Maxim Slipenko <maks1ms@altlinux.org> 1.9.2-alt1
- New version 1.9.2.

* Fri May 02 2025 Maxim Slipenko <maks1ms@altlinux.org> 1.8.1-alt1
- New version 1.8.1.

* Sun Mar 16 2025 Maxim Slipenko <maks1ms@altlinux.org> 1.7.7-alt1
- Initial build
