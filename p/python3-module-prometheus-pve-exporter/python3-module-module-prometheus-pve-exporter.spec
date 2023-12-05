%define  modulename prometheus-pve-exporter
%def_without check

Name:    python3-module-%modulename
Version: 3.0.2
Release: alt1

Summary: Prometheus Proxmox VE Exporter
License: Apache-2.0
Group:   Development/Python
URL:     https://github.com/prometheus-pve/prometheus-pve-exporter.git

BuildArch: noarch

Source: %modulename-%version.tar

Provides: prometheus-pve-exporter = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
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
install -pDm0644 pve.yml %buildroot%_sysconfdir/pve.yml

%check
#%%tox_create_default_config
%tox_check_pyproject

%files
%doc README.rst
%config(noreplace) %_sysconfdir/pve.yml
%_bindir/*
%python3_sitelibdir/*

%changelog
* Wed Dec 06 2023 Andrew A. Vasilyev <andy@altlinux.org> 3.0.2-alt1
- 3.0.2

* Tue Jun 27 2023 Andrew A. Vasilyev <andy@altlinux.org> 2.3.0-alt1
- initial build for ALT

