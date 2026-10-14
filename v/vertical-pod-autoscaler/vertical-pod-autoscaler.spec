%define _unpackaged_files_terminate_build 1
%define import_path k8s.io/autoscaler/vertical-pod-autoscaler

Name: vertical-pod-autoscaler
Version: 1.5.1
Release: alt1

Group: Development/Other
Summary: Automatically adjust amount of resources by pods in cluster

License: Apache-2.0
Url: https://github.com/kubernetes/autoscaler

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.26.0

%description
A set of components that automatically adjust the amount of CPU and memory
requested by pods running in the Kubernetes Cluster.

%package -n vpa-admission-controller
Version: %version
Release: %release
Summary: vertical-pod-autoscaller controller
Group: Development/Other
ExclusiveArch: %go_arches

%description -n vpa-admission-controller
%summary

%package -n vpa-recommender
Version: %version
Release: %release
Summary: vertical-pod-autoscaller recommender
Group: Development/Other
ExclusiveArch: %go_arches

%description -n vpa-recommender
%summary

%package -n vpa-updater
Version: %version
Release: %release
Summary: vertical-pod-autoscaller updater
Group: Development/Other
ExclusiveArch: %go_arches

%description -n vpa-updater
%summary

%prep
%setup
%patch -p1

%build
pushd vertical-pod-autoscaler/
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare
%golang_build pkg/admission-controller/
%golang_build pkg/recommender/
%golang_build pkg/updater/
popd

%install
export GOPATH="%go_path"
export IGNORE_SOURCES=1

pushd vertical-pod-autoscaler/
export BUILDDIR="$PWD/.build"
install -m755 -d %buildroot%_bindir
install -p -m755 "$BUILDDIR/bin/admission-controller" %buildroot%_bindir/vpa-admission-controller
install -p -m755 "$BUILDDIR/bin/recommender" %buildroot%_bindir/vpa-recommender
install -p -m755 "$BUILDDIR/bin/updater" %buildroot%_bindir/vpa-updater
popd

%check
pushd vertical-pod-autoscaler
%gotest ./...
popd

%files
%doc vertical-pod-autoscaler/*.md vertical-pod-autoscaler/OWNERS

%files -n vpa-admission-controller
%_bindir/vpa-admission-controller

%files -n vpa-recommender
%_bindir/vpa-recommender

%files -n vpa-updater
%_bindir/vpa-updater

%changelog
* Wed Sep 23 2026 Nikita Stavtsev <nst@altlinux.org> 1.5.1-alt1
- Initial build
