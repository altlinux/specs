%define _unpackaged_files_terminate_build 1
%define import_path github.com/yannh/kubeconform

Name: kubeconform
Version: 0.8.0
Release: alt1

Summary: Kubernetes manifest validation tool
License: Apache-2.0
Group: Development/Other
Url: https://github.com/yannh/kubeconform
Vcs: https://github.com/yannh/kubeconform

Source0: %name-%version.tar
Source1: vendor.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
Kubeconform is a fast and lightweight Kubernetes manifest validation tool.
It validates configuration files against the official Kubernetes OpenAPI
schemas, supporting both built-in and custom resources (CRDs).

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare
cd .build/src/%import_path/cmd/kubeconform
%golang_build .

%install
ln -sf %_licensedir/Apache-2.0 LICENSE
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%files
%_bindir/kubeconform
%doc --no-dereference LICENSE 
%doc Readme.md 

%changelog
* Tue Jun 09 2026 Maxim Tulskiy <tulskijms@altlinux.org> 0.8.0-alt1
- Updated to new version 0.8.0.

* Tue Aug 26 2025 Maxim Tulskiy <tulskijms@altlinux.org> 0.7.0-alt1
- Initial build for ALT Sisyphus.

