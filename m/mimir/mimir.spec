%global import_path github.com/grafana/mimir
%global _unpackaged_files_terminate_build 1

Name: mimir
Version: 2.15.2
Release: alt1

Summary: Grafana Mimir is an open source software project that provides a scalable long-term storage for Prometheus
License: AGPL-3.0-only
Group: Development/Other
Url: https://grafana.com/oss/mimir/
Vcs: https://github.com/grafana/mimir.git

Source: https://grafana.com/oss/mimir/archive/%name-%version/%name-%version.tar.gz
Patch: mimir-2.15.0-alt-systemd.patch

ExcludeArch: i586 armh
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: golang >= 1.23.0
BuildRequires: /proc

%description
Grafana Mimir provides horizontally scalable, highly available,
multi-tenant, long-term storage for Prometheus.

%package query-tee
Summary: Tool that you can use for testing purposes when comparing the query results and performance of two Grafana Mimir clusters
Group: Other

%description query-tee
The query-tee is a standalone tool that you can use for testing purposes when comparing the query results and performance of two Grafana Mimir clusters. The two Mimir clusters compared by the query-tee must ingest the same series and samples.

%package  -n mimirtool
Summary: Command-line tool that operators and tenants can use to execute a number of common tasks that involve Grafana Mimir or Grafana Cloud Metrics
Group: Other

%description -n mimirtool
Mimirtool is a command-line tool that operators and tenants can use to execute a number of common tasks that involve Grafana Mimir or Grafana Cloud Metrics.

%package -n mimir-continuous-test
Summary: Tool for run smoke tests on live Grafana Mimir clusters
Group: Other

%description -n mimir-continuous-test
Tool for run smoke tests on live Grafana Mimir clusters. This tool identifies a class of bugs that could be difficult to spot during development.

%package metaconvert
Summary: metaconvert
Group: Other

%description metaconvert
metaconvert.

%prep
%setup
%patch -p1

sed -i '/^ExecStart/ s|/usr/local/bin/|/usr/bin/|' packaging/nfpm/mimir/%name.service

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOFLAGS="-mod=vendor"

%golang_prepare

%golang_build ./cmd/query-tee
%golang_build ./cmd/mimirtool
%golang_build ./cmd/mimir-continuous-test
%golang_build ./cmd/mimir
%golang_build ./cmd/metaconvert

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

#install config files
install -Dm644 packaging/nfpm/%name/runtime_config.yml %buildroot%_sysconfdir/%name/runtime_config.yml
install -Dm644 packaging/nfpm/%name/config.yml %buildroot%_sysconfdir/%name/config.yml

#install servise files
install -Dm644 packaging/nfpm/%name/%name.service %buildroot%_unitdir/%name.service
install -Dm644 packaging/nfpm/%name/%name.env %buildroot%_sysconfdir/sysconfig/%name

install -dm770 %buildroot%_sharedstatedir/%name
install -dm770 %buildroot%_sharedstatedir/%name/data

%pre
groupadd -r -f %name > /dev/null 2>&1 ||:
useradd -r -g %name -d %_localstatedir/%name -s /sbin/nologin -c "Mimir services" %name > /dev/null 2>&1 ||:
usermod -a -G proc %name ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%doc README.md SECURITY.md CONTRIBUTING.md
%_bindir/mimir
%config(noreplace) %_sysconfdir/sysconfig/%name
%config(noreplace) %_sysconfdir/%name/*
%_unitdir/%name.service
%dir %attr(0770, %name, %name) %_sharedstatedir/%name
%dir %attr(0770, %name, %name) %_sharedstatedir/%name/data

%files query-tee
%doc README.md SECURITY.md CONTRIBUTING.md
%_bindir/query-tee

%files -n mimirtool
%doc README.md SECURITY.md CONTRIBUTING.md
%_bindir/mimirtool

%files -n mimir-continuous-test
%doc README.md SECURITY.md CONTRIBUTING.md
%_bindir/mimir-continuous-test

%files metaconvert
%doc README.md SECURITY.md CONTRIBUTING.md
%_bindir/metaconvert

%changelog
* Mon Apr 14 2025 Anton Meleshnikov <alton@altlinux.org> 2.15.2-alt1
- New version 2.15.2.

* Mon Mar 31 2025 Anton Meleshnikov <alton@altlinux.org> 2.15.1-alt1
- New version 2.15.1.

* Wed Feb 19 2025 Anton Meleshnikov <alton@altlinux.org> 2.15.0-alt3
- Added environment variables for systemd and config files (ALT #53125).

* Fri Feb 14 2025 Anton Meleshnikov <alton@altlinux.org> 2.15.0-alt2
- Added service and mimir group.

* Mon Feb 10 2025 Anton Meleshnikov <alton@altlinux.org> 2.15.0-alt1
- Initial build for Sisyphus (ALT #53014).
