%define prog_name kustomize-controller
%global import_path github.com/fluxcd/%prog_name

Name:       flux2-%prog_name
Version:    1.8.0
Release:    alt1
Summary:    Flux controller for continuous delivery of Kustomize and plain manifests
Group:      System/Configuration/Other
License:    Apache-2.0
Url:        https://github.com/fluxcd/kustomize-controller

Source0:    %name-%version.tar
Source1:    vendor.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-build-golang
BuildRequires(pre): golang >= 1.26
BuildRequires: /proc
# tests deps
BuildRequires: gnupg2

%description
The kustomize-controller is a Flux component, specialized in running continuous
delivery pipelines for infrastructure and workloads defined with Kubernetes
manifests and assembled with Kustomize.

%prep
%setup -a 1

%build
export CGO_ENABLED=0
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare
export TAGS="netgo,osusergo"
LDFLAGS="-w" %golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%check
export CGO_ENABLED=0
export SOPS_GPG_EXEC=gpg2
# Skip internal/controller: it needs envtest (kube-apiserver and etcd binaries)
%gotest -tags "netgo,osusergo" \
    $(go list -tags "netgo,osusergo" ./... | grep -vE '/internal/controller$')

%files
%_bindir/%prog_name
%doc README.md CHANGELOG.md LICENSE
%doc docs/spec/v1

%changelog
* Wed Oct 14 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 1.8.0-alt1
- New version 1.8.0.
- Set CGO_ENABLED=0.
- Enable tests.
- Fix import_path.

* Wed Feb 18 2026 Aleksandr Gamzin <gamzin@altlinux.org> 1.7.3-alt1
- 1.7.3.

* Sat Nov 02 2024 Alexey Kostarev <kaf@altlinux.org> 1.3.0-alt1
- Initial build.
