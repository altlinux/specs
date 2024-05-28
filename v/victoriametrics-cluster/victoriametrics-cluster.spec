%global import_path github.com/VictoriaMetrics/VictoriaMetrics

%global _unpackaged_files_terminate_build 1

Name: victoriametrics-cluster
Version: 1.101.0
Release: alt2
Summary: The best long-term remote storage for Prometheus

Group: Development/Other
License: Apache-2.0
Url: https://victoriametrics.com/
Source0: %name-%version.tar

Source2: vminsert.service
Source3: vminsert.sysconfig
Source4: vmselect.service
Source5: vmselect.sysconfig
Source6: vmstorage.service
Source7: vmstorage.sysconfig

#ExclusiveArch:  %go_arches
ExclusiveArch: x86_64 aarch64
BuildRequires(pre): rpm-build-golang

%description
VictoriaMetrics cluster consists of the following services:

- vmstorage - stores the data
- vminsert - proxies the ingested data to vmstorage shards using consistent hashing
- vmselect - performs incoming queries using the data from vmstorage

Each service may scale independently and may run on the most suitable hardware.
vmstorage nodes don't know about each other, don't communicate with each other and don't share any data.
This is shared nothing architecture.
It increases cluster availability, simplifies cluster maintenance and cluster scaling.

%package vmstorage
Summary: vmstorage for %name
Group: Development/Other
Provides: vmstorage = %EVR
Provides: victoriametrics-vmstorage = %EVR
Requires(pre): victoriametrics-common

%description vmstorage
vmstorage performs the following tasks:
- Accepts inserts from `vminsert` nodes and stores them to local storage.
- Performs select requests from `vmselect` nodes.

%package vminsert
Summary: vminsert for %name
Group: Development/Other
Provides: vminsert = %EVR
Provides: victoriametrics-vminsert = %EVR
Requires(pre): victoriametrics-common

%description vminsert
vminsert routes the ingested data to vmstorage.

%package vmselect
Summary: vmselect for %name
Group: Development/Other
Provides: vmselect = %EVR
Provides: victoriametrics-vmselect = %EVR
Requires(pre): victoriametrics-common

%description vmselect
vmselect performs the following tasks:
- Splits incoming selects to tasks for vmstorage nodes and issues these tasks
  to all the vmstorage nodes in the cluster.
- Merges responses from all the vmstorage nodes and returns a single response.

%prep
%setup -q

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .gopath/src/%import_path

export VERSION=%version
#export COMMIT=%%commit
export BRANCH=altlinux
export BUILDINFO_TAG=v%version

%make \
	vminsert \
	vmselect \
	vmstorage

%install
install -m 0755 -d %buildroot%_bindir
#cp victoria-metrics-prod %buildroot%_bindir/victoria-metrics-prod
cd .gopath/src/%import_path
install -m 0755 bin/vminsert %buildroot%_bindir/vminsert
install -m 0755 bin/vmselect %buildroot%_bindir/vmselect
install -m 0755 bin/vmstorage %buildroot%_bindir/vmstorage

mkdir -p %buildroot%_sharedstatedir/victoria-metrics/cluster-data
mkdir -p %buildroot%_sysconfdir/sysconfig
mkdir -p %buildroot%_unitdir
install -m644 %SOURCE2 %buildroot%_unitdir/vminsert.service
install -m644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/%name-vminsert
install -m644 %SOURCE4 %buildroot%_unitdir/vmselect.service
install -m644 %SOURCE5 %buildroot%_sysconfdir/sysconfig/%name-vmselect
install -m644 %SOURCE6 %buildroot%_unitdir/vmstorage.service
install -m644 %SOURCE7 %buildroot%_sysconfdir/sysconfig/%name-vmstorage

%post vminsert
%post_service vminsert
%preun vminsert
%preun_service vminsert

%post vmselect
%post_service vmselect
%preun vmselect
%preun_service vmselect

%post vmstorage
%post_service vmstorage
%preun vmstorage
%preun_service vmstorage

%files vminsert
%_bindir/vminsert
%config(noreplace) %_sysconfdir/sysconfig/%name-vminsert
%_unitdir/vminsert.service

%files vmselect
%_bindir/vmselect
%config(noreplace) %_sysconfdir/sysconfig/%name-vmselect
%_unitdir/vmselect.service

%files vmstorage
%_bindir/vmstorage
%config(noreplace) %_sysconfdir/sysconfig/%name-vmstorage
%_unitdir/vmstorage.service
%dir %attr(0755, _victoriametrics, _victoriametrics) %_sharedstatedir/victoria-metrics/cluster-data

%changelog
* Tue May 28 2024 Alexey Shabalin <shaba@altlinux.org> 1.101.0-alt2
- Fixed use Environment in systemd unit (ALT#50398).

* Fri May 17 2024 Alexey Shabalin <shaba@altlinux.org> 1.101.0-alt1
- New version 1.101.0.

* Tue Feb 20 2024 Alexey Shabalin <shaba@altlinux.org> 1.97.1-alt1
- New version 1.97.1.

* Mon Dec 04 2023 Alexey Shabalin <shaba@altlinux.org> 1.95.1-alt1
- new version 1.95.1
- add systemd units and configs

* Fri Oct 06 2023 Alexey Shabalin <shaba@altlinux.org> 1.94.0-alt1
- new version 1.94.0

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
- Initial build.
