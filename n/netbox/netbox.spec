%def_with docs

Name:    netbox
Version: 4.6.4
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
BuildRequires: python3-module-mkdocs >= 1.6.1
BuildRequires: python3-module-mkdocs-material >= 9.7.6
BuildRequires: python3-module-mkdocs-material-extensions
BuildRequires: python3-module-mkdocstrings >= 1.0.4
BuildRequires: python3-module-mkdocstrings-python >= 2.0.5
BuildRequires: python3-module-zensical >= 0.0.46
%endif
Requires: python3-module-colorama >= 0.4.6
Requires: python3-module-django >= 6.0.6
Requires: python3-module-django-cors-headers >= 4.9.0
Requires: python3-module-django-debug-toolbar >= 7.0.0
Requires: python3-module-django-filter >= 25.2
Requires: python3-module-django-htmx >= 1.27.0
Requires: python3-module-django-graphiql-debug-toolbar >= 0.2.0
Requires: python3-module-django-mptt >= 0.18
Requires: python3-module-django-pglocks >= 1.0.4
Requires: python3-module-django-prometheus >= 2.4.0
Requires: python3-module-django-redis >= 7.0.0
Requires: python3-module-django-rich >= 2.2.0
Requires: python3-module-django-rq >= 4.1.0
Requires: python3-module-django-storages >= 1.14.6
Requires: python3-module-django-taggit >= 6.1.0
Requires: python3-module-django-tables2 >= 2.8.0
Requires: python3-module-django-timezone-field >= 7.2.2
Requires: python3-module-djangorestframework >= 3.17.1
Requires: python3-module-drf-spectacular >= 0.29.0
Requires: python3-module-drf-spectacular-sidecar >= 2026.6.1
Requires: python3-module-feedparser >= 6.0.12
Requires: python3-module-jinja2 >= 3.1.6
Requires: python3-module-jsonschema >= 4.26.0
Requires: python3-module-markdown >= 3.10.2
Requires: python3-module-netaddr >= 1.3.0
Requires: python3-module-nh3 >= 0.3.6
Requires: python3-module-pillow >= 12.2.0
Requires: python3-module-psycopg >= 3.3.4
Requires: python3-module-yaml >= 6.0.3
Requires: python3-module-redis-py >= 7.4.1
Requires: python3-module-requests >= 2.34.2
Requires: python3-module-rq >= 2.10.0
Requires: python3-module-social-app-django >= 5.9.0
Requires: python3-module-social-core >= 4.8.7
Requires: python3-module-sorl-thumbnail >= 13.0.0
Requires: python3-module-strawberry-graphql >= 0.320.0
Requires: python3-module-strawberry-django >= 0.86.4
Requires: python3-module-svgwrite >= 1.4.3
Requires: python3-module-tablib >= 3.9.0
Requires: python3-module-tzdata >= 2026.2
Requires: python3-module-packaging
Requires: python3-module-django-auth-ldap
Requires: python3-module-sentry-sdk

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
zensical build
%endif

%install
# Sources
mkdir -p %buildroot{%_datadir,%_logdir,%_sysconfdir,%_sharedstatedir,%_defaultdocdir}/netbox
cp -r netbox/* %buildroot%_datadir/netbox/
mv %buildroot%_datadir/netbox/netbox/configuration_example.py %buildroot%_sysconfdir/netbox/configuration.py
ln -r -s %buildroot%_sysconfdir/netbox/configuration.py %buildroot%_datadir/netbox/netbox/configuration.py
cp contrib/gunicorn.py %buildroot%_sysconfdir/netbox/gunicorn.py
mkdir -p %buildroot%_sysconfdir/cron.daily/
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
groupadd -r -f _webserver >/dev/null 2>&1 ||:
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
* Wed Jul 01 2026 Alexander Burmatov <thatman@altlinux.org> 4.6.4-alt1
- New 4.6.4 version.

* Mon Jun 08 2026 Alexander Burmatov <thatman@altlinux.org> 4.6.2-alt1
- New 4.6.2 version.

* Thu May 28 2026 Alexander Burmatov <thatman@altlinux.org> 4.6.1-alt1
- New 4.6.1 version.

* Thu May 07 2026 Alexander Burmatov <thatman@altlinux.org> 4.6.0-alt1
- New 4.6.0 version.

* Tue May 05 2026 Alexander Burmatov <thatman@altlinux.org> 4.5.10-alt1
- New 4.5.10 version.

* Tue Apr 28 2026 Alexander Burmatov <thatman@altlinux.org> 4.5.9-alt1
- New 4.5.9 version.

* Tue Apr 14 2026 Alexander Burmatov <thatman@altlinux.org> 4.5.8-alt1
- New 4.5.8 version.

* Tue Apr 14 2026 Alexander Burmatov <thatman@altlinux.org> 4.5.7-alt1
- New 4.5.7 version.

* Mon Apr 13 2026 Alexander Burmatov <thatman@altlinux.org> 4.5.6-alt1
- New 4.5.6 version.

* Wed Mar 18 2026 Alexander Burmatov <thatman@altlinux.org> 4.5.5-alt1
- New 4.5.5 version.

* Wed Mar 04 2026 Alexander Burmatov <thatman@altlinux.org> 4.5.4-alt1
- New 4.5.4 version.

* Wed Feb 18 2026 Alexander Burmatov <thatman@altlinux.org> 4.5.3-alt1
- New 4.5.3 version.

* Wed Feb 04 2026 Alexander Burmatov <thatman@altlinux.org> 4.5.2-alt1
- New 4.5.2 version.

* Wed Jan 21 2026 Alexander Burmatov <thatman@altlinux.org> 4.5.1-alt1
- New 4.5.1 version.

* Tue Jan 13 2026 Alexander Burmatov <thatman@altlinux.org> 4.5.0-alt1
- New 4.5.0 version.

* Mon Jan 12 2026 Alexander Burmatov <thatman@altlinux.org> 4.4.10-alt1
- New 4.4.10 version.

* Wed Dec 24 2025 Alexander Burmatov <thatman@altlinux.org> 4.4.9-alt1
- New 4.4.9 version.

* Wed Dec 10 2025 Alexander Burmatov <thatman@altlinux.org> 4.4.8-alt1
- New 4.4.8 version.

* Fri Nov 28 2025 Alexander Burmatov <thatman@altlinux.org> 4.4.7-alt2
- Create _webserver group before useradd (ALT #55740).

* Wed Nov 26 2025 Alexander Burmatov <thatman@altlinux.org> 4.4.7-alt1
- New 4.4.7 version.

* Wed Nov 12 2025 Alexander Burmatov <thatman@altlinux.org> 4.4.6-alt1
- New 4.4.6 version.

* Thu Oct 30 2025 Alexander Burmatov <thatman@altlinux.org> 4.4.5-alt1
- New 4.4.5 version.

* Thu Oct 16 2025 Alexander Burmatov <thatman@altlinux.org> 4.4.4-alt1
- New 4.4.4 version.

* Wed Oct 15 2025 Alexander Burmatov <thatman@altlinux.org> 4.4.3-alt1
- New 4.4.3 version.

* Wed Oct 01 2025 Alexander Burmatov <thatman@altlinux.org> 4.4.2-alt1
- New 4.4.2 version.

* Mon Sep 22 2025 Alexander Burmatov <thatman@altlinux.org> 4.4.1-alt1
- New 4.4.1 version.
- README has fixed (ALT #55895).

* Wed Sep 03 2025 Alexander Burmatov <thatman@altlinux.org> 4.4.0-alt1
- New 4.4.0 version.

* Wed Aug 27 2025 Alexander Burmatov <thatman@altlinux.org> 4.3.7-alt1
- New 4.3.7 version.

* Wed Aug 13 2025 Alexander Burmatov <thatman@altlinux.org> 4.3.6-alt1
- New 4.3.6 version.

* Wed Jul 30 2025 Alexander Burmatov <thatman@altlinux.org> 4.3.5-alt1
- New 4.3.5 version.

* Mon Jul 28 2025 Alexander Burmatov <thatman@altlinux.org> 4.3.4-alt1
- New 4.3.4 version.

* Mon Jun 30 2025 Alexander Burmatov <thatman@altlinux.org> 4.3.3-alt1
- New 4.3.3 version.

* Sat Jun 07 2025 Alexander Burmatov <thatman@altlinux.org> 4.3.2-alt1
- New 4.3.2 version.

* Wed May 28 2025 Alexander Burmatov <thatman@altlinux.org> 4.3.1-alt1
- New 4.3.1 version.

* Mon May 12 2025 Alexander Burmatov <thatman@altlinux.org> 4.3.0-alt1
- New 4.3.0 version.

* Mon May 12 2025 Alexander Burmatov <thatman@altlinux.org> 4.2.9-alt1
- New 4.2.9 version.

* Sat Apr 26 2025 Alexander Burmatov <thatman@altlinux.org> 4.2.8-alt1
- New 4.2.8 version.

* Wed Apr 16 2025 Alexander Burmatov <thatman@altlinux.org> 4.2.7-alt1
- New 4.2.7 version.

* Tue Mar 25 2025 Alexander Burmatov <thatman@altlinux.org> 4.2.6-alt1
- New 4.2.6 version.

* Thu Mar 13 2025 Alexander Burmatov <thatman@altlinux.org> 4.2.5-alt1
- New 4.2.5 version.

* Thu Jan 30 2025 Alexander Burmatov <thatman@altlinux.org> 4.2.2-alt1
- New 4.2.2 version.

* Wed Dec 18 2024 Alexander Burmatov <thatman@altlinux.org> 4.1.9-alt1
- New 4.1.9 version.

* Thu Nov 14 2024 Alexander Burmatov <thatman@altlinux.org> 4.1.6-alt1
- New 4.1.6 version.

* Tue Nov 12 2024 Alexander Burmatov <thatman@altlinux.org> 4.0.11-alt1
- New 4.0.11 version.

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
