%global import_path github.com/aquasecurity/trivy-operator

Name:    trivy-operator
Version: 0.30.1
Release: alt1

Summary: Kubernetes-native security toolkit
License: Apache-2.0
Group:   Security/Networking
Url:     https://aquasecurity.github.io/trivy-operator

Source0: %name-%version.tar
Source1: vendor.tar
Source2: go.mod

BuildRequires(pre): rpm-build-golang
BuildRequires: golang
BuildRequires: /proc

%description
%summary.

%prep
%setup -a1
cp %{SOURCE2} ./go.mod

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOEXPERIMENT=jsonv2

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
* Wed Apr 22 2026 Aleksandr Gamzin <gamzin@altlinux.org> 0.30.1-alt1
- 0.30.1 (Fixes: #58074)
- Change trivy and trivy-db modules source to altlinux.space.

* Tue Jan 13 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.29.0-alt1
- Initial build for Sisyphus (Closes #51287).
