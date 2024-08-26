
%define oname blackbox_exporter
%global import_path github.com/prometheus/blackbox_exporter

%global _unpackaged_files_terminate_build 1

Name: prometheus-%oname
Version: 0.25.0
Release: alt1
Summary: Prometheus blackbox prober exporter

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

Requires(pre): prometheus-common

%description
The blackbox exporter allows blackbox probing of endpoints over HTTP, HTTPS, DNS, TCP and ICMP.

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

%install
export BUILDDIR="$PWD/.gopath"
#export GOPATH="%go_path"
%golang_install
rm -rf -- %buildroot%_datadir
rm -rf -- %buildroot%go_root
mkdir -p %buildroot{%_bindir,%_initdir,%_unitdir,%_sysconfdir/{sysconfig,prometheus}}

#install -m0755 %oname %buildroot%_bindir/%oname
install -m0644 blackbox.yml %buildroot%_sysconfdir/prometheus/blackbox.yml
install -m0644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name
install -m0755 %SOURCE3 %buildroot%_initdir/%name
install -m0644 %SOURCE4 %buildroot%_unitdir/%name.service

%post
%post_service %name

%preun
%preun_service %name

%files
%doc LICENSE README.md CONFIGURATION.md example.yml
%_bindir/*
%_unitdir/%name.service
%_initdir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%config(noreplace) %_sysconfdir/prometheus/blackbox.yml

%changelog
* Mon Aug 26 2024 Alexey Shabalin <shaba@altlinux.org> 0.25.0-alt1
- 0.25.0

* Thu Jul 27 2023 Alexey Shabalin <shaba@altlinux.org> 0.24.0-alt1
- 0.24.0

* Fri Dec 09 2022 Alexey Shabalin <shaba@altlinux.org> 0.23.0-alt1
- 0.23.0

* Fri Jul 30 2021 Alexey Shabalin <shaba@altlinux.org> 0.19.0-alt1
- 0.19.0

* Tue Jan 26 2021 Alexey Shabalin <shaba@altlinux.org> 0.18.0-alt1
- 0.18.0

* Wed Mar 18 2020 Alexey Shabalin <shaba@altlinux.org> 0.16.0-alt1
- 0.16.0

* Tue Aug 13 2019 Alexey Shabalin <shaba@altlinux.org> 0.14.0-alt1
- 0.14.0

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 0.13.0-alt2
- NMU: remove rpm-build-ubt from BR:

* Fri Jan 18 2019 Alexey Shabalin <shaba@altlinux.org> 0.13.0-alt1
- 0.13.0

* Thu May 10 2018 Alexey Shabalin <shaba@altlinux.ru> 0.12.0-alt2
- fix typo in option

* Thu May 10 2018 Alexey Shabalin <shaba@altlinux.ru> 0.12.0-alt1
- Initial build for ALT.
