%define _unpackaged_files_terminate_build 1
%define import_path github.com/controlplaneio/kubesec

Name: kubesec
Version: 2.14.2
Release: alt1

Summary: Security risk analysis for Kubernetes resources
License: Apache-2.0
Group: Development/Other
Url: https://kubesec.io
Vcs: https://github.com/controlplaneio/kubesec

Source0: %name-%version.tar
Source1: vendor.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
Kubesec is a security risk analysis tool for Kubernetes resources.
It inspects Kubernetes manifests and assigns a score based on security
best practices, helping detect risky configurations before they are applied.

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare
cd .build/src/%import_path/
%golang_build .

%install
ln -sf %_licensedir/Apache-2.0 LICENSE
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%_bindir/kubesec
%doc --no-dereference LICENSE 
%doc README.md 

%changelog
* Tue Aug 27 2025 Maxim Tulskiy <tulskijms@altlinux.org> 2.14.2-alt1
- Initial build for ALT Sisyphus.
