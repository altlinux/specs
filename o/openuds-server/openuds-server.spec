%add_python3_lib_path %_datadir/openuds
%allow_python3_import_path %_datadir/openuds
%add_findreq_skiplist %_datadir/openuds/uds/transports/*/scripts/windows/* %_datadir/openuds/uds/transports/*/scripts/macosx/*
%add_python3_req_skip uds.forward

Name: openuds-server
Version: 3.0.0
Release: alt1
Summary: Universal Desktop Services (UDS) Broker
License: BSD3
Group: Networking/Remote access
URL: https://github.com/dkmstr/openuds
AutoReqProv: yes, nopython
Source0: %name-%version.tar

Source10: openuds-httpd.conf
Source11: openuds-httpd-ssl.conf
Source12: openuds.logrotate

#Patch: %name-%version.patch

Requires: python3-module-django >= 2.2
Requires: python3-module-django-dbbackend-mysql >= 2.2
Requires: python3-module-django-dbbackend-sqlite3 >= 2.2
Requires: apache2-base
Requires: apache2-mod_wsgi-py3
Requires: openssl
Requires: logrotate

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): webserver-common rpm-build-webserver-common rpm-macros-apache2

%description
OpenUDS (Universal Desktop Services) is a multiplatform connection broker for:
- VDI: Windows and Linux virtual desktops administration and deployment
- App virtualization
- Desktop services consolidation

This package provides the required components
to allow this machine to work as UDS Broker.

%prep
%setup
#%patch -p1

sed -i 's|#!/usr/bin/env python3|#!/usr/bin/python3|' \
    $(find . -name '*.py')

%install

mkdir -p %buildroot{%_datadir,%_logdir,%_sysconfdir}/openuds
mkdir -p %buildroot%_logrotatedir
cp -r src/* %buildroot%_datadir/openuds/
mv %buildroot%_datadir/openuds/server/settings.py.sample %buildroot%_sysconfdir/openuds/settings.py
ln -r -s %buildroot%_logdir/openuds %buildroot%_datadir/openuds/log
ln -r -s %buildroot%_sysconfdir/openuds/settings.py %buildroot%_datadir/openuds/server/settings.py
# drop httpd-conf snippet
install -m 644 -D -p %SOURCE10 %buildroot%apache2_sites_available/openuds.conf
install -m 644 -D -p %SOURCE11 %buildroot%apache2_sites_available/openuds-ssl.conf
mkdir -p %buildroot%apache2_sites_enabled
touch %buildroot%apache2_sites_enabled/openuds.conf
install -p -D -m 644 %SOURCE12 %buildroot%_logrotatedir/openuds-server

%pre
%_sbindir/groupadd -r -f openuds >/dev/null 2>&1 ||:
%_sbindir/useradd -M -r -g openuds -G _webserver -c 'OpenUDS Brocker Daemon' \
        -s /bin/false  -d %_sharedstatedir/openuds openuds >/dev/null 2>&1 ||:

%post
# ugly hack to set a unique SECRET_KEY
sed -i "/^SECRET_KEY.*$/{N;s/^.*$/SECRET_KEY='`openssl rand -hex 10`'/}" %_sysconfdir/openuds/settings.py

%files
%_datadir/openuds
%dir %attr(0750, root, openuds) %_sysconfdir/openuds
%config(noreplace) %attr(0640, root, openuds) %_sysconfdir/openuds/settings.py
%config(noreplace) %apache2_sites_available/*.conf
%ghost %apache2_sites_enabled/*.conf
%dir %attr(0770, root, openuds) %_logdir/openuds
%config(noreplace) %_logrotatedir/openuds-server

%changelog
* Thu Nov 05 2020 Alexey Shabalin <shaba@altlinux.org> 3.0.0-alt1
- 3.0.0 Release

* Tue Apr 14 2020 Alexey Shabalin <shaba@altlinux.org> 3.0.0-alt0.1.git.d7e30d14
- Initial build for ALT

