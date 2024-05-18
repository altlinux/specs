%global import_path github.com/cert-manager/cert-manager

%global _unpackaged_files_terminate_build 1

Name: cert-manager
Version: 1.14.5
Release: alt1
Summary: Automatically provision and manage TLS certificates in Kubernetes
License: Apache-2.0
Group: Other
Url: https://cert-manager.io
Vcs: https://github.com/cert-manager/cert-manager

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
# Vendorized go modules.
# Also need to vendorize for every go module in cmd/
# $ go mod vendor
# $ for d in $(ls cmd); do pushd cmd/$d; go mod vendor; popd; done

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-trimpath -mod=vendor"
export CGO_ENABLED=0
export LDFLAGS="-X github.com/cert-manager/cert-manager/pkg/util.AppVersion=%version \
                -X github.com/cert-manager/cert-manager/pkg/util.AppGitCommit=%release"

%golang_prepare
%golang_build cmd/controller
%golang_build cmd/acmesolver
%golang_build cmd/webhook
%golang_build cmd/cainjector
%golang_build cmd/startupapicheck

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

mv %buildroot%_bindir/controller-binary %buildroot%_bindir/controller
mv %buildroot%_bindir/cainjector-binary %buildroot%_bindir/cainjector
mv %buildroot%_bindir/webhook-binary %buildroot%_bindir/webhook
mv %buildroot%_bindir/acmesolver-binary %buildroot%_bindir/acmesolver
mv %buildroot%_bindir/startupapicheck-binary %buildroot%_bindir/startupapicheck

# cleanup
rm -rf -- %buildroot%_datadir

%files
%_bindir/controller
%_bindir/cainjector
%_bindir/webhook
%_bindir/acmesolver
%_bindir/startupapicheck
%_bindir/cmctl
%_bindir/kubectl-cert_manager

%changelog
* Sat May 18 2024 Alexander Stepchenko <geochip@altlinux.org> 1.14.5-alt1
- 1.11.0 -> 1.14.5 (Fixes: CVE-2024-26147)
- Add startupapicheck binary.

* Wed Jan 11 2023 Alexey Shabalin <shaba@altlinux.org> 1.11.0-alt1
- new version 1.11.0

* Wed Sep 28 2022 Alexey Shabalin <shaba@altlinux.org> 1.9.1-alt1
- Initial build for Sisyphus

