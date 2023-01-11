%global import_path github.com/cert-manager/cert-manager

%global _unpackaged_files_terminate_build 1

Name: cert-manager
Version: 1.11.0
Release: alt1
Summary: Automatically provision and manage TLS certificates in Kubernetes
License: Apache-2.0
Group: Other
Url: https://cert-manager.io

Source: %name-%version.tar
Patch: %name-%version-%release.patch

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
cert-manager adds certificates and certificate issuers as resource types
in Kubernetes clusters, and simplifies the process of obtaining,
renewing and using those certificates.

It can issue certificates from a variety of supported sources,
including Let's Encrypt, HashiCorp Vault, and Venafi as well as private PKI,
and it ensures certificates remain valid and up to date,
attempting to renew certificates at an appropriate time before expiry.

%prep
%setup
%patch -p1

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-trimpath -mod=vendor"
export CGO_ENABLED=0
export LDFLAGS=" -w -s \
                 -X github.com/cert-manager/cert-manager/pkg/util.AppVersion=%version \
                 -X github.com/cert-manager/cert-manager/pkg/util.AppGitCommit=%release"

%golang_prepare
%golang_build cmd/controller
%golang_build cmd/acmesolver
%golang_build cmd/webhook
%golang_build cmd/cainjector

LDFLAGS="$LDFLAGS \
                 -X github.com/cert-manager/cert-manager/cmd/ctl/pkg/build.name=cmctl \
                 -X github.com/cert-manager/cert-manager/cmd/ctl/pkg/build/commands.registerCompletion=true" \
%golang_build cmd/ctl
mv $BUILDDIR/bin/ctl $BUILDDIR/bin/cmctl

LDFLAGS="$LDFLAGS \
                 -X \"github.com/cert-manager/cert-manager/cmd/ctl/pkg/build.name=kubectl cert-manager\" \
                 -X github.com/cert-manager/cert-manager/cmd/ctl/pkg/build/commands.registerCompletion=false" \
%golang_build cmd/ctl
mv $BUILDDIR/bin/ctl $BUILDDIR/bin/kubectl-cert_manager

%install
export BUILDDIR="$PWD/.gopath"
export GOPATH="%go_path"
%golang_install
# cleanup
rm -rf -- %buildroot%_datadir

%files
%_bindir/*

%changelog
* Wed Jan 11 2023 Alexey Shabalin <shaba@altlinux.org> 1.11.0-alt1
- new version 1.11.0

* Wed Sep 28 2022 Alexey Shabalin <shaba@altlinux.org> 1.9.1-alt1
- Initial build for Sisyphus

