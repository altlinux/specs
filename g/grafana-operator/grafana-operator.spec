%global _unpackaged_files_terminate_build 1
%global import_path github.com/grafana/grafana-operator/v5

Name:    grafana-operator
Version: 5.13.0
Release: alt1

Summary: Kubernetes operator for Grafana instances, dashboards and datasources
License: Apache-2.0
Group:   Other
Url:     https://github.com/grafana/grafana-operator

Source0: %name-%version.tar
Source1: vendor.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-build-golang

%description
The Grafana operator installs and manages Grafana instances, dashboards,
datasources, folders and alert resources through Kubernetes/OpenShift
custom resources.

%prep
%setup -a 1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export CGO_ENABLED=0

%golang_prepare
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%check
# Skip tests which cannot run in the build environment:
# - TestAPIs (controllers, controllers/fetchers) start envtest (kube-apiserver and etcd)
# - TestFetchDashboardFromGrafanaCom downloads a dashboard from grafana.com
# controllers/ contains only the envtest suite, so it is not tested at all
%gotest -skip '^(TestAPIs|TestFetchDashboardFromGrafanaCom)$' \
    ./api/... ./controllers/autodetect/... ./controllers/fetchers/... \
    ./controllers/reconcilers/...

%files
%doc README.md LICENSE
%_bindir/%name

%changelog
* Fri Oct 09 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 5.13.0-alt1
- Initial build for ALT.
