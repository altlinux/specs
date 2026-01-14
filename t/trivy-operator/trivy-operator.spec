%global import_path github.com/aquasecurity/trivy-operator

Name:    trivy-operator
Version: 0.29.0
Release: alt1

Summary: Kubernetes-native security toolkit
License: Apache-2.0
Group:   Security/Networking
Url:     https://aquasecurity.github.io/trivy-operator

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang
BuildRequires: /proc

%description
%summary.

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build ./cmd/%name

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc *.md
%_bindir/%name

%changelog
* Tue Jan 13 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.29.0-alt1
- Initial build for Sisyphus (Closes #51287).
