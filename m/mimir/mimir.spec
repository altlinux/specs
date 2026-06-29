%global import_path github.com/grafana/mimir
%global _unpackaged_files_terminate_build 1

Name: mimir
Version: 3.1.2
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
BuildRequires: golang >= 1.25.9
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

%package metaconvert
Summary: metaconvert
Group: Other

%description metaconvert
metaconvert.

%prep
%setup
%patch -p1

sed -i '/^ExecStart/ s|/usr/local/bin/|/usr/bin/|' packaging/nfpm/mimir/%name.service
sed -i '/^EnvironmentFile/ s|$OS_ENV_DIR|/etc/sysconfig|' packaging/nfpm/mimir/%name.service

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOFLAGS="-mod=vendor"
export GOFLAGS="-ldflags=-X=github.com/grafana/mimir/pkg/util/version.Version=%version"

%golang_prepare

%golang_build ./cmd/query-tee
%golang_build ./cmd/mimirtool
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
%doc README.md CONTRIBUTING.md
%_bindir/mimir
%config(noreplace) %_sysconfdir/sysconfig/%name
%config(noreplace) %_sysconfdir/%name/*
%_unitdir/%name.service
%dir %attr(0770, %name, %name) %_sharedstatedir/%name
%dir %attr(0770, %name, %name) %_sharedstatedir/%name/data

%files query-tee
%doc README.md CONTRIBUTING.md
%_bindir/query-tee

%files -n mimirtool
%doc README.md CONTRIBUTING.md
%_bindir/mimirtool

%files metaconvert
%doc README.md CONTRIBUTING.md
%_bindir/metaconvert

%changelog
* Mon Jun 29 2026 Anton Meleshnikov <alton@altlinux.org> 3.1.2-alt1
- New version 3.1.2.

* Wed Jun 17 2026 Anton Meleshnikov <alton@altlinux.org> 3.1.1-alt1
- New version 3.1.1 (Fixes: CVE-2026-42507, CVE-2026-39833,
  CVE-2026-39832, CVE-2026-46597, CVE-2026-42506, CVE-2026-39821,
  CVE-2026-42502, CVE-2026-25680, CVE-2026-25681, CVE-2026-27136,
  CVE-2026-39824).

* Wed Jun 03 2026 Anton Meleshnikov <alton@altlinux.org> 3.1.0-alt1
- New version 3.1.0.

* Mon Apr 27 2026 Anton Meleshnikov <alton@altlinux.org> 3.0.6-alt1
- New version 3.0.6.

* Fri Apr 03 2026 Anton Meleshnikov <alton@altlinux.org> 3.0.5-alt1
- New version 3.0.5 (Fixes: CVE-2026-33186).

* Mon Mar 16 2026 Anton Meleshnikov <alton@altlinux.org> 3.0.4-alt1
- New version 3.0.4 (Fixes: CVE-2026-24051, CVE-2026-27142,
  CVE-2026-27139, CVE-2026-25679, CVE-2026-27138, CVE-2026-27137).

* Tue Feb 24 2026 Anton Meleshnikov <alton@altlinux.org> 3.0.3-alt1
- New version 3.0.3 (Fixes: CVE-2025-61726).

* Mon Jan 12 2026 Anton Meleshnikov <alton@altlinux.org> 3.0.2-alt1
- New version 3.0.2 (Fixes: CVE-2025-61729, CVE-2025-61727).

* Tue Dec 02 2025 Anton Meleshnikov <alton@altlinux.org> 3.0.1-alt1
- New version 3.0.1.

* Mon Nov 17 2025 Anton Meleshnikov <alton@altlinux.org> 3.0.0-alt1
- New version 3.0.0.

* Wed Nov 12 2025 Anton Meleshnikov <alton@altlinux.org> 2.17.2-alt1
- New version 2.17.2.

* Wed Sep 17 2025 Anton Meleshnikov <alton@altlinux.org> 2.17.1-alt2
- Fixed EnvironmentFile variable in mimir.service.

* Tue Sep 09 2025 Anton Meleshnikov <alton@altlinux.org> 2.17.1-alt1
- New version 2.17.1.

* Wed Aug 20 2025 Anton Meleshnikov <alton@altlinux.org> 2.17.0-alt1
- New version 2.17.0.
- Fixed version output (ALT #53193).

* Wed Jul 16 2025 Anton Meleshnikov <alton@altlinux.org> 2.16.1-alt1
- New version 2.16.1.

* Mon Jun 02 2025 Anton Meleshnikov <alton@altlinux.org> 2.15.3-alt1
- New version 2.15.3.

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
