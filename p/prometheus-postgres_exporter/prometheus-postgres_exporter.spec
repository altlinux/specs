%global import_path github.com/prometheus-community/prometheus-postgres_exporter
Name:    prometheus-postgres_exporter
Version: 0.15.0
Release: alt1

Summary: A PostgreSQL metric exporter for Prometheus
License: Apache-2.0
Group:   Other
Url:     https://github.com/prometheus-community/postgres_exporter

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang
BuildRequires: promu

%description
%summary

%prep
%setup
tar xf %SOURCE1

%build
make common-build PROMU=/usr/bin/promu

%install
install -Dpm 0755 postgres_exporter %buildroot%_bindir/postgres_exporter

%files
%doc README.md
%_bindir/postgres_exporter

%changelog
* Tue Sep 24 2024 Andrey Cherepanov <cas@altlinux.org> 0.15.0-alt1
- Initial build for Sisyphus.
