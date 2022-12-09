
%define oname snmp_exporter
%global import_path github.com/prometheus/snmp_exporter

%global _unpackaged_files_terminate_build 1

Name: prometheus-%oname
Version: 0.21.0
Release: alt1
Summary: Prometheus snmp exporter

Group: Development/Other
License: Apache-2.0
Url: https://%import_path
Source: %name-%version.tar

Source2: %name.sysconfig
Source3: %name.init
Source4: %name.service

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang
#BuildRequires: promu
BuildRequires: /proc
# for build generator
BuildRequires: libnet-snmp-devel snmp-mibs-std

Requires(pre): prometheus-common

%description
This is an exporter that exposes information gathered
from SNMP for use by the Prometheus monitoring system.

%prep
%setup -q

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

%golang_build .
pushd $BUILDDIR/src/$IMPORT_PATH/generator
%gobuild
popd

%install
export BUILDDIR="$PWD/.gopath"
#export GOPATH="%go_path"
mkdir -p %buildroot{%_bindir,%_initdir,%_unitdir,%_sysconfdir/{sysconfig,prometheus}}
# generator
install -m0755 $BUILDDIR/src/%import_path/generator/generator %buildroot%_bindir/%oname-generator

%golang_install
rm -rf -- %buildroot%_datadir
rm -rf -- %buildroot%go_root
mkdir -p %buildroot{%_bindir,%_initdir,%_unitdir,%_sysconfdir/{sysconfig,prometheus}}

#install -m0755 %oname %buildroot%_bindir/%oname
install -m0644 snmp.yml %buildroot%_sysconfdir/prometheus/snmp.yml
install -m0644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name
install -m0755 %SOURCE3 %buildroot%_initdir/%name
install -m0644 %SOURCE4 %buildroot%_unitdir/%name.service

%post
%post_service %name

%preun
%preun_service %name

%files
%doc LICENSE README.md snmp.yml
%doc generator/generator.yml
%doc generator/FORMAT.md
%_bindir/*
%_unitdir/%name.service
%_initdir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%config(noreplace) %_sysconfdir/prometheus/snmp.yml

%changelog
* Fri Dec 09 2022 Alexey Shabalin <shaba@altlinux.org> 0.21.0-alt1
- 0.21.0

* Fri Jul 30 2021 Alexey Shabalin <shaba@altlinux.org> 0.20.0-alt1
- 0.20.0

* Tue Jan 26 2021 Alexey Shabalin <shaba@altlinux.org> 0.19.0-alt1
- 0.19.0.

* Sun May 31 2020 Alexey Shabalin <shaba@altlinux.org> 0.18.0-alt1
- 0.18.0

* Sat Sep 28 2019 Alexey Shabalin <shaba@altlinux.org> 0.15.0-alt3
- fixed build with golang-1.13

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 0.15.0-alt2
- NMU: remove rpm-build-ubt from BR:

* Wed Mar 06 2019 Alexey Shabalin <shaba@altlinux.org> 0.15.0-alt1
- 0.15.0

* Fri Jan 18 2019 Alexey Shabalin <shaba@altlinux.org> 0.14.0-alt1
- 0.14.0

* Thu May 10 2018 Alexey Shabalin <shaba@altlinux.ru> 0.10.0-alt2
- fix typo in option

* Thu May 10 2018 Alexey Shabalin <shaba@altlinux.ru> 0.10.0-alt1
- Initial build for ALT.
