%define _unpackaged_files_terminate_build 1

%global import_path github.com/prometheus-operator/prometheus-operator

Name: prometheus-operator
Version: 0.89.0
Release: alt1

Summary: Prometheus Operator creates/configures/manages Prometheus clusters atop Kubernetes
License: Apache-2.0
Group: Development/Other
Url: https://prometheus-operator.dev
Vcs: https://github.com/prometheus-operator/prometheus-operator

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.25.0

%description
The Prometheus Operator provides Kubernetes native deployment and management
of Prometheus and related monitoring components. The purpose of this project
is to simplify and automate the configuration of a Prometheus based
monitoring stack for Kubernetes clusters.

%package -n prometheus-admission-webhook
Summary: admission-webhook component for prometheus operator
Group: Development/Other

%description -n prometheus-admission-webhook
%summary.

%package -n prometheus-config-reloader
Summary: config-reloader component for prometheus operator
Group: Development/Other

%description -n prometheus-config-reloader
%summary.

%prep
%setup -a 1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build ./cmd/operator ./cmd/admission-webhook ./cmd/prometheus-config-reloader

mv "$BUILDDIR/bin/operator" "$BUILDDIR/bin/prometheus-operator"
mv "$BUILDDIR/bin/admission-webhook" "$BUILDDIR/bin/prometheus-admission-webhook"

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc *.md
%_bindir/prometheus-operator

%files -n prometheus-admission-webhook
%_bindir/prometheus-admission-webhook

%files -n prometheus-config-reloader
%_bindir/prometheus-config-reloader

%changelog
* Fri Feb 20 2026 Alexander Stepchenko <geochip@altlinux.org> 0.89.0-alt1
- Initial build.
