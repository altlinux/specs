Name: carapace-bin
Version: 1.7.3
Release: alt1
Summary: A multi-shell completion binary
License: MIT
Group: Shells
Url: https://github.com/carapace-sh/carapace-bin
Source: https://github.com/carapace-sh/carapace-bin/archive/refs/tags/v1.7.3.tar.gz#/%name-%version.tar.gz
# rm -rf vendor ; go mod vendor
Source1: vendor.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: ca-certificates rpm-build-golang

%description
Carapace-bin provides argument completion for multiple CLI commands (full list),
and works across multiple POSIX and non-POSIX shells.

Supported shells:
* Bash
* Cmd (experimental)
* Elvish
* Fish
* Ion (experimental)
* Nushell
* Oil
* Powershell
* Tcsh (experimental)
* Xonsh
* Zsh

%prep
%setup -a1

%build
go generate ./...

export BUILDDIR="$PWD/.build"
export GOPATH="$BUILDDIR:%go_path"
export VERSION=%version
export COMMIT=%release
export BRANCH=altlinux
export LDFLAGS="-X main.Version=$VERSION"
%golang_build ./cmd/carapace

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"
export IGNORE_SOURCES=1

%golang_install

#%%check

%files
%doc *.md
%_bindir/*

%changelog
* Sun Sep 06 2026 Ildar Mulyukov <ildar@altlinux.ru> 1.7.3-alt1
- Initial build for Sisyphus
