%global import_path github.com/cozystack/cozy-proxy
%define _unpackaged_files_terminate_build 1

Name:    cozy-proxy
Version: 0.4.0
Release: alt1

Summary: A simple kube-proxy addon for 1:1 NAT services in Kubernetes using an NFT backend
License: Apache-2.0
Group:   Other
Url:     https://github.com/cozystack/cozy-proxy

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang >= 1.26.4

%description
%summary.

%prep
%setup -a 1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-trimpath"
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
%doc LICENSE README.md
%_bindir/%name

%changelog
* Fri Oct 16 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.4.0-alt1
- New version 0.4.0.
- Set CGO_ENABLED=0.

* Tue Jun 02 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.3.0-alt1
- Initial build for ALT.

