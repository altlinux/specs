%define _unpackaged_files_terminate_build 1
%define import_path github.com/ahmetb/kubectx

Name: kubectx
Version: 0.11.0
Release: alt1

Summary: Fast utilities to switch kubectl contexts and namespaces
License: Apache-2.0
Group: Development/Other
Url: https://github.com/ahmetb/kubectx
Vcs: https://github.com/ahmetb/kubectx

Source0: %name-%version.tar
Source1: vendor.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
kubectx is a tool to switch between contexts (clusters) on kubectl faster.

%package -n kubens
Summary: A tool to switch between Kubernetes namespaces
Group: Development/Other

%description -n kubens
kubens is a tool to switch between Kubernetes namespaces (and configure
them for kubectl) easily.

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-X main.version=%version"

%golang_prepare
cd .build/src/%import_path
%golang_build ./cmd/kubectx
%golang_build ./cmd/kubens

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc LICENSE README.md
%_bindir/kubectx

%files -n kubens
%doc LICENSE README.md
%_bindir/kubens

%changelog
* Wed Apr 08 2026 Maxim Tulskiy <tulskijms@altlinux.org> 0.11.0-alt1
- Updated to new version v0.11.0.

* Wed Mar 25 2026 Maxim Tulskiy <tulskijms@altlinux.org> 0.10.2-alt1
- Updated to new version v0.10.2.

* Mon Aug 18 2025 Maxim Tulskiy <tulskijms@altlinux.org> 0.9.5-alt1
- Initial build for ALT Sisyphus.

