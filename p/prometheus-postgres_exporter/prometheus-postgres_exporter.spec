%global import_path github.com/prometheus-community/prometheus-postgres_exporter
Name:    prometheus-postgres_exporter
Version: 0.20.0
Release: alt1

Summary: A PostgreSQL metric exporter for Prometheus
License: Apache-2.0
Group:   Other
Url:     https://github.com/prometheus-community/postgres_exporter

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Source1: vendor.tar

Source2: postgres_exporter.yml
Source3: %name.sysconfig
Source4: %name.service

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang

Requires(pre): prometheus-common

%description
%summary.

%prep
%setup
tar xf %SOURCE1

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"
%golang_prepare
#promu build
export BUILDTAGS="netgo"
export LDFLAGS="-X github.com/prometheus/common/version.Version=%version \
         -X github.com/prometheus/common/version.Revision=%release \
         -X github.com/prometheus/common/version.Branch=tarball \
         -X github.com/prometheus/common/version.BuildDate=$(date -u +%%Y%%m%%d)"

%golang_build cmd/postgres_exporter

%install
export BUILDDIR="$PWD/.gopath"
#export GOPATH="%go_path"
export IGNORE_SOURCES=1

%golang_install

mkdir -p %buildroot{%_bindir,%_initdir,%_unitdir,%_sysconfdir/{sysconfig,prometheus}}
install -m0644 %SOURCE2 %buildroot%_sysconfdir/prometheus/postgres_exporter.yml
install -m0644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/%name
install -m0644 %SOURCE4 %buildroot%_unitdir/%name.service
mkdir -p %buildroot%_sharedstatedir/prometheus/postgres-exporter

%post
%post_service %name

%preun
%preun_service %name

%files
%doc README.md
%_bindir/postgres_exporter
%_unitdir/%name.*
%config(noreplace) %_sysconfdir/sysconfig/%name
%config(noreplace) %_sysconfdir/prometheus/postgres_exporter.yml
%dir %attr(0775,root,prometheus) %_sharedstatedir/prometheus/postgres-exporter

%changelog
* Mon Jun 29 2026 Andrey Cherepanov <cas@altlinux.org> 0.20.0-alt1
- New version.

* Thu Feb 26 2026 Andrey Cherepanov <cas@altlinux.org> 0.19.1-alt1
- New version.

* Fri Feb 06 2026 Andrey Cherepanov <cas@altlinux.org> 0.19.0-alt1
- New version.

* Mon Sep 29 2025 Andrey Cherepanov <cas@altlinux.org> 0.18.1-alt1
- New version.

* Fri Sep 26 2025 Andrey Cherepanov <cas@altlinux.org> 0.18.0-alt1
- New version.

* Sun Aug 24 2025 Andrey Cherepanov <cas@altlinux.org> 0.17.1-alt3
- Removed socket file, fixed service file.

* Thu Apr 17 2025 Alexey Shabalin <shaba@altlinux.org> 0.17.1-alt2
- Add default configs and systemd units.

* Thu Feb 27 2025 Andrey Cherepanov <cas@altlinux.org> 0.17.1-alt1
- New version.

* Sun Feb 23 2025 Andrey Cherepanov <cas@altlinux.org> 0.17.0-alt1
- New version.

* Mon Nov 11 2024 Andrey Cherepanov <cas@altlinux.org> 0.16.0-alt1
- New version.

* Tue Sep 24 2024 Andrey Cherepanov <cas@altlinux.org> 0.15.0-alt1
- Initial build for Sisyphus.
