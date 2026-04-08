%global _unpackaged_files_terminate_build 1
%global import_path github.com/kubernetes-csi/livenessprobe

Name:    livenessprobe
Version: 2.18.0
Release: alt1

Summary: A sidecar container that can be included in a CSI plugin pod to enable integration with Kubernetes Liveness Probe
License: Apache-2.0
Group:   Other
Url:     https://github.com/kubernetes-csi/livenessprobe

Source: %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
The liveness probe is a sidecar container that exposes an HTTP /healthz endpoint,
which serves as kubelet's livenessProbe hook to monitor health of a CSI driver.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build cmd/%name

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%check
%ifarch %ix86
%gotest ./cmd/...
%else
%gotest ./cmd/... -race
%endif

%files
%doc README.md LICENSE
%_bindir/%name

%changelog
* Tue Mar 24 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 2.18.0-alt1
- Initial build for ALT.
