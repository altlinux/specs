%global import_path github.com/grafana/loki
%global _unpackaged_files_terminate_build 1

Name: loki
Version: 2.9.2
Release: alt1.1
Summary: Loki: like Prometheus, but for logs
License: Apache-2.0
Group: Monitoring
Url: https://grafana.com/loki
Source: %name-%version.tar
Source1: loki.service
Source2: promtail.service
Source3: loki.sysconfig
Source4: promtail.sysconfig
Source5: loki.yaml
Source6: promtail.yaml

Patch1:  go.etcd.io-bbolt-loong64.patch

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-build-golang
BuildRequires: systemd-devel

%description
Loki is a horizontally-scalable, highly-available, multi-tenant log aggregation
system inspired by Prometheus.

%package -n promtail
Summary: Promtail is an agent which ships the contents of local logs to a Loki instance
Group: Monitoring
Provides: %name-promtail = %EVR

%description -n promtail
Promtail is an agent which ships the contents of local logs to a private Loki instance or Grafana Cloud.
It is usually deployed to every machine that has applications needed to be monitored.

It primarily:
- Discovers targets
- Attaches labels to log streams
- Pushes them to the Loki instance.

Currently, Promtail can tail logs from two sources: local log files and the systemd journal

%package docker-driver
Summary: Loki Docker Logging Driver
Group: Monitoring

%description docker-driver
Docker logging driver plugins extends Docker's logging capabilities.
You can use Loki Docker logging driver plugin to send Docker container
logs directly to your Loki instance or [Grafana Cloud](https://grafana.com/loki).

%prep
%setup -q
%autopatch -p1

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%define buildpkg github.com/grafana/loki/pkg/util/build
export CGO_ENABLED=0
export GOFLAGS="-mod=vendor"
export TAGS="netgo"
export DATE=$(date -u '+%%Y-%%m-%%d')
export GOLDFLAGS="-X %buildpkg.Version=%version \
                  -X %buildpkg.Revision=%release \
                  -X %buildpkg.Branch=master \
                  -X %buildpkg.BuildUser=alt \
                  -X %buildpkg.BuildDate=$DATE"

go build "$GOFLAGS" -tags "$TAGS" -ldflags="$GOLDFLAGS"  ./cmd/logql-analyzer
go build "$GOFLAGS" -tags "$TAGS" -ldflags="$GOLDFLAGS" ./cmd/loki
go build "$GOFLAGS" -tags "$TAGS" -ldflags="$GOLDFLAGS" ./cmd/logcli
go build "$GOFLAGS" -tags "$TAGS" -ldflags="$GOLDFLAGS" ./cmd/loki-canary
go build "$GOFLAGS" -tags "$TAGS" -ldflags="$GOLDFLAGS" ./cmd/querytee
go build "$GOFLAGS" -tags "$TAGS" -ldflags="$GOLDFLAGS" -o %name-docker-driver ./clients/cmd/docker-driver
go generate -x -v ./clients/pkg/promtail/server/ui
CGO_ENABLED=1 go build "$GOFLAGS" -tags "promtail_journal_enabled" -ldflags="$GOLDFLAGS" ./clients/cmd/promtail

%install
# Service files for Loki and promtail
install -Dm644 %SOURCE1 %buildroot%_unitdir/loki.service
install -Dm644 %SOURCE2 %buildroot%_unitdir/promtail.service
install -Dm644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/loki
install -Dm644 %SOURCE4 %buildroot%_sysconfdir/sysconfig/promtail

# Config files
install -Dm644 %SOURCE5 %buildroot%_sysconfdir/loki/loki.yaml
install -Dm644 %SOURCE6 %buildroot%_sysconfdir/loki/promtail.yaml

# Binaries
install -dm755 %buildroot%_bindir
install -Dm755 logql-analyzer %buildroot%_bindir
install -Dm755 loki %buildroot%_bindir
install -Dm755 loki-canary %buildroot%_bindir
install -Dm755 promtail %buildroot%_bindir
install -Dm755 querytee %buildroot%_bindir
install -Dm755 logcli %buildroot%_bindir
install -Dm755 %name-docker-driver %buildroot%_bindir

mkdir -p %buildroot%_sharedstatedir/{loki,promtail}

%pre
groupadd -r -f _loki 2>/dev/null ||:
useradd -r -N -g _loki -c 'Loki log aggregator' \
        -s /sbin/nologin -M -d %_sharedstatedir/loki _loki 2>/dev/null ||:

%pre -n promtail
groupadd -r -f _promtail 2>/dev/null ||:
useradd -r -N -g _promtail -G systemd-journal -c 'Promtail log collector' \
        -s /sbin/nologin -M -d %_sharedstatedir/promtail _promtail 2>/dev/null ||:

%post
%post_service %name

%preun
%preun_service %name

%post -n promtail
%post_service promtail

%preun -n promtail
%preun_service promtail

%files
%doc LICENSE README.md
%_bindir/logql-analyzer
%_bindir/loki
%_bindir/logcli
%_bindir/loki-canary
%_bindir/querytee
%_unitdir/loki.service
%dir %_sysconfdir/loki
%attr(0640,root,_loki) %config(noreplace) %_sysconfdir/loki/loki.yaml
%config(noreplace) %_sysconfdir/sysconfig/loki
%attr(0770,root,_loki) %_sharedstatedir/loki

%files -n promtail
%_bindir/promtail
%_unitdir/promtail.service
%dir %_sysconfdir/loki
%attr(0640,root,_promtail) %config(noreplace) %_sysconfdir/loki/promtail.yaml
%config(noreplace) %_sysconfdir/sysconfig/promtail
%attr(0770,root,_promtail) %_sharedstatedir/promtail

%files docker-driver
%_bindir/%name-docker-driver
%doc clients/cmd/docker-driver/docker-compose.yaml
%doc clients/cmd/docker-driver/pipeline-example.yaml

%changelog
* Thu Nov 02 2023 Ivan A. Melnikov <iv@altlinux.org> 2.9.2-alt1.1
- NMU: loongarch64 support

* Fri Oct 27 2023 Alexey Shabalin <shaba@altlinux.org> 2.9.2-alt1
- New version 2.9.2.

* Tue Jul 04 2023 Alexey Shabalin <shaba@altlinux.org> 2.8.2-alt1
- New version 2.8.2.

* Tue May 02 2023 Alexey Shabalin <shaba@altlinux.org> 2.8.1-alt1
- New version 2.8.1.

* Tue Aug 30 2022 Alexey Shabalin <shaba@altlinux.org> 2.6.1-alt2
- update loki config (Fixes: ALT#43661)

* Sat Jul 30 2022 Alexey Shabalin <shaba@altlinux.org> 2.6.1-alt1
- new version 2.6.1
- add docker-driver package
- fix License

* Sun Nov 14 2021 Alexey Shabalin <shaba@altlinux.org> 2.4.1-alt1
- new version 2.4.1

* Tue Aug 17 2021 Alexey Shabalin <shaba@altlinux.org> 2.3.0-alt1
- new version 2.3.0

* Sat Feb 20 2021 Alexey Shabalin <shaba@altlinux.org> 2.1.0-alt1
- Initial build

