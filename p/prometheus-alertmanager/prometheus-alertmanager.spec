
%define oname alertmanager
%global _unpackaged_files_terminate_build 1

Name: prometheus-%oname
Version: 0.33.0
Release: alt1
Summary: Prometheus Alertmanager

Group: Development/Other
License: Apache-2.0
Url: https://github.com/prometheus/alertmanager

Source: %name-%version.tar
Source1: vendor-%version.tar
Source2: %name.sysconfig
Source3: %name.init
Source4: %name.service
Patch0: %name-%version-%release.patch

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-macros-golang
BuildRequires(pre): prometheus-common
BuildRequires: rpm-build-golang golang >= 1.25

%description
The Alertmanager handles alerts sent by client applications such as the
Prometheus server. It takes care of deduplicating, grouping, and routing
them to the correct receiver integration such as email, PagerDuty, or
OpsGenie. It also takes care of silencing and inhibition of alerts.

%prep
%setup -a 1
%patch -p1

%build
export BUILDDIR="$PWD/.gopath"
export GOPATH="$BUILDDIR:%go_path"
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

mkdir -p %buildroot{%_bindir,%_initdir,%_unitdir,%_sysconfdir/{sysconfig,prometheus}}
install -d -m0750 %buildroot%_localstatedir/prometheus/%oname
install -d -m0750 %buildroot%_sysconfdir/prometheus/alertmanager/templates

#install -m0755 %oname %buildroot%_bindir/%oname
#install -m0755 amtool %buildroot%_bindir/amtool
install -m0640 doc/examples/simple.yml %buildroot%_sysconfdir/prometheus/%oname.yml
install -m0640 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name
install -m0755 %SOURCE3 %buildroot%_initdir/%name
install -m0644 %SOURCE4 %buildroot%_unitdir/%name.service
install -m0640 template/*.tmpl %buildroot%_sysconfdir/prometheus/alertmanager/templates/

%check
export LDFLAGS="-X github.com/prometheus/common/version.Version=%version  \
         -X github.com/prometheus/common/version.Revision=%release \
         -X github.com/prometheus/common/version.Branch=tarball      \
         -X github.com/prometheus/common/version.BuildDate=$(date -u +%%Y%%m%%d)"
for dir in cmd/*; do
    [ -d "$dir" ] || continue
    pushd "$dir"
        %gotest
    popd
done

%post
%post_service %name

%preun
%preun_service %name

%files
%doc LICENSE README.md doc examples
%_bindir/*
%_unitdir/%name.service
%_initdir/%name
%config(noreplace) %attr(0640,root,prometheus) %_sysconfdir/sysconfig/%name
%config(noreplace) %attr(0640,root,prometheus) %_sysconfdir/prometheus/%oname.yml
%dir %attr(0750,root,prometheus) %_sysconfdir/prometheus/alertmanager
%dir %attr(0750,root,prometheus) %_sysconfdir/prometheus/alertmanager/templates
%attr(0640,root,prometheus) %_sysconfdir/prometheus/alertmanager/templates/*
%dir %attr(0750, prometheus, prometheus) %_localstatedir/prometheus/%oname

%changelog
* Wed Jun 25 2026 Artyom Sinyugin <writers@altlinux.org> 0.33.0-alt1
- New version 0.33.0.
- Restricted default listeners and disabled HA cluster listener by default.
- Hardened systemd service sandboxing.
- Restricted permissions for configuration, templates and state directory.

* Fri Jan 23 2026 Artyom Sinyugin <writers@altlinux.org> 0.30.1-alt1
- New version 0.30.1.

* Thu Jun 05 2025 Artyom Sinyugin <writers@altlinux.org> 0.28.1-alt1
- New version 0.28.1.

* Fri Feb 14 2025 Artyom Sinyugin <writers@altlinux.org> 0.28.0-alt1
- 0.28.0

* Mon Aug 26 2024 Alexey Shabalin <shaba@altlinux.org> 0.27.0-alt1
- 0.27.0

* Fri Oct 06 2023 Alexey Shabalin <shaba@altlinux.org> 0.26.0-alt1
- 0.26.0

* Thu Jul 27 2023 Alexey Shabalin <shaba@altlinux.org> 0.25.0-alt1
- 0.25.0

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

* Thu May 10 2018 Alexey Shabalin <shaba@altlinux.ru> 0.14.0-alt1
- Initial build for ALT.
