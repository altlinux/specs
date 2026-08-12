%define _pseudouser_user     _uwsgi
%define _pseudouser_group    _uwsgi
%define _pseudouser_home     /var/empty
%define _name uwsgi

Name: uwsgi-py2
Version: 2.0.30
Release: alt2

Summary: fast (pure C), self-healing, developer-friendly WSGI server
License: GPLv2
Group: System/Servers

Url: http://projects.unbit.it/uwsgi/

Source: %_name-%version.tar
Source1: %_name.init
Source2: %_name.logrotate
Source3: %_name.sysconfig
Source4: %name@.service
Patch1: %_name-2.0.15-alt-no-rpath.patch
Patch2: %_name-2.0.30-py2.patch
Patch2000: %_name-e2k.patch

BuildRequires(pre): rpm-build-python
BuildRequires: libxml2-devel python-dev python-module-setuptools libpcre-devel
Requires(pre,preun): webserver-common
Requires: python-module-%_name

%description
uWSGI is a fast (pure C), self-healing, developer-friendly WSGI server,
aimed for professional python webapps deployment and development. Over
time it has evolved in a complete stack for networked/clustered python
applications, implementing message/object passing, RPC and process
management. It uses the uwsgi (all lowercase) protocol for all the
networking/interprocess communications.

This is python2 build of uwsgi.

%package sysvinit
Summary: SysV init scripts for %name
Group: System/Servers
%description sysvinit
%summary

%package systemd
Summary: Systemd service for %name
Group: System/Servers
%description systemd
%summary

%package -n python-module-%_name
Summary: Python2 module for %name
Group: Development/Python
BuildArch: noarch
Provides: python2.7(%_name)
%description -n python-module-%_name
%summary

%prep
%setup -n %_name-%version
%patch1 -p1
%patch2 -p1
%ifarch %e2k
%patch2000 -p1
%endif

%build
%python_build

%install
%python_install

install -dm0775 %buildroot%_logdir/%name
install -pDm0755 %SOURCE1 %buildroot%_initdir/%name
install -pDm0644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/%name
install -pDm0644 %SOURCE2 %buildroot%_sysconfdir/logrotate.d/%name
install -pDm0644 %SOURCE4 %buildroot%_unitdir/%name@.service

%pre
/usr/sbin/groupadd -r -f %_pseudouser_group ||:
/usr/sbin/useradd -g %_pseudouser_group -c 'The uwsgi daemon' \
	-d %_pseudouser_home -s /dev/null -r %_pseudouser_user >/dev/null 2>&1 ||:

%files
%_bindir/%name
%dir %attr(0775,root,%_pseudouser_group) %_logdir/%name
%config(noreplace) %_sysconfdir/logrotate.d/%name
%doc README contrib

%files sysvinit
%config %_initdir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name

%post sysvinit
%post_service %name

%preun sysvinit
%preun_service %name

%files systemd
%_unitdir/%name@.service

%post systemd
%post_service %name@

%preun systemd
%preun_service %name@

%files -n python-module-%_name
%python_sitelibdir_noarch/*

%changelog
* Mon Jul 27 2026 Fr. Br. George <george@altlinux.org> 2.0.30-alt2
- Add systemd service
- Separate sysvinit and systemd packages
- Rename to python-module-wsgi for compatibility

* Mon Aug 25 2025 Fr. Br. George <george@altlinux.org> 2.0.30-alt1
- Initial build for ALT
