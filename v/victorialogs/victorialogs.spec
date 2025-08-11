%global import_path github.com/VictoriaMetrics/VictoriaLogs

%global _unpackaged_files_terminate_build 1

Name: victorialogs
Version: 1.27.0
Release: alt1
Summary: Log management and log analytics system from VictoriaMetrics

Group: Development/Other
License: Apache-2.0
Url: https://victoriametrics.com/
Source0: %name-%version.tar

Source2: %name.service
Source3: %name.sysconfig
Source4: vlagent.service
Source5: vlagent.sysconfig
Patch: %name-%version.patch

#ExclusiveArch:  %go_arches
ExclusiveArch: x86_64 aarch64
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.24.6
Requires(pre): %name-common = %EVR
Provides: victoria-logs = %EVR

%description
VictoriaLogs is open source user-friendly database for logs from VictoriaMetrics.

VictoriaLogs provides the following key features:
 * VictoriaLogs can accept logs from popular log collectors.
 * VictoriaLogs is much easier to set up and operate compared to Elasticsearch
   and Grafana Loki.
 * VictoriaLogs provides easy yet powerful query language with full-text search
   capabilities across all the log fields - see LogsQL docs.
 * VictoriaLogs can be seamlessly combined with good old Unix tools for
   log analysis such as grep, less, sort, jq, etc.
 * VictoriaLogs capacity and performance scales linearly with
   the available resources (CPU, RAM, disk IO, disk space).
   It runs smoothly on both Raspberry PI and a server with hundreds
   of CPU cores and terabytes of RAM.
 * VictoriaLogs can handle up to 30x bigger data volumes than Elasticsearch
   and Grafana Loki when running on the same hardware.
 * VictoriaLogs supports fast full-text search over high-cardinality log fields
   such as trace_id, user_id and ip.
 * VictoriaLogs supports multitenancy.
 * VictoriaLogs supports out-of-order logs' ingestion aka backfilling.
 * VictoriaLogs provides a simple web UI for querying logs.


%package common
Summary: Common files and dirs for %name
Group: Development/Other

%description common
%summary.

%package vlagent
Summary: vlagent collects logs and routes it to VictoriaLogs
Group: Development/Other
Requires(pre): %name-common = %EVR
Provides: vlagent = %EVR

%description vlagent
vlagent is a tiny agent which helps you collect logs from various sources
and store them in VictoriaLogs.

- It can accept logs from popular log collectors.
- Can replicate collected logs simultaneously to multiple VictoriaLogs instances.
- Works smoothly in environments with unstable connections to remote storage.
  If the remote storage is unavailable, the collected logs are buffered
  at -remoteWrite.tmpDataPath. The buffered logs are sent to remote storage
  as soon as the connection to the remote storage is repaired.
  The maximum disk usage for the buffer can be limited with -remoteWrite.maxDiskUsagePerURL.

%prep
%setup -q
%patch -p1

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export VERSION=%version
export BRANCH=altlinux
export BUILDINFO_TAG=v%version
export PKG_TAG=v%version

%golang_prepare
pushd .gopath/src/%import_path
%make victoria-logs
%make vlagent
%make vlogscli
popd

%install
mkdir -p %buildroot%_sharedstatedir/victoria-logs/{data,vlagent-remotewrite-data}
mkdir -p %buildroot{%_bindir,%_sysconfdir/sysconfig,%_unitdir}
pushd .gopath/src/%import_path
install -m 0755 bin/victoria-logs %buildroot%_bindir/victoria-logs
install -m 0755 bin/vlogscli %buildroot%_bindir/vlogscli
install -m 0755 bin/vlagent %buildroot%_bindir/vlagent
install -m644 %SOURCE2 %buildroot%_unitdir/%name.service
install -m644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/%name
install -m644 %SOURCE4 %buildroot%_unitdir/vlagent.service
install -m644 %SOURCE5 %buildroot%_sysconfdir/sysconfig/%name-vlagent
popd

%pre common
groupadd -r -f _%name 2>/dev/null ||:
useradd -r -g _%name -c 'Victoria Logs Daemon' \
        -s /sbin/nologin -M -d %_sharedstatedir/victoria-logs _%name 2>/dev/null ||:

%post
%post_service %name
%preun
%preun_service %name

%post vlagent
%post_service vlagent
%preun vlagent
%preun_service vlagent

%files
%_bindir/victoria-logs
%_bindir/vlogscli
%_unitdir/%name.service
%dir %attr(0755, _%name, _%name) %_sharedstatedir/victoria-logs/data

%files common
%dir %attr(0755, _%name, _%name) %_sharedstatedir/victoria-logs
%config(noreplace) %attr(0640, root, _%name) %_sysconfdir/sysconfig/%name
%doc docs/victorialogs/CHANGELOG.md docs/victorialogs/FAQ.md docs/victorialogs/LogsQL.md
%doc docs/victorialogs/QuickStart.md docs/victorialogs/README.md docs/victorialogs/data-ingestion

%files vlagent
%_bindir/vlagent
%config(noreplace) %attr(0640, root, _%name) %_sysconfdir/sysconfig/%name-vlagent
%_unitdir/vlagent.service
%dir %attr(0755, _%name, _%name) %_sharedstatedir/victoria-logs/vlagent-remotewrite-data

%changelog
* Mon Aug 11 2025 Alexey Shabalin <shaba@altlinux.org> 1.27.0-alt1
- 1.27.0.

* Fri Jun 20 2025 Alexey Shabalin <shaba@altlinux.org> 1.23.3-alt1
- 1.23.3.

* Wed Mar 12 2025 Alexey Shabalin <shaba@altlinux.org> 1.15.0-alt1
- 1.15.0.

* Tue Mar 11 2025 Alexey Shabalin <shaba@altlinux.org> 1.14.0-alt1
- 1.14.0.

* Fri Feb 14 2025 Alexey Shabalin <shaba@altlinux.org> 1.10.1-alt1
- 1.10.1.

* Mon Dec 23 2024 Alexey Shabalin <shaba@altlinux.org> 1.4.0-alt1
- 1.4.0.
- Add vlogscli to package.

* Mon Dec 16 2024 Alexey Shabalin <shaba@altlinux.org> 1.3.2-alt1
- 1.3.2.

* Mon Oct 28 2024 Alexey Shabalin <shaba@altlinux.org> 0.37.0-alt1
- 0.37.0.

* Mon Jul 08 2024 Alexey Shabalin <shaba@altlinux.org> 0.27.1-alt1
- 0.27.1.

* Tue May 28 2024 Alexey Shabalin <shaba@altlinux.org> 0.10.0-alt1
- New version 0.10.0.
- Fix use Environment in systemd unit (ALT#50398).

* Fri May 17 2024 Alexey Shabalin <shaba@altlinux.org> 0.7.0-alt1
- New version 0.7.0.

* Mon Mar 04 2024 Alexey Shabalin <shaba@altlinux.org> 0.5.0-alt1
- New version 0.5.0.

* Mon Dec 04 2023 Alexey Shabalin <shaba@altlinux.org> 0.4.2-alt1
- Initial build.
