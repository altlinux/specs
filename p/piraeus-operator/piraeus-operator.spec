%global import_path github.com/piraeusdatastore/piraeus-operator/v2
%global _unpackaged_files_terminate_build 1

Name:    piraeus-operator
Version: 2.10.3
Release: alt1

Summary: The Piraeus Operator manages LINSTOR clusters in Kubernetes
License: Apache-2.0
Group:   Other
URL:     https://piraeus.io

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.24
BuildRequires: /proc

%description
Piraeus is a cloud-native storage system that empowers Kubernetes Local
Persistent Volumes with dynamic provisioning, resource management,
and high-availability. It deploys and scales out automatically within
Kubernetes nodes. With Piraeus, Kubernetes workloads can now consume high
performance local storage using the same volume APIs that app developers
have become accustomed to.

%prep
%setup

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

LDFLAGS="-X %import_path/pkg/vars.Version=%version"

%golang_prepare

cd .gopath/src/%import_path

go build \
  -ldflags "$LDFLAGS" \
  -o manager ./cmd

go build \
  -ldflags "$LDFLAGS" \
  -o gencert ./cmd/gencert

%install
export BUILDDIR="$PWD/.gopath"
export IGNORE_SOURCES=1
mkdir -p %buildroot%_bindir
install -D -m755 $BUILDDIR/src/%import_path/manager %buildroot%_bindir
install -D -m755 $BUILDDIR/src/%import_path/gencert %buildroot%_bindir

%files
%doc *.md
%_bindir/*

%changelog
* Mon Dec 15 2025 Aleksandr Gamzin <gamzin@altlinux.org> 2.10.3-alt1
- Initial build for sisyphus.
