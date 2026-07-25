%global import_path github.com/altinity/clickhouse-operator
%define _unpackaged_files_terminate_build 1

Name:    clickhouse-operator
Version: 0.27.1
Release: alt1

Summary: The Altinity Kubernetes Operator for ClickHouse
License: Apache-2.0
Group:   Other
Url:     https://altinity.com/kubernetes-operator
Vcs:     https://github.com/Altinity/clickhouse-operator.git

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
The Altinity Kubernetes Operator for ClickHouse creates, configures and manages ClickHouse clusters running on Kubernetes.

%package -n clickhouse-metrics-exporter
Summary: Metrics exporter for ClickHouse Operator
Group:   Other

%description -n clickhouse-metrics-exporter
%summary.

%prep
%setup -a 1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-w -s"
export GOFLAGS="-trimpath"
export GO111MODULE=on

%golang_prepare

%golang_build ./cmd/*

%install
mkdir -p %buildroot%_sysconfdir/%name
cp -pr config/. %buildroot%_sysconfdir/%name

export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

install -Dm755 $BUILDDIR/bin/operator %buildroot/usr/bin/clickhouse-operator
rm $BUILDDIR/bin/operator
install -Dm755 $BUILDDIR/bin/metrics_exporter %buildroot/usr/bin/clickhouse-metrics-exporter
rm $BUILDDIR/bin/metrics_exporter

%golang_install

%check
%gotest -vet=off ./...

%files -n clickhouse-metrics-exporter
%_bindir/clickhouse-metrics-exporter

%files
%doc LICENSE README.md
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name
%_bindir/%name

%changelog
* Wed Jul 15 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.27.1-alt1
- Initial build for ALT.


