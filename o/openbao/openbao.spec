%define _unpackaged_files_terminate_build 1
%define import_path github.com/openbao/openbao

Name: openbao
Version: 2.2.2
Release: alt1

Summary: Secure secrets and encryption management system
License: MPL-2.0
Group: Development/Other
Url: https://openbao.org/
Vcs: https://github.com/openbao/openbao

Source0: %name-%version.tar
Source1: vendor.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-build-golang

%description
OpenBao is an open-source secrets management platform designed to securely
store, manage, and distribute sensitive data such as API keys, certificates,
and credentials. It provides centralized control over secrets with encryption,
dynamic secret generation, and detailed audit logging.

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
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
install -Dm755 $BUILDDIR/bin/openbao "%buildroot%_bindir/bao"

%files
%_bindir/bao
%doc LICENSE README.md

%changelog
* Sun Jun 08 2025 Maxim Tulskiy <tulskijms@altlinux.org> 2.2.2-alt1
- Initial build for ALT Sisyphus.
