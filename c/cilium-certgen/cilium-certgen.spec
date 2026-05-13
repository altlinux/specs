%global import_path github.com/cilium/certgen
Name:    cilium-certgen
Version: 0.4.3
Release: alt1

Summary: A convenience tool to generate and store certificates for Hubble Relay mTLS
License: Apache-2.0
Group:   Other
URL:     https://github.com/cilium/certgen

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.26.0
BuildRequires: /proc

%description
%summary

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
export CGO_ENABLED=0
go build -o bin/%name main.go

%install
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
mkdir -p %buildroot%_bindir
install -m 0755 .build/src/%import_path/bin/%name %buildroot%_bindir/

%files
%doc *.md
%_bindir/%name

%changelog
* Thu Apr 30 2026 Aleksandr Gamzin <gamzin@altlinux.org> 0.4.3-alt1
- 0.4.3.

* Mon Oct 27 2025 Aleksandr Gamzin <gamzin@altlinux.org> 0.2.4-alt1
- Initial build for Sisyphus
