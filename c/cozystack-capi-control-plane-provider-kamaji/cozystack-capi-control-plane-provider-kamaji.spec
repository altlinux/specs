%global import_path github.com/clastix/cluster-api-control-plane-provider-kamaji
%define _unpackaged_files_terminate_build 1

%define bname cluster-api-control-plane-provider-kamaji

Name:    cozystack-capi-control-plane-provider-kamaji
Version: 0.19.0
Release: alt1

Summary: Cozystack-customized Kamaji Control Plane provider implementation of the Cluster Management API
License: Apache-2.0
Group:   Other
Url:     https://kamaji.clastix.io
Vcs:     https://github.com/clastix/cluster-api-control-plane-provider-kamaji.git

Conflicts: capi-control-plane-provider-kamaji

Source: %name-%version.tar
Source1: vendor.tar
Patch0:  0001-backport-additional-service-ports-pr347.diff

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
%summary.

%prep
%setup -a 1
%patch0 -p1

%build
export CGO_ENABLED=0
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-w -s"
export GOFLAGS="-trimpath"

%golang_prepare

%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%check
%gotest ./...

%files
%doc README.md LICENSE
%_bindir/%bname

%changelog
* Fri Jul 17 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.19.0-alt1
- Initial build for ALT.


