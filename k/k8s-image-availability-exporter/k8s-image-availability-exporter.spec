%global import_path github.com/flant/k8s-image-availability-exporter
%global _unpackaged_files_terminate_build 1

Name:    k8s-image-availability-exporter
Version: 0.15.0
Release: alt1

Summary: Application for monitoring the cluster workloads image presence in a container registry
License: Apache-2.0
Group:   Security/Networking
Url:     https://%import_path

Source: %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang
BuildRequires: /proc

%description
k8s-image-availability-exporter (or k8s-iae for short) is a Prometheus exporter
that warns you proactively about images that are defined in Kubernetes objects
(e.g., an image field in the Deployment) but are not available in the container
registry (such as Docker Registry, etc.).

%prep
%setup

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

LDFLAGS="-s -w -X %import_path/pkg/version.Version=v%version"

%golang_prepare

pushd $BUILDDIR/src/%import_path

%gobuild --ldflags "$LDFLAGS" -o %name .

%install
export BUILDDIR="$PWD/.gopath"
install -Dm755 $BUILDDIR/src/%import_path/%name %buildroot%_bindir/%name

%files
%doc *.md
%_bindir/%name

%changelog
* Tue Jun 09 2026 Aleksandr Gamzin <gamzin@altlinux.org> 0.15.0-alt1
- Initial build for Sisyphus.
