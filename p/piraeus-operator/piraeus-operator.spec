%global _unpackaged_files_terminate_build 1
%global import_path github.com/piraeusdatastore/piraeus-operator/v2

Name:    piraeus-operator
Version: 2.10.3
Release: alt2

Summary: The Piraeus Operator manages LINSTOR clusters in Kubernetes
License: Apache-2.0
Group:   Other
URL:     https://piraeus.io
Vcs:     https://github.com/piraeusdatastore/piraeus-operator

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang >= 1.24
BuildRequires: /proc

%description
Piraeus is a cloud-native storage system that empowers Kubernetes Local
Persistent Volumes with dynamic provisioning, resource management,
and high-availability. It deploys and scales out automatically within
Kubernetes nodes. With Piraeus, Kubernetes workloads can now consume high
performance local storage using the same volume APIs that app developers
have become accustomed to.

%prep
%setup -a 1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-trimpath"
export LDFLAGS="-X %import_path/pkg/vars.Version=%version -buildid="

%golang_prepare
%golang_build ./cmd ./cmd/gencert

_BBDIR="$BUILDDIR"/bin
mv "$_BBDIR"/cmd      "$_BBDIR"/%name
mv "$_BBDIR"/gencert  "$_BBDIR"/piraeus-gencert 

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%check
# skip envtest
%gotest -v $(go list ./... | grep -Ev '^%import_path/(internal/(controller|webhook/v1)|pkg/k8sgc)$')

%files
%doc LICENSE README.md
%_bindir/%name
%_bindir/piraeus-gencert

%changelog
* Thu Sep 03 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 2.10.3-alt2
- Refactor spec file.
- Use another binaries naming.
- Enable tests.

* Mon Dec 15 2025 Aleksandr Gamzin <gamzin@altlinux.org> 2.10.3-alt1
- Initial build for sisyphus.
