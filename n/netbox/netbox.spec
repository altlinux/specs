%def_with docs

Name:    netbox
Version: 4.0.8
Release: alt1

Summary: The premier source of truth powering network automation
License: Apache-2.0
Group:   Networking/WWW
URL:     https://github.com/netbox-community/netbox

AutoReqProv: yes, nopython

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-systemd
BuildRequires(pre): rpm-macros-apache2
BuildRequires(pre): rpm-build-webserver-common
BuildRequires(pre): webserver-common
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with docs
BuildRequires: python3-module-mkdocs
BuildRequires: python3-module-mkdocs-material
BuildRequires: python3-module-mkdocs-material-extensions
BuildRequires: python3-module-mkdocstrings
BuildRequires: python3-module-mkdocstrings-python
%endif
Requires: python3-module-django
Requires: python3-module-django-rq
Requires: python3-module-django-htmx
Requires: python3-module-django-mptt
Requires: python3-module-django-redis
Requires: python3-module-django-filter
Requires: python3-module-django-taggit
Requires: python3-module-django-tables2
Requires: python3-module-django-pglocks
Requires: python3-module-django-auth-ldap
Requires: python3-module-django-prometheus
Requires: python3-module-social-app-django
Requires: python3-module-djangorestframework
Requires: python3-module-django-cors-headers
Requires: python3-module-django-debug-toolbar
Requires: python3-module-django-timezone-field
Requires: python3-module-django-graphiql-debug-toolbar
Requires: python3-module-nh3
Requires: python3-module-Pillow
Requires: python3-module-tablib
Requires: python3-module-tzdata
Requires: python3-module-netaddr
Requires: python3-module-svgwrite
Requires: python3-module-markdown
Requires: python3-module-packaging
Requires: python3-module-feedparser
Requires: python3-module-sentry-sdk
Requires: python3-module-drf-spectacular
Requires: python3-module-drf-spectacular-sidecar
Requires: python3-module-strawberry-graphql
Requires: python3-module-strawberry-django

BuildArch: noarch

Source: %name-%version.tar
Source1: netbox-tmpfile.conf
Source2: httpd2.conf
Source3: httpd2-ssl.conf
Source4: README
Source5: upgrade_netbox
Source6: netbox.logrotate

%description
NetBox is the leading solution for modeling and documenting modern networks.
By combining the traditional disciplines of IP address management (IPAM) and
datacenter infrastructure management (DCIM) with powerful APIs and extensions,
NetBox provides the ideal "source of truth" to power network automation.

%package apache2
Group: Networking/WWW
BuildArch: noarch
Summary: apache2 configs for %name
Requires: %name = %version-%release
Requires: apache2-httpd-prefork-like
Requires: apache2-base
Requires: apache2-mod_wsgi-py3
Requires: apache2-mod_ssl

%description apache2
%summary.

%package nginx
Group: Networking/WWW
BuildArch: noarch
Summary: nginx configs for %name
Requires: %name = %version-%release
Requires: nginx
Requires: python3-module-gunicorn
Requires: cert-sh-functions

%description nginx
%summary.

%prep
%setup
find . -name '*.py' -o -name 'cxxtestgen' | xargs sed -i \
    -e '1 s:#!%_bindir/env python$:#!%_bindir/python3:' \
    -e '1 s:#! %_bindir/env python$:#! %_bindir/python3:' \
    %nil

%build
%if_with docs
export PYTHONPATH=$PWD/netbox
mkdocs build
%endif

%install
# Sources
mkdir -p %buildroot{%_datadir,%_logdir,%_sysconfdir,%_sharedstatedir,%_defaultdocdir}/netbox
cp -r netbox/* %buildroot%_datadir/netbox/
mv %buildroot%_datadir/netbox/netbox/configuration_example.py %buildroot%_sysconfdir/netbox/configuration.py
ln -r -s %buildroot%_sysconfdir/netbox/configuration.py %buildroot%_datadir/netbox/netbox/configuration.py
cp contrib/gunicorn.py %buildroot%_sysconfdir/netbox/gunicorn.py
mkdir -p %buildroot%_sysconfdir/cron.daily/
cp contrib/netbox-housekeeping.sh %buildroot%_sysconfdir/cron.daily/netbox-housekeeping
touch %buildroot%_logdir/netbox/netbox.log
install -p -D -m 644 %SOURCE6 %buildroot%_logrotatedir/netbox
# httpd2
mkdir -p %buildroot%apache2_sites_available
install -p -D -m 644 %SOURCE2 %buildroot%apache2_sites_available/netbox.conf
install -p -D -m 644 %SOURCE3 %buildroot%apache2_sites_available/netbox-ssl.conf
mkdir -p %buildroot%apache2_sites_enabled
touch %buildroot%apache2_sites_enabled/netbox.conf
touch %buildroot%apache2_sites_enabled/netbox-ssl.conf
# nginx
mkdir -p %buildroot%_sysconfdir/nginx/sites-available.d
cp contrib/nginx.conf %buildroot%_sysconfdir/nginx/sites-available.d/netbox.conf
mkdir -p %buildroot%_sysconfdir/nginx/sites-enabled.d
touch %buildroot%_sysconfdir/nginx/sites-enabled.d/netbox.conf
# Units files
mkdir -p %buildroot%_unitdir
cp contrib/netbox.service %buildroot%_unitdir/netbox.service
cp contrib/netbox-rq.service %buildroot%_unitdir/netbox-rq.service
# Tmp file
install -p -D -m 644 %SOURCE1 %buildroot%_tmpfilesdir/netbox.conf
# Documentation
install -p -D -m 644 %SOURCE4 %buildroot%_defaultdocdir/netbox/README
# Scripts
install -p -D -m 755 %SOURCE5 %buildroot%_bindir/upgrade_netbox

%pre
groupadd -r -f netbox >/dev/null 2>&1 ||:
useradd -M -r -g netbox -G _webserver -c 'NetBox Broker Daemon' \
        -s /bin/false  -d %_sharedstatedir/netbox netbox >/dev/null 2>&1 ||:

%post
if [ $1 -eq 1 ]; then
# ugly hack to set a unique SECRET_KEY
    sed -i "/^SECRET_KEY.*$/{N;s/^.*$/SECRET_KEY='`openssl rand -hex 50`'/}" %_sysconfdir/netbox/configuration.py
    python3 %_datadir/netbox/manage.py collectstatic --no-input
fi

%post_systemd_postponed netbox-rq.service

%preun
%preun_systemd netbox-rq.service

%post nginx
%post_systemd_postponed netbox.service
# Create SSL certificate for HTTPS server
cert-sh generate nginx-netbox ||:

%preun nginx
%preun_systemd netbox.service

%post apache2
# Create SSL certificate for HTTPS server
cert-sh generate apache2-netbox ||:

%files
%_datadir/netbox
%_bindir/upgrade_netbox
%dir %attr(0750, root, netbox) %_sysconfdir/netbox
%config(noreplace) %attr(0640, root, netbox) %_sysconfdir/netbox/configuration.py
%config(noreplace) %attr(0640, root, netbox) %_sysconfdir/netbox/gunicorn.py
%_sysconfdir/cron.daily/netbox-housekeeping
%dir %attr(0770, root, netbox) %_sharedstatedir/netbox
%dir %attr(0770, root, netbox) %_logdir/netbox
%attr(0644, netbox, netbox) %_logdir/netbox/netbox.log
%config(noreplace) %_logrotatedir/netbox
%_unitdir/netbox-rq.service
%_defaultdocdir/netbox/README

%files apache2
%config(noreplace) %apache2_sites_available/*.conf
%ghost %apache2_sites_enabled/*.conf

%files nginx
%_unitdir/netbox.service
%_tmpfilesdir/netbox.conf
%config(noreplace) %_sysconfdir/nginx/sites-available.d/netbox.conf
%ghost %_sysconfdir/nginx/sites-enabled.d/netbox.conf

%changelog
* Mon Aug 12 2024 Alexander Burmatov <thatman@altlinux.org> 4.0.8-alt1
- New 4.0.8 version.

* Tue Jul 16 2024 Alexander Burmatov <thatman@altlinux.org> 4.0.7-alt1
- New 4.0.7 version.

* Mon May 20 2024 Alexander Burmatov <thatman@altlinux.org> 3.7.8-alt1
- New 3.7.8 version.

* Fri Mar 22 2024 Alexander Burmatov <thatman@altlinux.org> 3.7.4-alt1
- New 3.7.4 version.

* Wed Jan 10 2024 Alexander Burmatov <thatman@altlinux.org> 3.6.9-alt1
- New 3.6.9 version.

* Mon Dec 11 2023 Alexander Burmatov <thatman@altlinux.org> 3.6.6-alt1
- New 3.6.6 version.
- Set the correct runtime dir.

* Thu Nov 09 2023 Alexander Burmatov <thatman@altlinux.org> 3.6.3-alt3
- Fix upgrade script.

* Tue Nov 07 2023 Alexander Burmatov <thatman@altlinux.org> 3.6.3-alt2
- Add logrotate file.

* Fri Sep 15 2023 Alexander Burmatov <thatman@altlinux.org> 3.6.3-alt1
- Initial build for Sisyphus.
