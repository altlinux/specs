%global import_path github.com/json_exporter
%define mod json_exporter

Name:    prometheus-json_exporter
Version: 0.7.0
Release: alt1

Summary: A prometheus exporter which scrapes remote JSON by JSONPath
License: Apache-2.0
Group:   Other
Url:     https://github.com/prometheus-community/json_exporter

Source: %mod-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
A prometheus exporter which scrapes remote JSON by JSONPath.

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
* Thu May 15 2025 Andrey Cherepanov <cas@altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus.
