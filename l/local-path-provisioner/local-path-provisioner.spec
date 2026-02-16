%define _unpackaged_files_terminate_build 1

%global import_path github.com/rancher/local-path-provisioner

Name: local-path-provisioner
Version: 0.0.34
Release: alt1

Summary: Dynamically provisioning persistent local storage with Kubernetes
License: Apache-2.0
Group: System/Configuration/Other
Url: https://github.com/rancher/local-path-provisioner
Vcs: https://github.com/rancher/local-path-provisioner

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.25.5

%description
Local Path Provisioner provides a way for the Kubernetes users to utilize
the local storage in each node. Based on the user configuration,
the Local Path Provisioner will create either hostPath or local based
persistent volume on the node automatically. It utilizes the features
introduced by Kubernetes Local Persistent Volume feature, but makes it
a simpler solution than the built-in local volume feature in Kubernetes.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

export LDFLAGS='-X main.VERSION=v%version'

%golang_prepare

cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc *.md
%_bindir/local-path-provisioner

%changelog
* Sun Feb 15 2026 Alexander Stepchenko <geochip@altlinux.org> 0.0.34-alt1
- Initial build.
