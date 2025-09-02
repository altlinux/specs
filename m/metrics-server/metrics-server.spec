Name: metrics-server
Version: 0.8.0
Release: alt1

Summary:  Scalable and efficient source of container resource metrics for Kubernetes built-in autoscaling pipelines
Group: Development/Other
License: Apache-2.0
Url: https://github.com/kubernetes-sigs/metrics-server

Source0: %name-%version.tar
Source1: vendor.tar

Patch0: metrics-server-0.8.0-fix-makefile-to-use-vendor.patch

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Metrics Server collects resource metrics from Kubelets and exposes them
in Kubernetes apiserver through Metrics API for use by Horizontal Pod
Autoscaler and Vertical Pod Autoscaler. Metrics API can also be accessed
by kubectl top, making it easier to debug autoscaling pipelines.

%prep
%setup -a1
%autopatch -p1

%build
export GOROOT="%_libexecdir/golang"
make ARCH=$(go env GOARCH)

%install
install -Dm755 %name "%buildroot%_bindir/%name"

# unit tests don't work under i586
%ifnarch i586
%check
export GOROOT="%_libexecdir/golang"
make test-unit ARCH=$(go env GOARCH)
%endif

%files
%_bindir/*
%doc LICENSE README.md


%changelog
* Tue Aug 12 2025 Evgeniy Gorbanyov <esgor@altlinux.org> 0.8.0-alt1
- Initial build for Sisyphus.
