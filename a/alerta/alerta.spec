%define _unpackaged_files_terminate_build 1

Name:       alerta
Version:    9.1.0
Release:    alt1
Summary:    Alerta monitoring system server
License:    Apache-2.0
Group:      System/Servers
Url:        https://docs.alerta.io/index.html
Vcs:        https://github.com/alerta/alerta

BuildArch: noarch

Source: %name-%version.tar
Source1: alertad.conf
Source2: alertad
Source3: alertad.service

BuildRequires(pre): rpm-macros-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pip
BuildRequires: python3-module-wheel

Requires: python3 >= 3.9

%description
Alerta is a monitoring system that accepts alerts from any source,
provides visualization and drill-down to detail.

%prep
%setup

%build
%pyproject_build

%install
mkdir -p %buildroot%_logdir/%name
install -Dm 644 %SOURCE1 %buildroot%_sysconfdir/%name/alertad.conf
install -Dm 644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/alertad
install -Dm 644 %SOURCE3 %buildroot%_unitdir/alertad.service
%pyproject_install --exclude-paths 'tests/*'

%pre
groupadd -r alertad
useradd -r -M -g alertad -s /sbin/nologin -c "alerta daemon" alertad

%post
%systemd_post alertad.service

%preun
%systemd_preun alertad.service

%files
%doc README.md NOTICE
%_bindir/alertad
%python3_sitelibdir_noarch/%name
%python3_sitelibdir_noarch/%{name}_server-%version.dist-info
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/alertad.conf
%config(noreplace) %_sysconfdir/sysconfig/alertad
%config(noreplace) %_unitdir/alertad.service
%attr(1770,root,alertad) %dir %_logdir/%name

%changelog
* Fri Sep 25 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 9.1.0-alt1
- Initial build for ALT.

