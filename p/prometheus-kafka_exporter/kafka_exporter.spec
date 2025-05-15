%global import_path github.com/kafka_exporter
%define mod kafka_exporter

Name:    prometheus-kafka_exporter
Version: 1.9.0
Release: alt1

Summary: Kafka exporter for Prometheus
License: Apache-2.0
Group:   Other
Url:     https://github.com/danielqsj/kafka_exporter

Source: %mod-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Kafka exporter for Prometheus. For other metrics from Kafka, have a look at the
JMX exporter.

%prep
%setup -n %mod-%version
tar xf %SOURCE1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc *.md
%_bindir/*

%changelog
* Thu May 15 2025 Andrey Cherepanov <cas@altlinux.org> 1.9.0-alt1
- Initial build for Sisyphus.
