%global import_path github.com/VictoriaMetrics/operator

%global _unpackaged_files_terminate_build 1

Name:    victoriametrics-operator
Version: 0.68.3
Release: alt1
Summary: Kubernetes operator for Victoria Metrics
License: Apache-2.0
Group:   Other
Url:     https://github.com/VictoriaMetrics/operator

Source: %name-%version.tar

ExclusiveArch: x86_64 aarch64
BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Operator serves to make running VictoriaMetrics applications
on top of Kubernetes as easy as possible while preserving
Kubernetes-native configuration options.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export CGO_ENABLED=0

VERSION_STR="operator-%version"
LDFLAGS="-X github.com/VictoriaMetrics/VictoriaMetrics/lib/buildinfo.Version=${VERSION_STR}"

%golang_prepare
pushd $BUILDDIR/src/%import_path
%gobuild -o vmoperator --ldflags "$LDFLAGS" ./cmd
popd

%install
export BUILDDIR="$PWD/.build"
install -Dm755 $BUILDDIR/src/%import_path/vmoperator %buildroot%_bindir/vmoperator

%files
%doc *.md
%_bindir/vmoperator

%changelog
* Wed Mar 25 2026 Aleksandr Gamzin <gamzin@altlinux.org> 0.68.3-alt1
- Initial build for Sisyphus
