%define prog_name source-controller
%global import_path github.com/fluxcd/%prog_name

Name:       flux2-%prog_name
Version:    1.8.0
Release:    alt1
Summary:    Flux source controller for GitOps artifacts acquisition
Group:      System/Configuration/Other
License:    Apache-2.0
Url:        https://github.com/fluxcd/source-controller

Source0:    %name-%version.tar
Source1:    vendor.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-build-golang
BuildRequires(pre): golang >= 1.26
BuildRequires: /proc

%description
The source-controller is a Kubernetes operator, specialised in artifacts
acquisition from external sources such as Git, OCI,
Helm repositories and S3-compatible buckets.
The source-controller implements the source.toolkit.fluxcd.io API and
is a core component of the GitOps toolkit.

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
# Skip packages that cannot run in hasher:
# - internal/controller needs envtest (kube-apiserver and etcd binaries)
# - internal/bucket/minio starts a MinIO container through docker
# TestRepoUrlWithDigest resolves tags against ghcr.io
%gotest -tags "netgo,osusergo" -skip "^TestRepoUrlWithDigest$" \
    $(go list -tags "netgo,osusergo" ./... | grep -vE '/internal/(controller|bucket/minio)$')

%files
%_bindir/%prog_name
%doc README.md CHANGELOG.md LICENSE
%doc docs/spec/v1

%changelog
* Wed Oct 14 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 1.8.0-alt1
- New version 1.8.0.
- Set CGO_ENABLED=0.
- Enable tests.

* Wed Feb 18 2026 Aleksandr Gamzin <gamzin@altlinux.org> 1.7.4-alt1
- 1.7.4.

* Thu Oct 31 2024 Alexey Kostarev <kaf@altlinux.org> 1.3.0-alt1
- Initial build.
