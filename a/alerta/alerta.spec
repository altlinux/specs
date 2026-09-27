%define _unpackaged_files_terminate_build 1

Name:       alerta
Version:    9.1.0
Release:    alt2
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
BuildRequires(pre): rpm-macros-systemd
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
getent group alertad >/dev/null || groupadd -r alertad
getent passwd alertad >/dev/null || \
    useradd -r -g alertad -d /dev/null -s /sbin/nologin \
    --no-create-home -c "alerta daemon" alertad

%post
# Replace placeholder with random key
if grep -q "CHANGE-ME" %_sysconfdir/%name/alertad.conf 2>/dev/null; then
    sed -i "s/SECRET_KEY = '<CHANGE-ME>'/SECRET_KEY = '$(tr -dc 'A-Za-z0-9' < /dev/urandom | head -c 32)'/" %_sysconfdir/%name/alertad.conf
fi
%systemd_post alertad.service

%preun
%systemd_preun alertad.service

%postun
%systemd_postun_with_restart alertad.service

%files
%doc README.md NOTICE
%_bindir/alertad
%python3_sitelibdir_noarch/%name
%python3_sitelibdir_noarch/%{name}_server-%version.dist-info
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/alertad.conf
%config(noreplace) %_sysconfdir/sysconfig/alertad
%_unitdir/alertad.service
%attr(0750,alertad,alertad) %dir %_logdir/%name

%changelog
* Sun Sep 27 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 9.1.0-alt2
- Now the default SECREY_KEY is randomly generated during the installation process.
- Made user/group creation idempotent.
- Fixed unit file and logdir attributes.

* Fri Sep 25 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 9.1.0-alt1
- Initial build for ALT.

