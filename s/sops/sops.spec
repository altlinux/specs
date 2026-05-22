%define _unpackaged_files_terminate_build 1
%global import_path github.com/getsops/sops/v3

Name: sops
Version: 3.13.1
Release: alt1

Group: Security/Networking
Summary: Simple And Flexible Tool For Managing Secrets
License: MPL-2.0 AND BSD-3-Clause AND Apache-2.0
Url: https://getsops.io
Vcs: https://github.com/getsops/sops.git
Source0: %name-%version.tar
Source1: vendor-%version.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.25.0

%description
SOPS is an editor of encrypted files that supports YAML, JSON, ENV, INI and
BINARY formats and encrypts with AWS KMS, GCP KMS, Azure Key Vault,
HuaweiCloud KMS, age, and PGP.

%prep
%setup -a 1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
export LDFLAGS="-X %import_path/version.Version=%version"
%golang_build ./cmd/sops

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

mkdir -p %buildroot%_datadir/bash-completion/completions
%buildroot%_bindir/%name completion bash > %buildroot%_datadir/bash-completion/completions/%name
mkdir -p %buildroot%_datadir/zsh/site-functions
%buildroot%_bindir/%name completion zsh > %buildroot%_datadir/zsh/site-functions/_%name

%files
%doc README.rst CHANGELOG.md CHANGELOG.rst CODE_OF_CONDUCT.md CONTRIBUTING.md
%doc shamir/README.md DCO
%_bindir/*
%_datadir/bash-completion/completions/%name
%_datadir/zsh/site-functions/_%name

%changelog
* Fri May 22 2026 Artyom Sinyugin <writers@altlinux.org> 3.13.1-alt1
- New version 3.13.1.

* Thu Mar 18 2026 Artyom Sinyugin <writers@altlinux.org> 3.12.1-alt1
- Initial build 3.12.1.
