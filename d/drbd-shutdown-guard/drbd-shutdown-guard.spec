%global import_path github.com/piraeusdatastore/drbd-shutdown-guard
%define _unpackaged_files_terminate_build 1

Name:    drbd-shutdown-guard
Version: 1.1.1
Release: alt1

Summary: Aid Kubernetes cluster using DRBD with suspend-io behaviour during shutdown
License: Apache-2.0
Group:   Other
Url:     https://github.com/piraeusdatastore/drbd-shutdown-guard

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang >= 1.24.0

%description
%summary.

%prep
%setup -a 1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-trimpath"
export LDFLAGS="-X %import_path/pkg/vars.Version=%version"
export CGO_ENABLED=0

%golang_prepare

%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%check
export CGO_ENABLED=0
%gotest ./...

%files
%doc README.md
%_bindir/%name

%changelog
* Wed Oct 21 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 1.1.1-alt1
- Initial build for ALT.
