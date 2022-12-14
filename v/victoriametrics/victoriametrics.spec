%global import_path github.com/VictoriaMetrics/VictoriaMetrics

%global _unpackaged_files_terminate_build 1

Name: victoriametrics
Version: 1.85.0
Release: alt1
Summary: The best long-term remote storage for Prometheus

Group: Development/Other
License: Apache-2.0
Url: https://victoriametrics.com/
Source0: %name-%version.tar
Source2: %name.service

#ExclusiveArch:  %go_arches
ExclusiveArch: x86_64 aarch64
BuildRequires(pre): rpm-build-golang

%description
VictoriaMetrics - the best long-term remote storage for Prometheus

%package utils
Summary: Utils for %name
Group: Development/Other
Provides: vmutils = %EVR
Provides: vmctl = %EVR
Provides: victoriametrics-vmctl = %EVR
Obsoletes: victoriametrics-vmctl < 0.5.0

%description utils
Utils for VictoriaMetrics:
 * vmagent is a tiny but brave agent,
   which helps you collecting metrics from various sources
   and storing them to VictoriaMetrics or any other Prometheus-compatible
   storage system that supports remote_write protocol.
 * vmbackup - creates VictoriaMetrics data backups
 * vmrestore - restores data from backups

%prep
%setup -q

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export VERSION=%version
export COMMIT=%commit
export BRANCH=altlinux
export BUILDINFO_TAG=v%version


%golang_prepare

pushd $BUILDDIR/src/%import_path
%make \
	victoria-metrics \
	vmagent \
	vmalert \
	vmauth \
	vmbackup \
	vmrestore \
	vmctl
popd

%install
export BUILDDIR="$PWD/.gopath"
install -m 0755 -d %buildroot%_bindir
#cp victoria-metrics-prod %buildroot%_bindir/victoria-metrics-prod
pushd $BUILDDIR/src/%import_path
install -m 0755 bin/victoria-metrics %buildroot%_bindir/victoria-metrics
install -m 0755 bin/vmagent %buildroot%_bindir/vmagent
install -m 0755 bin/vmalert %buildroot%_bindir/vmalert
install -m 0755 bin/vmauth %buildroot%_bindir/vmauth
install -m 0755 bin/vmbackup %buildroot%_bindir/vmbackup
install -m 0755 bin/vmrestore %buildroot%_bindir/vmrestore
install -m 0755 bin/vmctl %buildroot%_bindir/vmctl
popd
install -m 0755 -d %buildroot%_sharedstatedir/victoria-metrics-data

mkdir -p %buildroot%_unitdir
install -m644 %SOURCE2 \
    %buildroot%_unitdir/%name.service

%pre
%_sbindir/groupadd -r -f _%name 2>/dev/null ||:
%_sbindir/useradd -r -g _%name -c 'Victoria Metrics Daemon' \
        -s /sbin/nologin  -d %_sharedstatedir/victoria-metrics-data _%name 2>/dev/null ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%_bindir/victoria-metrics
%dir %attr(0755, _%name, _%name) %_sharedstatedir/victoria-metrics-data
%_unitdir/%name.service

%files utils
%_bindir/vm*

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

