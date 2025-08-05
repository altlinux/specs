%define _unpackaged_files_terminate_build 1
%define import_path github.com/external-secrets/external-secrets/

Name: external-secrets
Version: 0.18.2
Release: alt1

Summary: Kubernetes operator for syncing external secrets into Kubernetes Secrets
License: Apache-2.0
Group: Development/Other
Url: https://external-secrets.io
Vcs: https://github.com/external-secrets/external-secrets

Source0: %name-%version.tar
Source1: vendor.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-build-golang

%description
External Secrets Operator is a Kubernetes operator that integrates external
secret management systems like AWS Secrets Manager, HashiCorp Vault, Google
Secrets Manager, Azure Key Vault, IBM Cloud Secrets Manager, Akeyless, CyberArk
Conjur, Pulumi ESC and many more. The operator reads information from external
APIs and automatically injects the values into a Kubernetes Secret.

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare
cd .build/src/%import_path
%golang_build .

%install
ln -sf %_licensedir/Apache-2.0 LICENSE
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%_bindir/external-secrets
%doc --no-dereference LICENSE 
%doc README.md 

%changelog
* Tue Jul 22 2025 Maxim Tulskiy <tulskijms@altlinux.org> 0.18.2-alt1
- Initial build for ALT Sisyphus.
