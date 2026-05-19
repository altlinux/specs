%define  modulename prometheus-pve-exporter
%def_without check

Name:    python3-module-%modulename
Version: 3.9.0
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
* Tue May 19 2026 Andrew A. Vasilyev <andy@altlinux.org> 3.9.0-alt1
- 3.9.0

* Mon Apr 27 2026 Andrew A. Vasilyev <andy@altlinux.org> 3.8.3-alt1
- 3.8.3

* Thu Mar 26 2026 Andrew A. Vasilyev <andy@altlinux.org> 3.8.2-alt1
- 3.8.2

* Sun Feb 15 2026 Andrew A. Vasilyev <andy@altlinux.org> 3.8.1-alt1
- 3.8.1

* Wed Dec 24 2025 Andrew A. Vasilyev <andy@altlinux.org> 3.8.0-alt1
- 3.8.0

* Thu Dec 18 2025 Andrew A. Vasilyev <andy@altlinux.org> 3.7.0-alt1
- 3.7.0

* Tue Dec 02 2025 Andrew A. Vasilyev <andy@altlinux.org> 3.6.0-alt1
- 3.6.0

* Thu Oct 30 2025 Andrew A. Vasilyev <andy@altlinux.org> 3.5.5-alt2
- fix config file option (Closes: #56561) (thnx kolesnichenko@)

* Sat Jun 21 2025 Andrew A. Vasilyev <andy@altlinux.org> 3.5.5-alt1
- 3.5.5

* Mon May 05 2025 Andrew A. Vasilyev <andy@altlinux.org> 3.5.4-alt1
- 3.5.4

* Thu Apr 17 2025 Andrew A. Vasilyev <andy@altlinux.org> 3.5.3-alt1
- 3.5.3

* Sat Feb 22 2025 Andrew A. Vasilyev <andy@altlinux.org> 3.5.2-alt1
- 3.5.2

* Wed Jan 22 2025 Andrew A. Vasilyev <andy@altlinux.org> 3.5.1-alt1
- 3.5.1

* Fri Jan 03 2025 Andrew A. Vasilyev <andy@altlinux.org> 3.5.0-alt1
- 3.5.0

* Thu Dec 19 2024 Andrew A. Vasilyev <andy@altlinux.org> 3.4.7-alt1
- 3.4.7

* Fri Dec 06 2024 Andrew A. Vasilyev <andy@altlinux.org> 3.4.6-alt1
- 3.4.6

* Tue Sep 24 2024 Andrew A. Vasilyev <andy@altlinux.org> 3.4.5-alt1
- 3.4.5

* Mon Aug 19 2024 Andrew A. Vasilyev <andy@altlinux.org> 3.4.4-alt1
- 3.4.4

* Fri Jul 05 2024 Andrew A. Vasilyev <andy@altlinux.org> 3.4.3-alt1
- 3.4.3

* Thu Jun 06 2024 Andrew A. Vasilyev <andy@altlinux.org> 3.4.2-alt1
- 3.4.2

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

