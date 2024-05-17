%global import_path github.com/VictoriaMetrics/VictoriaMetrics

%global _unpackaged_files_terminate_build 1

Name: victoriametrics
Version: 1.101.0
Release: alt1
Summary: The best long-term remote storage for Prometheus

Group: Development/Other
License: Apache-2.0
Url: https://victoriametrics.com/
Source0: %name-%version.tar
Source2: %name.service
Source3: %name.sysconfig
Source4: vmagent.service
Source5: vmagent.sysconfig
Source6: vmalert.service
Source7: vmalert.sysconfig
Source8: vmauth.service
Source9: vmauth.sysconfig

Source11: scrape.yml
Source12: alerts.yml
Source13: config.yml

Patch: %name-%version.patch

#ExclusiveArch:  %go_arches
ExclusiveArch: x86_64 aarch64
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.21
Requires(pre): %name-common = %EVR
Provides: victoria-metrics = %EVR

%description
VictoriaMetrics - the best long-term remote storage for Prometheus

%package common
Summary: Common files and dirs for %name
Group: Development/Other

%description common
%summary.

%package utils
Summary: Utils for %name
Group: Development/Other
Provides: vmutils = %EVR
Provides: vmctl = %EVR
Provides: vmbackup = %EVR
Provides: vmrestore = %EVR
Provides: vmalert-tool = %EVR
Provides: victoriametrics-vmctl = %EVR
Provides: victoriametrics-vmbackup = %EVR
Provides: victoriametrics-vmrestore = %EVR
Provides: victoriametrics-vmalert-tool = %EVR
Obsoletes: victoriametrics-vmctl < 0.5.0
Requires(pre): %name-common = %EVR

%description utils
Utils for VictoriaMetrics:
 * vmbackup - creates VictoriaMetrics data backups
 * vmrestore - restores data from backups
 * vmctl - command-line tool
 * vmalert-tool -VMAlert command-line tool

%package vmagent
Summary: Collect, relabel, filter, store metrics
Group: Development/Other
Requires(pre): %name-common = %EVR
Provides: vmagent = %EVR

%description vmagent
vmagent is a tiny agent which helps you collect metrics from various sources,
relabel and filter the collected metrics and store them in VictoriaMetrics
or any other storage systems via Prometheus remote_write protocol or
via VictoriaMetrics remote_write protocol.

%package vmalert
Summary: Executes a list of the given alerting or recording rules
Group: Development/Other
Requires(pre): %name-common = %EVR
Provides: vmalert = %EVR

%description vmalert
vmalert executes a list of the given alerting or recording rules against configured address.
It is heavily inspired by Prometheus implementation and aims to be compatible with its syntax.

%package vmauth
Summary: Simple auth proxy, router and load balancer for VictoriaMetrics
Group: Development/Other
Requires(pre): %name-common = %EVR
Provides: vmalert = %EVR

%description vmauth
%summary.

%prep
%setup -q
%patch -p1

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export BUILDINFO_TAG=v%version

%golang_prepare

pushd $BUILDDIR/src/%import_path
%make victoria-metrics
%make vmutils
popd

%install
export BUILDDIR="$PWD/.gopath"
install -m 0755 -d %buildroot%_bindir
#cp victoria-metrics-prod %buildroot%_bindir/victoria-metrics-prod
pushd $BUILDDIR/src/%import_path
install -m 0755 bin/victoria-metrics %buildroot%_bindir/victoria-metrics
install -m 0755 bin/vmagent %buildroot%_bindir/vmagent
install -m 0755 bin/vmalert %buildroot%_bindir/vmalert
install -m 0755 bin/vmalert-tool %buildroot%_bindir/vmalert-tool
install -m 0755 bin/vmauth %buildroot%_bindir/vmauth
install -m 0755 bin/vmbackup %buildroot%_bindir/vmbackup
install -m 0755 bin/vmrestore %buildroot%_bindir/vmrestore
install -m 0755 bin/vmctl %buildroot%_bindir/vmctl
popd
mkdir -p %buildroot%_sharedstatedir/victoria-metrics/{data,vmagent-remotewrite-data}
mkdir -p %buildroot%_sysconfdir/sysconfig
mkdir -p %buildroot%_sysconfdir/%name/{vmagent,vmalert,vmauth}
mkdir -p %buildroot%_unitdir
install -m644 %SOURCE2 %buildroot%_unitdir/%name.service
install -m644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/%name
install -m644 %SOURCE4 %buildroot%_unitdir/vmagent.service
install -m644 %SOURCE5 %buildroot%_sysconfdir/sysconfig/%name-vmagent
install -m644 %SOURCE6 %buildroot%_unitdir/vmalert.service
install -m644 %SOURCE7 %buildroot%_sysconfdir/sysconfig/%name-vmalert
install -m644 %SOURCE8 %buildroot%_unitdir/vmauth.service
install -m644 %SOURCE9 %buildroot%_sysconfdir/sysconfig/%name-vmauth
install -m644 %SOURCE11 %buildroot%_sysconfdir/%name/scrape.yml
install -m644 %SOURCE11 %buildroot%_sysconfdir/%name/vmagent/scrape.yml
install -m644 %SOURCE12 %buildroot%_sysconfdir/%name/vmalert/alerts.yml
install -m644 %SOURCE13 %buildroot%_sysconfdir/%name/vmauth/config.yml

%pre common
%_sbindir/groupadd -r -f _%name 2>/dev/null ||:
%_sbindir/useradd -r -g _%name -c 'Victoria Metrics Daemon' \
        -s /sbin/nologin -M -d %_sharedstatedir/victoria-metrics _%name 2>/dev/null ||:

%post
%post_service %name
%preun
%preun_service %name

%post vmagent
%post_service vmagent
%preun vmagent
%preun_service vmagent

%post vmalert
%post_service vmalert
%preun vmalert
%preun_service vmalert

%post vmauth
%post_service vmauth
%preun vmauth
%preun_service vmauth

%files
%_bindir/victoria-metrics
%_unitdir/%name.service
%dir %attr(0755, _%name, _%name) %_sharedstatedir/victoria-metrics/data
%config(noreplace) %_sysconfdir/sysconfig/%name

%files common
%dir %attr(0755, _%name, _%name) %_sharedstatedir/victoria-metrics
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/scrape.yml
%doc README.md SECURITY.md 
%doc docs/CHANGELOG.md docs/MetricsQL.md docs/FAQ.md docs/Single-server-VictoriaMetrics.md

%files utils
%_bindir/vmalert-tool
%_bindir/vmbackup
%_bindir/vmrestore
%_bindir/vmctl

%files vmagent
%_bindir/vmagent
%dir %attr(0755, _%name, _%name) %_sharedstatedir/victoria-metrics/vmagent-remotewrite-data
%dir %_sysconfdir/%name/vmagent
%config(noreplace) %_sysconfdir/%name/vmagent/scrape.yml
%config(noreplace) %_sysconfdir/sysconfig/%name-vmagent
%_unitdir/vmagent.service

%files vmalert
%_bindir/vmalert
%dir %_sysconfdir/%name/vmalert
%config(noreplace) %_sysconfdir/%name/vmalert/alerts.yml
%config(noreplace) %_sysconfdir/sysconfig/%name-vmalert
%_unitdir/vmalert.service

%files vmauth
%_bindir/vmauth
%dir %_sysconfdir/%name/vmauth
%config(noreplace) %_sysconfdir/%name/vmauth/config.yml
%config(noreplace) %_sysconfdir/sysconfig/%name-vmauth
%_unitdir/vmauth.service

%changelog
* Fri May 17 2024 Alexey Shabalin <shaba@altlinux.org> 1.101.0-alt1
- New version 1.101.0.

* Mon Mar 04 2024 Alexey Shabalin <shaba@altlinux.org> 1.97.3-alt1
- New version 1.97.3.

* Tue Feb 20 2024 Alexey Shabalin <shaba@altlinux.org> 1.97.1-alt1
- New version 1.97.1.

* Wed Nov 22 2023 Alexey Shabalin <shaba@altlinux.org> 1.95.1-alt1
- New version 1.95.1.
- Update systemd unit.
- Add common package with user _victoriametrics.
- Home dir for user _victoriametrics set /var/lib/victoria-metrics
- Data dir for single node /var/lib/victoria-metrics/data
- Add packages vmagent, vmalert, vmauth. Add units and config.

* Fri Oct 06 2023 Alexey Shabalin <shaba@altlinux.org> 1.94.0-alt1
- New version 1.94.0.

* Thu Jul 27 2023 Alexey Shabalin <shaba@altlinux.org> 1.91.2-alt1
- new version 1.91.2

* Wed Dec 14 2022 Alexey Shabalin <shaba@altlinux.org> 1.85.0-alt1
- new version 1.85.0

* Mon Apr 25 2022 Alexey Shabalin <shaba@altlinux.org> 1.76.1-alt1
- new version 1.76.1

* Sat Dec 11 2021 Alexey Shabalin <shaba@altlinux.org> 1.70.0-alt1
- new version 1.70.0

* Fri Jul 30 2021 Alexey Shabalin <shaba@altlinux.org> 1.63.0-alt1
- new version 1.63.0

* Mon Jul 12 2021 Alexey Shabalin <shaba@altlinux.org> 1.62.0-alt1
- new version 1.62.0

* Thu Jun 24 2021 Alexey Shabalin <shaba@altlinux.org> 1.61.1-alt1
- new version 1.61.1

* Sat Mar 06 2021 Alexey Shabalin <shaba@altlinux.org> 1.55.1-alt1
- new version 1.55.1

* Sat Jan 23 2021 Alexey Shabalin <shaba@altlinux.org> 1.52.0-alt1
- new version 1.52.0

* Sun Nov 15 2020 Alexey Shabalin <shaba@altlinux.org> 1.46.0-alt1
- new version 1.46.0

* Sat Sep 19 2020 Alexey Shabalin <shaba@altlinux.org> 1.41.0-alt1
- new version 1.41.0

* Mon Aug 17 2020 Alexey Shabalin <shaba@altlinux.org> 1.40.0-alt1
- new version 1.40.0

* Fri Aug 07 2020 Alexey Shabalin <shaba@altlinux.org> 1.39.3-alt1
- new version 1.39.3

* Sun May 31 2020 Alexey Shabalin <shaba@altlinux.org> 1.36.2-alt1
- 1.36.2.

* Mon Apr 20 2020 Alexey Shabalin <shaba@altlinux.org> 1.34.9-alt1
- Initial build.

