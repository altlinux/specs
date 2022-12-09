
%define oname alertmanager
%global import_path github.com/prometheus/alertmanager
%global _unpackaged_files_terminate_build 1

Name: prometheus-%oname
Version: 0.24.0
Release: alt1
Summary: Prometheus Alertmanager

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
The Alertmanager handles alerts sent by client applications such as the
Prometheus server. It takes care of deduplicating, grouping, and routing
them to the correct receiver integration such as email, PagerDuty, or
OpsGenie. It also takes care of silencing and inhibition of alerts.

%prep
%setup -q

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare
#promu build
export LDFLAGS="-X github.com/prometheus/common/version.Version=%version  \
         -X github.com/prometheus/common/version.Revision=%release \
         -X github.com/prometheus/common/version.Branch=tarball      \
         -X github.com/prometheus/common/version.BuildDate=$(date -u +%%Y%%m%%d)"
%golang_build cmd/*

%install
export BUILDDIR="$PWD/.gopath"
%golang_install
rm -rf -- %buildroot%_datadir
rm -rf -- %buildroot%go_root

mkdir -p %buildroot{%_bindir,%_initdir,%_unitdir,%_sysconfdir/{sysconfig,prometheus},%_localstatedir/prometheus/%oname}
mkdir -p %buildroot%_sysconfdir/prometheus/alertmanager/templates

#install -m0755 %oname %buildroot%_bindir/%oname
#install -m0755 amtool %buildroot%_bindir/amtool
install -m0644 doc/examples/simple.yml %buildroot%_sysconfdir/prometheus/%oname.yml
install -m0644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name
install -m0755 %SOURCE3 %buildroot%_initdir/%name
install -m0644 %SOURCE4 %buildroot%_unitdir/%name.service
install -m0644 template/*.tmpl %buildroot%_sysconfdir/prometheus/alertmanager/templates/

%post
%post_service %name

%preun
%preun_service %name

%files
%doc LICENSE README.md doc examples
%_bindir/*
%_unitdir/%name.service
%_initdir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%config(noreplace) %_sysconfdir/prometheus/%oname.yml
%_sysconfdir/prometheus/alertmanager
%dir %attr(775, root, prometheus) %_localstatedir/prometheus/%oname

%changelog
* Fri Dec 09 2022 Alexey Shabalin <shaba@altlinux.org> 0.24.0-alt1
- 0.24.0

* Mon Feb 07 2022 Alexey Shabalin <shaba@altlinux.org> 0.21.0-alt2
- Fix config example.

* Tue Jan 26 2021 Alexey Shabalin <shaba@altlinux.org> 0.21.0-alt1
- 0.21.0.

* Sat Apr 18 2020 Alexey Shabalin <shaba@altlinux.org> 0.20.0-alt1
- 0.20.0

* Wed Jul 17 2019 Alexey Shabalin <shaba@altlinux.org> 0.18.0-alt1
- 0.18.0

* Wed Mar 06 2019 Alexey Shabalin <shaba@altlinux.org> 0.16.1-alt1
- 0.16.1

* Fri Jan 18 2019 Alexey Shabalin <shaba@altlinux.org> 0.15.3-alt1
- 0.15.3

* Thu May 10 2018 Alexey Shabalin <shaba@altlinux.ru> 0.14.0-alt1%ubt
- Initial build for ALT.
