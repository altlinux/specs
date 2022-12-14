%global import_path github.com/VictoriaMetrics/VictoriaMetrics

%global _unpackaged_files_terminate_build 1

Name: victoriametrics-cluster
Version: 1.85.0
Release: alt1
Summary: The best long-term remote storage for Prometheus

Group: Development/Other
License: Apache-2.0
Url: https://victoriametrics.com/
Source0: %name-%version.tar

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

%description vmstorage
vmstorage performs the following tasks:
- Accepts inserts from `vminsert` nodes and stores them to local storage.
- Performs select requests from `vmselect` nodes.

%package vminsert
Summary: vminsert for %name
Group: Development/Other
Provides: vminsert = %EVR

%description vminsert
vminsert routes the ingested data to vmstorage.

%package vmselect
Summary: vmselect for %name
Group: Development/Other
Provides: vmselect = %EVR

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

%files vminsert
%_bindir/vminsert

%files vmselect
%_bindir/vmselect

%files vmstorage
%_bindir/vmstorage

%changelog
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
