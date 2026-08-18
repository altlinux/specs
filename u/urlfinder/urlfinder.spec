%define _unpackaged_files_terminate_build 1
%define import_path github.com/projectdiscovery/urlfinder

%def_with check

Name: urlfinder
Version: 0.0.3
Release: alt1

Summary: High-speed passive URL discovery tool
License: MIT
Group: Networking/Other
Url: https://github.com/projectdiscovery/urlfinder
Vcs: https://github.com/projectdiscovery/urlfinder
ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: /proc

%description
URLFinder is a high-speed, passive URL discovery tool designed to
simplify and accelerate web asset discovery, ideal for penetration
testers, security researchers, and developers looking to gather URLs
without active scanning.

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
# consumed by golang-build as `go install -ldflags`
export LDFLAGS="-s -w"

%golang_prepare

cd .build/src/%import_path
%golang_build ./cmd/urlfinder

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%check
export GOPATH="$PWD/.build:%go_path"
export GOFLAGS="-mod=vendor"

cd .build/src/%import_path
go test ./...

%files
%doc README.md LICENSE.md
%_bindir/%name

%changelog
* Tue Jul 21 2026 Andrey Kuzma <kuzmaav@altlinux.org> 0.0.3-alt1
- Initial build for ALT Sisyphus.
