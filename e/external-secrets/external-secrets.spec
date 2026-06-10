%define _unpackaged_files_terminate_build 1
%define import_path github.com/external-secrets/external-secrets/

Name: external-secrets
Version: 2.4.1
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
* Wed Apr 29 2026 Maxim Tulskiy <tulskijms@altlinux.org> 2.4.1-alt1
- Updated to new version 2.4.1.

* Wed Apr 15 2026 Maxim Tulskiy <tulskijms@altlinux.org> 2.3.0-alt1
- Updated to new version 2.3.0.

* Thu Feb 26 2026 Maxim Tulskiy <tulskijms@altlinux.org> 2.0.1-alt1
- Updated to new version v2.0.1.

* Thu Feb 19 2026 Maxim Tulskiy <tulskijms@altlinux.org> 2.0.0-alt1
- Updated to new version v2.0.0.

* Tue Jan 27 2026 Maxim Tulskiy <tulskijms@altlinux.org> 1.3.1-alt1
- Updated to new version v1.3.1.

* Tue Jul 22 2025 Maxim Tulskiy <tulskijms@altlinux.org> 0.18.2-alt1
- Initial build for ALT Sisyphus.
