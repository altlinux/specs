%define _unpackaged_files_terminate_build 1
%define import_path github.com/openbao/openbao

Name: openbao
Version: 2.4.4
Release: alt1

Summary: Secure secrets and encryption management system
License: MPL-2.0
Group: Development/Other
Url: https://openbao.org/
Vcs: https://github.com/openbao/openbao

Source0: %name-%version.tar
Source1: vendor.tar
Source2: web-ui-assets.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-build-golang

%description
OpenBao is an open-source secrets management platform designed to securely
store, manage, and distribute sensitive data such as API keys, certificates,
and credentials. It provides centralized control over secrets with encryption,
dynamic secret generation, and detailed audit logging.

%prep
%setup -a1 -a2

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export BUILD_TAGS="openbao ui"

export TAGS="${BUILD_TAGS}"
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
* Mon Dec 29 2025 Maxim Tulskiy <tulskijms@altlinux.org> 2.4.4-alt1
- Updated to new version v2.4.4.
- Support building package with bundled web ui (Closes: #56797).

* Sun Jun 08 2025 Maxim Tulskiy <tulskijms@altlinux.org> 2.2.2-alt1
- Initial build for ALT Sisyphus.
