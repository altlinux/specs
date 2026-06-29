%define _unpackaged_files_terminate_build 1
Name:    mamonsu
Version: 3.5.16
Release: alt1

Summary: mamonsu is an active agent for collecting PostgreSQL instance and operating system metrics that can interact with Zabbix
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/postgrespro/mamonsu

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %name-%version.tar
Source1: %name.service

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
install -Dpm 0644 %SOURCE1 %buildroot%_unitdir/%name.service
mkdir -p %buildroot/%_sysconfdir/%name
mkdir -p %buildroot/%_sysconfdir/logrotate.d
mkdir -p %buildroot/%_datadir/%name
install -m 0600 -p packaging/conf/example_linux.conf %buildroot/%_sysconfdir/%name/agent.conf
install -m 0644 -p packaging/conf/template_linux.xml %buildroot/%_datadir/%name/template.xml
install -m 0644 -p examples/*.py %buildroot/%_datadir/%name/
mkdir -p %buildroot/%_sysconfdir/%name/plugins
touch %buildroot/%_sysconfdir/%name/plugins/__init__.py
mkdir -p %buildroot%_logdir/%name
mkdir -p %buildroot%_runtimedir/%name

%pre
getent group mamonsu >/dev/null || /usr/sbin/groupadd -r mamonsu
getent passwd mamonsu >/dev/null || /usr/sbin/useradd -r \
  -g mamonsu -d %_runtimedir/%name -s /sbin/nologin -c "mamonsu monitoring user" mamonsu

%preun
%preun_service %name.service

%post
%post_service %name.service

%files
%doc *.md
%attr(0660,mamonsu,mamonsu) %config(noreplace) %_sysconfdir/%name/agent.conf
%_bindir/%name
%python3_sitelibdir/%name/
%python3_sitelibdir/%pyproject_distinfo %name
%_sysconfdir/%name
%_datadir/%name
%_unitdir/%name.service
%attr(0755,mamonsu,mamonsu) %dir %_logdir/%name
%attr(0750,mamonsu,mamonsu) %dir %_runtimedir/%name

%changelog
* Mon Jun 29 2026 Andrey Cherepanov <cas@altlinux.org> 3.5.16-alt1
- New version.

* Thu Jun 04 2026 Andrey Cherepanov <cas@altlinux.org> 3.5.15-alt3
- Added service file (ALT #59436).
- Added config file (ALT #59437).

* Fri May 29 2026 Andrey Cherepanov <cas@altlinux.org> 3.5.15-alt2
- Remove %%check for compatibility.

* Fri May 29 2026 Andrey Cherepanov <cas@altlinux.org> 3.5.15-alt1
- Initial build for Sisyphus
