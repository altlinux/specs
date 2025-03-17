%global import_path github.com/Zxilly/go-size-analyzer
%global _unpackaged_files_terminate_build 1

Name:    go-size-analyzer
Version: 1.7.7
Release: alt1

Summary: A tool for analyzing the size of compiled Go binaries, offering cross-platform support, detailed breakdowns, and multiple output formats
License: AGPL-3.0-only
Group:   Development/Tools
Url:     https://gsa.zxilly.dev
Vcs:     https://github.com/Zxilly/go-size-analyzer.git

Source: %name-%version.tar
Source1: %name-%version-vendor.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

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
export GOROOT="%_libexecdir/golang"

%golang_prepare

cd .build/src/%import_path
%golang_build cmd/gsa

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
export GOROOT="%_libexecdir/golang"

%golang_install

%files
%doc *.md
%_bindir/*

%changelog
* Sun Mar 16 2025 Maxim Slipenko <maks1ms@altlinux.org> 1.7.7-alt1
- Initial build

