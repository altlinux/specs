%define _unpackaged_files_terminate_build 1

%global import_path github.com/kubernetes/kube-state-metrics

Name: kube-state-metrics
Version: 2.15.0
Release: alt1

Summary: Generate metrics about the state of Kubernetes objects
License: Apache-2.0
Group: Development/Other
Url: https://kubernetes.io/docs/concepts/cluster-administration/kube-state-metrics/
Vcs: https://github.com/kubernetes/kube-state-metrics

ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
kube-state-metrics (KSM) is a simple service that listens to the Kubernetes
API server and generates metrics about the state of the objects.
It is not focused on the health of the individual Kubernetes components,
but rather on the health of the various objects inside, such as deployments,
nodes and pods.

%prep
%setup -a1

%build
export GOROOT="%_libexecdir/golang"
%gobuild -mod=vendor

%install
install -Dpm755 %name %buildroot%_bindir/%name

%files
%doc LICENSE OWNERS *.md docs
%_bindir/kube-state-metrics

%changelog
* Thu Jul 24 2025 Denis Rastyogin <gerben@altlinux.org> 2.15.0-alt1
- Initial build for Sisyphus.
