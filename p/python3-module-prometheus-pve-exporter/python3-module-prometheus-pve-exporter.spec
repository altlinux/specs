%define  modulename prometheus-pve-exporter
%def_without check

Name:    python3-module-%modulename
Version: 3.4.1
Release: alt1

Summary: Prometheus Proxmox VE Exporter
License: Apache-2.0
Group:   Development/Python
URL:     https://github.com/prometheus-pve/prometheus-pve-exporter.git

BuildArch: noarch

Source: %modulename-%version.tar
Source1: %modulename.service

Provides: %modulename = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: rpm-build-systemd
%if_with check
BuildRequires: python3(pyflakes)
BuildRequires: python3(pylint)
%endif

%description
This is an exporter that exposes information gathered from Proxmox VE node
for use by the Prometheus monitoring system.

%prep
%setup -n %modulename-%version

%build
%pyproject_build

%install
%pyproject_install
install -pDm0644 pve.yml %buildroot%_sysconfdir/prometheus/pve.yml
install -pDm0644 %SOURCE1 %buildroot%_unitdir/%modulename.service

%pre
groupadd -r -f prometheus 2>/dev/null ||:
useradd -r -g prometheus -c 'Prometheus PVE exporter user' \
        -d /var/lib/prometheus prometheus 2>/dev/null ||:

%post
%systemd_user_post %modulename.service

%preun
%systemd_user_preun %modulename.service

%postun
%systemd_user_postun %modulename.service

%check
#%%tox_create_default_config
%tox_check_pyproject

%files
%doc README.rst
%config(noreplace) %_sysconfdir/prometheus/pve.yml
%_unitdir/*
%_bindir/*
%python3_sitelibdir/*

%changelog
* Mon May 06 2024 Andrew A. Vasilyev <andy@altlinux.org> 3.4.1-alt1
- 3.4.1
- fix spec name and add systemd macro

* Thu May 02 2024 Andrew A. Vasilyev <andy@altlinux.org> 3.4.0-alt1
- 3.4.0

* Sun Apr 28 2024 Andrew A. Vasilyev <andy@altlinux.org> 3.3.0-alt1
- 3.3.0

* Mon Apr 22 2024 Andrew A. Vasilyev <andy@altlinux.org> 3.2.5-alt1
- 3.2.5

* Wed Apr 17 2024 Andrew A. Vasilyev <andy@altlinux.org> 3.2.4-alt1
- 3.2.4

* Thu Feb 08 2024 Andrew A. Vasilyev <andy@altlinux.org> 3.2.2-alt1
- 3.2.2

* Mon Jan 15 2024 Andrew A. Vasilyev <andy@altlinux.org> 3.2.1-alt1
- 3.2.1

* Wed Dec 06 2023 Andrew A. Vasilyev <andy@altlinux.org> 3.0.2-alt1
- 3.0.2

* Tue Jun 27 2023 Andrew A. Vasilyev <andy@altlinux.org> 2.3.0-alt1
- initial build for ALT

