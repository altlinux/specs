%define _unpackaged_files_terminate_build 1
%define import_path github.com/kpetremann/salt-exporter

Name: salt-exporter
Version: 0.13.0
Release: alt1

Summary: Prometheus exporter for Salt events
License: MIT
Group: Monitoring
Url: https://github.com/kpetremann/salt-exporter

Source0: %name-%version.tar
Source1: vendor.tar
Source2: salt-exporter.service
Source3: config.yml

BuildRequires(pre): rpm-build-golang
BuildRequires: golang >= 1.26.0

%description
Salt Exporter is a Prometheus exporter for Salt events.
It passively listens to the Salt Master event bus and exposes
metrics about Salt jobs, responses and minion health.

%prep
%setup -q -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOFLAGS="-mod=vendor"
export GOPATH="$BUILDDIR"
export CGO_ENABLED=0

%golang_prepare

pushd .build/src/%import_path
%golang_build ./cmd/salt-exporter
popd

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

install -Dpm0644 %SOURCE2 \
    %buildroot%_unitdir/salt-exporter.service

install -Dpm0644 %SOURCE3 \
    %buildroot%_sysconfdir/salt-exporter/config.yml

%files
%doc README.md LICENSE
%_bindir/salt-exporter
%_unitdir/salt-exporter.service
%dir %_sysconfdir/salt-exporter
%config(noreplace) %_sysconfdir/salt-exporter/config.yml

%changelog
* Thu Oct 08 2026 Olesya Shuster <lesyafox@altlinux.org> 0.13.0-alt1
- Initial build for ALT Linux Sisyphus.
