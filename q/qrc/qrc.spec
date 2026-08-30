Name: qrc
Version: 0.9.0
Release: alt1
Source: %name-%version.tar.gz
Source1: vendor.tar
Group: Other

Summary: QR code generator for text terminals
License: MIT
VCS: https://github.com/fumiyas/qrc

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-macros-golang
# Automatically added by buildreq on Sun Aug 30 2026
# optimized out: bash5 golang golang-src libgpg-error python3 python3-base sh5
BuildRequires: rpm-build-golang

BuildRequires: rpm-build-golang

%description
This program generates QR codes in ANSI colors, Sixel or Unicode Block
Elements format for text terminals, e.g., console, xterm (with -ti 340
option to enable Sixel), mlterm, Windows command prompt and so on.

%prep
%setup -a1

%build

export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .gopath/src/import_path

export VERSION=%version
export COMMIT=%release
export BRANCH=altlinux
export GOFLAGS="-mod=vendor"

go install -ldflags "-X main.version=$VERSION -X main.commit=$COMMIT -X main.branch=$BRANCH" ./...

%install
export BUILDDIR="$PWD/.gopath"
export GOPATH="%go_path"

%golang_install
rm -rf -- %buildroot%_datadir

%files
%_bindir/*

%changelog
* Sun Aug 30 2026 Fr. Br. George <george@altlinux.org> 0.9.0-alt1
- Initial build for ALT
