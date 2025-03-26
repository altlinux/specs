%define _unpackaged_files_terminate_build 1
%define import_path github.com/projectdiscovery/katana

Name: katana
Version: 1.1.2
Release: alt1

Summary: Next-generation crawling and spidering framework
License: MIT
Group: Security/Networking
Url: https://github.com/projectdiscovery/katana
Vcs: https://github.com/projectdiscovery/katana

ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang >= 1.18

%description
Katana is a fast, next-generation web crawling and spidering
framework developed by ProjectDiscovery. Designed for
automation, reconnaissance, and security testing, it
supports both standard and headless crawling modes.

Key Features:
- High-speed, fully configurable crawling engine.
- JavaScript parsing, DOM rendering, and endpoint
  extraction.
- Headless browser support via Chrome for deep analysis.
- Form auto-filling, scope filtering, and regex-based
  input/output control.
- Works with stdin, URL, or file input; outputs to stdout,
  file, or JSONL.
- Advanced filtering, rate-limiting, and automation-ready
  CLI.
- Can be used both as a standalone binary and Go library.

%prep
%setup -a1
%autopatch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

cd $BUILDDIR/src/%import_path
%golang_build cmd/katana

%install
export BUILDDIR="$PWD/.build"
export GOPATH="$BUILDDIR:%go_path"
export IGNORE_SOURCES=1
%golang_install

%files
%doc README* LICENSE*
%_bindir/%name

%changelog
* Wed Mar 26 2025 Denis Sergeev <zeff@altlinux.org> 1.1.2-alt1
- Initial build for ALT Sisyphus.
