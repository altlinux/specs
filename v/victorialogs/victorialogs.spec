%global import_path github.com/VictoriaMetrics/VictoriaMetrics

%global _unpackaged_files_terminate_build 1

Name: victorialogs
Version: 0.7.0
Release: alt1
Summary: Log management and log analytics system from VictoriaMetrics

Group: Development/Other
License: Apache-2.0
Url: https://victoriametrics.com/
Source0: %name-%version.tar

Source2: %name.service
Source3: %name.sysconfig

#ExclusiveArch:  %go_arches
ExclusiveArch: x86_64 aarch64
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.21

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

%prep
%setup -q

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .gopath/src/%import_path

export VERSION=%version
export BRANCH=altlinux
export BUILDINFO_TAG=v%version

%make victoria-logs

%install
install -m 0755 -d %buildroot%_bindir
cd .gopath/src/%import_path
install -m 0755 bin/victoria-logs %buildroot%_bindir/victoria-logs
mkdir -p %buildroot%_sharedstatedir/victoria-logs/data
mkdir -p %buildroot%_sysconfdir/sysconfig
mkdir -p %buildroot%_unitdir
install -m644 %SOURCE2 %buildroot%_unitdir/%name.service
install -m644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/%name

%pre
groupadd -r -f _%name 2>/dev/null ||:
useradd -r -g _%name -c 'Victoria Logs Daemon' \
        -s /sbin/nologin -M -d %_sharedstatedir/victoria-logs _%name 2>/dev/null ||:
%post
%post_service %name
%preun
%preun_service %name

%files
%_bindir/victoria-logs
%_unitdir/%name.service
%dir %attr(0755, _%name, _%name) %_sharedstatedir/victoria-logs/data
%config(noreplace) %_sysconfdir/sysconfig/%name
%doc docs/VictoriaLogs/CHANGELOG.md docs/VictoriaLogs/FAQ.md docs/VictoriaLogs/LogsQL.md
%doc docs/VictoriaLogs/QuickStart.md docs/VictoriaLogs/README.md docs/VictoriaLogs/data-ingestion

%changelog
* Fri May 17 2024 Alexey Shabalin <shaba@altlinux.org> 0.7.0-alt1
- New version 0.7.0.

* Mon Mar 04 2024 Alexey Shabalin <shaba@altlinux.org> 0.5.0-alt1
- New version 0.5.0.

* Mon Dec 04 2023 Alexey Shabalin <shaba@altlinux.org> 0.4.2-alt1
- Initial build.
